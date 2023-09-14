import os
import time

import pytest
from dotenv import load_dotenv


load_dotenv()


@pytest.mark.parametrize(
    "email,password,result",
    [
        # (os.getenv("EMAIL"), os.getenv("PASSWORD"), True),
        # ("some_email@gmail.com", os.getenv("PASSWORD"), False),
        # (os.getenv("EMAIL"), "some_password", False),
        ("some_email@gmail.com", "some_password", False),
    ],
)
def test_user_login(user_login_fixture, email, password, result):
    page = user_login_fixture

    page.click_element(page.find_hello_login())
    time.sleep(2)
    page.write_email(page.find_email(), email)
    time.sleep(2)
    page.write_password(page.find_password(), password)
    time.sleep(2)
    page.click_element(page.find_login())
    time.sleep(10)

    assert page.is_element("com.ajaxsystems:id/authLogin") == result



# def test_sidebar(user_login_fixture, email, password, expected_result):
#     pass

