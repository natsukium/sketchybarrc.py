from sketchybarrc._types import Event
from sketchybarrc.command import SketchyBar
from sketchybarrc.properties import BarProps, ItemProps, LabelProps


def test_set_bar():
    sketchybar = SketchyBar().set_bar(BarProps(color="dummy", position="top"))
    assert sketchybar.command == ["sketchybar", "--bar", "color=dummy", "position=top"]


def test_set_default():
    sketchybar = SketchyBar().set_default(
        ItemProps(label=LabelProps(font="dummy_font"))
    )
    assert sketchybar.command == ["sketchybar", "--default", "label.font=dummy_font"]


def test_add_item():
    item = "dummy"
    sketchybar = SketchyBar().add_item(item, "right")
    assert sketchybar.command == ["sketchybar", "--add", "item", item, "right"]


def test_set_item():
    item = "dummy"
    sketchybar = SketchyBar().set_item(
        item, LabelProps(label="dummy_label", color="dummy_color")
    )
    assert sketchybar.command == [
        "sketchybar",
        "--set",
        item,
        "label.color=dummy_color",
        "label=dummy_label",
    ]


def test_set_subscribe():
    item = "dummy"
    sketchybar = SketchyBar().set_subscribe(
        item, [Event.wifi_change, Event.mouse_entered]
    )
    assert sketchybar.command == [
        "sketchybar",
        "--subscribe",
        item,
        "wifi_change",
        "mouse.entered",
    ]


def test_chain():
    sketchybar = (
        SketchyBar().set_bar(BarProps(color="dummy")).add_item("dummy", "right")
    )
    assert sketchybar.command == [
        "sketchybar",
        "--bar",
        "color=dummy",
        "--add",
        "item",
        "dummy",
        "right",
    ]
