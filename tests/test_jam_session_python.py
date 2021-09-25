# -*- coding: utf-8 -*-
"""Tests for `jam_session_python` package."""
import pytest

from jam_session_python import jam_session_python


@pytest.fixture
def generate_numbers():
    """Sample pytest fixture. Generates list of random integers.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """

    return [1, 3, 5, 7, 8]


def test_sum_numbers(generate_numbers):
    """Sample test function for sum_numbers, using pytest fixture."""

    our_result = jam_session_python.sum_numbers(generate_numbers)
    assert our_result == 24


def test_max_number(generate_numbers):
    """Sample test function for max_number, using pytest fixture."""

    our_result = jam_session_python.max_number(generate_numbers)
    assert our_result == 8
