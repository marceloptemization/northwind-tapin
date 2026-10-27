from src.tapin.badge_cache import BadgeCache


def test_lookup_returns_remembered_user():
    cache = BadgeCache()
    cache.remember("badge-1", "user-a")
    assert cache.lookup("badge-1") == "user-a"


def test_expired_entry_is_dropped():
    cache = BadgeCache(window_seconds=-1)
    cache.remember("badge-1", "user-a")
    assert cache.lookup("badge-1") is None
