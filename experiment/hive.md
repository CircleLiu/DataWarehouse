```
select avg(score) from all_review where product_id='B0000V4906';
```

### text, mr

```
MapReduce Total cumulative CPU time: 1 minutes 54 seconds 120 msec
Ended Job = job_1576948544982_0009
MapReduce Jobs Launched: 
Stage-Stage-1: Map: 32  Reduce: 1   Cumulative CPU: 114.12 sec   HDFS Read: 8233710733 HDFS Write: 107 SUCCESS
Total MapReduce CPU Time Spent: 1 minutes 54 seconds 120 msec
OK
4.67089
Time taken: 46.063 seconds, Fetched: 1 row(s)
```



### text, tez

```
----------------------------------------------------------------------------------------------
        VERTICES      MODE        STATUS  TOTAL  COMPLETED  RUNNING  PENDING  FAILED  KILLED  
----------------------------------------------------------------------------------------------
Map 1 .......... container     SUCCEEDED     31         31        0        0       0       0  
Reducer 2 ...... container     SUCCEEDED      1          1        0        0       0       0  
----------------------------------------------------------------------------------------------
VERTICES: 02/02  [==========================>>] 100%  ELAPSED TIME: 19.58 s    
----------------------------------------------------------------------------------------------
OK
4.67089
Time taken: 20.268 seconds, Fetched: 1 row(s)
```

### sequence, mr

```
Total MapReduce CPU Time Spent: 2 minutes 14 seconds 790 msec
OK
4.67089
Time taken: 60.564 seconds, Fetched: 1 row(s)
```

### sequence, tez

```
----------------------------------------------------------------------------------------------
        VERTICES      MODE        STATUS  TOTAL  COMPLETED  RUNNING  PENDING  FAILED  KILLED  
----------------------------------------------------------------------------------------------
Map 1 .......... container     SUCCEEDED     32         32        0        0       0       0  
Reducer 2 ...... container     SUCCEEDED      1          1        0        0       0       0  
----------------------------------------------------------------------------------------------
VERTICES: 02/02  [==========================>>] 100%  ELAPSED TIME: 20.63 s    
----------------------------------------------------------------------------------------------
OK
4.67089
Time taken: 24.625 seconds, Fetched: 1 row(s)
```

### rcfile, mr

```
MapReduce Total cumulative CPU time: 1 minutes 8 seconds 380 msec
Ended Job = job_1576948544982_0022
MapReduce Jobs Launched: 
Stage-Stage-1: Map: 32  Reduce: 1   Cumulative CPU: 68.38 sec   HDFS Read: 148565044 HDFS Write: 107 SUCCESS
Total MapReduce CPU Time Spent: 1 minutes 8 seconds 380 msec
OK
4.67089
Time taken: 38.888 seconds, Fetched: 1 row(s)
```

### rcfile, tez

```
----------------------------------------------------------------------------------------------
        VERTICES      MODE        STATUS  TOTAL  COMPLETED  RUNNING  PENDING  FAILED  KILLED  
----------------------------------------------------------------------------------------------
Map 1 .......... container     SUCCEEDED     32         32        0        0       0       0  
Reducer 2 ...... container     SUCCEEDED      1          1        0        0       0       0  
----------------------------------------------------------------------------------------------
VERTICES: 02/02  [==========================>>] 100%  ELAPSED TIME: 14.13 s    
----------------------------------------------------------------------------------------------
OK
4.67089
Time taken: 14.601 seconds, Fetched: 1 row(s)
```

