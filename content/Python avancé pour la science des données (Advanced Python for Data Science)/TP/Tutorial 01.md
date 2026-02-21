Based on the course materials provided (specifically Files 1, 3, 5, and 6), here are the answers to the exercises and the reasoning behind them.

---

# Exercise 1: Identify Applications

**Objective:** Decide which domain (Data Science, ML, AI, Big Data, BI) fits each scenario.

### 1. A company wants to predict customer churn using historical data.
*   **Answer:** **Machine Learning (ML)**
*   **Reasoning:**
    *   **File 3 (Careers):** Describes the Data Scientist/ML role as "Predictive: What will happen?"
    *   **File 6 (DS vs. Related Domains):** Defines Machine Learning as the specific step of creating algorithms that learn from data. Since the core task here is *prediction* based on history, it is an ML task.

### 2. An app recommends products based on user behavior.
*   **Answer:** **Machine Learning (or Data Science)**
*   **Reasoning:**
    *   **File 1 (Introduction):** Under "Key Benefits," the text lists **Personalization** (e.g., Netflix recommendations) as a primary output of Data Science.
    *   **File 3 (Careers):** This involves algorithms predicting what a user might like next, which falls under the "Predictive" nature of ML/DS.

### 3. Storing and processing terabytes of sensor data from IoT devices.
*   **Answer:** **Big Data**
*   **Reasoning:**
    *   **File 5 (Tools):** Section 5.4 states, "When data becomes too large for your laptop's RAM... (a cluster)."
    *   **File 6 (DS vs. Related Domains):** Explicitly defines Big Data as referring to the **Volume, Velocity, and Variety** of data and the infrastructure (like Hadoop/Spark) required to handle it. "Terabytes" and "IoT" indicate volume and velocity.

### 4. A dashboard shows last year’s sales trends.
*   **Answer:** **Business Intelligence (BI)**
*   **Reasoning:**
    *   **File 3 (Careers):** Describes the Data Analyst (who uses BI tools) as answering "What happened?" (Descriptive).
    *   **File 6 (DS vs. Related Domains):** The comparison table explicitly states that BI focuses on the **Past & Present** (e.g., "What happened last quarter?") and outputs **Static Reports/Dashboards**.

### 5. An AI agent plays chess and learns strategies over time.
*   **Answer:** **Artificial Intelligence (AI)**
*   **Reasoning:**
    *   **File 6 (DS vs. Related Domains):** Defines AI as "The broad goal of simulating human intelligence (reasoning, perception)." Playing a game like chess and reasoning through strategies fits the definition of simulating human intelligence rather than just analyzing a dataset.

---

# Exercise 2: Roles in a Data Science Project

## 1. Match the Roles

### (a) Collect patient records from multiple hospital databases and prepare them for use.
*   **Role:** **Data Engineer**
*   **Reasoning (File 3):** The text defines the Data Engineer as the "Plumber/Architect" whose task is **ETL (Extract, Transform, Load)**. Their example is "building a pipeline that automatically pulls lab results."

### (b) Build a predictive model using patient data to estimate heart disease risk.
*   **Role:** **Data Scientist**
*   **Reasoning (File 3):** The Data Scientist is described as the "Inventor who builds a crystal ball." Their primary focus is **Predictive** ("What will happen?") and their specific task is "building predictive models."

### (c) Create a dashboard to show current statistics about patient risk factors (age, weight, smoking).
*   **Role:** **Data Analyst**
*   **Reasoning (File 3):** The Data Analyst's focus is **Descriptive** ("What happened?" or "What is happening?"). Their task is explicitly listed as "create dashboards" and visualizing current data.

### (d) Deploy the predictive model so doctors can access it via a web application.
*   **Role:** **ML Engineer**
*   **Reasoning (File 3):** The ML Engineer's focus is **Production**. Their specific example is "Taking the Data Scientist's model... and optimizing it to run... on a cloud server." They handle the deployment and scalability.

### (e) Define the business question: “How can we reduce the number of undetected high-risk patients?”
*   **Role:** **Business Analyst**
*   **Reasoning (File 3):** The Business Analyst is described as the "Translator." Their focus is bridging technical and business teams to ensure the right questions are being asked.

---

## 2. Critical Thinking

### Explain why a Data Engineer and a Machine Learning Engineer cannot simply replace each other.
*   **Answer:** A Data Engineer focuses on the **infrastructure** *before* the model exists (pipelines, storage, cleaning data), while an ML Engineer focuses on the **production** *after* the model exists (scaling, optimizing speed, deployment).
*   **Course Reasoning (File 3):** The notes use the analogy of a "Plumber" (Data Engineer) versus a "Factory Manager" (ML Engineer). A plumber builds the pipes to move the water (data), while the factory manager mass-produces the product (the model). You cannot mass-produce a model if the data pipes aren't built, and the plumber isn't trained to optimize complex neural networks for deployment.

### Also explain why a Data Analyst and a Data Scientist cannot fully replace each other.
*   **Answer:** They focus on different timeframes and complexities. A Data Analyst looks at the **Past** (Descriptive Analytics) using tools like SQL and Excel to report news. A Data Scientist looks at the **Future** (Predictive Analytics) using advanced statistics, Python, and algorithms.
*   **Course Reasoning (File 6):** The notes emphasize that converting from Analyst to Scientist is a shift from "What happened?" to "What will happen?" A Data Scientist requires deep knowledge of **Machine Learning** and **Statistics** (File 2 & 3) to build models, whereas an analyst focuses on interpreting known data. An analyst generally cannot build the "Crystal Ball" (predictive model) without additional training in algorithms.