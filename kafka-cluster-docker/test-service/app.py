from flask import Flask, jsonify
from kafka import KafkaProducer
import json
import random

app = Flask(__name__)

# Kafka Producer setup
producer = KafkaProducer(
    bootstrap_servers=['kafka1:9092'],  # Use the Kafka broker address
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

@app.route('/send', methods=['POST'])
def send_data():
    data = {
        'id': random.randint(1, 100),
        'value': random.random()
    }
    producer.send('test-topic1', value=data)
    producer.flush()
    return jsonify({'status': 'success', 'data': data})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
