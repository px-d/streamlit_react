import os
import streamlit.components.v1 as components


_RELEASE = False

if not _RELEASE:
    _component_func = components.declare_component(
        "my_component", url="http://localhost:5173"
    )
else:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/dist")
    _component_func = components.declare_component("my_component", path=build_dir)


def table(name, key=None):
    component_value = _component_func(name=name, key=key, default=0)
    return component_value
