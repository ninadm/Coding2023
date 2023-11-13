# Choosing Databases

System design always deals with database choices. Truthfully speaking any database you choose will satisfy your functional requirement, but it is the non functional requirements where the decision to choose the right database gets complicated. 

Here are 3 things to consider when choosing databases
- Nature of the data, is it structured or unstructured
- Query patterns
- What is the expected scale at which one needs to operate


## Caching

Whenever you want to store values temporarily for fast access but do not care about persistence you can use caching. 
Caching also helps reduce the load on either our web server or the DB if it is a web based application.

Popular choices are 
- Redis
- etcd
- memcached


## File Storage

Blob Storage!
S3 is the most popular choice. 

You can use S3 with a CDN for faster access around the world if your app is accessible all over the world

## Text Searching

Let's say you want to search products on amazon or titles on netflix. 
We use text search engines for this. 

Popular products are 
- Solr
- ElasticSearch

These are built on top of Apache Lucine

They also support something called fuzzy search (basically edit distance)

(These are search engines not database, data can be lost in these above products, these are just search engines)

## Metrics (time series)

In a traditional relational database, you have the capability to update any record at any point in time,
With metrics and time series, you do not need to necessarily update anything, and the next writes are sequentially done in an append only manner

Read queries are bulk read queries.

Time series database are optimized for these kinds of query patterns. 

examples are 
- InfluxDB

## Analytics (offline reporting)

Let's say you want analytics on the data for a company like amazon!

- Hadoop
- Redshift

## Relational vs Non Relational
```
Is data relational YES  
    Do you need ACID YES (payments/inventory management)  
        Choose RDBMS
    Do you need ACID NO
        Any database is fine since you can map 
        structured data into NoSQL
Is data relational NO
    You can have a lot of Volume of data and 
    also attributes to a database
    You can use 
    - MongoDB
    - CouchBase DB
    - DynamoDB
Do you have ever increasing data YES
    For example, uber where number of drivers keeps increasing 
    and their location stats keep getting added.
    If you do not have complex queries then use Columnar databases like Redshift or Cassandra

```

Let's take the example of us building Amazon!

For inventory management, use RDBMS
But it also has ever increasing dataset
so the recommendation is to also use a columnar DB 
Let's say an order has been placed but not fulfilled, then use a RDBMS, once fulfilled, remove it from there and put it to Cassandra. (explore this idea further)

This article is still evolving...







