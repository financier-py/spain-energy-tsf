from pathlib import Path
import kagglehub
import config

config.RAW_DIR.mkdir(parents=True, exist_ok=True)
src = Path(kagglehub.dataset_download(config.KAGGLE_DATASET))

for name in (config.ENERGY_FILE, config.WEATHER_FILE):
    (config.RAW_DIR / name).write_bytes((src / name).read_bytes())
    print(f"Скопировали файлик {name} в нашу папку с данными ")