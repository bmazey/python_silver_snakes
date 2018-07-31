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
    id = db.Column(db.Integer, primary_key=True, description='random generated ID')
    filename = db.Column(db.String(64), required=True, description='filename of audio')
    data = db.Column(db.LargeBinary, required=True, description='audio')


@api.route("/text/<path:audiopath>")
class HelloWorld(Resource):
    def get(self):
        pass

    def post(self):
        pass




def main():
    application.debug = True
    application.run()


def get_app():
    return application


if __name__ == "__main__":
    main()
