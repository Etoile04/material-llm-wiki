"""Minimal observability logger for GapRequest processing."""

import json
import uuid
import os
from datetime import datetime


class RefLogger:
    def __init__(self, log_dir: str = "data/ref-logs"):
        self.log_dir = log_dir
        os.makedirs(log_dir, exist_ok=True)
        self._current = None

    def start_request(self, items_count: int = 0) -> str:
        """Start recording a new request. Returns request_id (uuid4)."""
        rid = str(uuid.uuid4())
        self._current = {
            "request_id": rid,
            "timestamp": datetime.now().isoformat(),
            "items_requested": items_count,
            "cache_hits": {"L1": 0, "L2": 0, "L3": 0},
            "express_results": 0,
            "gaps_remaining": 0,
            "duration_seconds": 0.0,
            "slowlane_tagged_papers": 0,
            "errors": [],
        }
        return rid

    def record_cache_hit(self, level: str) -> None:
        """Record a cache hit. level: 'L1' | 'L2' | 'L3'."""
        if self._current is not None and level in self._current["cache_hits"]:
            self._current["cache_hits"][level] += 1

    def record_express_result(self) -> None:
        """Record one express search+extract result."""
        if self._current is not None:
            self._current["express_results"] += 1

    def record_error(self, error: str) -> None:
        """Record an error."""
        if self._current is not None:
            self._current["errors"].append(error)

    def finish_request(self, duration_seconds: float, gaps_remaining: int = 0) -> dict:
        """Finish recording, append to daily JSON file, return the entry."""
        self._current["duration_seconds"] = duration_seconds
        self._current["gaps_remaining"] = gaps_remaining

        today = datetime.now().strftime("%Y-%m-%d")
        filepath = os.path.join(self.log_dir, f"{today}.json")

        entries = []
        if os.path.exists(filepath):
            with open(filepath) as f:
                entries = json.load(f)

        entries.append(self._current)

        with open(filepath, "w") as f:
            json.dump(entries, f, indent=2, ensure_ascii=False)

        entry = self._current
        self._current = None
        return entry
