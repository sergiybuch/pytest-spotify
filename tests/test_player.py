from pytest import mark
from page_objects.main_page import MainPage
from page_objects.player_page import Player


@mark.usefixtures('login_logout')
class TestSpotifyPlayer:

    def test_button_play(self, driver, player, action):
        action.wait_until_element_visible(MainPage.see_all_button)
        if len(driver.find_elements(*Player.pause_button)) > 0:
            player.click_pause_button()
        player.click_play_button()
        action.wait_for_element_invisible(Player.play_button)

        assert driver.find_element(*Player.pause_button) is not None
        assert driver.find_element(*Player.playback_bar) is not None

    def test_button_next(self, driver, player, action):
        was_playing = driver.find_element(*Player.now_playing_song).text
        action.wait_for_element_invisible(Player.control_loading)
        player.click_next_button()
        action.wait_until_element_visible(Player.progress_bar_3_sec)
        now_playing = driver.find_element(*Player.now_playing_song).text

        assert now_playing != was_playing
        assert driver.find_element(*Player.next_button).is_enabled()
        assert driver.find_element(*Player.pause_button) is not None
        assert driver.find_element(*Player.previous_button).is_enabled()

    def test_button_previous(self, driver, player, action):
        was_playing = driver.find_element(*Player.now_playing_song).text
        if len(driver.find_elements(*Player.play_button)) > 0:
            player.click_play_button()
        action.wait_for_element_invisible(Player.control_loading)
        player.click_next_button()
        action.wait_until_element_visible(Player.progress_bar_3_sec)
        player.click_previous_button()
        action.wait_until_element_visible(Player.progress_bar_1_sec)
        now_playing = driver.find_element(*Player.now_playing_song).text

        assert now_playing == was_playing
        assert driver.find_element(*Player.next_button).is_enabled()
        assert driver.find_element(*Player.pause_button) is not None
        assert driver.find_element(*Player.previous_button).is_enabled()

    def test_button_shuffle(self, driver, player, action):
        action.wait_for_element_invisible(Player.control_loading)
        player.click_enable_shuffle_button()
        action.wait_until_element_visible(Player.disable_shuffle_button)
        player.click_disable_shuffle_button()

        assert driver.find_element(*Player.enable_shuffle_button).is_enabled()

    def test_button_repeat(self, driver, player, action):
        action.wait_for_element_invisible(Player.control_loading)
        player.click_enable_repeat_button()
        action.wait_until_element_visible(Player.enable_repeat_one_button)
        player.click_enable_repeat_one_button()
        action.wait_until_element_visible(Player.disable_repeat_button)
        player.click_disable_repeat_button()

        assert driver.find_element(*Player.enable_repeat_button).is_enabled()
