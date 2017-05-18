from flask_restful import Resource, reqparse
from models.stores import StoreModel


class Store(Resource):
    def get(self, name):
        store = StoreModel.find_by_name(name)

        if store:
            return store.json()
        return {'message': 'Store not found broh!'}

    def post(self, name):
        if StoreModel.find_by_name(name):
            return {'message': 'a store with name {} already exists, breh!'}, 400

        store = StoreModel(name)

        try:
            store.save_to_db()

        except:
            return {'message':'oh dang unable to save store name breh!'}, 500

        return store.json(), 201

    def delete(self, name):
        store = StoreModel.find_by_name(name)

        if store:
            store.delete_from_db()

        return {'message': 'store deleted, breh!'}


class StoreList(Resource):
    def get(self):
        return {'stores': [store.json() for store in StoreModel.query.all()]}
