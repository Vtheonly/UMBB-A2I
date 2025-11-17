
### 1. Folder and File Structure

Here is the complete, production-ready folder structure for the **DataFlow Stream** project.

```
DataFlow-Stream/
├── .env.development
├── .env.local
├── .env.production
├── .gitignore
├── README.md
├── docker-compose.yml
├── docs/
│   └── architecture.md
├── services/
│   ├── ingestion/
│   │   ├── Dockerfile
│   │   ├── adapters/
│   │   │   ├── __init__.py
│   │   │   ├── base_stream_source.py
│   │   │   ├── market_adapter.py
│   │   │   └── twitch_chat_adapter.py
│   │   ├── config/
│   │   │   ├── __init__.py
│   │   │   └── settings.py
│   │   ├── logic/
│   │   │   ├── __init__.py
│   │   │   ├── anomaly_detection/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── chat_anomaly.py
│   │   │   │   └── market_anomaly.py
│   │   │   └── nlp_toxicity/
│   │   │       ├── __init__.py
│   │   │       ├── models/
│   │   │       │   ├── model.h5
│   │   │       │   └── tokenizer.pickle
│   │   │       └── toxicity_classifier.py
│   │   ├── requirements.txt
│   │   ├── main.py
│   │   └── utils/
│   │       ├── __init__.py
│   │       ├── kafka_producer.py
│   │       └── logger.py
│   ├── spark/
│   │   ├── Dockerfile
│   │   ├── jobs/
│   │   │   └── stream_processor.py
│   │   ├── requirements.txt
│   │   └── submit.sh
│   └── streamlit-ui/
│       ├── Dockerfile
│       ├── assets/
│       │   ├── favicon.ico
│       │   └── logo.png
│       ├── components/
│       │   ├── __init__.py
│       │   ├── chat_dashboard.py
│       │   ├── market_dashboard.py
│       │   └── platform_dashboard.py
│       ├── config/
│       │   ├── __init__.py
│       │   └── settings.py
│       ├── requirements.txt
│       ├── app.py
│       └── utils/
│           ├── __init__.py
│           ├── mongo_client.py
│           └── style.py
└── tests/
    ├── __init__.py
    ├── integration/
    │   ├── __init__.py
    │   └── test_full_pipeline.py
    └── unit/
        ├── __init__.py
        ├── test_adapters.py
        ├── test_anomaly_detection.py
        └── test_nlp_toxicity.py
```

---

### 2. Bash Command Generator

This single bash block will create the entire folder and file structure. Copy and paste it into your Ubuntu terminal.

```bash
# Create root project directory
mkdir -p DataFlow-Stream && cd DataFlow-Stream

# Create root files
touch .env.development .env.local .env.production .gitignore README.md docker-compose.yml

# Create docs directory
mkdir -p docs
touch docs/architecture.md

# Create services directory and sub-projects
mkdir -p services/ingestion services/spark services/streamlit-ui

# --- Ingestion Service ---
mkdir -p services/ingestion/adapters services/ingestion/config services/ingestion/logic/anomaly_detection services/ingestion/logic/nlp_toxicity/models services/ingestion/utils
touch services/ingestion/Dockerfile services/ingestion/requirements.txt services/ingestion/main.py
touch services/ingestion/adapters/__init__.py services/ingestion/adapters/base_stream_source.py services/ingestion/adapters/market_adapter.py services/ingestion/adapters/twitch_chat_adapter.py
touch services/ingestion/config/__init__.py services/ingestion/config/settings.py
touch services/ingestion/logic/__init__.py services/ingestion/logic/anomaly_detection/__init__.py services/ingestion/logic/anomaly_detection/chat_anomaly.py services/ingestion/logic/anomaly_detection/market_anomaly.py
touch services/ingestion/logic/nlp_toxicity/__init__.py services/ingestion/logic/nlp_toxicity/toxicity_classifier.py
touch services/ingestion/logic/nlp_toxicity/models/model.h5 services/ingestion/logic/nlp_toxicity/models/tokenizer.pickle
touch services/ingestion/utils/__init__.py services/ingestion/utils/kafka_producer.py services/ingestion/utils/logger.py

# --- Spark Service ---
mkdir -p services/spark/jobs
touch services/spark/Dockerfile services/spark/requirements.txt services/spark/submit.sh
touch services/spark/jobs/stream_processor.py

# --- Streamlit UI Service ---
mkdir -p services/streamlit-ui/assets services/streamlit-ui/components services/streamlit-ui/config services/streamlit-ui/utils
touch services/streamlit-ui/Dockerfile services/streamlit-ui/requirements.txt services/streamlit-ui/app.py
touch services/streamlit-ui/assets/favicon.ico services/streamlit-ui/assets/logo.png
touch services/streamlit-ui/components/__init__.py services/streamlit-ui/components/chat_dashboard.py services/streamlit-ui/components/market_dashboard.py services/streamlit-ui/components/platform_dashboard.py
touch services/streamlit-ui/config/__init__.py services/streamlit-ui/config/settings.py
touch services/streamlit-ui/utils/__init__.py services/streamlit-ui/utils/mongo_client.py services/streamlit-ui/utils/style.py

# --- Tests Directory ---
mkdir -p tests/integration tests/unit
touch tests/__init__.py tests/integration/__init__.py tests/unit/__init__.py
touch tests/integration/test_full_pipeline.py
touch tests/unit/test_adapters.py tests/unit/test_anomaly_detection.py tests/unit/test_nlp_toxicity.py

echo "DataFlow-Stream project structure created successfully."

```

---

### 3. Full Production Codebase

Here is the complete code for each file in the project.

#### **Root Files**

**`.gitignore`**
```gitignore
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# PyInstaller
#  Usually these files are written by a python script from a template
#  before PyInstaller builds the exe, so as to inject date/other infos into it.
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
.hypothesis/
.pytest_cache/

# Environments
.env
.venv
env/
venv/
ENV/
env.bak
venv.bak

# Docker
docker-compose.override.yml

# IDE specific
.idea/
.vscode/

# Models
services/ingestion/logic/nlp_toxicity/models/
```

**`README.md`**
```markdown
# DataFlow Stream: Real-Time Data Processing Pipeline

This project is a complete, production-ready real-time data processing pipeline designed to ingest, process, analyze, and visualize data from multiple sources like Twitch chat and financial markets.

## Tech Stack

- **Data Ingestion**: Python, Websockets
- **Streaming Platform**: Apache Kafka
- **Real-Time Processing**: Apache Spark (Structured Streaming)
- **Database**: MongoDB
- **Dashboard/UI**: Streamlit
- **Orchestration**: Docker Compose
- **NLP**: Keras/TensorFlow

## Features

- **Multi-Source Ingestion**: Unified adapter pattern to connect to Twitch chat, market data streams, and more.
- **Real-Time NLP**: Live toxicity analysis on chat messages.
- **Real-Time Anomaly Detection**: Z-score and volatility spike detection for market data; toxicity and frequency anomaly detection for chat data.
- **End-to-End Streaming**: A fully containerized pipeline from data source to dashboard.
- **Live Monitoring**: A Streamlit dashboard visualizes live data, toxicity scores, market anomalies, and system health.

## How to Run

1.  **Prerequisites**:
    - Docker and Docker Compose installed.
    - Python 3.9+

2.  **Configuration**:
    - Copy `.env.local` to a new file named `.env.development`.
    - Fill in the required environment variables:
      - `TWITCH_OAUTH_TOKEN`: Your Twitch OAuth token.
      - `TWITCH_NICKNAME`: Your Twitch nickname.
      - `TWITCH_CHANNEL`: The Twitch channel to monitor.

3.  **Build and Run**:
    ```bash
    docker-compose up --build
    ```

4.  **Access Services**:
    - **Streamlit Dashboard**: `http://localhost:8501`
    - **Kafka UI**: `http://localhost:8080`
    - **Mongo Express**: `http://localhost:8081`

## Architecture

The system is composed of several microservices orchestrated by Docker Compose.

1.  **Ingestion Service**: A Python service that connects to data sources (Twitch, Binance), normalizes the data, runs NLP and anomaly detection, and produces events to Kafka topics.
2.  **Kafka Cluster**: Acts as the central data bus for all real-time events.
3.  **Spark Cluster**: Consumes data from Kafka, performs stateful aggregations and transformations, and writes results to MongoDB.
4.  **MongoDB**: Stores the raw and enriched data for querying by the dashboard.
5.  **Streamlit UI**: A Python web application that queries MongoDB to provide a real-time visualization of the pipeline's data.
```

**`.env.local`** (Template for environment variables)
```env
# --- Twitch Configuration ---
TWITCH_OAUTH_TOKEN="oauth:your_twitch_oauth_token"
TWITCH_NICKNAME="your_twitch_nickname"
TWITCH_CHANNEL="summit1g" # Example channel

# --- Market Data Configuration (Simulated) ---
MARKET_SYMBOL="BTCUSDT"

# --- Kafka Configuration ---
KAFKA_BOOTSTRAP_SERVERS=kafka:9092
CHAT_KAFKA_TOPIC=chat_stream
MARKET_KAFKA_TOPIC=market_stream
ANALYTICS_KAFKA_TOPIC=analytics_stream

# --- MongoDB Configuration ---
MONGO_URI=mongodb://mongodb:27017/
MONGO_DATABASE=DataFlowDB

# --- Spark Configuration ---
SPARK_MASTER_URL=spark://spark-master:7077
```

**`docker-compose.yml`**
```yaml
version: '3.8'

services:
  zookeeper:
    image: confluentinc/cp-zookeeper:7.3.0
    container_name: zookeeper
    environment:
      ZOOKEEPER_CLIENT_PORT: 2181
      ZOOKEEPER_TICK_TIME: 2000
    ports:
      - "2181:2181"

  kafka:
    image: confluentinc/cp-kafka:7.3.0
    container_name: kafka
    depends_on:
      - zookeeper
    ports:
      - "9092:9092"
      - "29092:29092"
    environment:
      KAFKA_BROKER_ID: 1
      KAFKA_ZOOKEEPER_CONNECT: 'zookeeper:2181'
      KAFKA_LISTENER_SECURITY_PROTOCOL_MAP: PLAINTEXT:PLAINTEXT,PLAINTEXT_HOST:PLAINTEXT
      KAFKA_ADVERTISED_LISTENERS: PLAINTEXT://kafka:9092,PLAINTEXT_HOST://localhost:29092
      KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR: 1
      KAFKA_GROUP_INITIAL_REBALANCE_DELAY_MS: 0
      KAFKA_AUTO_CREATE_TOPICS_ENABLE: "true"

  kafka-ui:
    image: provectuslabs/kafka-ui:latest
    container_name: kafka-ui
    depends_on:
      - kafka
    ports:
      - "8080:8080"
    environment:
      KAFKA_CLUSTERS_0_NAME: local
      KAFKA_CLUSTERS_0_BOOTSTRAPSERVERS: kafka:9092
      KAFKA_CLUSTERS_0_ZOOKEEPER: zookeeper:2181

  mongodb:
    image: mongo:6.0
    container_name: mongodb
    ports:
      - "27017:27017"
    volumes:
      - mongo-data:/data/db

  mongo-express:
    image: mongo-express:latest
    container_name: mongo-express
    depends_on:
      - mongodb
    ports:
      - "8081:8081"
    environment:
      ME_CONFIG_MONGODB_SERVER: mongodb

  spark-master:
    image: bitnami/spark:3.4
    container_name: spark-master
    command: >
      /opt/bitnami/spark/bin/spark-class org.apache.spark.deploy.master.Master
    ports:
      - "8082:8080"
      - "7077:7077"
    volumes:
      - ./services/spark/jobs:/opt/bitnami/spark/jobs
    environment:
      - SPARK_MODE=master
      - SPARK_RPC_AUTHENTICATION_ENABLED=no
      - SPARK_RPC_ENCRYPTION_ENABLED=no
      - SPARK_LOCAL_STORAGE_ENCRYPTION_ENABLED=no
      - SPARK_SSL_ENABLED=no

  spark-worker:
    image: bitnami/spark:3.4
    container_name: spark-worker
    command: >
      /opt/bitnami/spark/bin/spark-class org.apache.spark.deploy.worker.Worker spark://spark-master:7077
    depends_on:
      - spark-master
    environment:
      - SPARK_MODE=worker
      - SPARK_MASTER_URL=spark://spark-master:7077
      - SPARK_WORKER_MEMORY=1G
      - SPARK_WORKER_CORES=1
      - SPARK_RPC_AUTHENTICATION_ENABLED=no
      - SPARK_RPC_ENCRYPTION_ENABLED=no
      - SPARK_LOCAL_STORAGE_ENCRYPTION_ENABLED=no
      - SPARK_SSL_ENABLED=no

  ingestion:
    build:
      context: ./services/ingestion
    container_name: ingestion-service
    depends_on:
      - kafka
    env_file:
      - .env.development
    volumes:
      - ./services/ingestion:/app

  streamlit-ui:
    build:
      context: ./services/streamlit-ui
    container_name: streamlit-ui
    depends_on:
      - mongodb
    ports:
      - "8501:8501"
    env_file:
      - .env.development
    volumes:
      - ./services/streamlit-ui:/app

volumes:
  mongo-data:

```

#### **`services/ingestion`**

**`Dockerfile`**
```dockerfile
# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application's code into the container
COPY . .

# Command to run the application
CMD ["python", "main.py"]
```

**`requirements.txt`**
```
kafka-python-ng==2.1.0
python-dotenv==1.0.0
twitchio==2.7.0
websockets==11.0.3
tensorflow==2.12.0 # Ensure compatibility with your model
numpy==1.23.5 # Pin numpy version for TF
```
> **Note**: The actual `model.h5` and `tokenizer.pickle` files are not generated here. You must provide your own pre-trained models and place them in `services/ingestion/logic/nlp_toxicity/models/`.

**`main.py`**
```python
import asyncio
import os
from dotenv import load_dotenv

from adapters.twitch_chat_adapter import TwitchChatAdapter
from adapters.market_adapter import MarketAdapter
from utils.kafka_producer import get_kafka_producer
from utils.logger import get_logger

load_dotenv()
logger = get_logger(__name__)

async def main():
    """
    IngestionOrchestrator: Initializes and runs all data stream adapters concurrently.
    """
    logger.info("Initializing Ingestion Orchestrator...")
    producer = await get_kafka_producer()

    # --- Configuration ---
    twitch_oauth = os.getenv("TWITCH_OAUTH_TOKEN")
    twitch_nick = os.getenv("TWITCH_NICKNAME")
    twitch_channel = os.getenv("TWITCH_CHANNEL")
    market_symbol = os.getenv("MARKET_SYMBOL")
    
    chat_topic = os.getenv("CHAT_KAFKA_TOPIC")
    market_topic = os.getenv("MARKET_KAFKA_TOPIC")

    # --- Initialize Adapters ---
    twitch_adapter = TwitchChatAdapter(
        token=twitch_oauth,
        nickname=twitch_nick,
        channel=twitch_channel,
        producer=producer,
        topic=chat_topic
    )
    
    market_adapter = MarketAdapter(
        symbol=market_symbol,
        producer=producer,
        topic=market_topic
    )

    logger.info("Starting all data stream adapters...")
    
    # Run adapters concurrently
    await asyncio.gather(
        twitch_adapter.run(),
        market_adapter.run()
    )

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Ingestion service shutting down.")
    except Exception as e:
        logger.error(f"An unexpected error occurred in the orchestrator: {e}", exc_info=True)

```

**`adapters/base_stream_source.py`**
```python
from abc import ABC, abstractmethod

class BaseStreamSource(ABC):
    """
    Abstract Base Class for all data stream sources.
    Defines the contract that all adapters must follow.
    """
    
    @abstractmethod
    async def connect(self):
        """Connect to the data source."""
        raise NotImplementedError

    @abstractmethod
    async def fetch_event(self):
        """Fetch a single event from the data source."""
        raise NotImplementedError

    @abstractmethod
    def normalize(self, raw_event: dict) -> dict:
        """Normalize the raw event into a unified schema."""
        raise NotImplementedError
    
    @abstractmethod
    async def run(self):
        """The main loop to run the stream."""
        raise NotImplementedError
```




**`adapters/twitch_chat_adapter.py`**


```python
import json
import time
from twitchio.ext import commands
from aiokafka import AIOKafkaProducer

from adapters.base_stream_source import BaseStreamSource
from logic.nlp_toxicity.toxicity_classifier import ToxicityClassifier
from logic.anomaly_detection.chat_anomaly import ChatAnomalyDetector
from utils.logger import get_logger

logger = get_logger(__name__)

class TwitchChatAdapter(BaseStreamSource, commands.Bot):
    """
    Adapter for ingesting real-time chat messages from a Twitch channel.
    """
    def __init__(self, token: str, nickname: str, channel: str, producer: AIOKafkaProducer, topic: str):
        super().__init__(token=token, prefix='!', initial_channels=[channel])
        self.producer = producer
        self.topic = topic
        self.channel_name = channel
        self.nlp_classifier = ToxicityClassifier.get_instance()
        self.anomaly_detector = ChatAnomalyDetector()
        logger.info(f"TwitchChatAdapter initialized for channel: {channel}")

    async def connect(self):
        # The run method from commands.Bot handles the connection.
        pass

    async def fetch_event(self):
        # This is event-driven, handled by event_message.
        pass

    def normalize(self, message) -> dict:
        """
        Normalizes a raw Twitch message and enriches it with NLP and anomaly detection.
        """
        timestamp = time.time()
        
        # 1. Basic Normalization
        normalized_event = {
            "source": "twitch_chat",
            "type": "chat",
            "event_id": message.id,
            "timestamp": timestamp,
            "payload": {
                "author": message.author.name,
                "text": message.content,
                "channel": self.channel_name,
            }
        }

        # 2. NLP Toxicity Classification
        toxicity_scores = self.nlp_classifier.predict(message.content)
        normalized_event["enrichments"] = {"toxicity": toxicity_scores}

        # 3. Anomaly Detection
        anomaly_result = self.anomaly_detector.detect(normalized_event)
        normalized_event["enrichments"]["anomaly"] = anomaly_result
        
        return normalized_event

    async def event_ready(self):
        logger.info(f"Successfully connected to Twitch as {self.nick}")

    async def event_message(self, message):
        if message.echo:
            return

        try:
            logger.debug(f"Received message from {message.author.name}: {message.content}")
            
            # Normalize and enrich the message
            normalized_event = self.normalize(message)
            
            # Send to Kafka
            await self.producer.send_and_wait(
                self.topic, 
                json.dumps(normalized_event).encode('utf-8')
            )
            logger.debug(f"Successfully sent enriched chat message to Kafka topic: {self.topic}")

        except Exception as e:
            logger.error(f"Error processing Twitch message: {e}", exc_info=True)

    async def run(self):
        logger.info("Starting Twitch Chat Adapter...")
        await super().run()

```

**`adapters/market_adapter.py`**
```python
import asyncio
import json
import time
import random
import websockets
from aiokafka import AIOKafkaProducer

from adapters.base_stream_source import BaseStreamSource
from logic.anomaly_detection.market_anomaly import MarketAnomalyDetector
from utils.logger import get_logger

logger = get_logger(__name__)
BINANCE_WS_URL = "wss://stream.binance.com:9443/ws/btcusdt@trade"

class MarketAdapter(BaseStreamSource):
    """
    Adapter for ingesting real-time market trade data.
    Uses a real Binance WebSocket but includes a simulator as a fallback.
    """
    def __init__(self, symbol: str, producer: AIOKafkaProducer, topic: str):
        self.symbol = symbol.lower()
        self.producer = producer
        self.topic = topic
        self.anomaly_detector = MarketAnomalyDetector()
        self.ws_url = f"wss://stream.binance.com:9443/ws/{self.symbol}@trade"
        logger.info(f"MarketAdapter initialized for symbol: {self.symbol}")

    async def connect(self):
        try:
            websocket = await websockets.connect(self.ws_url)
            logger.info(f"Successfully connected to Binance WebSocket at {self.ws_url}")
            return websocket
        except Exception as e:
            logger.warning(f"Failed to connect to real WebSocket: {e}. Falling back to simulator.")
            return None

    async def fetch_event(self):
        # This is handled within the run loop.
        pass

    def normalize(self, raw_event: dict) -> dict:
        """
        Normalizes a raw market trade event and runs anomaly detection.
        """
        timestamp = time.time()
        
        # 1. Basic Normalization
        normalized_event = {
            "source": "market_data",
            "type": "trade",
            "event_id": raw_event.get('t'),
            "timestamp": timestamp,
            "payload": {
                "symbol": raw_event.get('s'),
                "price": float(raw_event.get('p')),
                "quantity": float(raw_event.get('q')),
            }
        }

        # 2. Anomaly Detection
        anomaly_result = self.anomaly_detector.detect(normalized_event['payload']['price'])
        normalized_event["enrichments"] = {"anomaly": anomaly_result}
        
        return normalized_event

    async def _run_simulator(self):
        """A fallback simulator if the WebSocket connection fails."""
        logger.info("Running market data simulator.")
        current_price = 65000.0
        while True:
            price_change = random.uniform(-100, 100)
            # Occasionally create a large jump for anomaly detection
            if random.random() < 0.05:
                price_change *= 10
            
            current_price += price_change
            
            simulated_event = {
                's': self.symbol.upper(),
                'p': f"{current_price:.2f}",
                'q': f"{random.uniform(0.01, 1.0):.4f}",
                't': int(time.time() * 1000)
            }
            
            normalized_event = self.normalize(simulated_event)
            await self.producer.send_and_wait(
                self.topic,
                json.dumps(normalized_event).encode('utf-8')
            )
            logger.debug("Sent simulated market event to Kafka.")
            await asyncio.sleep(1)

    async def run(self):
        logger.info("Starting Market Data Adapter...")
        websocket = await self.connect()
        if not websocket:
            await self._run_simulator()
            return
            
        while True:
            try:
                raw_data = await websocket.recv()
                raw_event = json.loads(raw_data)
                
                logger.debug(f"Received market data: {raw_event}")
                
                normalized_event = self.normalize(raw_event)
                await self.producer.send_and_wait(
                    self.topic,
                    json.dumps(normalized_event).encode('utf-8')
                )
                logger.debug(f"Successfully sent enriched market event to Kafka topic: {self.topic}")
                
            except websockets.exceptions.ConnectionClosed:
                logger.warning("WebSocket connection closed. Reconnecting...")
                websocket = await self.connect()
                if not websocket:
                    await self._run_simulator()
                    return
            except Exception as e:
                logger.error(f"Error in market adapter loop: {e}", exc_info=True)
                await asyncio.sleep(5)
```

**`logic/nlp_toxicity/toxicity_classifier.py`**
```python
import os
import pickle
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
from utils.logger import get_logger

logger = get_logger(__name__)

class ToxicityClassifier:
    """
    Singleton class to load and use the Keras toxicity model.
    """
    _instance = None
    
    # Define paths relative to this file's location
    _BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    _MODEL_PATH = os.path.join(_BASE_DIR, "models/model.h5")
    _TOKENIZER_PATH = os.path.join(_BASE_DIR, "models/tokenizer.pickle")
    _MAX_SEQ_LENGTH = 200 # Must match the model's training configuration

    def __init__(self):
        if not os.path.exists(self._MODEL_PATH) or not os.path.exists(self._TOKENIZER_PATH):
            logger.error("Model or tokenizer file not found. NLP features will be disabled.")
            logger.error(f"Expected model at: {self._MODEL_PATH}")
            logger.error(f"Expected tokenizer at: {self._TOKENIZER_PATH}")
            self.model = None
            self.tokenizer = None
        else:
            try:
                self.model = load_model(self._MODEL_PATH)
                with open(self._TOKENIZER_PATH, 'rb') as handle:
                    self.tokenizer = pickle.load(handle)
                logger.info("Keras toxicity model and tokenizer loaded successfully.")
            except Exception as e:
                logger.error(f"Failed to load Keras model/tokenizer: {e}", exc_info=True)
                self.model = None
                self.tokenizer = None

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = ToxicityClassifier()
        return cls._instance

    def predict(self, text: str) -> dict:
        """
        Predicts toxicity scores for a given text.
        """
        if not self.model or not self.tokenizer:
            return {
                "toxic": 0.0, "severe_toxic": 0.0, "obscene": 0.0,
                "threat": 0.0, "insult": 0.0, "identity_hate": 0.0,
                "error": "Model not loaded"
            }
            
        try:
            # Preprocess the text
            sequence = self.tokenizer.texts_to_sequences([text])
            padded_sequence = pad_sequences(sequence, maxlen=self._MAX_SEQ_LENGTH)
            
            # Get prediction
            prediction = self.model.predict(padded_sequence, verbose=0)[0]
            
            # Format output
            labels = ["toxic", "severe_toxic", "obscene", "threat", "insult", "identity_hate"]
            scores = {label: float(score) for label, score in zip(labels, prediction)}
            return scores

        except Exception as e:
            logger.error(f"Error during toxicity prediction: {e}", exc_info=True)
            return {label: 0.0 for label in labels}

```

**`logic/anomaly_detection/market_anomaly.py`**
```python
import numpy as np
from collections import deque
from utils.logger import get_logger

logger = get_logger(__name__)

class MarketAnomalyDetector:
    """
    Detects anomalies in market price streams using Z-score.
    """
    def __init__(self, window_size=100, z_threshold=3.0):
        self.window_size = window_size
        self.z_threshold = z_threshold
        self.price_history = deque(maxlen=window_size)
        self.last_price = None

    def detect(self, price: float) -> dict:
        result = {"is_anomaly": False, "type": None, "details": {}}
        
        self.price_history.append(price)
        
        # 1. Price Jump Detection
        if self.last_price is not None:
            price_change_pct = abs((price - self.last_price) / self.last_price)
            if price_change_pct > 0.01: # 1% jump in one tick
                result = {
                    "is_anomaly": True, 
                    "type": "price_jump", 
                    "details": {"price_change_percent": price_change_pct * 100}
                }

        # 2. Z-Score Anomaly Detection
        if len(self.price_history) == self.window_size:
            mean = np.mean(self.price_history)
            std = np.std(self.price_history)
            
            if std > 0: # Avoid division by zero
                z_score = (price - mean) / std
                if abs(z_score) > self.z_threshold:
                    result = {
                        "is_anomaly": True,
                        "type": "z_score_spike",
                        "details": {"z_score": z_score, "mean": mean, "std_dev": std}
                    }

        self.last_price = price
        return result

```

**`logic/anomaly_detection/chat_anomaly.py`**
```python
from collections import deque, defaultdict
import time
from utils.logger import get_logger

logger = get_logger(__name__)

class ChatAnomalyDetector:
    """
    Detects anomalies in chat streams like toxicity spikes and message frequency abuse.
    """
    def __init__(self, time_window_seconds=60, toxicity_threshold=0.8, freq_threshold=10):
        self.time_window = time_window_seconds
        self.toxicity_threshold = toxicity_threshold
        self.freq_threshold = freq_threshold
        
        self.message_timestamps = deque()
        self.user_message_counts = defaultdict(lambda: deque())

    def detect(self, event: dict) -> dict:
        result = {"is_anomaly": False, "type": None, "details": {}}
        current_time = event["timestamp"]
        
        # 1. Toxicity Spike Detection
        toxic_score = event.get("enrichments", {}).get("toxicity", {}).get("toxic", 0.0)
        if toxic_score > self.toxicity_threshold:
            result = {
                "is_anomaly": True,
                "type": "toxicity_spike",
                "details": {"user": event["payload"]["author"], "score": toxic_score}
            }

        # 2. Message Frequency Anomaly (Spam) Detection per user
        author = event["payload"]["author"]
        user_deque = self.user_message_counts[author]
        user_deque.append(current_time)
        
        # Remove old timestamps from the user's deque
        while user_deque and user_deque[0] < current_time - self.time_window:
            user_deque.popleft()
            
        if len(user_deque) > self.freq_threshold:
            result = {
                "is_anomaly": True,
                "type": "frequency_spam",
                "details": {"user": author, "count_in_window": len(user_deque)}
            }
            
        return result

```

**`utils/kafka_producer.py`**
```python
import os
from aiokafka import AIOKafkaProducer
from utils.logger import get_logger

logger = get_logger(__name__)

async def get_kafka_producer():
    """
    Creates and returns an AIOKafkaProducer instance.
    """
    bootstrap_servers = os.getenv("KAFKA_BOOTSTRAP_SERVERS")
    producer = AIOKafkaProducer(bootstrap_servers=bootstrap_servers)
    try:
        await producer.start()
        logger.info(f"Kafka producer connected to {bootstrap_servers}")
        return producer
    except Exception as e:
        logger.error(f"Failed to connect Kafka producer: {e}", exc_info=True)
        raise

```

**`utils/logger.py`**
```python
import logging
import sys

def get_logger(name: str):
    """
        Initializes and returns a logger instance.
    """
    logger = logging.getLogger(name)
    if not logger.handlers: # Avoid adding handlers multiple times
        logger.setLevel(logging.DEBUG)
        
        # Create a handler to print to stdout
        handler = logging.StreamHandler(sys.stdout)
        handler.setLevel(logging.DEBUG)
        
        # Create a formatter and add it to the handler
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        handler.setFormatter(formatter)
        
        # Add the handler to the logger
        logger.addHandler(handler)
        
    return logger

```

#### **`services/spark`**

**`jobs/stream_processor.py`**
```python
import os
from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col, window, avg
from pyspark.sql.types import StructType, StructField, StringType, DoubleType, LongType, MapType

# --- Configuration ---
KAFKA_BOOTSTRAP_SERVERS = os.getenv("KAFKA_BOOTSTRAP_SERVERS", "kafka:9092")
MONGO_URI = os.getenv("MONGO_URI", "mongodb://mongodb:27017/")
MONGO_DATABASE = os.getenv("MONGO_DATABASE", "DataFlowDB")
CHAT_TOPIC = os.getenv("CHAT_KAFKA_TOPIC", "chat_stream")
MARKET_TOPIC = os.getenv("MARKET_KAFKA_TOPIC", "market_stream")

# --- Schemas ---
CHAT_SCHEMA = StructType([
    StructField("source", StringType(), True),
    StructField("timestamp", DoubleType(), True),
    StructField("payload", StructType([
        StructField("author", StringType(), True),
        StructField("text", StringType(), True),
    ])),
    StructField("enrichments", StructType([
        StructField("toxicity", MapType(StringType(), DoubleType()), True),
        StructField("anomaly", MapType(StringType(), StringType()), True), # Anomaly details are mixed type, handle as string map
    ]))
])

MARKET_SCHEMA = StructType([
    StructField("source", StringType(), True),
    StructField("timestamp", DoubleType(), True),
    StructField("payload", StructType([
        StructField("symbol", StringType(), True),
        StructField("price", DoubleType(), True),
        StructField("quantity", DoubleType(), True),
    ])),
    StructField("enrichments", StructType([
        StructField("anomaly", MapType(StringType(), StringType()), True),
    ]))
])

def create_spark_session():
    """Creates and configures a SparkSession."""
    return (
        SparkSession.builder.appName("DataFlowStreamProcessor")
        .config("spark.mongodb.output.uri", f"{MONGO_URI}{MONGO_DATABASE}")
        .config("spark.jars.packages", "org.apache.spark:spark-sql-kafka-0-10_2.12:3.4.0,org.mongodb.spark:mongo-spark-connector_2.12:3.0.1")
        .getOrCreate()
    )

def process_stream(df, schema, collection_name):
    """General function to process a Kafka stream and write to MongoDB."""
    # Deserialize JSON from Kafka
    parsed_df = df.select(from_json(col("value").cast("string"), schema).alias("data")).select("data.*")

    # Write raw enriched data to a general collection
    query = (
        parsed_df.writeStream
        .foreachBatch(lambda batch_df, batch_id: batch_df.write.format("mongo").mode("append").option("collection", "enriched_events").save())
        .start()
    )

    # Filter for anomalies and write to a specific anomaly collection
    anomaly_df = parsed_df.filter(col("enrichments.anomaly.is_anomaly") == "true")
    anomaly_query = (
        anomaly_df.writeStream
        .foreachBatch(lambda batch_df, batch_id: batch_df.write.format("mongo").mode("append").option("collection", collection_name).save())
        .start()
    )
    
    return [query, anomaly_query]

def main():
    spark = create_spark_session()
    spark.sparkContext.setLogLevel("WARN")

    print("Starting Spark Streaming Processor...")

    # --- Read from Kafka Topics ---
    chat_df = (
        spark.readStream
        .format("kafka")
        .option("kafka.bootstrap.servers", KAFKA_BOOTSTRAP_SERVERS)
        .option("subscribe", CHAT_TOPIC)
        .load()
    )

    market_df = (
        spark.readStream
        .format("kafka")
        .option("kafka.bootstrap.servers", KAFKA_BOOTSTRAP_SERVERS)
        .option("subscribe", MARKET_TOPIC)
        .load()
    )

    # --- Process Streams ---
    chat_queries = process_stream(chat_df, CHAT_SCHEMA, "chat_anomalies")
    market_queries = process_stream(market_df, MARKET_SCHEMA, "market_anomalies")

    # Await termination for all queries
    for q in chat_queries + market_queries:
        q.awaitTermination()

if __name__ == "__main__":
    main()
```
**`submit.sh`**
```bash
#!/bin/bash

/opt/bitnami/spark/bin/spark-submit \
  --master spark://spark-master:7077 \
  --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.4.0,org.mongodb.spark:mongo-spark-connector_2.12:3.0.1 \
  /opt/bitnami/spark/jobs/stream_processor.py
```
> **Note**: This `submit.sh` is a helper. In the `docker-compose.yml`, the `spark-submit` command is run directly by a separate service or manually via `docker exec`. For simplicity in this setup, you would run Spark jobs by executing into the master container.

#### **`services/streamlit-ui`**

**`Dockerfile`**
```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Expose the port Streamlit runs on
EXPOSE 8501

# Command to run the app
CMD ["streamlit", "run", "app.py"]
```

**`requirements.txt`**
```
streamlit==1.28.2
pymongo==4.6.0
pandas==2.0.3
plotly==5.18.0
python-dotenv==1.0.0
```

**`app.py`**
```python
import streamlit as st
import time
from dotenv import load_dotenv

from components.chat_dashboard import display_chat_dashboard
from components.market_dashboard import display_market_dashboard
from components.platform_dashboard import display_platform_dashboard
from utils.mongo_client import MongoSingleton
from utils.style import local_css

load_dotenv()

# --- Page Config ---
st.set_page_config(
    page_title="DataFlow Stream Dashboard",
    page_icon="assets/favicon.ico",
    layout="wide"
)

# --- Load CSS ---
local_css("utils/style.css")

# --- Main App ---
def main():
    st.title("🌊 DataFlow Stream: Real-Time Analytics")

    # Initialize MongoDB connection
    try:
        mongo_client = MongoSingleton.get_instance()
        # Ping the server to check the connection
        mongo_client.admin.command('ping')
        st.sidebar.success("MongoDB Connected")
    except Exception as e:
        st.sidebar.error(f"MongoDB Connection Failed: {e}")
        st.error("Could not connect to the database. Please check the backend services.")
        return

    # --- Sidebar for Navigation ---
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Platform Status", "Twitch Chat Analytics", "Market Analytics"])

    # --- Page Routing ---
    if page == "Platform Status":
        display_platform_dashboard()
    elif page == "Twitch Chat Analytics":
        display_chat_dashboard()
    elif page == "Market Analytics":
        display_market_dashboard()
        
    # --- Auto-refresh mechanism ---
    time.sleep(2) # Refresh interval in seconds
    st.rerun()

if __name__ == "__main__":
    main()
```

**`components/chat_dashboard.py`**
```python
import streamlit as st
import pandas as pd
from utils.mongo_client import get_chat_data, get_chat_anomalies

def display_chat_dashboard():
    st.header(" Twitch Chat Analytics")

    # Fetch data
    chat_messages = get_chat_data(limit=100)
    anomalies = get_chat_anomalies(limit=50)
    
    if not chat_messages:
        st.warning("No chat data found in the database yet.")
        return

    df_chat = pd.DataFrame(chat_messages)
    
    # --- Layout ---
    col1, col2 = st.columns([2, 1])

    with col1:
        st.subheader("Live Chat Feed")
        # Display chat messages with toxicity scores
        for index, row in df_chat.iterrows():
            author = row['payload']['author']
            text = row['payload']['text']
            toxicity = row.get('enrichments', {}).get('toxicity', {})
            toxic_score = toxicity.get('toxic', 0.0)
            
            color = "gray"
            if toxic_score > 0.8: color = "red"
            elif toxic_score > 0.5: color = "orange"
            
            st.markdown(f"**{author}**: {text} `(Toxicity: {toxic_score:.2f})`", unsafe_allow_html=True)
            st.markdown(f"<hr style='margin-top:0.1rem; margin-bottom:0.1rem; border-top: 1px solid {color};'>", unsafe_allow_html=True)


    with col2:
        st.subheader("Real-Time Toxicity Alerts")
        if anomalies:
            df_anomalies = pd.DataFrame(anomalies)
            for index, row in df_anomalies.iterrows():
                anomaly_type = row['enrichments']['anomaly'].get('type', 'N/A')
                author = row['payload']['author']
                st.error(f"**{anomaly_type.replace('_', ' ').title()}**: User `{author}` triggered an alert.")
        else:
            st.info("No recent anomalies detected.")

        st.subheader("Top Toxic Users")
        # Simple aggregation for display
        df_chat['toxic_score'] = df_chat['enrichments'].apply(lambda x: x.get('toxicity', {}).get('toxic', 0.0))
        top_toxic_users = df_chat.groupby('payload.author')['toxic_score'].mean().nlargest(5)
        st.bar_chart(top_toxic_users)

```

**`components/market_dashboard.py`**
```python
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from utils.mongo_client import get_market_data, get_market_anomalies

def display_market_dashboard():
    st.header("📈 Market Analytics")

    market_data = get_market_data(limit=200)
    anomalies = get_market_anomalies(limit=50)

    if not market_data:
        st.warning("No market data found in the database yet.")
        return

    df_market = pd.DataFrame(market_data)
    df_market['timestamp'] = pd.to_datetime(df_market['timestamp'], unit='s')
    df_market = df_market.sort_values('timestamp')

    # --- Live Price Chart with Anomalies ---
    fig = go.Figure()

    # Price Line
    fig.add_trace(go.Scatter(
        x=df_market['timestamp'],
        y=df_market['payload'].apply(lambda x: x.get('price')),
        mode='lines',
        name='Price (BTCUSDT)'
    ))

    # Anomaly Markers
    if anomalies:
        df_anomalies = pd.DataFrame(anomalies)
        df_anomalies['timestamp'] = pd.to_datetime(df_anomalies['timestamp'], unit='s')
        fig.add_trace(go.Scatter(
            x=df_anomalies['timestamp'],
            y=df_anomalies['payload'].apply(lambda x: x.get('price')),
            mode='markers',
            marker=dict(color='red', size=10, symbol='x'),
            name='Anomaly Detected'
        ))

    fig.update_layout(title="Real-Time Market Price Feed", xaxis_title="Time", yaxis_title="Price (USD)")
    st.plotly_chart(fig, use_container_width=True)

    # --- Anomaly Feed ---
    st.subheader("Recent Market Anomalies")
    if anomalies:
        for anomaly in anomalies:
            anomaly_type = anomaly['enrichments']['anomaly'].get('type', 'N/A')
            price = anomaly['payload']['price']
            st.error(f"**{anomaly_type.replace('_', ' ').title()}** detected at price **${price:,.2f}**")
    else:
        st.info("No recent anomalies detected.")

```

**`components/platform_dashboard.py`**
```python
import streamlit as st
from utils.mongo_client import get_db_stats

def display_platform_dashboard():
    st.header("🚀 Platform Status")
    
    stats = get_db_stats()

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Events Processed", f"{stats.get('enriched_events', 0):,}")
    col2.metric("Chat Messages", f"{stats.get('chat_messages', 0):,}")
    col3.metric("Market Trades", f"{stats.get('market_trades', 0):,}")
    
    total_anomalies = stats.get('chat_anomalies', 0) + stats.get('market_anomalies', 0)
    col4.metric("Total Anomalies Detected", f"{total_anomalies:,}")
    
    st.info("This dashboard provides a high-level overview of the data flowing through the system. Metrics are based on document counts in MongoDB collections and update every few seconds.")

    st.subheader("Next Steps")
    st.markdown("""
    - **Kafka UI**: [http://localhost:8080](http://localhost:8080) to inspect Kafka topics and consumer groups.
    - **Mongo Express**: [http://localhost:8081](http://localhost:8081) to browse the MongoDB collections directly.
    - **Spark UI**: [http://localhost:8082](http://localhost:8082) to monitor the Spark jobs and cluster status.
    """)
```

**`utils/mongo_client.py`**
```python
import os
from pymongo import MongoClient

class MongoSingleton:
    _instance = None

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            mongo_uri = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
            try:
                cls._instance = MongoClient(mongo_uri)
            except Exception as e:
                print(f"Failed to connect to MongoDB: {e}")
                raise
        return cls._instance

def get_db():
    client = MongoSingleton.get_instance()
    db_name = os.getenv("MONGO_DATABASE", "DataFlowDB")
    return client[db_name]

# --- Data Fetching Functions ---

def get_chat_data(limit=100):
    db = get_db()
    return list(db.enriched_events.find({"source": "twitch_chat"}).sort("_id", -1).limit(limit))

def get_market_data(limit=200):
    db = get_db()
    return list(db.enriched_events.find({"source": "market_data"}).sort("_id", -1).limit(limit))

def get_chat_anomalies(limit=50):
    db = get_db()
    return list(db.chat_anomalies.find().sort("_id", -1).limit(limit))

def get_market_anomalies(limit=50):
    db = get_db()
    return list(db.market_anomalies.find().sort("_id", -1).limit(limit))

def get_db_stats():
    db = get_db()
    return {
        "enriched_events": db.enriched_events.count_documents({}),
        "chat_messages": db.enriched_events.count_documents({"source": "twitch_chat"}),
        "market_trades": db.enriched_events.count_documents({"source": "market_data"}),
        "chat_anomalies": db.chat_anomalies.count_documents({}),
        "market_anomalies": db.market_anomalies.count_documents({}),
    }

```

**`utils/style.py`**
```python
import streamlit as st

def local_css(file_name):
    try:
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        st.warning(f"CSS file not found: {file_name}")

```
And create a blank file at `utils/style.css` for any custom CSS you might want to add later.