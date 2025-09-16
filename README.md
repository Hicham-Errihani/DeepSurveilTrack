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

\`\`\`
DeepSurveilTrack/
├─ src/
│  ├─ producer/producer.py       # Kafka producer (sends video frames)
│  ├─ consumer/spark_consumer.py # Spark consumer (CNN+LSTM scoring, ES indexing)
│
├─ models/
│  ├─ cnn_model.py               # CNN (MobileNetV2-based feature extractor)
│
├─ docs/
│  ├─ elasticsearch_mapping.json # ES index mapping
│
├─ dashboard.py                   # Streamlit monitoring UI
├─ docker-compose.yml             # Infrastructure: Kafka, Zookeeper, ES, Kibana, Spark
├─ scripts/run_all.sh             # Launches the entire pipeline
├─ requirements.txt
├─ .gitignore
└─ README.md
\`\`\`

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
