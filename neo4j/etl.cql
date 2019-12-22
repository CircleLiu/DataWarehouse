USING PERIODIC COMMIT 1000
LOAD CSV FROM "file:///neo4j_data.csv" AS line
merge (p:product{product_id:line[0], running_time:line[1],sales_rank:line[2],publication_date_id:line[3],movie_id:line[4],binding_id:line[5],studio_id:line[6],release_date_id:line[7],price:line[8]})

MATCH (m:movie) DETACH DELETE m

USING PERIODIC COMMIT 1000
LOAD CSV FROM "file:///movie_ex.csv" AS line
create (m:movie{movie_id:line[0],title:line[1],version_count:line[2]})

match (p:product),(m:movie) where p.movie_id=m.movie_id 
create (p)-[h:have]->(m)

USING PERIODIC COMMIT 1000
LOAD CSV FROM "file:///actor2.csv" AS line
match (p:product{product_id:line[0]})
create (a:actor{movie_id:p.movie_id, actor:line[1]})

USING PERIODIC COMMIT 1000
LOAD CSV FROM "file:///actor.csv" AS line
create (a:actor{actor_name:line[1]})

match (p:product),(a:actor) where p.product_id=a.product_id
create (p)-[h:have_actor]->(a)

USING PERIODIC COMMIT 1000
LOAD CSV FROM "file:///user.csv" AS line
create (u:user{user_id:line[0],user_name:line[1]})

USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM "file:///user.csv" AS row
match (m:movie{movie_id:row[]})

USING PERIODIC COMMIT 1000
LOAD CSV FROM "file:///actor4.csv" AS line
match (m:movie{movie_id:line[0]})
match (a:actor{actor_name:line[1]})
merge (m)-[h:have_actor]->(a)
on create set h.movie_id = line[0], h.actor_name = line[1]

USING PERIODIC COMMIT 1000
LOAD CSV FROM "file:///director.csv" AS line
create (a:director{director_name:line[1]})
create index on: director(director_name) 

USING PERIODIC COMMIT 1000
LOAD CSV FROM "file:///have_director.csv" AS line
match (m:movie{movie_id:line[0]})
match (d:director{director_name:line[1]})
merge (m)-[h:have_director]->(d)
on create set h.movie_id = line[0], h.director_name = line[1]

USING PERIODIC COMMIT 1000
LOAD CSV FROM "file:///author.csv" AS line
create (a:author{author_name:line[0]})
create index on: author(author_name)

USING PERIODIC COMMIT 1000
LOAD CSV FROM "file:///have_author.csv" AS line
match (m:movie{movie_id:line[0]})
match (a:author{author_name:line[1]})
merge (m)-[h:have_author]->(a)
on create set h.movie_id = line[0], h.author_name = line[1]

USING PERIODIC COMMIT 1000
LOAD CSV FROM "file:///genre.csv" AS line
create (g:genre{genre_name:line[0]})
create index on:genre(genre_name)

using periodic commit 1000
load csv from "file:///have_genre.csv" as line
match (m:movie{movie_id:line[0]})
match (g:genre{genre_name:line[1]})
merge (m)-[h:have_genre]->(g)
on create set h.movie_id = line[0], h.genre_name = line[1]

USING PERIODIC COMMIT 1000
LOAD CSV FROM "file:///binding.csv" AS line
create (b:binding{binding_id:line[0],binding_name:line[1]})
create index on:binding(binding_id)
create index on:binding(binding_name)

match (p:product),(b:binding) where p.binding_id = b.binding_id
merge (p)-[h:have_binding]->(b)
on create set h.product_id = p.product_id, h.binding_id = b.binding_id

USING PERIODIC COMMIT 1000
LOAD CSV FROM "file:///studio.csv" AS line
create (s:studio{studio_name:line[0]})
create index on:studio(studio_name)

using periodic commit 1000
load csv from "file:///have_studio.csv" as line
match (m:movie{movie_id:line[0]})
match (s:studio{studio_name:line[1]})
merge (m)-[h:have_genre]->(s)
on create set h.movie_id = line[0], h.studio_name = line[1]

USING PERIODIC COMMIT 1000
LOAD CSV FROM "file:///date.csv" AS line
create (d:date{date_id:line[0],date:line[1]})
create index on:date(date_id)

match (p:product),(d:date) where p.release_date_id = d.date_id
merge (p)-[h:have_release_date]->(d)
on create set h.product_id = p.product_id, h.release_date_id = d.date_id

using periodic commit 1000
load csv from "file:///have_publication_date.csv" as line
match (p:product{product_id:line[0]})
match (d:date{date:line[1]})
merge (p)-[h:have_publication_date]->(d)
on create set h.product_id = line[0], h.publication_date_id = d.date_id

match (a:actor)
match p = (d1:actor)-[:have_actor]-(m:movie)-[:have_actor]-(d2:actor) where d1.actor_name = a.actor_name and d2.actor_name <> a.actor_name 
return d1.actor_name,d2.actor_name,count(p) order by count(p) desc
