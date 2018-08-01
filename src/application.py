import uuid
from flask import Flask, request, flash, redirect, url_for
from glob import glob
import os
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

UPLOAD_FOLDER = '/uploads'
ALLOWED_EXTENSIONS = set(['wav'])

audio = api.model('audio', {
    'id': fields.String(required=True, description='id'),
    'data': fields.Raw(required=True, description='audio file binary')
})


# store audio file in database
class Audio(db.Model):
    id = db.Column(db.String(128), primary_key=True)
    data = db.Column(db.LargeBinary)


@api.route("/audio")
class AudioFiles(Resource):
    @api.expect(audio)
    def post(self):
        file = "/Users/alansun/Documents/columbia_summer/silver_snakes/src/ibm/resources/sample_ibm_conversion_computer.wav"
        with open(file, 'rb') as audio_file:
            _id = str(uuid.uuid4())
            aud = Audio(id=_id, data=audio_file.read())
            db.session.add(aud)
            db.session.commit()
        return {'id': _id}


@api.route("/audio/<string:id>")
class AudioIdRoute(Resource):
    def get(self, id):
        return Audio.query.filter(Audio.id == id).one()

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@api.route('/file', methods=['GET', 'POST'])
class UploadFile(Resource):
    def upload_file(self):
        if request.method == 'POST':
            # check if the post request has the file part
            if 'file' not in request.files:
                flash('No file part')
                return redirect(request.url)
            file = request.files['file']
            # if user does not select file, browser also
            # submit an empty part without filename
            if file.filename == '':
                flash('No selected file')
                return redirect(request.url)
            if file and allowed_file(file.filename):
                # filename = secure_filename(file.filename)
                file.save(os.path.join(application.config['UPLOAD_FOLDER'], file.filename))
                return redirect(url_for('uploaded_file',
                                            filename=file.filename))
        return '''
        <!doctype html>
        <title>Upload new File</title>
        <h1>Upload new File</h1>
        <form method=post enctype=multipart/form-data>
          <input type=file name=file>
          <input type=submit value=Upload>
        </form>
        '''


def configure_db():
    db.create_all()
    db.session.commit()


def main():
    configure_db()
    application.debug = True
    application.run()


def get_app():
    return application


def get_db():
    return db

if __name__ == "__main__":
    main()

