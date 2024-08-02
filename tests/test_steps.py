import allure
from selene import by, be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


def test_issue_designed_steps():
    with allure.step('Заходим на гитхаб'):
        browser.open("https://github.com")

    with allure.step('Кликаем на поиск'):
        s(".octicon-search").click()

    with allure.step('Вводим искомые данные'):
        s("#query-builder-test").send_keys('eroshenkoam/allure-example')

    with allure.step('Запускаем поиск'):
        s("#query-builder-test").submit()

    with allure.step('Ищем нужную страницу'):
        s(by.link_text("eroshenkoam/allure-example")).click()

    with allure.step('Нажимаем на нужную страницу'):
        s("#issues-tab").click()

    with allure.step('Проверяем результат'):
        s(by.partial_text("#76")).should(be.visible)