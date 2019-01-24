from pymongo import mongo_client

db = object()


class DataBaseManager(object):


    def __init__(self,connection_string):
        self.connection_string = connection_string


    def connect(self):
        global db
        try:
            client = mongo_client(self.connection_string)
        except:
            print("Failed to connect to the database")

        db = client["models"]

       # return self.client["models"]




