# DeepSurveilTrack

DeepSurveilTrack is an intelligent video surveillance system designed for real-time behavioral analysis and incident detection. Built using cutting-edge technologies like Kafka, PySpark, Elasticsearch, and Deep Learning models, the system provides real-time alerts and insights into video data.

## Table of Contents

1. [Project Overview](#project-overview)
2. [Technologies Used](#technologies-used)
3. [Installation Instructions](#installation-instructions)
4. [Usage](#usage)
5. [Configuration](#configuration)
6. [Testing](#testing)
7. [Contributing](#contributing)
8. [License](#license)
9. [Acknowledgments](#acknowledgments)

## Project Overview

DeepSurveilTrack is designed for real-time surveillance in smart cities, providing analysis on behavior, incidents, and threats. The system leverages multiple deep learning models, including Convolutional Neural Networks (CNN) for face recognition and Long Short-Term Memory (LSTM) networks for behavioral analysis.

The system is built to scale and support distributed environments, leveraging technologies like **Apache Kafka** for real-time streaming, **Elasticsearch** for indexing and searching, and **Streamlit** for interactive visualization.

## Technologies Used

- **Kafka**: Messaging system for real-time data processing
- **PySpark**: Distributed data processing framework
- **Elasticsearch**: Search engine for data indexing
- **Deep Learning**: CNN (for face recognition), LSTM (for behavioral analysis)
- **Streamlit**: Framework for building interactive dashboards
- **Docker**: Containerization for deployment

## Installation Instructions

To set up DeepSurveilTrack on your local machine or server, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/DeepSurveilTrack.git
    cd DeepSurveilTrack
    ```

2. Create a virtual environment (if you haven't already):
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up Docker (if using Docker for deployment):
    ```bash
    docker-compose up
    ```

## Usage

Once the setup is complete, you can start the Streamlit app by running the following command:
```bash
streamlit run dashboard_attractif.py
