# Spark

 [Will Spark overtake Hadoop? Will Hadoop be replaced by Spark? - Quora](https://www.quora.com/Will-Spark-overtake-Hadoop-Will-Hadoop-be-replaced-by-Spark) 

> Spark is in a sense already part of Hadoop. It already runs on YARN, which is Hadoop 2's generalized execution environment ([Launching Spark on YARN](http://spark.incubator.apache.org/docs/0.8.0/running-on-yarn.html)) -- not just Mesos. And for example we (Cloudera) support it via Databricks on top of CDH ([Databricks and Cloudera Partner to Support Spark](http://www.databricks.com/blog/2013/10/28/databricks-and-cloudera-partner-to-support-spark.html)). So there is no either/or here to begin with.
>
> The larger point, I suppose, is that Hadoop is not one thing to be replaced by one other thing. It actually names a large ecosystem of components. Spark itself has no counterpart for a lot of what's under the Hadoop umbrella (M/R, Zookeeper, Sentry, Hue, HDFS, etc.) But it is also almost surely true that many things in the Hadoop ecosystem will subsume others. M/R is not going away for example, but, it is not the right tool for many jobs on Hadoop, and Spark is a right-er tool for many of those things, so it or something like it is going to replace plenty of M/R usages.

> Following are the reasons, Spark can not replace Hadoop:
>
> 1. **Spark doesn't have storage layer**. The best storage layer for Spark is Hadoop’s HDFS.
> 2. Hadoop’s Yarn also provides a resource management layer, used by Spark quite efficently
> 3. Spark is an alternative of Hadoop’s MapReduce, and it is replacing MapReduce.
>
> **Conclusion:**
>
> Spark is complementing Hadoop with a brand new data processing layer. Earlier Hadoop was limited just to batch processing, but with Spark it can handle: Batch, interactive, iterative, in-memory, real-time (stream), graph, etc.

