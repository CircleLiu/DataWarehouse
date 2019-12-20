create table movie.all_review_t(product_id string, user_id string, profile_name string, helpfulness string, score decimal(2,1), time timestamp, summary string, text string)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde'
WITH SERDEPROPERTIES (
   "separatorChar" = ",",
   "quoteChar"     = "\""
)
STORED AS TEXTFILE;

load data local inpath '/opt/all_review.csv' into table movie.all_review_t;

create table movie.all_review(product_id string, user_id string, profile_name string, helpfulness string, score decimal(2,1), time date, summary string, text string);

insert into table movie.all_review select product_id, user_id, profile_name, helpfulness, score, cast(time as date), summary, text from movie.all_review_t;

drop table movie.all_review_t;