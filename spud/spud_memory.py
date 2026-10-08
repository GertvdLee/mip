import json
from datetime import date
from pathlib import Path
from typing import Any

from config import MEMORY_FILE


DEFAULT_MEMORY: dict[str, Any] = {
    "first_seen": None,
    "last_seen": None,
    "days_active": 0,
    "total_interactions": 0,
    "mood_history": [],
}


def _today_iso() -> str:
    return date.today().isoformat()


def _safe_memory_data(data: Any) -> dict[str, Any]:
    merged = dict(DEFAULT_MEMORY)
    if isinstance(data, dict):
        merged.update({k: data[k] for k in merged.keys() if k in data})
    return merged


def load_memory(path: Path = MEMORY_FILE) -> dict[str, Any]:
    if path.exists():
        try:
            return _safe_memory_data(json.loads(path.read_text(encoding="utf-8")))
        except (json.JSONDecodeError, OSError):
            pass

    data = dict(DEFAULT_MEMORY)
    today = _today_iso()
    data["first_seen"] = today
    data["last_seen"] = today
    data["days_active"] = 1
    save_memory(data, path)
    return data


def save_memory(data: dict[str, Any], path: Path = MEMORY_FILE) -> None:
    path.write_text(json.dumps(_safe_memory_data(data), indent=2), encoding="utf-8")


def update_daily_tracking(data: dict[str, Any]) -> dict[str, Any]:
    memory = _safe_memory_data(data)
    today = _today_iso()

    if not memory["first_seen"]:
        memory["first_seen"] = today

    if memory["last_seen"] != today:
        memory["days_active"] = int(memory["days_active"] or 0) + 1

    memory["last_seen"] = today
    return memory
