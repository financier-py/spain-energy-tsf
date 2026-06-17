from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA_DIR = ROOT / "data"
RAW_DIR = DATA_DIR / "raw"

KAGGLE_DATASET = "nicholasjhana/energy-consumption-generation-prices-and-weather"
ENERGY_FILE = "energy_dataset.csv"
WEATHER_FILE = "weather_features.csv"