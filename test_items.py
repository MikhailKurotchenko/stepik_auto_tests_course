from selenium.webdriver.common.by import By


def test_sale_button_exists(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser.get(link)
    assert len(browser.find_elements(By.CSS_SELECTOR, '.btn-add-to-basket')) > 0, 'КНОПКИ ДОБАВЛЕНИЯ В ' \
                                                                                  'КОРЗИНУ НЕТ'
