import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(autouse=True)
def testing():
    pytest.driver = webdriver.Chrome('C:/Users/Lena/PycharmProjects/pythonProject/chromedriver-win64/chromedriver.exe')
    # Переходим на страницу авторизации
    pytest.driver.get('http://petfriends.skillfactory.ru/login')
    yield
    pytest.driver.quit()


def test_show_my_pets():
    # Вводим email
    pytest.driver.find_element(By.ID, 'email').send_keys('qapython@mail.ru')
    # Вводим пароль
    pytest.driver.find_element(By.ID, 'pass').send_keys('1234')
    # Нажимаем на кнопку входа в аккаунт
    pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    # Проверяем, что мы оказались на главной странице пользователя
    assert pytest.driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"

    # Добавляем неявное ожидание элементов (фото, имя питомца, возраст)
    pytest.driver.implicitly_wait(10)
    # Переходим на страницу питомцев пользователя
    pytest.driver.get('https://petfriends.skillfactory.ru/my_pets')
    images = pytest.driver.find_elements(By.XPATH, '//div[@id="all_my_pets"]//img')
    names = pytest.driver.find_elements(By.XPATH, '//div[@id="all_my_pets"]//td[1]')
    ages = pytest.driver.find_elements(By.XPATH, '//div[@id="all_my_pets"]//td[3]')

    for i in range(len(names)):
        assert images[i].get_attribute('src') != ''
        assert names[i].text != ''
        assert ages[i].text != ''


def test_count_of_my_pets():
    # Вводим email
    pytest.driver.find_element(By.ID, 'email').send_keys('qapython@mail.ru')
    # Вводим пароль
    pytest.driver.find_element(By.ID, 'pass').send_keys('1234')
    # Нажимаем на кнопку входа в аккаунт
    pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    # Проверяем, что мы оказались на главной странице пользователя
    assert pytest.driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"

    # Переходим на страницу питомцев пользователя
    pytest.driver.get('https://petfriends.skillfactory.ru/my_pets')
    # Добавляем явное ожидание таблицы питомцев пользователя
    element = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//table[@class="table table-hover"]//tbody')))

    cards = pytest.driver.find_elements(By.XPATH, '//table[@class="table table-hover"]//tbody/tr')

    assert len(cards) > 0
