# 🧠 Kafka Local – Exécution sans Docker

Ce dossier contient Kafka (v3.2.0) prêt à être lancé **localement sans Docker**, utile pour le débogage ou le développement hors conteneur.

---

## ⚙️ Prérequis

- Java installé (`java -version`)
- Port 2181 (Zookeeper) et 9092 (Kafka) libres

---

## 🚀 Lancer Kafka et Zookeeper en local

### 1. Démarrer ZooKeeper

```bash
cd docker/kafka_local
bin/zookeeper-server-start.sh config/zookeeper.properties
