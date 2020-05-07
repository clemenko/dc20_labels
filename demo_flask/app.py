from flask import Flask, render_template, request, jsonify, redirect, url_for
from redis import Redis
from pymongo import MongoClient

import os

version = "0.1"
app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False
redis = Redis(host='redis', port=6379)
server_name = os.getenv('HOSTNAME')

if os.path.isfile('/run/secrets/demo_title'):
   open('/run/secrets/demo_title', 'r')
   title = open('/run/secrets/demo_title', 'r')
   red_secret = title.read()
   title.close
else:
   red_secret = 'you should use secrets.'

client = MongoClient('mongo')
db = client.ipdb

@app.route('/healthz')
def health_check():
    return jsonify({'redis': 'up', 'mongo': 'up'}), 200

@app.route('/info')
def info(server_name=None):
    redis.incr('hits')
    #return os.getenv('HOSTNAME') + " : " +  str(redis.get('hits').decode('utf-8')) + " : " + version, 200
    return jsonify(os.getenv('HOSTNAME'),redis.get('hits').decode('utf-8'),version), 200


@app.route("/get_my_ip", methods=["GET"])
def get_my_ip():
    redis.incr('hits')
    print(jsonify({'ip': request.headers.get('X-Forwarded-For', '')}), 200)
    print(request.headers.get("X-Forwarded-Host"))
    print(request.remote_addr)
    return jsonify({'ip': request.headers.getlist("X-Forwarded-For")}), 500
    #X-Real-IP

@app.route('/list')
def listip():
    redis.incr('hits')
    results = []
    for ip in db.ipdb.find():
        ip.pop('_id')
        results.append(ip)
    return jsonify(results)


@app.route('/secret')
def secret():
    redis.incr('hits')
    return red_secret

@app.route('/hits')
def hits():
    redis.incr('hits')
    return redis.get('hits')

@app.route('/')
def index(server_name=None):
    redis.incr('hits')
    server_name = os.getenv('HOSTNAME')
    item_doc = {
        'ip': request.remote_addr
    }
    db.ipdb.insert_one(item_doc)
    return render_template('index.html', hits=redis.get('hits').decode('utf-8'), server_name=server_name, ip=request.remote_addr, secret=red_secret)

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)