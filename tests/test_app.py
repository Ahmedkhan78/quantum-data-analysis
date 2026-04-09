import sys
import os
import pytest
from dash.testing.application_runners import import_app

# FIX: add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


@pytest.fixture
def app():
    return import_app("app")


def test_header_present(dash_duo, app):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("h1", timeout=10)
    assert "Pink Morsel Sales Over Time" in dash_duo.find_element("h1").text


def test_graph_present(dash_duo, app):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#sales-line-chart", timeout=10)
    assert dash_duo.find_element("#sales-line-chart")


def test_region_picker_present(dash_duo, app):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#region-selector", timeout=10)
    assert dash_duo.find_element("#region-selector")