from behave import when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

@when('I click the "{button}" button')
def step_impl(context, button):
    element_id = button.lower() + '-btn'
    context.driver.find_element(By.ID, element_id).click()

@then('I should see "{text}" in the results')
def step_impl(context, text):
    found = WebDriverWait(context.driver, context.wait_seconds).until(
        expected_conditions.text_to_be_present_in_element(
            (By.ID, 'search_results'), text
        )
    )
    assert(found)

@then('I should see the message "{message}"')
def step_impl(context, message):
    found = WebDriverWait(context.driver, context.wait_seconds).until(
        expected_conditions.text_to_be_present_in_element(
            (By.ID, 'flash_message'), message
        )
    )
    assert(found)
