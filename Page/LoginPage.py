from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Utilities.BasePage import BasePage


class Login(BasePage):
    sign_in_locator = (By.CSS_SELECTOR, "a[href='https://www.linkedin.com/login']")
    email_textbox_locator = (By.ID, "username")
    password_textbox_locator = (By.ID, "password")
    sign_in_button_locator = (By.CSS_SELECTOR, "button[type='submit']")
    profile_name_locator = (By.CSS_SELECTOR, "div[class='t-16 t-black t-bold']")

    # Enter User details
    email = ""
    password = ""
    name = ""

    def __init__(self, driver):
        self.driver = driver

    def sign_in(self):
        try:
            # Wait until the element is clickable and then click it
            element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.sign_in_locator)
            )
            element.click()
            return True
        except Exception as e:
            print(f"Error during sign in: {str(e)}")
            return False

    def input_email(self):
        try:
            # Wait until the email input field is visible
            email_input = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.email_textbox_locator)
            )
            email_input.clear()  # Clear any pre-filled text
            email_input.send_keys(self.email)
            return True
        except Exception as e:
            print(f"Error during inputting email: {str(e)}")
            return False

    def input_password(self):
        try:
            # Wait until the email input field is visible
            email_input = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.password_textbox_locator)
            )
            email_input.clear()  # Clear any pre-filled text
            email_input.send_keys(self.password)
            return True
        except Exception as e:
            print(f"Error during inputting email: {str(e)}")
            return False

    def click_signin_button(self):
        try:
            # Wait until the element is clickable and then click it
            element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.sign_in_button_locator)
            )
            element.click()
            return True
        except Exception as e:
            print(f"Error during sign in: {str(e)}")
            return False

    def get_profile_name(self):
        try:
            # Locate the profile name element and get the text
            profile_name = self.driver.find_element(*self.profile_name_locator).text
            return profile_name
        except Exception as e:
            print(f"Error retrieving profile name: {str(e)}")
            return None
