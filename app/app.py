from flask import Flask, render_template
from prometheus_flask_exporter import PrometheusMetrics
import redis

app = Flask(__name__)

# Enable Prometheus metrics
metrics = PrometheusMetrics(app)

# Redis connection
cache = redis.Redis(host='redis', port=6379)

@app.route('/')
def index():
    count = cache.incr('hits')
    return render_template('index.html', count=count)

# Remove any manual /metrics route — PrometheusMetrics handles it

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8082)

