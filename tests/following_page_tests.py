from ptest.decorator import TestClass, Test
from ptest.assertion import assert_equals, assert_false, assert_true
from .base_test import PTestBase
from resources.test_data import data
from ptest.plogger import preporter


@TestClass()
class FollowingPageTests(PTestBase):

    @Test(data_provider=data.ONBOARDING_DATA)
    def test_001_complete_on_boarding(self, onboarding_team, onboarding_nationality):
        self.on_boarding_screen.search_and_select_content(onboarding_team)
        self.on_boarding_screen.search_and_select_content(onboarding_nationality)
        self.on_boarding_screen.accept_privacy_confirmation()
        self.following_screen.navigate_to_following_page()
        assert_equals(self.following_screen.get_favourite_club_name(), onboarding_team)
        assert_equals(self.following_screen.get_favourite_nation_name(), onboarding_nationality)

    @Test(data_provider=data.USER_CHOICES)
    def test_002_content_follow_unfollow_workflow_from_search(self, team, competition, player):
        self.following_screen.follow_item(team)
        self.following_screen.follow_item(competition)
        self.following_screen.follow_item(player)
        follow_result = self.following_screen.get_all_following_item_names()
        assert_true(team and competition and player in follow_result)
        self.following_screen.unfollow_item(team.lower())
        self.following_screen.unfollow_item(competition.lower())
        self.following_screen.unfollow_item(player.lower())
        unfollow_result = self.following_screen.get_all_following_item_names()
        assert_true(team and competition and player not in unfollow_result)

    @Test()
    def test_003_cancel_remove_workflow_favourite_club_at_end(self):
        self.following_screen.clear_favourite_club()
        self.following_screen.discard_user_favourite_deletion()
        assert_false(self.following_screen.is_user_favourite_club_cleared())

    @Test()
    def test_004_cancel_remove_workflow_favourite_nation_at_end(self):
        self.following_screen.clear_favourite_club()
        self.following_screen.discard_user_favourite_deletion()
        assert_false(self.following_screen.is_user_favourite_club_cleared())

    @Test()
    def test_005_complete_remove_favourite_club(self):
        self.following_screen.clear_favourite_club()
        self.following_screen.confirm_user_favourite_deletion()
        assert_true(self.following_screen.is_user_favourite_club_cleared())

    @Test()
    def test_006_complete_remove_favourite_nation(self):
        self.following_screen.clear_favourite_nation()
        self.following_screen.confirm_user_favourite_deletion()
        assert_true(self.following_screen.is_user_favourite_nation_cleared())
