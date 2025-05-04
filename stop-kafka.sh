#!/bin/bash

echo "🛑 Arrêt de Kafka et Zookeeper..."

# Arrêt de Kafka
pkill -f kafka.Kafka

# Arrêt de Zookeeper
pkill -f zookeeper

echo "✅ Processus Kafka et Zookeeper arrêtés."
