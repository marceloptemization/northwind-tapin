"""Session lifecycle on a shared workstation."""
from dataclasses import dataclass, field
from enum import Enum


class SessionState(Enum):
    ACTIVE = "active"
    SUSPENDED = "suspended"
    ENDED = "ended"


@dataclass
class Session:
    user_id: str
    workstation_id: str
    state: SessionState = SessionState.ACTIVE


@dataclass
class SessionBroker:
    workstation_id: str
    sessions: list[Session] = field(default_factory=list)

    def active(self) -> Session | None:
        return next((s for s in self.sessions if s.state is SessionState.ACTIVE), None)

    def start(self, user_id: str) -> Session:
        session = Session(user_id, self.workstation_id)
        self.sessions.append(session)
        return session

    def end(self, session: Session) -> None:
        session.state = SessionState.ENDED

    def switch(self, user_id: str) -> Session:
        """Tap-to-switch: suspend the current user's session and start one for the next user.

        Scaffold only. Suspend timeout, audit events and the admin setting land with the
        tap-to-switch work items.
        """
        current = self.active()
        if current is not None:
            if current.user_id == user_id:
                return current
            current.state = SessionState.SUSPENDED
        return self.start(user_id)
