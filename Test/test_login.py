from Page.LoginPage import Login
from Utilities.BasePage import BasePage


class TestLogin(BasePage):

    def test_login(self):
        log = self.get_logger()
        linkedin = Login(self.driver)

        log.info("Opened Linkedin.com")
        linkedin.sign_in()

        log.info("Opened sign in page")
        linkedin.input_email()
        linkedin.input_password()

        log.info("Entered credentials")
        linkedin.click_signin_button()

        profile_name = linkedin.get_profile_name()
        log.info("Profile name: %s", profile_name)
        log.info("assertion to verify login success")
        assert linkedin.name in profile_name, f"Expected '{linkedin.name}' to be in '{profile_name}', but it was not."

