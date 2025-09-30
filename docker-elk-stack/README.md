# Elasticsearch + Kibana single node and cluster and test service using docker

- I have useed the devopshobbies repo.<br />
<br />
Steps to setup and test:<br />
1- Git pull<br />
2- Edit the .env file.<br />
3- docker compose -f elk-single-node-compose.yml up -d or  docker compose -f elk-cluster-compose.yml up -d <br />
* For setup the elasticsearch and assign shards, your host needs enough ram and disk space and it can be the cause of any error on elasticsearch and kibana.<br />
4- Wait until all containers be up and healthy<br />
5- Access Kibana Console: Open http://localhost:5601 in your browser.<br />