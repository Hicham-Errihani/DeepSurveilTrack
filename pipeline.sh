#!/bin/bash

# Récupère le dossier où se trouve ce script
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR" || exit

case "$1" in
  start)
    echo "🚀 Lancement du pipeline complet..."
    
    cd "$SCRIPT_DIR/docker/kafka" || exit
    sudo docker compose up -d
    cd "$SCRIPT_DIR" || exit

    echo "⏳ Attente que Kafka soit prêt..."
    until nc -z localhost 9092; do
      echo "🔄 Kafka pas encore prêt, on attend 2s..."
      sleep 2
    done
    echo "✅ Kafka est prêt !"

    echo "🎬 Activation de l'environnement virtuel..."
    source "$SCRIPT_DIR/venv/bin/activate"

    echo "📸 Lancement du producteur Kafka (en arrière-plan)..."
    python3 "$SCRIPT_DIR/src/producer/kafka_producer.py" &

    echo "🧠 Lancement du Spark Consumer..."
    python3 "$SCRIPT_DIR/src/consumer/spark_consumer.py"
    ;;

  stop)
    echo "🛑 Arrêt du pipeline..."
    sudo docker stop kafka zookeeper
    pkill -f kafka_producer.py
    pkill -f spark_consumer.py
    echo "✅ Tous les composants sont arrêtés"
    ;;

  status)
    echo "📊 État des conteneurs Docker :"
    sudo docker ps
    ;;

  *)
    echo "❌ Usage incorrect"
    echo "✅ Utilisation : $0 {start|stop|status}"
    exit 1
    ;;
esac
