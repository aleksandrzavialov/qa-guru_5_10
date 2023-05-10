import allure
from allure_commons.types import Severity
from selene import be, by
from selene.support.shared import browser


def test_selene_github_issue():
    browser.open('https://github.com')

    browser.element('.header-search-input').type('eroshenkoam/allure-example').submit()
    browser.all('.repo-list-item a').first.click()
    browser.element('#issues-tab').click()
    browser.element(by.text('issue_to_test_allure_report')).should(be.clickable)


def test_lambda_github_issue():
    with allure.step('Оpen main page'):
        browser.open('https://github.com')

    with allure.step('Search for a repo'):
        browser.element('.header-search-input').type('eroshenkoam/allure-example').submit()

    with allure.step('Open first found repo'):
        browser.all('.repo-list-item a').first.click()

    with allure.step('Open Issues tab'):
        browser.element('#issues-tab').click()

    with allure.step("Check that issue with text 'issue_to_test_allure_report' is available"):
        browser.element(by.text('issue_to_test_allure_report')).should(be.clickable)


def test_decorator_github_issue():
    open_main_page()
    search_for_repository('eroshenkoam/allure-example')
    open_first_found_repository()
    open_issue_tab()
    should_see_issue_with_number('issue_to_test_allure_report')


@allure.step('Оpen main page')
def open_main_page():
    browser.open('https://github.com')


@allure.step("Search for a repo '{repo}'")
def search_for_repository(repo):
    browser.element('.header-search-input').type(repo).submit()


@allure.step('Open first found repo')
def open_first_found_repository():
    browser.all('.repo-list-item a').first.click()


@allure.step('Open Issues tab')
def open_issue_tab():
    browser.element('#issues-tab').click()


@allure.step('Check that issue with text {issue_text} is available')
def should_see_issue_with_number(issue_text):
    browser.element(by.text(issue_text)).should(be.clickable)


@allure.tag('web')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'azavialov')
@allure.feature('Repo issues')
@allure.story('An issue with defined text should exist')
@allure.link('https://github.com', name='Github')
def test_decorator_labels_github_issue():
    with allure.step('Оpen main page'):
        browser.open('https://github.com')

    with allure.step('Search for a repo'):
        browser.element('.header-search-input').type('eroshenkoam/allure-example').submit()

    with allure.step('Open first found repo'):
        browser.all('.repo-list-item a').first.click()

    with allure.step('Open Issues tab'):
        browser.element('#issues-tab').click()

    with allure.step("Check that issue with text 'issue_to_test_allure_report' is available"):
        browser.element(by.text('issue_to_test_allure_report')).should(be.clickable)
