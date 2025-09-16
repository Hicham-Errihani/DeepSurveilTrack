#!/usr/bin/env bash
set -euo pipefail

echo "[1/4] Lancement de l'infrastructure Docker..."
docker compose up -d

echo "[2/4] Création de l'index Elasticsearch (si absent)..."
curl -s -o /dev/null -X PUT "http://localhost:9200/events" \
  -H 'Content-Type: application/json' \
  -d @docs/elasticsearch_mapping.json || true

echo "[3/4] Démarrage du consumer Spark..."
spark-submit \
  --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.5 \
  src/consumer/spark_consumer.py &

echo "[4/4] Lancement du dashboard Streamlit..."
streamlit run dashboard.py
