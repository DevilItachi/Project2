# Databricks notebook source
# MAGIC %sql
# MAGIC Create catalog Spark_Practice;

# COMMAND ----------

# MAGIC %sql
# MAGIC use catalog Spark_Practice;
# MAGIC     
# MAGIC create schema if not exists BigMart;

# COMMAND ----------

# MAGIC %sql
# MAGIC Use Schema bigmart

# COMMAND ----------

print(spark.catalog.currentDatabase())

# COMMAND ----------

# MAGIC %sql
# MAGIC create volume ext_vol

# COMMAND ----------


