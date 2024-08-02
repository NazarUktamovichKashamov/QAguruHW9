import allure
from selene import by, be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s
repo = 'eroshenkoam/allure-example'


def test_issue():
    browser.open("https://github.com")
    s(".octicon-search").click()
    s("#query-builder-test").send_keys('eroshenkoam/allure-example')
    s("#query-builder-test").submit()
    s(by.link_text("eroshenkoam/allure-example")).click()
    s("#issues-tab").click()
    s(by.partial_text("#76")).should(be.visible)


#def test_decorator_steps():


