
python measure_model.py

📤 Sending prompt to model: llama3.2
💬 Prompt: Explain what machine learning is in 100 words.

--------------------------------------------------
Machine learning is a subset of artificial intelligence that enables computers to learn from data without being explicitly programmed. It involves training algorithms on large datasets, allowing them to identify patterns and make predictions or decisions based on that information. Machine learning models can be categorized into supervised, unsupervised, and reinforcement learning, each with its own strengths and weaknesses. By leveraging machine learning, businesses and organizations can automate tasks, improve accuracy, and gain insights from vast amounts of data, leading to increased efficiency, productivity, and decision-making capabilities. This technology is increasingly used in various industries.
--------------------------------------------------

📊 PERFORMANCE METRICS
  ⏱️  Time to First Token (TTFT) : 12.815 seconds
  🔤  Tokens Per Second (TPS)    : 83.7 tokens/sec
  🕐  Total Response Latency     : 14.176 seconds
  📝  Total Tokens Generated     : 114
--------------------------------------------------

$ python3 measure_temperature_variance.py 

🚀 Model     : llama3.2
📋 Prompt    : Explain what machine learning is in 100 words.
🌡️  Temps     : [0.0, 0.3, 0.7, 1.0, 1.5]
🔁 Runs/Temp : 3
======================================================================

🌡️  Temperature = 0.0
--------------------------------------------------
  ▶ Run 1/3 ... TTFT=1.449s | TPS=83.1 | Latency=2.845s | Tokens=116
  ▶ Run 2/3 ... TTFT=0.136s | TPS=82.5 | Latency=1.543s | Tokens=116
  ▶ Run 3/3 ... TTFT=0.125s | TPS=82.7 | Latency=1.528s | Tokens=116

  📊 Summary for temp=0.0:
     TTFT     → mean=0.57s  | min=0.125s  | max=1.449s  | variance=0.3863
     TPS      → mean=82.767    | min=82.5    | max=83.1    | variance=0.0622
     Latency  → mean=1.972s  | min=1.528s  | max=2.845s  | variance=0.3811

🌡️  Temperature = 0.3
--------------------------------------------------
  ▶ Run 1/3 ... TTFT=0.142s | TPS=82.3 | Latency=1.563s | Tokens=117
  ▶ Run 2/3 ... TTFT=0.129s | TPS=82.8 | Latency=1.422s | Tokens=107
  ▶ Run 3/3 ... TTFT=0.136s | TPS=83.0 | Latency=1.509s | Tokens=114

  📊 Summary for temp=0.3:
     TTFT     → mean=0.136s  | min=0.129s  | max=0.142s  | variance=0.0
     TPS      → mean=82.7    | min=82.3    | max=83.0    | variance=0.0867
     Latency  → mean=1.498s  | min=1.422s  | max=1.563s  | variance=0.0034

🌡️  Temperature = 0.7
--------------------------------------------------
  ▶ Run 1/3 ... TTFT=0.128s | TPS=82.8 | Latency=1.494s | Tokens=113
  ▶ Run 2/3 ... TTFT=0.133s | TPS=83.0 | Latency=1.591s | Tokens=121
  ▶ Run 3/3 ... TTFT=0.128s | TPS=83.1 | Latency=1.535s | Tokens=117

  📊 Summary for temp=0.7:
     TTFT     → mean=0.13s  | min=0.128s  | max=0.133s  | variance=0.0
     TPS      → mean=82.967    | min=82.8    | max=83.1    | variance=0.0156
     Latency  → mean=1.54s  | min=1.494s  | max=1.591s  | variance=0.0016

🌡️  Temperature = 1.0
--------------------------------------------------
  ▶ Run 1/3 ... TTFT=0.137s | TPS=82.9 | Latency=1.476s | Tokens=111
  ▶ Run 2/3 ... TTFT=0.122s | TPS=64.7 | Latency=1.838s | Tokens=111
  ▶ Run 3/3 ... TTFT=0.137s | TPS=82.6 | Latency=1.553s | Tokens=117

  📊 Summary for temp=1.0:
     TTFT     → mean=0.132s  | min=0.122s  | max=0.137s  | variance=0.0001
     TPS      → mean=76.733    | min=64.7    | max=82.9    | variance=72.4156
     Latency  → mean=1.622s  | min=1.476s  | max=1.838s  | variance=0.0242

🌡️  Temperature = 1.5
--------------------------------------------------
  ▶ Run 1/3 ... TTFT=0.132s | TPS=82.7 | Latency=1.534s | Tokens=116
  ▶ Run 2/3 ... TTFT=0.128s | TPS=82.8 | Latency=1.432s | Tokens=108
  ▶ Run 3/3 ... TTFT=0.138s | TPS=82.8 | Latency=1.599s | Tokens=121

  📊 Summary for temp=1.5:
     TTFT     → mean=0.133s  | min=0.128s  | max=0.138s  | variance=0.0
     TPS      → mean=82.767    | min=82.7    | max=82.8    | variance=0.0022
     Latency  → mean=1.522s  | min=1.432s  | max=1.599s  | variance=0.0047


✅ Raw results saved to: results.csv

======================================================================
📈 FINAL VARIANCE SUMMARY ACROSS TEMPERATURES
======================================================================
Temp      TTFT Mean   TTFT Var   TPS Mean    TPS Var   Lat Mean    Lat Var
----------------------------------------------------------------------
0.0            0.57     0.3863     82.767     0.0622      1.972     0.3811
0.3           0.136        0.0       82.7     0.0867      1.498     0.0034
0.7            0.13        0.0     82.967     0.0156       1.54     0.0016
1.0           0.132     0.0001     76.733    72.4156      1.622     0.0242
1.5           0.133        0.0     82.767     0.0022      1.522     0.0047
======================================================================