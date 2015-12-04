from roles import *
from flask import Flask,jsonify
from flask import abort
from flask import request
from flask import make_response
from flask import url_for
from flask.ext.httpauth import HTTPBasicAuth
from controller import Controller
from controller import Controller
app = Flask(__name__)

tasks = Controller.search()
@app.route('/todo/api/tasks',methods=['GET'])
def get_task(task_id):
	task = filter(lambda t:t['id'] == task_id,tasks)
	if len(task) == 0:
		abort(404)
	return jsonify({'task':task[0]})

if __name__=='__main__':
        app.run(host='0.0.0.0',port=80,debug=True)
