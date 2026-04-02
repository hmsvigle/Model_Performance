Here’s a clean, structured Markdown version of your results:

---

# 🧪 Model Performance Report

## 📌 Test 1: Single Prompt Evaluation

**Command**

```bash
python measure_model.py
```

**Model:** `llama3.2`
**Prompt:** *Explain what machine learning is in 100 words.*

---

### 💬 Model Response

> Machine learning is a subset of artificial intelligence that enables computers to learn from data without being explicitly programmed. It involves training algorithms on large datasets, allowing them to identify patterns and make predictions or decisions based on that information. Machine learning models can be categorized into supervised, unsupervised, and reinforcement learning, each with its own strengths and weaknesses. By leveraging machine learning, businesses and organizations can automate tasks, improve accuracy, and gain insights from vast amounts of data, leading to increased efficiency, productivity, and decision-making capabilities. This technology is increasingly used in various industries.

---

### 📊 Performance Metrics

| Metric                        | Value           |
| ----------------------------- | --------------- |
| ⏱️ Time to First Token (TTFT) | 12.815 s        |
| 🔤 Tokens Per Second (TPS)    | 83.7 tokens/sec |
| 🕐 Total Latency              | 14.176 s        |
| 📝 Tokens Generated           | 114             |

---

# 🌡️ Test 2: Temperature Variance Analysis

**Command**

```bash
python3 measure_temperature_variance.py
```

* **Model:** `llama3.2`
* **Prompt:** Same as above
* **Temperatures Tested:** `0.0, 0.3, 0.7, 1.0, 1.5`
* **Runs per Temperature:** `3`

---

## 🔍 Detailed Results

### 🌡️ Temperature = 0.0

| Run | TTFT (s) | TPS  | Latency (s) | Tokens |
| --- | -------- | ---- | ----------- | ------ |
| 1   | 1.449    | 83.1 | 2.845       | 116    |
| 2   | 0.136    | 82.5 | 1.543       | 116    |
| 3   | 0.125    | 82.7 | 1.528       | 116    |

**Summary**

| Metric  | Mean   | Min   | Max   | Variance |
| ------- | ------ | ----- | ----- | -------- |
| TTFT    | 0.57   | 0.125 | 1.449 | 0.3863   |
| TPS     | 82.767 | 82.5  | 83.1  | 0.0622   |
| Latency | 1.972  | 1.528 | 2.845 | 0.3811   |

---

### 🌡️ Temperature = 0.3

| Run | TTFT  | TPS  | Latency | Tokens |
| --- | ----- | ---- | ------- | ------ |
| 1   | 0.142 | 82.3 | 1.563   | 117    |
| 2   | 0.129 | 82.8 | 1.422   | 107    |
| 3   | 0.136 | 83.0 | 1.509   | 114    |

**Summary**

| Metric  | Mean  | Min   | Max   | Variance |
| ------- | ----- | ----- | ----- | -------- |
| TTFT    | 0.136 | 0.129 | 0.142 | 0.0      |
| TPS     | 82.7  | 82.3  | 83.0  | 0.0867   |
| Latency | 1.498 | 1.422 | 1.563 | 0.0034   |

---

### 🌡️ Temperature = 0.7

| Run | TTFT  | TPS  | Latency | Tokens |
| --- | ----- | ---- | ------- | ------ |
| 1   | 0.128 | 82.8 | 1.494   | 113    |
| 2   | 0.133 | 83.0 | 1.591   | 121    |
| 3   | 0.128 | 83.1 | 1.535   | 117    |

**Summary**

| Metric  | Mean   | Min   | Max   | Variance |
| ------- | ------ | ----- | ----- | -------- |
| TTFT    | 0.13   | 0.128 | 0.133 | 0.0      |
| TPS     | 82.967 | 82.8  | 83.1  | 0.0156   |
| Latency | 1.54   | 1.494 | 1.591 | 0.0016   |

---

### 🌡️ Temperature = 1.0

| Run | TTFT  | TPS  | Latency | Tokens |
| --- | ----- | ---- | ------- | ------ |
| 1   | 0.137 | 82.9 | 1.476   | 111    |
| 2   | 0.122 | 64.7 | 1.838   | 111    |
| 3   | 0.137 | 82.6 | 1.553   | 117    |

**Summary**

| Metric  | Mean   | Min   | Max   | Variance |
| ------- | ------ | ----- | ----- | -------- |
| TTFT    | 0.132  | 0.122 | 0.137 | 0.0001   |
| TPS     | 76.733 | 64.7  | 82.9  | 72.4156  |
| Latency | 1.622  | 1.476 | 1.838 | 0.0242   |

---

### 🌡️ Temperature = 1.5

| Run | TTFT  | TPS  | Latency | Tokens |
| --- | ----- | ---- | ------- | ------ |
| 1   | 0.132 | 82.7 | 1.534   | 116    |
| 2   | 0.128 | 82.8 | 1.432   | 108    |
| 3   | 0.138 | 82.8 | 1.599   | 121    |

**Summary**

| Metric  | Mean   | Min   | Max   | Variance |
| ------- | ------ | ----- | ----- | -------- |
| TTFT    | 0.133  | 0.128 | 0.138 | 0.0      |
| TPS     | 82.767 | 82.7  | 82.8  | 0.0022   |
| Latency | 1.522  | 1.432 | 1.599 | 0.0047   |

---

## 📈 Final Variance Summary Across Temperatures

| Temp | TTFT Mean | TTFT Var | TPS Mean | TPS Var | Latency Mean | Latency Var |
| ---- | --------- | -------- | -------- | ------- | ------------ | ----------- |
| 0.0  | 0.57      | 0.3863   | 82.767   | 0.0622  | 1.972        | 0.3811      |
| 0.3  | 0.136     | 0.0      | 82.7     | 0.0867  | 1.498        | 0.0034      |
| 0.7  | 0.13      | 0.0      | 82.967   | 0.0156  | 1.54         | 0.0016      |
| 1.0  | 0.132     | 0.0001   | 76.733   | 72.4156 | 1.622        | 0.0242      |
| 1.5  | 0.133     | 0.0      | 82.767   | 0.0022  | 1.522        | 0.0047      |

---

## ✅ Output

* Results saved to: `results.csv`

---

If you want, I can also convert this into:

* a polished README section
* a PDF report
* or add charts (latency vs temperature, variance plots)
