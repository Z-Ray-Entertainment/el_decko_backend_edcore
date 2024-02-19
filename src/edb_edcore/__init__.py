from ed_core.core import switch_key_config

VERSION = "2024.2"


def edb_init():
    pass


def edb_stop():
    pass


def edb_fire_event(even_type: str, event_properties: dict = None):
    match even_type:
        case "SWITCH_CONFIG":
            switch_key_config(event_properties["config_index"], event_properties["deck_serial"])


def edb_available_events():
    pass
