import uuid
from flask import Flask
from glob import glob
from flask_restplus import Resource, Api
from src.speech import Speech
from flask_restplus import Resource, Api, fields
from flask_sqlalchemy import SQLAlchemy



# welcome to flask: http://flask.pocoo.org/
# working with sqlalchemy & swagger:
# http://michal.karzynski.pl/blog/2016/06/19/building-beautiful-restful-apis-using-flask-swagger-ui-flask-restplus/
application = Flask(__name__)
api = Api(application)
application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
db = SQLAlchemy(application)


# store audio file in database
class Audio(db.Model):
    __tablename__ = 'audio_filename'
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(64))
    data = db.Column(db.LargeBinary)


@api.route("/hello")
class HelloWorld(Resource):
    def get(self):
        return {'hello', 'world'}

    def post(self):
        pass


def main():
    application.debug = True
    application.run()


def get_app():
    return application


if __name__ == "__main__":
    main()
