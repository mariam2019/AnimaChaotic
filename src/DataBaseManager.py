from pymongo import MongoClient

db = object()


class DataBaseManager(object):


    def __init__(self,connection_string):
        self.connection_string = connection_string


    def connect(self):
        global db
        try:
            client = MongoClient(self.connection_string)

        except:
            print("Failed to connect to the database")
            raise

        db = client["models"]

def get_database():
    return db



       # return self.client["models"]




