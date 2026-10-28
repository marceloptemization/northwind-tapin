from tapin.session_broker import SessionBroker, SessionState


def test_switch_suspends_previous_user():
    broker = SessionBroker("ws-demo-01")
    first = broker.start("user-a")
    second = broker.switch("user-b")
    assert first.state is SessionState.SUSPENDED
    assert broker.active() is second


def test_switch_to_same_user_is_noop():
    broker = SessionBroker("ws-demo-01")
    first = broker.start("user-a")
    assert broker.switch("user-a") is first
