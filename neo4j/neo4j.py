# coding=utf-8
from datetime import datetime
import numpy
import re
import time
from py2neo import Graph, Node, Relationship, NodeMatcher

graph = Graph("http://localhost:7474", auth=("neo4j", "12345"))

map = {
    "Product": "product.product_id",
    "Movie": "movie.title",
    "Actor": "actor.actor_name",
    "Author": "actor.actor_name",
    "Director": "author.author_name",
    "Studio": "studio.studio_name",
    "Binding": "binding.binding_name",
    "Genre": "genre.genre_name",
    "ReleaseDate": "release.date",
    "PublicationDate": "publication.date",
    "VersionCount": "movie.version_count",
    "SalesRank": "product.sales_rank",
    "Price": "product.price",
    "PublicationWeekday": "publication.weekday",
    "ReleaseWeekday": "release.weekday"
}


def search(field, condition, value):
    for i in range(len(field)):
        field[i] = map[field[i]]
    for i in range(len(condition)):
        if condition[i] == "!=":
            condition[i] = "<>"

    s = "match (product:product)-[]->(movie:movie) " \
        "match (product)-[:have_publication_date]-(publication:date) " \
        "match (product)-[:have_release_date]-(release:date) " \
        "match (product)-[:have_binding]-(binding:binding) " \
        "match (movie)-[:have_studio]->(studio:studio) " \
        "match (movie)-[]-(actor:actor) " \
        "match (movie)-[]-(author:author) " \
        "match (movie)-[]-(director:director) " \
        "match (movie)-[]-(genre:genre) "

    for i in range(len(field)):
        if i == 0:
            s += " where " + field[i] + condition[i] + "\"" + value[i] + "\" "
        else:
            s += " and " + field[i] + condition[i] + "\"" + value[i] + "\" "

    s += "return product.product_id, movie.title, movie.version_count, product.price, product.running_time, " \
         "product.sales_rank, publication.date, publication.weekday, release.date, release.weekday , " \
         "binding.binding_name, studio.studio_name, genre.genre," \
         "actor.actor_name, author.author_name, director.director_name"
    print(s)
    g = graph.run(s).data()
    return g


def search_amount_of_publication_date(field, condition, value):
    for i in range(len(field)):
        field[i] = map[field[i]]
    for i in range(len(condition)):
        if condition[i] == "!=":
            condition[i] = "<>"

    s = "match a = (publication:date)-[:have_publication_date]-(p:product)-[]-(m:movie) "
    for i in range(len(field)):
        if i == 0:
            s += " where " + field[i] + condition[i] + "\"" + value[i] + "\" "
        else:
            s += " and " + field[i] + condition[i] + "\"" + value[i] + "\" "
    s += "return count(a)"

    print (s)
    g = graph.run(s).data()
    return g


def search_amount_of_release_date(field, condition, value):
    for i in range(len(field)):
        field[i] = map[field[i]]
    for i in range(len(condition)):
        if condition[i] == "!=":
            condition[i] = "<>"

    s = "match a = (release:date)-[:have_release_date]-(p:product)-[]-(m:movie) "
    for i in range(len(field)):
        if i == 0:
            s += " where " + field[i] + condition[i] + "\"" + value[i] + "\" "
        else:
            s += " and " + field[i] + condition[i] + "\"" + value[i] + "\" "
    s += "return count(a)"

    print (s)
    g = graph.run(s).data()
    return g


def search_amount(field, condition, value):
    for i in range(len(field)):
        field[i] = map[field[i]]
    for i in range(len(condition)):
        if condition[i] == "!=":
            condition[i] = "<>"

    s = "match (product:product)-[]->(movie:movie) " \
        "match (product)-[:have_publication_date]-(publication:date) " \
        "match (product)-[:have_release_date]-(release:date) " \
        "match (product)-[:have_binding]-(binding:binding) " \
        "match (movie)-[:have_studio]->(studio:studio) " \
        "match (movie)-[]-(actor:actor) " \
        "match (movie)-[]-(author:author) " \
        "match (movie)-[]-(director:director) " \
        "match (movie)-[]-(genre:genre) "
    for i in range(len(field)):
        if i == 0:
            s += " where " + field[i] + condition[i] + "\"" + value[i] + "\" "
        else:
            s += " and " + field[i] + condition[i] + "\"" + value[i] + "\" "
    s += "return count(distinct movie.movie_id)"
    print(s)
    g = graph.run(s).data()
    return g


def collaboration_of_actor(amount):
    s = "match p = (d1:actor)-[:have_actor]-(m:movie)-[:have_actor]-(d2:actor) where d2.actor_name <> d1.actor_name " \
        "return d1.actor_name,d2.actor_name,count(p) order by count(p) desc limit " + amount
    g = graph.run(s).data()
    return g


def collaboration_of_director(amount):
    s = "match p = (d1:director)-[:have_director]-(m:movie)-[:have_director]-(d2:director) where d2.director_name <> " \
        "d1.director_name " \
        "return d1.director_name,d2.director_name,count(p) order by count(p) desc limit " + amount
    g = graph.run(s).data()
    return g


def collaboration_of_director_and_actor(amount):
    s = "match p = (d1:actor)-[:have_actor]-(m:movie)-[:have_director]-(d2:director) where d2.director_name <> " \
        "d1.actor_name return d1.actor_name, d2.director_name, count(p) order by count(p) desc limit " + amount
    g = graph.run(s).data()
    return g


def actor_with_actor(actor_name):
    s = "match p = (d1:actor)-[:have_actor]-(m:movie)-[:have_actor]-(d2:actor) where d2.actor_name <> " \
        "d1.actor_name and d1.actor_name = \"" + actor_name + \
        "\" return d2.actor_name, count(p) order by count(p) desc "
    print(s)
    g = graph.run(s).data()
    return g


def actor_with_director(actor_name):
    s = "match p = (d1:actor)-[:have_actor]-(m:movie)-[:have_director]-(d2:director) where d2.director_name <> " \
        "d1.actor_name and d1.actor_name = \"" + actor_name + \
        "\" return d2.director_name, count(p) order by count(p) desc "
    print(s)
    g = graph.run(s).data()
    return g


def director_with_director(director_name):
    s = "match p = (d1:director)-[:have_director]-(m:movie)-[:have_director]-(d2:director) where d2.director_name <> " \
        "d1.director_name and d1.director_name = \"" + director_name + \
        "\" return d2.director_name, count(p) order by count(p) desc "
    print(s)
    g = graph.run(s).data()
    return g


def director_with_actor(director_name):
    s = "match p = (d1:director)-[:have_director]-(m:movie)-[:have_actor]-(d2:actor) where d2.actor_name <> " \
        "d1.director_name and d1.director_name = \"" + director_name + \
        "\" return d2.actor_name, count(p) order by count(p) desc "
    print(s)
    g = graph.run(s).data()
    return g


def movie_of_genre(field, condition, value):
    for i in range(len(field)):
        field[i] = map[field[i]]
    for i in range(len(condition)):
        if condition[i] == "!=":
            condition[i] = "<>"

    s = "MATCH p=(genre:genre)-[]-(movie:movie)"
    for i in range(len(field)):
        if i == 0:
            s += " where " + field[i] + condition[i] + "\"" + value[i] + "\" "
        else:
            s += " or " + field[i] + condition[i] + "\"" + value[i] + "\" "
    s += "return count(distinct movie.movie_id)"

    g = graph.run(s).data()
    return g


matcher = NodeMatcher(graph)

nodes = matcher.match("genre")
new_nodes = list(nodes)
# x = Node("user", user_name = "Adam Lane")
# print (x.user_id)

# print(movie_of_year("1993"))
# print(movie_of_year_and_month("1993", "01"))
# print(movie_of_year_and_quarter("1993", 1))
# print(get_movie_by_title("Awake Live"))
# print(movie_of_director("Lo Wei"))
# # print(collaboration_of_director_and_actor())
# print(collaboration_of_director_and_actor())
# print(movie_of_genre("Action"))
# print(collaboration_of_director_and_author())
# print(movie_of_studio("Gospel Light Publications"))
# print(get_product_by_id("B001C0I630"))
# print(movie_info("Awake Live"))
# print(date("1999-12-26").weekday())
# print(search(["Product"], ["="], ["0790742446"]))
# print(search_amount(["Product"], ["!="], ["0790742446"]))
# print(search_amount_of_publication_date(["PublicationDate", "PublicationDate"], [">", "<"], ["1997-01-01", "1998-01-01"]))
# print(search_amount_of_release_date(["ReleaseDate", "ReleaseDate"], [">", "<"], ["1997-01-01", "1998-01-01"]))
# print(search_amount_of_release_date(["ReleaseWeekday", "ReleaseWeekday"], [">", "<="], ["2", "3"]))
# print(collaboration_of_actor("10"))
# print(collaboration_of_actor("20"))
# print(movie_of_genre(["Genre"], ["="], ["Action"]))
# print(actor_with_actor("John Wayne"))
# print(actor_with_director("John Wayne"))
# print(director_with_director("Robert Smigel"))
# print(director_with_actor("Robert Smigel"))
