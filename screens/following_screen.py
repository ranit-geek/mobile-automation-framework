import time

from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import TimeoutException
from .base_screen import Screen


class FollowingScreen(Screen):

    following_nav_button = (MobileBy.XPATH, '(//*[@resource-id="de.motain.iliga:id/fixed_bottom_navigation_icon"])[3]')
    search_icon = (MobileBy.ID, 'toolbar')
    search_input_box = (MobileBy.ID, 'search_src_text')
    search_result_type = (MobileBy.XPATH, '(//*[@resource-id="de.motain.iliga:id/name"])[1]')
    edit_button = (MobileBy.ACCESSIBILITY_ID, 'Edit')
    complete_edit_button = (MobileBy.ID, 'action_done')
    push_notification_done_button = (MobileBy.ID, 'button_primary')
    favourite_club = (MobileBy.ID, 'favouriteClubText')
    favourite_nation = (MobileBy.ID, 'favouriteNationalTeamTxt')
    remove_favourite_club = (MobileBy.ID, 'removeFavouriteClub')
    remove_favourite_nation = (MobileBy.ID, 'removeFavouriteNationalTeam')
    remove_confirmation_button = (MobileBy.ID, 'tutorial_button_secondary')
    keep_button = (MobileBy.ID, 'tutorial_button_primary')
    browse_teams = (MobileBy.XPATH, '(//*[@resource-id="de.motain.iliga:id/actionBtn"])[1]')
    browse_competitions = (MobileBy.XPATH, '(//*[@resource-id="de.motain.iliga:id/actionBtn"])[2]')
    browse_players = (MobileBy.XPATH, '(//*[@resource-id="de.motain.iliga:id/actionBtn"])[3]')
    following_item = (MobileBy.XPATH, '(//*[@resource-id="de.motain.iliga:id/following_item_name"])[1]')
    all_following_items = (MobileBy.XPATH, '(//*[@resource-id="de.motain.iliga:id/following_item_name"])')
    searched_first_result = (MobileBy.XPATH, '(//*[@resource-id="de.motain.iliga:id/item_name"])[1]')
    follow_first_search_result = (MobileBy.XPATH, '(//*[@resource-id="de.motain.iliga:id/item_check"])[1]')

    def navigate_to_following_page(self):
        time.sleep(1)  # Added time sleep as following button do not have unique id
        following_button_element = self.driver.find_element_visible(self.following_nav_button, wait_until=10)
        self.tap(following_button_element)

    def search_item_and_click_on_star(self, item):
        self.navigate_to_following_page()
        search_element = self.driver.find_element_visible(self.search_icon, wait_until=10)
        self.tap(search_element)
        search_box_element = self.driver.find_element_visible(self.search_input_box, wait_until=10)
        search_box_element.send_keys(item)
        first_search_result_element = self.driver.find_element_visible(self.searched_first_result, wait_until=10)
        search_result_type = self.driver.find_element_visible(self.search_result_type, wait_until=10).text
        if item.lower() == first_search_result_element.text.lower():
            follow_button = self.driver.find_element_visible(self.follow_first_search_result, wait_until=10)
            self.tap(follow_button)
            return search_result_type
        else:
            raise ValueError("Did't found proper search result for {}".format(item))

    def follow_item(self, item):
        search_result_type = self.search_item_and_click_on_star(item)
        if "Competitions" not in search_result_type:
            done_element = self.driver.find_element_visible(self.push_notification_done_button, wait_until=10)
            self.tap(done_element)
        self.driver.back()
        self.driver.back()

    def unfollow_item(self, item):
        self.search_item_and_click_on_star(item)
        self.driver.back()
        self.driver.back()

    def get_all_following_item_names(self):
        self.navigate_to_following_page()
        following_item_names = []
        try:
            following_item_elements = self.driver.find_elements_present(self.all_following_items, wait_until=3)
            for item in following_item_elements:
                following_item_names.append(item.text)
        except TimeoutException:
            return following_item_names
        return following_item_names

    def is_user_favourite_club_cleared(self):
        self.navigate_to_following_page()
        return "Favorite team" == self.get_favourite_club_name()

    def is_user_favourite_nation_cleared(self):
        self.navigate_to_following_page()
        return "National team" == self.get_favourite_nation_name()

    def confirm_user_favourite_deletion(self):
        remove_confirmation_element = self.driver.find_element_present(self.remove_confirmation_button, wait_until=10)
        self.tap(remove_confirmation_element)
        self.driver.back()

    def discard_user_favourite_deletion(self):
        keep_element = self.driver.find_element_present(self.keep_button, wait_until=10)
        self.tap(keep_element)
        self.driver.back()
        self.navigate_to_following_page()

    def clear_favourite_nation(self):
        self.navigate_to_following_page()
        edit_element = self.driver.find_element_present(self.edit_button, wait_until=10)
        self.tap(edit_element)
        remove_favourite_nation_element = self.driver.find_element_present(self.remove_favourite_nation, wait_until=10)
        self.tap(remove_favourite_nation_element)

    def clear_favourite_club(self):
        self.navigate_to_following_page()
        edit_element = self.driver.find_element_present(self.edit_button, wait_until=10)
        self.tap(edit_element)
        remove_favourite_club_element = self.driver.find_element_present(self.remove_favourite_club, wait_until=10)
        self.tap(remove_favourite_club_element)

    def get_favourite_club_name(self):
        return self.driver.find_element_present(self.favourite_club, wait_until=10).text

    def get_favourite_nation_name(self):
        return self.driver.find_element_present(self.favourite_nation, wait_until=10).text
