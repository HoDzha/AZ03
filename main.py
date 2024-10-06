# Импорт необходимых библиотек
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
# Настройки для запуска браузера

# Создание объекта драйвера

driver = webdriver.Chrome()

# Открытие страницы с предложениями аренды квартир
url = "https://kazan.cian.ru/snyat-kvartiru-studiya-ili-1-komn/"
driver.get(url)

# Задержка, чтобы страница успела загрузиться
time.sleep(10)

# Парсинг цен квартир
try:
    # Используем XPath для нахождения цены
    prices = driver.find_elements(By.XPATH, '//div[@data-name="PriceLayout"]//span[contains(@class, "aee5b7c44e--text--e4SBY")]')

except Exception as e:
    print(f'Произошла ошибка: {e}')
finally:
    pass
    # Закрытие драйвера

price_list = [price.text for price in prices]

# Вывод полученных данных
for i, price in enumerate(price_list, start=1):
    print(f"Квартира {i}: {price}")

# Закрытие браузера
driver.quit()



