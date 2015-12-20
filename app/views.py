from app import app, db, csrf
from models import Work
from flask import send_from_directory, jsonify, request, render_template
from datetime import datetime
import time


@app.before_request
def check_csrf():
    csrf.protect()


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory(app.static_folder + '/js', path)

@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory(app.static_folder + '/css', path)

@app.route('/fonts/<path:path>')
def send_font(path):
    return send_from_directory(app.static_folder + '/fonts', path)


@app.route('/api/v1/getall')
def getAll():
    return jsonify(result=[w.serialize() for w in Work.query.all()])

@app.route('/api/v1/delet', methods=['POST'])
def delet():
    if request.method == 'POST':
        json = request.get_json()
        work = Work.query.filter_by(id=json['id']).delete()
        db.session.commit()
        return jsonify(delete=True)

@app.route('/api/v1/trig', methods=['POST'])
def trig():
    if request.method == 'POST':
        json = request.get_json()
        work = Work.query.filter_by(id=json['id']).first().trig()
        db.session.commit()
        return jsonify(done=work.done)

@app.route('/api/v1/work', methods=['POST'])
def work():
    if request.method == 'POST':
        json = request.get_json()
        work = Work(json['body'], json['importance'], False, datetime.utcfromtimestamp(json['expired']));
        db.session.add(work);
        db.session.commit();
        return jsonify(work.serialize())
