"""
UI test for CV
"""
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


URL = "https://qa-aleksandranaumova.github.io/"


def test_page_titles(browser):
    """
    Test case TC-1. Наличие заголовков на странице
    """

    browser.get(URL)
    element_main = browser.find_element(by=By.CSS_SELECTOR, value="header  h1")
    assert element_main.text == "Наумова Александра 💛", 'Top menu does not matching to expected'

    element_secondary = browser.find_element(by=By.CSS_SELECTOR, value="section:nth-child(1) h2")
    assert element_secondary.text == "Contacts", 'Top menu does not matching to expected'

    element_secondary = browser.find_element(by=By.CSS_SELECTOR, value="section:nth-child(2) h2")
    assert element_secondary.text == "О себе", 'Top menu does not matching to expected'
    

def test_page_links(browser):
    """
    Test case TC-2. Наличие ссылок на странице
    """

    browser.get(URL)
    link_first = browser.find_element(By.XPATH,'//a[contains(@href,"https://t.me/Saymuria")]')
    assert link_first.text == "@Saymuria", 'Top menu does not matching to expected'

    link_second = browser.find_element(By.XPATH,'//a[contains(@href,"naumova.al2001@yandex.ru")]')
    assert link_second.text == "naumova.al2001", 'Top menu does not matching to expected'

    link_third = browser.find_element(By.XPATH,'//a[contains(@href,"https://vk.com/saymuria")]')
    assert link_third.text == "Aleksandra Saymuria", 'Top menu does not matching to expected'

    link_fourth = browser.find_element(By.XPATH,'//a[contains(@href,"https://github.com/QA-AleksandraNaumova")]')
    assert link_fourth.text == "github.com/QA-AleksandraNaumova/", 'Top menu does not matching to expected'


def test_page_buttons(browser):
    """
    Test case TC-3. Кликабельность ссылок
    """

    browser.get(URL)
    button_tg = browser.find_element(By.CSS_SELECTOR,'li:nth-child(1)  a')
    button_tg.click
    WebDriverWait(browser, timeout=5, poll_frequency=1).until(
        EC.url_changes("https://t.me/Saymuria"))

    button_tg = browser.find_element(By.CSS_SELECTOR,'li:nth-child(2)  a')
    button_tg.click
    WebDriverWait(browser, timeout=5, poll_frequency=1).until(
        EC.url_changes("naumova.al2001@yandex.ru"))

    button_tg = browser.find_element(By.CSS_SELECTOR,'li:nth-child(3)  a')
    button_tg.click
    WebDriverWait(browser, timeout=5, poll_frequency=1).until(
        EC.url_changes("https://vk.com/saymuria"))

    button_tg = browser.find_element(By.CSS_SELECTOR,'li:nth-child(4)  a')
    button_tg.click
    WebDriverWait(browser, timeout=5, poll_frequency=1).until(
        EC.url_changes("https://github.com/QA-AleksandraNaumova"))
