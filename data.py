from model import Creature

_creatures: list[Creature] = [
    Creature(
        name="yeti",
        country="CN",
        area="Himalayas",
        description="Hirsute Himalayan",
        aka="Abominable Snowman"
    ),
    Creature(
        name="sasquatch",
        country="US",
        area="*",
        description="Furrified",
        aka="Big Foot"
    )
]


def get_creatures() -> list[Creature]:
    return _creatures