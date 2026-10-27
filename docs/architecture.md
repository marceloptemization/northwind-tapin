# Architecture

Badge tap -> reader -> workstation agent -> identity server -> session broker.

The session broker owns session lifecycle on a workstation: start, suspend, resume, end.
Relay's pool service tracks shared devices: checked out, checked in, wiping, ready.
