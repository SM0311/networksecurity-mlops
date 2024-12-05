## for mongo db connetion to push the data from local to cluster

from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://msuraj20:003Suraj@cluster0.kqy24.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)






