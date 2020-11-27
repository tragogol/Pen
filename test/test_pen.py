from model import Pen
from test.constants import *
from test.conftest import *
import pytest


@pytest.mark.init
def test_empty_init(set_pen):
    pen = set_pen()
    container_bool = pen.check_pen_state()
    output_color = pen.get_color()
    output_word = pen.write(word_test)
    assert (output_word == word_test and output_color is not None and container_bool)


@pytest.mark.init
def test_wrong_format_container(set_pen):
    pen = set_pen(container_value=wrong_format)
    assert pen.check_pen_state() is False


@pytest.mark.init
def test_incorrect_container_value(set_pen):
    pen = set_pen(ink_container_value_incorrect, size_letter_correct, color_correct_blue)
    container_value_bool = pen.check_pen_state()
    assert container_value_bool is False


@pytest.mark.init
@pytest.mark.parametrize("size_letter", [wrong_format, size_letter_incorrect])
def test_incorrect_size_letter(size_letter, set_pen):
    pen = set_pen(size_letter=size_letter)
    assert pen.write(word_test) != word_test


@pytest.mark.init
def test_wrong_format_color(set_pen):
    with pytest.raises(ValueError):
        set_pen(color=wrong_format_color)


@pytest.mark.writefunc
def test_correct_write_func(set_pen):
    pen = set_pen()
    assert pen.write(word_test) == word_test


@pytest.mark.writefunc
def test_empty_write_func(set_pen):
    pen = set_pen()
    pen.write()


@pytest.mark.writefunc
def test_wrong_format_write_func(set_pen):
    pen = set_pen()
    pen.write(wrong_format_word)


@pytest.mark.writefunc
def test_correct_massive_write_func(set_pen):
    pen = set_pen()
    for word in words_massive:
        assert pen.write(word) == word


@pytest.mark.writefunc
@pytest.mark.parametrize("word", words_massive)
def test_check_container_value_write_func_avg(word, set_pen):
    container_len_avg = len(word) + len(word) / 2
    pen = set_pen(container_value=container_len_avg)
    assert pen.write(word) == word


@pytest.mark.writefunc
@pytest.mark.parametrize("word", words_massive)
def test_check_container_value_write_func(word, set_pen):
    container_len = len(word)
    pen = set_pen(container_value=container_len)
    assert pen.write(word) == word


@pytest.mark.writefunc
@pytest.mark.parametrize("word", words_massive)
def test_check_container_value_write_func_less(word, set_pen):
    container_len_less = len(word) - 1
    pen = set_pen(container_value=container_len_less)
    assert pen.write(word) == word[0:len(word) - 1]


@pytest.mark.others
def test_correct_container_value(set_pen):
    pen = set_pen(ink_container_value_correct, size_letter_correct, color_correct_blue)
    container_value_bool = pen.check_pen_state()
    assert container_value_bool is True


@pytest.mark.others
@pytest.mark.parametrize("color", color_correct_massive)
def test_get_color_correct(color, set_pen):
    pen = set_pen(color=color)
    assert pen.get_color() == color


@pytest.mark.others
@pytest.mark.parametrize("color", color_correct_massive)
def test_do_something_else_correct(color, capfd, set_pen):
    pen = set_pen(color=color)
    pen.do_something_else()
    out, err = capfd.readouterr()
    assert out == color + '\n'


@pytest.mark.writefunc
@pytest.mark.parametrize("word", words_massive)
@pytest.mark.parametrize("size_letter", size_letter_massive)
def test_size_letter(word, size_letter, set_pen):
    pen = set_pen(container_value=len(word), size_letter=size_letter)
    output_word = pen.write(word)
    if (size_letter * len(word)) <= len(word):
        assert output_word == word
    else:
        assert output_word == word[0: int((size_letter * len(word)) / len(word))]
