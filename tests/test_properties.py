from __future__ import annotations

import pytest

from sketchybarrc._types import nat
from sketchybarrc.properties import (
    BackgroundProps,
    BarProps,
    GeometryProps,
    IconProps,
    ImageProps,
    ItemProps,
    LabelProps,
    ScriptingProps,
    ShadowProps,
    TextProps,
)


@pytest.fixture
def bar_props() -> BarProps:
    return BarProps(color="dummy_color", position="top", margin=10)


@pytest.fixture
def icon_props() -> IconProps:
    return IconProps(icon="dummy_icon", color="dummy_color")


@pytest.fixture
def label_props() -> LabelProps:
    return LabelProps(label="dummy_label", color="dummy_color")


@pytest.fixture
def image_props() -> ImageProps:
    return ImageProps(image="dummy.png", scale=1.5)


@pytest.fixture
def shadow_props() -> ShadowProps:
    return ShadowProps(color="dummy_color", angle=nat(20))


@pytest.fixture
def background_props(
    image_props: ImageProps, shadow_props: ShadowProps
) -> BackgroundProps:
    return BackgroundProps(color="dummy_color", image=image_props, shadow=shadow_props)


@pytest.fixture
def geometry_props(background_props: BackgroundProps) -> GeometryProps:
    return GeometryProps(
        drawing="true",
        associated_space=[nat(3), nat(4), nat(5)],
        background=background_props,
    )


@pytest.fixture
def text_props(
    background_props: BackgroundProps, shadow_props: ShadowProps
) -> TextProps:
    return TextProps(
        color="dummy_color", background=background_props, shadow=shadow_props
    )


@pytest.fixture
def scripting_props() -> ScriptingProps:
    return ScriptingProps(script="dummy.sh", update_freq=nat(10))


@pytest.fixture
def item_props(
    icon_props: IconProps, label_props: LabelProps, geometry_props: GeometryProps
) -> ItemProps:
    return ItemProps(icon=icon_props, label=label_props, geometry=geometry_props)


def test_bar_props_to_dict(bar_props: BarProps):
    expected = {"color": "dummy_color", "position": "top", "margin": 10}
    assert bar_props.asdict() == expected


def test_image_props_to_dict(image_props: ImageProps):
    expected = {"image": "dummy.png", "scale": 1.5}
    assert image_props.asdict() == expected


def test_icon_props_to_dict(icon_props: IconProps):
    expected = {"icon": "dummy_icon", "icon.color": "dummy_color"}
    assert icon_props.asdict() == expected


def test_label_props_to_dict(label_props: LabelProps):
    expected = {"label": "dummy_label", "label.color": "dummy_color"}
    assert label_props.asdict() == expected


def test_item_props_to_dict(item_props: ItemProps):
    expected = {
        "icon": "dummy_icon",
        "icon.color": "dummy_color",
        "label": "dummy_label",
        "label.color": "dummy_color",
        "drawing": "true",
        "associated_space": [3, 4, 5],
        "background.color": "dummy_color",
        "background.image": "dummy.png",
        "background.image.scale": 1.5,
        "background.shadow.color": "dummy_color",
        "background.shadow.angle": 20,
    }
    assert item_props.asdict() == expected


def test_background_props_to_dict(background_props: BackgroundProps):
    expected = {
        "color": "dummy_color",
        "image": "dummy.png",
        "image.scale": 1.5,
        "shadow.color": "dummy_color",
        "shadow.angle": 20,
    }
    assert background_props.asdict() == expected


def test_geometry_props_to_dict(geometry_props: GeometryProps):
    expected = {
        "drawing": "true",
        "associated_space": [3, 4, 5],
        "background.color": "dummy_color",
        "background.image": "dummy.png",
        "background.image.scale": 1.5,
        "background.shadow.color": "dummy_color",
        "background.shadow.angle": 20,
    }
    assert geometry_props.asdict() == expected


def test_scripting_props_to_dict(scripting_props: ScriptingProps):
    expected = {"script": "dummy.sh", "update_freq": 10}
    assert scripting_props.asdict() == expected
