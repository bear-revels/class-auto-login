import os
import time
import logging
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException, NoSuchElementException

class MoodleAutoAttendance:
    def __init__(self, url):
        self.url = url
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        self.driver = webdriver.Chrome(options=chrome_options)
        self.logger = logging.getLogger(__name__)

    def login(self, username, password):
        try:
            self.driver.get(self.url)
            self.logger.info("Logging in...")
            username_field = self.driver.find_element_by_id('username')
            username_field.send_keys(username)
            password_field = self.driver.find_element_by_id('password')
            password_field.send_keys(password)
            login_button = self.driver.find_element_by_id('loginbtn')
            login_button.click()
            self.logger.info("Login successful.")
        except NoSuchElementException as e:
            self.logger.error("Element not found: %s", e)
        except Exception as e:
            self.logger.error("An unexpected error occurred during login: %s", e)

    def check_in_out(self, location, check_in_times, check_out_times):
        while True:
            current_time = time.strftime("%H:%M")
            current_day = time.strftime("%A")
            try:
                if current_day in check_in_times and current_time in check_in_times[current_day]:
                    self.driver.get(self.url)
                    check_in_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, 'Check in')))
                    check_in_button.click()
                    location_dropdown = self.driver.find_element_by_id('id_location')
                    location_dropdown.send_keys(location[current_day])
                    location_dropdown.send_keys(Keys.RETURN)
                if current_day in check_out_times and current_time in check_out_times[current_day]:
                    self.driver.get(self.url)
                    check_out_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, 'Check out')))
                    check_out_button.click()
            except TimeoutException as e:
                self.logger.error("Timeout waiting for element: %s", e)
            except NoSuchElementException as e:
                self.logger.error("Element not found: %s", e)
            except Exception as e:
                self.logger.error("An unexpected error occurred: %s", e)
            time.sleep(60)  # Check time every minute

if __name__ == "__main__":
    url = "https://moodle.becode.org/mod/attendance/view.php?id=90"

    # Retrieve username and password from environment variables
    username = os.getenv("MOODLE_USERNAME")
    password = os.getenv("MOODLE_PASSWORD")

    # Configure logging
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    check_in_times = {
        "Monday": ["09:00", "13:30"],
        "Tuesday": ["09:00", "13:30"],
        "Wednesday": ["09:00", "13:30"],
        "Thursday": ["09:00", "13:30"],
        "Friday": ["09:00", "13:30"]
    }

    check_out_times = {
        "Monday": ["12:30", "17:00"],
        "Tuesday": ["12:30", "17:00"],
        "Wednesday": ["12:30", "17:00"],
        "Thursday": ["12:30", "17:00"],
        "Friday": ["12:30", "17:00"]
    }

    location = {
        "Monday": "oncampus",
        "Tuesday": "athome",
        "Wednesday": "athome",
        "Thursday": "oncampus",
        "Friday": "athome"
    }

    # Configure logging
    logging.basicConfig(level=logging.ERROR)

    moodle_auto_attendance = MoodleAutoAttendance(url)
    moodle_auto_attendance.login(username, password)
    moodle_auto_attendance.check_in_out(location, check_in_times, check_out_times)
