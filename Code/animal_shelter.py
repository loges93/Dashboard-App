from pymongo import MongoClient
from bson.objectid import ObjectId 

class AnimalShelter:
    def __init__(self, user='aacuser', password='aacpassword', host='nv-desktop-services.apporto.com', port=30887, db_name='AAC', collection_name='animals'):
        # Initialize MongoDB client and connect to the database and collection
        self.client = MongoClient(f'mongodb://{user}:{password}@{host}:{port}/?authSource={db_name}')
        self.database = self.client[db_name]
        self.collection = self.database[collection_name]

    def create(self, data):
        """
        Insert a document into the collection.
        """
        if data:
            try:
                insert_result = self.collection.insert_one(data)
                return str(insert_result.inserted_id)  # Return the string representation of the ObjectId
            except Exception as e:
                print(f"Insert failed: {e}")
                return False
        else:
            return False

    def read(self, query):
        """
        Query for documents in the collection.
        """
        try:
            # If the query contains an _id, convert it to ObjectId (if it is a valid ObjectId string)
            if '_id' in query:
                query['_id'] = ObjectId(query['_id'])
            
            # Find documents matching the query
            cursor = self.collection.find(query)
            return list(cursor)  # Convert cursor to list
        except Exception as e:
            print(f"Query failed: {e}")
            return []

    def update(self, query, new_values):
        """
        Update a document in the collection.
        """
        if query and new_values:
            try:
                # If the query contains an _id, convert it to ObjectId
                if '_id' in query:
                    query['_id'] = ObjectId(query['_id'])

                # Set the new values (use $set to specify the fields to update)
                update_result = self.collection.update_one(query, {"$set":new_values})

                # Return True if a document was updated, otherwise False
                return update_result.modified_count > 0
            except Exception as e:
                print(f"Update failed: {e}")
                return False
        else:
            return False
        
    def delete(self, query):
        """
        Delete a document from the collection.

        """
        if query:
            try:
                # If the query contains an _id, convert it to ObjectId
                if '_id' in query:
                    query['_id'] = ObjectId(query['_id'])

                # Delete the document(s) that match the query
                delete_result = self.collection.delete_one(query)

                # Return True if a document was deleted, otherwise False
                return delete_result.deleted_count > 0
            except Exception as e:
                print(f"Delete failed: {e}")
                return False
        else:
            return False


    
    




