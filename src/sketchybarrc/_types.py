from __future__ import annotations

from enum import Enum
from typing import Literal, NewType, TypeAlias

boolean: TypeAlias = Literal["true", "false"]

Nat = NewType("Nat", int)


def nat(v: int) -> Nat:
    if v >= 0:
        return Nat(v)
    else:
        raise ValueError(f"value {v} must be positive integer")


class Event(Enum):
    front_app_switched = "front_app_switched"
    space_change = "space_change"
    display_change = "display_change"
    volume_change = "volume_change"
    brightness_change = "brightness_change"
    power_source_change = "power_source_change"
    wifi_change = "wifi_change"
    system_will_sleep = "system_will_sleep"
    system_woke = "system_woke"
    mouse_entered = "mouse.entered"
    mouse_exited = "mouse.exited"
    mouse_entered_global = "mouse.entered_global"
    mouse_exited_global = "mouse.exited.global"
    mouse_clicked = "mouse.clicked"
