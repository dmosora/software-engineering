import time

from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Pylint code to name mapping: https://github.com/janjur/readable-pylint-messages
from behave import * # pylint:disable=wildcard-import,unused-wildcard-import

from webdriver_manager.chrome import ChromeDriverManager

def setup_chrome():
    # Needed to give the headless Chrome something to "draw" to
    display = Display(visible=0, size=(800, 600))
    display.start()

    # Needed because we are the root user, and root needs `--no-sandbox`
    # as per http://chromedriver.chromium.org/help/chrome-doesn-t-start
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")

    # Add debugging options, logs for each run will overwrite the file here
    service_log_path = "/var/log/chromedriver.log"
    service_args = ['--verbose']
    return webdriver.Chrome(ChromeDriverManager().install(),
                            options=options,
                            service_args=service_args,
                            service_log_path=service_log_path)

@given(u'we are browsing amazon.com')
def navigate_step_impl(context):
    browser = setup_chrome()
    context.browser = browser 
    browser.get("https://www.amazon.com")
    time.sleep(4)
    assert "Amazon.com" in browser.title

@when(u'we search for "{target}"')
def search_step_impl(context, target):
    browser = context.browser
    searchbox = browser.find_element_by_name("field-keywords")
    searchbox.clear()
    searchbox.send_keys(target)
    searchbox.send_keys(Keys.RETURN)
    time.sleep(4)
    assert "Amazon.com" in browser.title

@then(u'we should see a "{result}"')
def result_step_impl(context, result):
    browser = context.browser
    assert result in browser.page_source