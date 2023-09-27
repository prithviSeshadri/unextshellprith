# Databricks notebook source
# MAGIC %md
# MAGIC #Day 2
# MAGIC ##Databricks
# MAGIC ###Prithvi

# COMMAND ----------

df=spark.read.json("dbfs:/mnt/saunextadls/raw/json")

# COMMAND ----------

df.display()

# COMMAND ----------

from pyspark.sql.functions import *

# COMMAND ----------

df1=df.withColumn("ingestiondate",current_timestamp()).withColumn("path",input_file_name())

# COMMAND ----------

# MAGIC %sql
# MAGIC create schema if not exists json

# COMMAND ----------



# COMMAND ----------

df1.write.mode("overwrite").option("path","dbfs:/mnt/saunextadls/raw/output/prithvi/json").saveAsTable("json.bronze")

# COMMAND ----------

# MAGIC %sql
# MAGIC select count(*) from json.bronze

# COMMAND ----------


