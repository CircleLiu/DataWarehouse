create table movie.all_movie_t(id int, name string, version_count int)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde'
WITH SERDEPROPERTIES (
   "separatorChar" = ",",
   "quoteChar"     = "\""
)
STORED AS TEXTFILE;

load data local inpath '/opt/movie.csv' into table movie.all_movie_t;

create table movie.all_movie(id int, name string, version_count int);

insert into table movie.all_movie select * from movie.all_movie_t;

drop table movie.all_movie_t;