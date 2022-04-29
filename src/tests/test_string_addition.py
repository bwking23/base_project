import pytest

from src.string_addition import string_addition


class TestStringAddition:
    def test_addition_success(self):
        assert string_addition("test") == 448
        assert string_addition("long string to add") == 1715
        assert string_addition("abc") == 24

    def test_addition_failure(self):
        with pytest.raises(TypeError) as e_info:
            string_addition(12)
