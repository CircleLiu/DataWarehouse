create table movie.all_product_t(asin string, name string, actor string, director string, rank int, price decimal(10,2), category string, language string, media string, studio string, genres string, running_time int, publication_date date, release_date date)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde'
WITH SERDEPROPERTIES (
   "separatorChar" = ",",
   "quoteChar"     = "\""
)
STORED AS TEXTFILE;

load data local inpath '/opt/warehouse_product.csv' into table movie.all_product_t;

create table movie.all_product(asin string, name string, actor string, director string, rank int, price decimal(10,2), category string, language string, media string, studio string, genres string, running_time int, publication_date date, release_date date);

insert into table movie.all_product select * from movie.all_product_t;

drop table movie.all_product_t;

create table movie.all_product_s(asin string, name string, actor string, director string, rank int, price decimal(10,2), category string, language string, media string, studio string, genres string, running_time int, publication_date date, release_date date) 
stored as sequencefile;

insert into table movie.all_product_s select * from movie.all_product;

create table movie.all_product_rc(asin string, name string, actor string, director string, rank int, price decimal(10,2), category string, language string, media string, studio string, genres string, running_time int, publication_date date, release_date date) 
stored as rcfile;

insert into table movie.all_product_rc select * from movie.all_product;