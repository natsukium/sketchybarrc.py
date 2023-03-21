from __future__ import annotations

import subprocess
from typing import Literal

from typing_extensions import Self

from ._types import Event
from .properties import BarProps, Props


class SketchyBar:
    def __init__(self: Self, command: list[str] | None = None) -> None:
        self.command = command if command is not None else [self._default_command]

    @property
    def _default_command(self) -> str:
        return "sketchybar"

    def set_bar(self: Self, props: BarProps) -> Self:
        _props = [f"{k}={v}" for k, v in props.asdict().items() if v is not None]
        return SketchyBar(self.command + ["--bar"] + _props)

    def set_default(self: Self, props: Props) -> Self:
        _props = [f"{k}={v}" for k, v in props.asdict().items() if v is not None]
        return SketchyBar(self.command + ["--default"] + _props)

    def add_item(self: Self, item: str, pos: Literal["right", "left"]) -> Self:
        return SketchyBar(self.command + ["--add", "item", item, pos])

    def set_item(self: Self, item: str, props: Props) -> Self:
        _props = [f"{k}={v}" for k, v in props.asdict().items() if v is not None]
        return SketchyBar(self.command + ["--set", item] + _props)

    def set_subscribe(self: Self, item: str, events: list[Event]) -> Self:
        return SketchyBar(
            self.command + ["--subscribe", item] + [e.value for e in events]
        )

    def run(self: Self) -> None:
        subprocess.run(self.command)

    def update(self: Self) -> None:
        subprocess.run([self._default_command, "--update"])
