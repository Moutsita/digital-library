import json
import os

os.makedirs("metrics", exist_ok=True)

metrics = {
    "rmse": 0.85,
    "mae": 0.62
}

with open("metrics.json", "w") as f:
    json.dump(metrics, f, indent=4)

print("Metrics saved")