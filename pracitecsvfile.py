
# from pymongo import MongoClient
# from pymongo.server_api import ServerApi
#
# uri = "mongodb+srv://gauravc:connect@cluster0.rrvqccb.mongodb.net/?retryWrites=true&w=majority"
#
# # Create a new client and connect to the server
# client = MongoClient(uri, server_api=ServerApi('1'))
#
# # # Send a ping to confirm a successful connection
# # try:
# #     client.admin.command('ping')
# #     print("Pinginig your deployment....")
# # except Exception as e:
# #     print(e)
# # finally:
# #     print('You successfully connected to MongoDB!')
# #
#
# # Connect to MongoDB
# db = client['gauravc']
# collection = db['proj']
#
# # Fetch data from the collection
# cursor = collection.find({})
#
# # Iterate through the documents and display them
# for document in cursor:
#     print(document)



# from pyspark.sql import *
# from pyspark.sql.functions import*
# # from pyspark.sql.types import*
# #
# # spark = SparkSession.builder.master('local[*]') .appName('monodataprocessing').getOrCreate()
#
# df = spark.read.format('json').load(cursor)
# df.show()
#
#




# p = r'E:\AVD\SPARK BY VENU SIR\drivers\asl.csv'
# df = spark.read.format('csv').option('header','true').option('inferSchema','true').load(p)
# df.show()
# # proccess = df.where(col('age')>49)
# # proccess1 = df.where(col('city')=='hyd')
# #
# # # proccess1.show()
# # # df.show(truncate=True)
# #
# # proccess2 = df.where([(col('age'))>30 & (col('city'))=='hyd'])
# # proccess2.show()
#
# # proc = df.where[col('age')>21]
# # proc.show()'''


#
# import pymysql
#
# try:
#     conn = pymysql.connect(username= 'root', password= 'PASSWORD', host ='localhost', database='sys')
#
#     if conn.open:
#         print('connection with database established successfully.')
#
#     cursor = conn.cursor()
#     table = '''create table drp if not exists (
#             name varchar(20),
#             id int,
#             sal int);'''
#     cursor.execute(table)
#     conn.commit()
#     print('table drp succesfully created to the db')
#
# except pymysql.Error as e:
#     print(f'Error:{e}')
#
# finally:
#     cusror.close()
#     conn.close()
#     print('connection with db closed')


from pyspark import *
from pyspark.sql import *
from pyspark.sql.functions import *

spark = SparkSession.builder.master('local[*]').appName('testing').getOrCreate()

df =   spark.read.format('mongo').option('url','mongodb+srv://gauravc:connect@cluster0.rrvqccb.mongodb.net/?retryWrites=true&w=majority')\
    .option('db','gauravc').option('collection','proj').load()
df.show()
# df = spark.read.format('json').option('inferSchema', 'true').load(data)
# pr = df.find({})
# for i in pr:print(i)








