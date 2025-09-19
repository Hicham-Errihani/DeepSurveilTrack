## 🚀 Introduction

**DeepSurveilTrack** est un prototype de surveillance vidéo en temps réel utilisant des technologies modernes telles que Kafka, PySpark (CNN+LSTM), et Elasticsearch. Ce système intelligent permet de traiter des flux vidéo en continu, d'analyser des événements en temps réel et d'afficher les résultats via une interface Streamlit. Le projet est conçu pour la surveillance en temps réel avec un traitement rapide des données et une intégration complète de l'IA pour l'analyse vidéo.

- 📡 Kafka gère le flux de vidéos en temps réel.
- 🔥 PySpark avec LSTM analyse les vidéos et génère des prédictions.
- 🔎 Elasticsearch est utilisé pour l'indexation des résultats et leur stockage.
- 📊 Streamlit fournit une interface de monitoring en temps réel.
## ⚙️ Installation

### Prérequis

- Python 3.x
- Docker & Docker Compose
- Kafka
- Elasticsearch

### Étapes d'installation

1. Clonez ce repository :
   ```bash
   git clone https://github.com/Hicham-Errihani/DeepSurveilTrack.git
   cd DeepSurveilTrack


# DeepSurveilTrack

🚀 **DeepSurveilTrack** is an **intelligent real-time video surveillance platform** built using a modern big data & AI stack.  
It demonstrates how to combine **Kafka, Spark Streaming, Deep Learning (CNN/LSTM), Elasticsearch, and Streamlit** into a scalable end-to-end pipeline.

> 🎓 Academic Project – ENSA Berrechid, Hassan 1st University  
> 👨‍💻 Author: **Hicham Errihani** | 2025

---

## 🌐 Project Overview

Traditional video surveillance systems are passive and rely on human monitoring.  
**DeepSurveilTrack** brings automation and intelligence by:

- Detecting **faces** and **abnormal behaviors** in real time.  
- Streaming video frames via **Apache Kafka**.  
- Processing them with **PySpark Streaming + Deep Learning models (CNN & LSTM)**.  
- Indexing events into **Elasticsearch**.  
- Displaying results in an interactive **Streamlit dashboard**.  

---

## 🛠️ Tech Stack

- **Programming**: Python 3.10, TensorFlow/Keras, OpenCV  
- **Streaming & Processing**: Apache Kafka 3.6, Apache Spark 3.5  
- **Datastore & Search**: Elasticsearch 8.x  
- **Visualization**: Streamlit 1.46, Kibana  
- **Infrastructure**: Docker, Docker Compose  
- **Version Control**: GitHub (SSH workflow)  

---

## 📂 Repository Structure

```bash
DeepSurveilTrack/
├── src/                        # Source code
│   ├── producer/
│   │   └── producer.py         # Kafka Producer – streams video frames
│   ├── consumer/
│   │   └── spark_consumer.py   # Spark Consumer – CNN+LSTM scoring, ES indexing
│
├── models/
│   └── cnn_model.py            # CNN (MobileNetV2-based feature extractor)
│
├── docs/
│   └── elasticsearch_mapping.json # Elasticsearch index mapping
│
├── dashboard.py                 # Streamlit monitoring dashboard
├── docker-compose.yml           # Infra: Kafka, Zookeeper, Spark, ES, Kibana
├── scripts/
│   └── run_all.sh               # Script to launch the entire pipeline
│
├── requirements.txt             # Python dependencies
├── .gitignore                   # Ignore rules (venv, cache, logs, etc.)
└── README.md                    # Project documentation

---

## 🚀 Quickstart

\`\`\`bash
# start infrastructure
docker compose up -d

# send frames
export DST_VIDEO=./sample.mp4
python src/producer/producer.py

# stream processing -> ES
spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.5 src/consumer/spark_consumer.py

# dashboard
streamlit run dashboard.py
\`\`\`

---

## 📊 Features

- ✅ Real-time video ingestion via **Kafka**  
- ✅ Parallel processing with **Spark Structured Streaming**  
- ✅ AI-based detection:
  - **CNN** (MobileNetV2) for face detection
  - **LSTM** for abnormal behavior scoring  
- ✅ Events indexed in **Elasticsearch**  
- ✅ **Interactive dashboard** (filters, charts, export)  
- ✅ **Scalable architecture** with Docker  

---

## 🔮 Future Improvements

- Replace CNN/LSTM with **Transformers**  
- Connect to **live cameras (RTSP/ONVIF)**  
- Add a **mobile app + incident map**  
- Kubernetes deployment with Helm  

---

## 📜 License

[MIT License](LICENSE) © 2025 Hicham Errihani
