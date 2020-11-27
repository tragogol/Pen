import pytest
from test.constants import *
from model import Pen


@pytest.fixture
def set_pen():
    def _set_pen(container_value=1000, size_letter=1.0, color='blue'):
        pen = Pen.Pen(ink_container_value=container_value,
                      size_letter=size_letter,
                      color=color)
        return pen
    yield _set_pen
