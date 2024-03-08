import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

class MoodleAutoAttendance:
    def __init__(self, url, username, password):
        self.url = url
        self.username = username
        self.password = password
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        self.driver = webdriver.Chrome(options=chrome_options)

    def login(self):
        self.driver.get(self.url)
        username_field = self.driver.find_element_by_id('username')
        username_field.send_keys(self.username)
        password_field = self.driver.find_element_by_id('password')
        password_field.send_keys(self.password)
        login_button = self.driver.find_element_by_id('loginbtn')
        login_button.click()

    def check_in_out(self, location, check_in_times, check_out_times):
        while True:
            current_time = time.strftime("%H:%M")
            current_day = time.strftime("%A")
            if current_day in check_in_times:
                if current_time in check_in_times[current_day]:
                    self.driver.get(self.url)
                    check_in_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, 'Check in')))
                    check_in_button.click()
                    location_dropdown = self.driver.find_element_by_id('id_location')
                    location_dropdown.send_keys(location[current_day])
                    location_dropdown.send_keys(Keys.RETURN)
            if current_day in check_out_times:
                if current_time in check_out_times[current_day]:
                    self.driver.get(self.url)
                    check_out_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, 'Check out')))
                    check_out_button.click()
            time.sleep(60)  # Check time every minute

if __name__ == "__main__":
    url = "https://moodle.becode.org/mod/attendance/view.php?id=90"
    username = "gnt-2024-01-arai-revels"
    password = "BECODEhambone43!"

    check_in_times = {
        "Monday": ["09:00"],
        "Thursday": ["09:00"],
        "Tuesday": ["13:30"],
        "Wednesday": ["13:30"],
        "Friday": ["13:30"]
    }

    check_out_times = {
        "Monday": ["12:30"],
        "Thursday": ["17:00"],
        "Tuesday": ["17:00"],
        "Wednesday": ["17:00"],
        "Friday": ["12:30"]
    }

    location = {
        "Monday": "oncampus",
        "Thursday": "oncampus",
        "Tuesday": "athome",
        "Wednesday": "athome",
        "Friday": "athome"
    }

    moodle_auto_attendance = MoodleAutoAttendance(url, username, password)
    moodle_auto_attendance.login()
    moodle_auto_attendance.check_in_out(location, check_in_times, check_out_times)