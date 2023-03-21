from __future__ import annotations

from dataclasses import asdict, dataclass, fields
from functools import reduce
from typing import Any, Literal

from typing_extensions import Self

from ._types import Nat, boolean


def _nest_asdict(self: Props) -> dict[str, Any]:
    ret: dict[str, Any] = {}
    for k, v in {
        field.name: getattr(self, field.name) for field in fields(self)
    }.items():
        if v is not None:
            if isinstance(v, Props):
                ret |= {
                    (f"{k}.{kv}" if kv != k else kv): vv
                    for kv, vv in v.asdict().items()
                }
            else:
                ret[k] = v
    return ret


@dataclass
class Props:
    def asdict(self: Self) -> dict[str, Any]:
        return {k: v for k, v in asdict(self).items() if v is not None}


@dataclass
class BarProps(Props):
    color: str | None = None
    border_color: str | None = None
    position: Literal["top", "bottom"] | None = None
    height: int | None = None
    margin: int | None = None
    y_offset: int | None = None
    corner_radius: Nat | None = None
    border_width: Nat | None = None
    blur_radius: Nat | None = None
    padding_left: Nat | None = None
    padding_right: Nat | None = None
    notch_width: Nat | None = None
    notch_offset: Nat | None = None
    display: Literal["main", "all"] | None = None
    hidden: boolean | Literal["current"] | None = None
    topmost: boolean | None = None
    sticky: boolean | None = None
    font_smoothing: boolean | None = None
    shadow: boolean | None = None


@dataclass
class ImageProps(Props):
    image: str | None = None  # WARN: change from official properties
    drawing: boolean | None = None
    scale: float | None = None


@dataclass
class ShadowProps(Props):
    drawing: boolean | None = None
    color: str | None = None
    angle: Nat | None = None
    distance: Nat | None = None


@dataclass
class BackgroundProps(Props):
    drawing: boolean | None = None
    color: str | None = None
    border_color: str | None = None
    border_width: str | None = None
    height: Nat | None = None
    corner_radius: Nat | None = None
    padding_left: int | None = None
    padding_right: int | None = None
    y_offset: int | None = None
    clip: float | None = None
    image: ImageProps | None = None
    shadow: ShadowProps | None = None

    def asdict(self) -> dict[str, Any]:
        return _nest_asdict(self)


@dataclass
class GeometryProps(Props):
    drawing: boolean | None = None
    position: Literal["left", "right", "center"] | None = None
    associated_space: list[Nat] | None = None
    associated_display: list[Nat] | Literal["active"] | None = None
    ignore_association: boolean | None = None
    y_offset: int | None = None
    padding_left: int | None = None
    padding_right: int | None = None
    width: Nat | Literal["dynamic"] | None = None
    blur_radius: Nat | None = None
    background: BackgroundProps | None = None

    def asdict(self) -> dict[str, Any]:
        return _nest_asdict(self)


@dataclass
class TextProps(Props):
    drawing: boolean | None = None
    highlight: boolean | None = None
    color: str | None = None
    highlight_color: str | None = None
    padding_left: int | None = None
    padding_right: int | None = None
    y_offset: int | None = None
    font: str | None = None
    string: str | None = None
    width: Nat | Literal["dynamic"] | None = None
    align: Literal["center", "left", "right"] | None = None
    background: BackgroundProps | None = None
    shadow: ShadowProps | None = None

    def asdict(self) -> dict[str, Any]:
        return _nest_asdict(self)


@dataclass
class IconProps(TextProps):
    icon: str | None = None

    def asdict(self) -> dict[str, Any]:
        return {
            (f"icon.{k}" if k != "icon" else k): v
            for k, v in asdict(self).items()
            if v is not None
        }


@dataclass
class LabelProps(TextProps):
    label: str | None = None

    def asdict(self) -> dict[str, Any]:
        return {
            (f"label.{k}" if k != "label" else k): v
            for k, v in asdict(self).items()
            if v is not None
        }


@dataclass
class ScriptingProps(Props):
    script: str | None = None
    click_script: str | None = None
    update_freq: Nat | None = None
    updates: boolean | Literal["when_shown"] | None = None
    mach_helper: str | None = None


@dataclass
class ItemProps(Props):
    icon: IconProps | None = None
    label: LabelProps | None = None
    geometry: GeometryProps | None = None

    def asdict(self) -> dict[str, Any]:
        dicts = [
            y.asdict()
            for y in (
                self.icon,
                self.label,
                self.geometry,
            )
            if y is not None
        ]
        return reduce(lambda d1, d2: d1 | d2, dicts)
