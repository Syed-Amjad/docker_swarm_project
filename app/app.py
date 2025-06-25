from flask import Flask, render_template
import redis
import os

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

@app.route('/')
def index():
    count = cache.incr('hits')
    return render_template('index.html', count=count)

@app.route('/metrics')
def metrics():
    count = cache.get('hits') or 0
    return f"hits_total {count.decode() if isinstance(count, bytes) else count}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8082)

