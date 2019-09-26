from ptest.decorator import TestClass, Test
from ptest.assertion import assert_equals
from .base_test import PTestBase


@TestClass()
class AppMainScreen(PTestBase):

    @Test()
    def test_001_dummy(self):
        assert_equals(True, True)
