# Databricks notebook source
# MAGIC %sql
# MAGIC create schema if not exists sample

# COMMAND ----------

# MAGIC %sql
# MAGIC Create table emp(id int, name string, age int, dept string) location "dbfs:/mnt/saunextadls/raw/delta/naval/emp"

# COMMAND ----------

# MAGIC %sql
# MAGIC describe extended emp

# COMMAND ----------

# MAGIC %sql
# MAGIC describe history emp

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from emp

# COMMAND ----------

# MAGIC %sql
# MAGIC insert into table emp values(1,'a',23,'DE')
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC insert into table emp values(2,'b',23,'DE')
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC insert into table emp values(3,'c',23,'DE'),
# MAGIC                             (4,'d',23,'DE')

# COMMAND ----------

# MAGIC %sql
# MAGIC describe history emp

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from emp

# COMMAND ----------

# MAGIC %sql
# MAGIC Update emp
# MAGIC set dept='DS'
# MAGIC where id= 4

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from emp version as of 3

# COMMAND ----------

# MAGIC %sql
# MAGIC create table oldemp as 
# MAGIC select * from emp version as of 3

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from emp timestamp as of '2023-09-27T08:20:01.000+0000'

# COMMAND ----------


