from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

puppies = []

class PuppyNames(Resource):
    def get(self, name):
        for pup in puppies:
            if pup['name'] == name:
                return pup
        return {'name': None}, 404

    def post(self, name):
        pup = {'name' : name}
        puppies.append(pup)
        return pup

    def delete(self, name):
        for pup in puppies:
            if pup['name'] == name:
                deleted_pup = pup
                puppies.remove(pup)
                return {
                    'note': 'delete successful',
                    'name': deleted_pup['name']
                    }

class AllNames(Resource):
    def get(self):
        return {'puppies': puppies}

api.add_resource(PuppyNames, f'/puppy/<string:name>')
api.add_resource(AllNames, f'/puppies')

if __name__=='__main__':
    app.run(debug=True)