## Model Performance Parameters

These are **speed & performance metrics** used to evaluate how fast an AI model responds. Here's what each means:

---

### 1. 🔤 Tokens Per Second (TPS)
- **What it is:** How many tokens (words/word-pieces) the model generates every second
- **Example:** A model doing **80 TPS** produces roughly 60 words/sec
- **Why it matters:** Higher = faster streaming output, better user experience
- **Typical range:** 30–150 TPS depending on model size and hardware

---

### 2. ⏱️ Time to First Token (TTFT)
- **What it is:** The delay between sending your prompt and receiving the **very first word** of the response
- **Example:** If TTFT = **500ms**, you wait half a second before anything appears
- **Why it matters:** Affects how "responsive" the model *feels*, even before full output arrives
- **Typical range:** 200ms – 3 seconds depending on server load and model size

---

### 3. 🕐 Total Response Latency
- **What it is:** The **end-to-end time** from sending a request to receiving the **complete** response
- **Formula:**
  > `Total Latency = TTFT + (Total Tokens ÷ TPS)`
- **Example:** TTFT of 1s + generating 200 tokens at 100 TPS = **3 seconds total**
- **Why it matters:** The overall wait time — critical for batch processing and non-streaming use cases

---

### 🔁 How They Relate

```
User sends prompt
       ↓
  [TTFT delay]        ← Time to First Token
       ↓
First token appears
       ↓
  [Tokens stream]     ← Tokens Per Second
       ↓
Last token appears
       ↓
  [Total Latency]     ← Full round-trip time
```

---

**In short:**
| Metric | Measures | Optimize for |
|---|---|---|
| TPS | Generation speed | Throughput |
| TTFT | Responsiveness | Interactivity |
| Total Latency | Full wait time | Batch / APIs |