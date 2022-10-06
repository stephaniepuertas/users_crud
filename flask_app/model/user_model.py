from flask_app.config.mysqlconnection import connectToMySQL
from pprint import pprint
import re
from flask import flash
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


# links to database
DATABASE = 'user_schema'


class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    def __repr__(self):
        return f'<User: {self.first_name}>'

    # create
    @classmethod
    def save(cls, data):
        query = 'INSERT INTO users (column1, column2, column3) VALUES (%(column1)s, %(column2)s, %(column3)s);'
        user_id = connectToMySQL(DATABASE).query_db(query, data)
        print(f'Created: <User {user_id}>')
        return user_id

    # find all (no data needed)
    @classmethod
    def find_all(cls):
        query = 'SELECT * from users;'
        results = connectToMySQL(DATABASE).query_db(query)
        users = []
        for result in results:
            users.append(User(result))
        print(f'Found all users:')
        pprint(users)
        return users

    # find one by id
    @classmethod
    def find_by_id(cls, data):
        query = 'SELECT * from users WHERE id = %(id)s;'
        results = connectToMySQL(DATABASE).query_db(query, data)
        user = User(results[0])
        print(f'Found: <User {data["id"]}>')
        return user

    # update one by id
    @classmethod
    def find_by_id_and_update(cls, data):
        query = 'UPDATE users SET column1 = %(column1)s, column2 = %(column2)s, column3 = %(column3)s WHERE id = %(id)s;'
        connectToMySQL(DATABASE).query_db(query, data)
        print(f'Updated: <User {data["id"]}>')
        return True

    # delete one by id
    @classmethod
    def find_by_id_and_delete(cls, data):
        query = 'DELETE FROM users WHERE id = %(id)s;'
        connectToMySQL(DATABASE).query_db(query, data)
        print(f'Deleted: <User {data["id"]}>')
        return True