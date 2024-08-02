import allure
from selene import by, be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s
from allure_commons.types import Severity


@allure.tag("web")
@allure.severity(Severity.BLOCKER)
@allure.label("owner", "Nazar")
@allure.feature("ExampleTest")
@allure.story("Issue")
@allure.step('Открываем главную страницу')
def open_main_page():
    browser.open("https://github.com")

@allure.step('Ищем репозиторий {repo}')
def search_for_repos(repo):
    s(".octicon-search").click()
    s("#query-builder-test").send_keys(repo)
    s("#query-builder-test").submit()

@allure.step('Переходим к репозиторию')
def go_to_repos(repo):
    s(by.link_text(repo)).click()

@allure.step('Открываем Issue Tab')
def open_issue_tab():
    s("#issues-tab").click()

@allure.step('Проверяем результат')
def check_result():
    s(by.partial_text("#76")).should(be.visible)


def test_decoration():
    open_main_page()
    search_for_repos('eroshenkoam/allure-example')
    go_to_repos('eroshenkoam/allure-example')
    open_issue_tab()
    check_result()