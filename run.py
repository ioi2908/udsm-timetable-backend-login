from app import app
from  flask import Flask


app.config['CORS_HEADERS'] = 'Content-Type'
app = Flask(__name__)

CORS(app, resource={"origin":"https://timetableudsmstudent.herokuapp.com/"})

if __name__ == "__main__":
	app.run(debug=True)