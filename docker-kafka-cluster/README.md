# Kafka cluster and test service using docker

- You can find useful commands in the useful-command.txt file in the repo.<br />
<br />
Steps to setup and test:<br />
1- Git pull<br />
2- docker compose -f kafka-cluster-zookeeper.yml up -d or  docker compose -f kafka-cluster-controller.yml up <br />
3- Wait until all containers be up and healthy<br />
4- Access Redpanda Console: Open http://localhost:8080 in your browser.<br />
<br />
## Send Test Data<br />
1- Test the Service by test-app:<br />
Run this command:<br />
curl -X POST http://localhost:5000/send<br />
Every time you hit this endpoint, it will generate random data and send it <br />to test-topic1 in your Kafka cluster.
<br />
or<br />
<br />
docker exec -it kafka1 /opt/bitnami/kafka/bin/kafka-console-producer.sh \<br />
  --topic test-topic1 \<br />
  --bootstrap-server kafka1:9092<br />
<br />
Once this command runs, you can start typing messages, and they’ll be sent <br />to test-topic1.
<br />
<br />
2- Check messages from UI.<br />