from ptest.decorator import TestClass, Test
from ptest.assertion import assert_equals
from .base_test import PTestBase


@TestClass()
class FollowingPageTests(PTestBase):

    @Test()
    def test_001_complete_on_boarding(self):
        self.on_boarding_screen.search_and_select_content("Real Madrid")
        self.on_boarding_screen.search_and_select_content("India")
        self.on_boarding_screen.accept_privacy_confirmation()
