# from pyspark.sql import SparkSession
# from pyspark.sql.types import *
#
# # Create a SparkSession
# spark = SparkSession.builder.appName("example").getOrCreate()
#
# # Define the schema
# schema = StructType([
#     StructField("id", IntegerType(), False),
#     StructField("name", StringType(), True)
# ])
#
# # Provide the data as a list of tuples
# data = [(1, "Alice"), (2, "Bob"), (3, "Charlie")]
#
# # Create a DataFrame using the schema and data
# df = spark.createDataFrame(data, schema=schema)
#
# # Show the DataFrame
# df.show()


# import pandas as pd
