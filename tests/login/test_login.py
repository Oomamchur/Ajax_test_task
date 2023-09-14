import os
import time

import pytest
from dotenv import load_dotenv

load_dotenv()


@pytest.mark.parametrize(
    "email,password,result",
    [
        (os.getenv("EMAIL"), os.getenv("PASSWORD"), True),
        ("some_email@gmail.com", os.getenv("PASSWORD"), False),
        (os.getenv("EMAIL"), "some_password", False),
        ("some_email@gmail.com", "some_password", False),
    ],
)
def test_user_login(user_login_fixture, email, password, result):
    page = user_login_fixture
    page.click_element(page.find_hello_login())
    page.write_email(page.find_email(), email)
    page.write_password(page.find_password(), password)
    page.click_element(page.find_login())

    time.sleep(10)

    assert page.is_element("com.ajaxsystems:id/authLogin") == result


@pytest.mark.parametrize(
    "email,password,sidebar_element",
    [
        (
            os.getenv("EMAIL"),
            os.getenv("PASSWORD"),
            "com.ajaxsystems:id/settings",
        ),
        (
            "some_email@gmail.com",
            os.getenv("PASSWORD"),
            "com.ajaxsystems:id/help",
        ),
        (
                os.getenv("EMAIL"),
                "some_password",
                "com.ajaxsystems:id/logs"
        ),
        (
                "some_email@gmail.com",
                "some_password",
                "com.ajaxsystems:id/addHub"
        ),
    ],
)
def test_sidebar(user_login_fixture, email, password, sidebar_element):
    page = user_login_fixture
    page.click_element(page.find_hello_login())
    page.write_email(page.find_email(), email)
    page.write_password(page.find_password(), password)
    page.click_element(page.find_login())

    time.sleep(10)

    page.click_element(page.find_sidebar())

    assert page.is_element(sidebar_element)
