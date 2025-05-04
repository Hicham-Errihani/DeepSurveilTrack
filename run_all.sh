#!/bin/bash

echo "🚀 Démarrage de Kafka & Zookeeper..."
cd docker/kafka
docker-compose up -d
cd ../../

echo "✅ Kafka est prêt !"
sleep 5

echo "🎬 Activation de l'environnement virtuel..."
source env/bin/activate

echo "📸 Lancement du producteur Kafka (en arrière-plan)..."
python3 src/producer/kafka_producer.py &

echo "🧠 Lancement du Spark Consumer..."
python3 src/consumer/spark_consumer.py
