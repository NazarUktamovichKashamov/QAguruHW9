import allure
from allure_commons.types import Severity
from selene import browser, by, be
from selene.support.shared.jquery_style import s


@allure.tag("web")
@allure.severity(Severity.BLOCKER)
@allure.label("owner", "Nazar")
@allure.feature("ExampleTest")
@allure.story("Issue")
def test_labels():
    browser.open("https://github.com")
    s(".octicon-search").click()
    s("#query-builder-test").send_keys('eroshenkoam/allure-example')
    s("#query-builder-test").submit()
    s(by.link_text("eroshenkoam/allure-example")).click()
    s("#issues-tab").click()
    s(by.partial_text("#76")).should(be.visible)
