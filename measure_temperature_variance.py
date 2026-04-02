import requests
import time
import json
import csv
from datetime import datetime

# ── Config ──────────────────────────────────────────
OLLAMA_URL   = "http://localhost:11434/api/generate"
MODEL        = "llama3.2"
PROMPT       = "Explain what machine learning is in 100 words."
TEMPERATURES = [0.0, 0.3, 0.7, 1.0, 1.5]
RUNS_PER_TEMP = 3          # repeat each temp N times to measure variance
OUTPUT_CSV   = "results.csv"
# ─────────────────────────────────────────────────────


def run_single(prompt: str, model: str, temperature: float) -> dict:
    """Run one inference and return metrics."""
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": True,
        "options": {
            "temperature": temperature
        }
    }

    request_start    = time.time()
    first_token_time = None
    full_response    = ""
    token_count      = 0

    response = requests.post(OLLAMA_URL, json=payload, stream=True)

    for line in response.iter_lines():
        if line:
            data  = json.loads(line)
            token = data.get("response", "")

            if token and first_token_time is None:
                first_token_time = time.time()

            full_response += token
            token_count   += 1

            if data.get("done"):
                break

    end_time        = time.time()
    ttft            = (first_token_time - request_start) if first_token_time else 0
    generation_time = (end_time - first_token_time) if first_token_time else 0
    total_latency   = end_time - request_start
    tps             = token_count / generation_time if generation_time > 0 else 0

    return {
        "temperature"    : temperature,
        "ttft_s"         : round(ttft, 3),
        "tps"            : round(tps, 1),
        "total_latency_s": round(total_latency, 3),
        "token_count"    : token_count,
        "response"       : full_response.strip()
    }


def calc_variance_stats(values: list) -> dict:
    """Calculate min, max, mean, and variance for a list of values."""
    n    = len(values)
    mean = sum(values) / n
    variance = sum((x - mean) ** 2 for x in values) / n
    return {
        "mean"    : round(mean, 3),
        "min"     : round(min(values), 3),
        "max"     : round(max(values), 3),
        "variance": round(variance, 4)
    }


def run_experiment():
    all_rows     = []   # raw rows for CSV
    summary      = []   # aggregated per temperature

    print(f"\n🚀 Model     : {MODEL}")
    print(f"📋 Prompt    : {PROMPT}")
    print(f"🌡️  Temps     : {TEMPERATURES}")
    print(f"🔁 Runs/Temp : {RUNS_PER_TEMP}")
    print("=" * 70)

    for temp in TEMPERATURES:
        print(f"\n🌡️  Temperature = {temp}")
        print("-" * 50)

        ttft_list    = []
        tps_list     = []
        latency_list = []

        for run in range(1, RUNS_PER_TEMP + 1):
            print(f"  ▶ Run {run}/{RUNS_PER_TEMP} ... ", end="", flush=True)

            result = run_single(PROMPT, MODEL, temp)

            ttft_list.append(result["ttft_s"])
            tps_list.append(result["tps"])
            latency_list.append(result["total_latency_s"])

            print(
                f"TTFT={result['ttft_s']}s | "
                f"TPS={result['tps']} | "
                f"Latency={result['total_latency_s']}s | "
                f"Tokens={result['token_count']}"
            )

            # Save raw row
            all_rows.append({
                "timestamp"      : datetime.now().isoformat(),
                "model"          : MODEL,
                "temperature"    : temp,
                "run"            : run,
                "ttft_s"         : result["ttft_s"],
                "tps"            : result["tps"],
                "total_latency_s": result["total_latency_s"],
                "token_count"    : result["token_count"],
                "response"       : result["response"]
            })

            time.sleep(0.5)  # small pause between runs

        # ── Per-temperature summary ──
        ttft_stats    = calc_variance_stats(ttft_list)
        tps_stats     = calc_variance_stats(tps_list)
        latency_stats = calc_variance_stats(latency_list)

        print(f"\n  📊 Summary for temp={temp}:")
        print(f"     TTFT     → mean={ttft_stats['mean']}s  | min={ttft_stats['min']}s  | max={ttft_stats['max']}s  | variance={ttft_stats['variance']}")
        print(f"     TPS      → mean={tps_stats['mean']}    | min={tps_stats['min']}    | max={tps_stats['max']}    | variance={tps_stats['variance']}")
        print(f"     Latency  → mean={latency_stats['mean']}s  | min={latency_stats['min']}s  | max={latency_stats['max']}s  | variance={latency_stats['variance']}")

        summary.append({
            "temperature"      : temp,
            "ttft_mean"        : ttft_stats["mean"],
            "ttft_variance"    : ttft_stats["variance"],
            "tps_mean"         : tps_stats["mean"],
            "tps_variance"     : tps_stats["variance"],
            "latency_mean"     : latency_stats["mean"],
            "latency_variance" : latency_stats["variance"],
        })

    # ── Export raw data to CSV ──
    with open(OUTPUT_CSV, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=all_rows[0].keys())
        writer.writeheader()
        writer.writerows(all_rows)

    print(f"\n\n✅ Raw results saved to: {OUTPUT_CSV}")

    # ── Final comparison table ──
    print("\n" + "=" * 70)
    print("📈 FINAL VARIANCE SUMMARY ACROSS TEMPERATURES")
    print("=" * 70)
    print(f"{'Temp':<8} {'TTFT Mean':>10} {'TTFT Var':>10} {'TPS Mean':>10} {'TPS Var':>10} {'Lat Mean':>10} {'Lat Var':>10}")
    print("-" * 70)
    for s in summary:
        print(
            f"{s['temperature']:<8} "
            f"{s['ttft_mean']:>10} "
            f"{s['ttft_variance']:>10} "
            f"{s['tps_mean']:>10} "
            f"{s['tps_variance']:>10} "
            f"{s['latency_mean']:>10} "
            f"{s['latency_variance']:>10}"
        )
    print("=" * 70)


if __name__ == "__main__":
    run_experiment()