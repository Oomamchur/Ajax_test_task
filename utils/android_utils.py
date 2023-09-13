from udid import device_udid


def android_get_desired_capabilities():
    return {
        "autoGrantPermissions": True,
        "automationName": "uiautomator2",
        "newCommandTimeout": 500,
        "noSign": True,
        "platformName": "Android",
        "platformVersion": "10",
        "resetKeyboard": True,
        "systemPort": 8301,
        "takesScreenshot": True,
        "udid": device_udid(),
        "appPackage": "com.ajaxsystems",
        "appActivity": "com.ajaxsystems.ui.activity.LauncherActivity",
    }
