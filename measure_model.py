import requests
import time
import json

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3.2"  # change to your model name
PROMPT = "Explain what machine learning is in 100 words."

def measure_model(prompt: str, model: str):
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": True  # streaming lets us capture TTFT
    }

    print(f"\n📤 Sending prompt to model: {model}")
    print(f"💬 Prompt: {prompt}\n")
    print("-" * 50)

    # ── Start timer ──
    request_start = time.time()

    response = requests.post(OLLAMA_URL, json=payload, stream=True)

    first_token_time = None
    full_response = ""
    token_count = 0

    for line in response.iter_lines():
        if line:
            data = json.loads(line)
            token = data.get("response", "")

            # ── Capture Time to First Token ──
            if token and first_token_time is None:
                first_token_time = time.time()
                ttft = first_token_time - request_start

            full_response += token
            token_count += 1
            print(token, end="", flush=True)

            if data.get("done"):
                break

    # ── End timer ──
    end_time = time.time()
    total_latency = end_time - request_start
    generation_time = end_time - first_token_time
    tps = token_count / generation_time if generation_time > 0 else 0

    # ── Results ──
    print("\n" + "-" * 50)
    print("\n📊 PERFORMANCE METRICS")
    print(f"  ⏱️  Time to First Token (TTFT) : {ttft:.3f} seconds")
    print(f"  🔤  Tokens Per Second (TPS)    : {tps:.1f} tokens/sec")
    print(f"  🕐  Total Response Latency     : {total_latency:.3f} seconds")
    print(f"  📝  Total Tokens Generated     : {token_count}")
    print("-" * 50)

if __name__ == "__main__":
    measure_model(PROMPT, MODEL)