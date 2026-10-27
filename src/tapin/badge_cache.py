"""Offline badge cache (see PRD: Offline badge cache)."""
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
        self._entries[badge_id] = (user_id, time.time())

    def lookup(self, badge_id: str) -> str | None:
        entry = self._entries.get(badge_id)
        if entry is None:
            return None
        user_id, seen_at = entry
        if time.time() - seen_at > self.window_seconds:
            del self._entries[badge_id]
            return None
        return user_id
