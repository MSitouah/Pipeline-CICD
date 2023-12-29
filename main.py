from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from views import getData, api_username, api_pwd
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
api = Api(app)
# Configure basic auth settings
auth = HTTPBasicAuth()
# Sample user credentials for demonstration purposes
users = {
    api_username : api_pwd
}

@auth.verify_password
def verify_password(username, password):
    if username in users and users[username] == password:
        return username

class user(Resource):
    @auth.login_required
    def get(self,id):
        try:
            return getData("select * from all_users where LOWER(username) = :id ", id)     
        except KeyError  as e:
            return {}
api.add_resource(user, '/user/<id>')
        
class userList(Resource):
    @auth.login_required      
    def get(self):
        try:
            return getData("select * from all_users where :id = :id ", 1)
        except Exception as e:
            return e
api.add_resource(userList,'/users')

class emp(Resource):
    @auth.login_required
    def get(self):
        try:
            return getData("select * from hr.employees where :id = :id ", 1)
        except Exception as e:
            return e
api.add_resource(emp, '/hr/emp')


if __name__ == '__main__':
    app.run(host ='0.0.0.0', port = 5001, debug=True)

