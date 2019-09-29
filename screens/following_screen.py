import time
from ptest.plogger import preporter
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
        """
        This method navigates user to the following page by clicking on following icon in navigation bar in bottom
        :return:
        """
        time.sleep(1)  # Added time sleep as following button do not have unique id
        preporter.info("Navigating to following page")
        following_button_element = self.driver.find_element_visible(self.following_nav_button, wait_until=10)
        self.tap(following_button_element)

    def search_item_and_click_on_star(self, item):
        """
        This method performs search for a given content and clicks on the star button which is present in the right side
        of the first result.
        :param item: Name of the content which will get searched
        :return: It returns the type of searched result it acted on. For example player,competition or team.
        """
        self.navigate_to_following_page()
        search_element = self.driver.find_element_visible(self.search_icon, wait_until=10)
        self.tap(search_element)
        search_box_element = self.driver.find_element_visible(self.search_input_box, wait_until=10)
        preporter.info("Searching for :  {}".format(item))
        search_box_element.send_keys(item)
        first_search_result_element = self.driver.find_element_visible(self.searched_first_result, wait_until=10)
        search_result_type = self.driver.find_element_visible(self.search_result_type, wait_until=10).text
        actual_search_result_title = first_search_result_element.text
        if item.lower() == actual_search_result_title.lower():
            follow_button = self.driver.find_element_visible(self.follow_first_search_result, wait_until=10)
            self.tap(follow_button)
            return search_result_type
        else:
            preporter.info("Searching for {} but found {}".format(item,actual_search_result_title))
            raise ValueError("Did't found proper search result for {}".format(item))

    def follow_item(self, item):
        """
        This method searches for a given content and adds it to the following list. It also navigates back to the
        following page by pressing back twice. This method expects that the content provided is not in followed state.
        :param item: Content to be followed
        :return:
        """
        preporter.info("Following {}".format(item))
        search_result_type = self.search_item_and_click_on_star(item)
        if "Competitions" not in search_result_type:
            done_element = self.driver.find_element_visible(self.push_notification_done_button, wait_until=10)
            self.tap(done_element)
        self.driver.back()
        self.driver.back()

    def unfollow_item(self, item):
        """
        This method searches for a given content and removes it from the following list. It also navigates back to the
        following page by pressing back twice. This method expects that the content provided is in followed state.
        :param item: Content to be un-followed
        :return:
        """
        preporter.info("Unfollowing {}".format(item))
        self.search_item_and_click_on_star(item)
        self.driver.back()
        self.driver.back()

    def get_all_following_item_names(self):
        """
        This method gets all user followed contents and returns it as a list.
        :return: It returns a list consists of contents user followed or an empty list if user haven't followed
        anything.
        """
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
        """
        This method checks if user favourite club is present or removed.
        :return: returns true if user's favourite club gets cleared otherwise false
        """
        self.navigate_to_following_page()
        return "Favorite team" == self.get_favourite_club_name()

    def is_user_favourite_nation_cleared(self):
        """
        This method checks if user favourite nation is present or removed.
        :return: returns true if user's favourite nation gets cleared otherwise false
        """
        self.navigate_to_following_page()
        return "National team" == self.get_favourite_nation_name()

    def confirm_user_favourite_deletion(self):
        """
        This confirms the prompt which comes when deleting user favourite content.
        :return:
        """
        remove_confirmation_element = self.driver.find_element_present(self.remove_confirmation_button, wait_until=10)
        self.tap(remove_confirmation_element)
        self.driver.back()

    def discard_user_favourite_deletion(self):
        """
        This discards the prompt which comes when deleting user favourite content.
        :return:
        """
        keep_element = self.driver.find_element_present(self.keep_button, wait_until=10)
        self.tap(keep_element)
        self.driver.back()
        self.navigate_to_following_page()

    def clear_favourite_nation(self):
        """
        This is first part of remove user favourite nation workflow.This clears the user favourite nation. After this
        method the confirmation discard or accept method should get called in order to finish the workflow.
        :return:
        """
        self.navigate_to_following_page()
        edit_element = self.driver.find_element_present(self.edit_button, wait_until=10)
        self.tap(edit_element)
        remove_favourite_nation_element = self.driver.find_element_present(self.remove_favourite_nation, wait_until=10)
        self.tap(remove_favourite_nation_element)

    def clear_favourite_club(self):
        """
        This is first part of remove user favourite club workflow.This clears the user favourite club. After this
        method the confirmation discard or accept method should get called in order to finish the workflow.
        :return:
        """
        self.navigate_to_following_page()
        edit_element = self.driver.find_element_present(self.edit_button, wait_until=10)
        self.tap(edit_element)
        remove_favourite_club_element = self.driver.find_element_present(self.remove_favourite_club, wait_until=10)
        self.tap(remove_favourite_club_element)

    def get_favourite_club_name(self):
        """
        :return: Returns favourite user's favourite club name
        """
        return self.driver.find_element_present(self.favourite_club, wait_until=10).text

    def get_favourite_nation_name(self):
        """
        :return: Returns favourite user's favourite nation name
        """
        return self.driver.find_element_present(self.favourite_nation, wait_until=10).text
