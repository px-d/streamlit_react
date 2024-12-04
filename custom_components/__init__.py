import os
import streamlit.components.v1 as components

_RELEASE = True

parent_dir = os.path.dirname(os.path.abspath(__file__))


def table(name="Table", key=None):
    if _RELEASE:
        build_dir = os.path.join(parent_dir, "table/frontend/dist")
        _component_func = components.declare_component("table", path=build_dir)

    else:
        _component_func = components.declare_component(
            "table", url="http://localhost:5173"
        )

    component_value = _component_func(name=name, key=key, default=0)
    return component_value


def counter():
    if _RELEASE:
        build_dir = os.path.join(parent_dir, "counter/dist")
        _component_func = components.declare_component("counter", path=build_dir)
    else:
        _component_func = components.declare_component(
            "counter", url="http://localhost:5172"
        )

    component_value = _component_func(default=0)
    return component_value
