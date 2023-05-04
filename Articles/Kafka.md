# Apache Kafka Concepts Overview

## What is Kafka?
Apache kafka solves the problems of scaling and distributing of messaging systems. 
Messaging systems are an integral need of large scale systems. However, messaging using a single queue on a single server can quickly become a bottleneck in a system and become a hindrance to scalability. 
Kafka solves this problems by making sure all of the benefits that a queue provides can still be provided in a distributed manner.
Let's understand with the help of some key concepts.

## Example scenario
Let's consider the example of a gaming system's backend where a basketball game is generating a lot of events and they are being consumed by multiple clients. We will write our concepts with this example in mind

## Producer
The entity producing new events (or records) and pushing them into the queue is called a producer, since it is producing new events.
In our case, let's say there are cameras that are producing new events by watching a game (hypothetical producer)

## Consumer
If these events are being consumed by a variety of different clients, like cell phones, TVs, news articles etc, they're called consumers.

## Problem
Over time, if we want to expand and start following more and more games, this becomes a problem. Since we have assumed that currently no distributed queue exists. So we want to distribute these events, but how do we distribute a queue??????

## Partition and Partition Count
The different instances of a queue are called partitions in Kafka. The total number of paritions is called a partition count.

## Broker
A server can hold some or all of these partitions. Each such server holding partitions is called a broker.

## Record
Each itme in a partition is called a record.

## Partition Key
The producer where the events are being produced can specify the key where (which partition) each record will be placed on. This field is called the partition key. In our case we can consider this to be the game name for example. If no key is specified then Kafka will simply decide on a random partition.

## Topic
A grouping of paritions handling the same type of data is called a Topic.

## Offset
In order to identify each record independantly Kafka provides a unique sequential number to each record. So a record in a topic is identified by partition number and an offset.

## Consumers and consumer grouping
We typically assign a consumer to a parition, not a topic. However, it is not uncommon to have just one parition in a topic. 
So that would mean, one consumer per topic. Kafka consumers are (or should be very light weight) The offset is always useful and is what Kafka needs to keep track of per consumer to identify what records have already been consumed. Consumers can also be distributed btw on different servers. It is on the consumer to determine what is the sequence of reading records it wants to engage in.

Consumers in a consumer group, do not share partitions to garauntee that they do not read the same records.

BUT different consumer groups can be created to read the same data, they can process them differently.

## Deleting records

Kafka provides retention policies for records to automatically delete records.

## Fault Tolerance & durability.
Each record is stored on a persistant storage. so that when a broker goes down, it can be quickly recovered. Kafka also replicates partitions, so that if a partition goes down it can be quickly recovered. the replication factor is a measure of how many backup partitions are created. For example, a replication factor of 3 equals 2 partitions. 

## Read further
[Comparison of similar technologies](https://blog.scottlogic.com/2018/04/17/comparing-big-data-messaging.html)









