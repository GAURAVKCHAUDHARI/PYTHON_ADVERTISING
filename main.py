
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://gauravc:connect@cluster0.rrvqccb.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinginig your deployment....")
except Exception as e:
    print(e)
finally:
    print('You successfully connected to MongoDB!')


# Connect to MongoDB
db = client['gauravc']
collection = db['proj']

# Fetch data from the collection
cursor = collection.find({})

# Iterate through the documents and display them
for document in cursor:
    print(document)








