"""Offline badge cache (see PRD: Offline badge cache)."""
import hashlib
import time

DEFAULT_WINDOW_SECONDS = 8 * 60 * 60  # ADR: cache window defaults to 8 hours


class BadgeCache:
    def __init__(self, window_seconds: int = DEFAULT_WINDOW_SECONDS, max_entries: int = 500):
        self.window_seconds = window_seconds
        self.max_entries = max_entries
        self._entries: dict[str, tuple[str, float]] = {}

    def remember(self, badge_id: str, user_id: str) -> None:
        if len(self._entries) >= self.max_entries:
            oldest = min(self._entries, key=lambda k: self._entries[k][1])
            del self._entries[oldest]
        self._entries[self._key(badge_id)] = (user_id, time.time())

    def lookup(self, badge_id: str) -> str | None:
        key = self._key(badge_id)
        entry = self._entries.get(key)
        if entry is None:
            return None
        user_id, seen_at = entry
        if time.time() - seen_at > self.window_seconds:
            del self._entries[key]
            return None
        return user_id

    @staticmethod
    def _key(badge_id: str) -> str:
        # Never store raw badge ids on disk or in memory dumps.
        return hashlib.sha256(badge_id.encode()).hexdigest()
