# Shop: отображение страницы товара
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select # импортируем класс Select или библиотеки webdriver
from selenium import webdriver
driver = webdriver.Chrome()

# 1 Откроем страницу http://practice.automationtesting.in/
driver.get("http://practice.automationtesting.in/")
# Реализация неявного ожидания поиска элементов
driver.implicitly_wait(3) # говорим WebDriver искать каждый элемент в течение 3 секунд

# 2 Залогинемся
# Нажмём на вкладку "My Account Menu"
driver.find_element_by_css_selector('[href="http://practice.automationtesting.in/my-account/"]').click()

# В разделе "Login", введём email для логина 		# данные можно взять из предыдущего теста
email = driver.find_element_by_id("username")
email.send_keys("nadez.anikina@gmail.com")

# В разделе "Login", введём пароль для логина 	# данные можно взять из предыдущего теста
password = driver.find_element_by_id("password")
password.send_keys("@Admin#123654!^")

# Нажмём на кнопку "Login"
driver.find_element_by_css_selector('[name="login"]').click()

# 3 Нажмём на вкладку "Shop"
driver.find_element_by_css_selector('[href="http://practice.automationtesting.in/shop/"]').click()

# 4 Откроем книгу "HTML 5 Forms"
driver.find_element_by_css_selector('[href="http://practice.automationtesting.in/product/html5-forms/"]').click()

# 5 Добавим тест, что заголовок книги называется: "HTML5 Forms"
h1 = driver.find_element_by_css_selector('.product_title.entry-title')
h1_text = h1.text
assert "HTML5 Forms" in h1_text
print("Заголовок книги называется: HTML5 Forms")

# # Разлогинимся, нажав на вкладку "My Account Menu"
# driver.find_element_by_css_selector('[href="http://practice.automationtesting.in/my-account/"]').click()
# # Нажмём Logout
# driver.find_element_by_css_selector('[href="http://practice.automationtesting.in/my-account/customer-logout/"]').click()

# Shop: количество товаров в категории
# 1 Откроем страницу http://practice.automationtesting.in/
driver.get("http://practice.automationtesting.in/")
# Реализация неявного ожидания поиска элементов
driver.implicitly_wait(3) # говорим WebDriver искать каждый элемент в течение 3 секунд

# 2 Залогинемся
# Нажмём на вкладку "My Account Menu"
driver.find_element_by_css_selector('[href="http://practice.automationtesting.in/my-account/"]').click()

# В разделе "Login", введём email для логина 		# данные можно взять из предыдущего теста
email = driver.find_element_by_id("username")
email.send_keys("nadez.anikina@gmail.com")

# В разделе "Login", введём пароль для логина 	# данные можно взять из предыдущего теста
password = driver.find_element_by_id("password")
password.send_keys("@Admin#123654!^")

# Нажмём на кнопку "Login"
driver.find_element_by_css_selector('[name="login"]').click()

# 3 Нажмём на вкладку "Shop"
driver.find_element_by_css_selector('[href="http://practice.automationtesting.in/shop/"]').click()

# 4 Откроем категорию "HTML"
driver.find_element_by_css_selector('[href="http://practice.automationtesting.in/product-category/html/"]').click()

# 5 Добавим тест, что отображается три товара
items_count = driver.find_elements_by_class_name('woocommerce-LoopProduct-link')
if len(items_count) == 3:
      print("На экране отображается три товара")				# len здесь посчитает количество элементов, найденных при помощи find_elements

# # Разлогинимся, нажав на вкладку "My Account Menu"
# driver.find_element_by_css_selector('[href="http://practice.automationtesting.in/my-account/"]').click()
# # Нажмём Logout
# driver.find_element_by_css_selector('[href="http://practice.automationtesting.in/my-account/customer-logout/"]').click()

# Shop: сортировка товаров
# 1 Откроем страницу http://practice.automationtesting.in/
driver.get("http://practice.automationtesting.in/")
# Реализация неявного ожидания поиска элементов
driver.implicitly_wait(3) # говорим WebDriver искать каждый элемент в течение 3 секунд

# 2 Залогинемся
# Нажмём на вкладку "My Account Menu"
driver.find_element_by_css_selector('[href="http://practice.automationtesting.in/my-account/"]').click()

# В разделе "Login", введём email для логина 		# данные можно взять из предыдущего теста
email = driver.find_element_by_id("username")
email.send_keys("nadez.anikina@gmail.com")

# В разделе "Login", введём пароль для логина 	# данные можно взять из предыдущего теста
password = driver.find_element_by_id("password")
password.send_keys("@Admin#123654!^")

# Нажмём на кнопку "Login"
driver.find_element_by_css_selector('[name="login"]').click()

# 3 Нажмём на вкладку "Shop"
driver.find_element_by_css_selector('[href="http://practice.automationtesting.in/shop/"]').click()

# 4 Добавим тест, что в селекторе выбран вариант сортировки от большего к меньшему
order_by = driver.find_element_by_css_selector('.orderby >[value="price"]')
element_selected = order_by.get_attribute("selected")

if element_selected is not None:
    print("В селекторе выбран вариант сортировки от большего к меньшему")
else:
    print("В селекторе НЕ выбран вариант сортировки от большего к меньшему")

# 5 Отсортируем товары от большего к меньшему
price = driver.find_element_by_css_selector('[name="orderby"]')
selecting = Select(price)
selecting.select_by_value("price")

# 6 Снова объявите переменную с локатором основного селектора сортировки # т.к после сортировки страница обновится
order_by_2 = driver.find_element_by_css_selector('.orderby >[value="price"]')

# Добавим тест, что в селекторе выбран вариант сортировки от большего к меньшему
sheduled = driver.find_element_by_css_selector('.orderby >[value="price"]')
element_selected = sheduled.get_attribute("selected")

if element_selected is not None:
     print("В селекторе выбран вариант сортировки от большего к меньшему")
else:
     print("В селекторе НЕ выбран вариант сортировки от большего к меньшему")

# # Разлогинимся, нажав на вкладку "My Account Menu"
# driver.find_element_by_css_selector('[href="http://practice.automationtesting.in/my-account/"]').click()
# # Нажмём Logout
# driver.find_element_by_css_selector('[href="http://practice.automationtesting.in/my-account/customer-logout/"]').click()

# Shop: отображение, скидка товара
# 1 Откроем страницу http://practice.automationtesting.in/
driver.get("http://practice.automationtesting.in/")
# Реализация неявного ожидания поиска элементов
driver.implicitly_wait(3) # говорим WebDriver искать каждый элемент в течение 3 секунд

# 2 Залогинемся
# Нажмём на вкладку "My Account Menu"
driver.find_element_by_css_selector('[href="http://practice.automationtesting.in/my-account/"]').click()

# В разделе "Login", введём email для логина 		# данные можно взять из предыдущего теста
email = driver.find_element_by_id("username")
email.send_keys("nadez.anikina@gmail.com")

# В разделе "Login", введём пароль для логина 	# данные можно взять из предыдущего теста
password = driver.find_element_by_id("password")
password.send_keys("@Admin#123654!^")

# Нажмём на кнопку "Login"
driver.find_element_by_css_selector('[name="login"]').click()

# 3 Нажмём на вкладку "Shop"
driver.find_element_by_css_selector('[href="http://practice.automationtesting.in/shop/"]').click()

# 4 Откроем книгу "Android Quick Start Guide"
driver.find_element_by_css_selector('[href="http://practice.automationtesting.in/product/android-quick-start-guide/"]').click()

# 5 Добавим тест, что содержимое старой цены = "₹600.00"	# используйте assert
onsale = driver.find_element_by_css_selector('del .woocommerce-Price-amount')
onsale_text = onsale.text
assert "600.00" in onsale_text
print("Содержимое старой цены = ₹600.00")

# 6 Добавим тест, что содержимое новой цены = "₹450.00"		# используйте assert
price = driver.find_element_by_css_selector('ins .woocommerce-Price-amount')
price_text = price.text
assert "450.00" in price_text
print("Содержимое новой цены = ₹450.00")

# 7 Добавим явное ожидание и нажмём на обложку книги
face_book = WebDriverWait(driver, 3).until(
     EC.invisibility_of_element_located((By.CSS_SELECTOR, '#fullResImage[style="height: 413px; width: 309px;"]')))
driver.find_element_by_css_selector('[href="http://practice.automationtesting.in/wp-content/uploads/2017/01/Android-Quick-Start-Guide.png"]').click()

# 8 Добавим явное ожидание и закройте предпросмотр нажав на крестик (кнопка вверху справа)
close = WebDriverWait(driver, 3).until_not(
      EC.element_to_be_clickable((By.CLASS_NAME, "pp_close")))
driver.find_element_by_class_name("pp_close").click()

# Shop: проверка цены в корзине
# 1 Откроем страницу http://practice.automationtesting.in/
driver.get("http://practice.automationtesting.in/")
# Реализация неявного ожидания поиска элементов
driver.implicitly_wait(3) # говорим WebDriver искать каждый элемент в течение 3 секунд

# 2 Нажмём на вкладку "Shop"
driver.find_element_by_css_selector('[href="http://practice.automationtesting.in/shop/"]').click()

# 3 Добавим в корзину книгу "HTML5 WebApp Development"
driver.find_element_by_css_selector('[href="/shop/?add-to-cart=182"]').click()
time.sleep(3)
# 4 Добавим тест, что возле корзины(вверху справа) количество товаров = "1 Item", а стоимость = "₹180.00"
num_item = driver.find_element_by_class_name("cartcontents")
num_item_text = num_item.text
print(num_item_text)
assert "1 Item" in num_item_text

total_price = driver.find_element_by_css_selector('.wpmenucart-contents span.amount')
total_price_text = total_price.text
print(total_price_text)
assert "₹180.00" in total_price_text
print("Возле корзины(вверху справа) количество товаров = 1 Item, а стоимость = ₹180.00")

# 5 Перейдём в корзину
driver.find_element_by_css_selector('[href="http://practice.automationtesting.in/basket/"]').click()

# 6 Используя явное ожидание, проверим, что в Subtotal отобразилась стоимость
Subtotal = WebDriverWait(driver, 3).until_not(
     EC.invisibility_of_element_located((By.CSS_SELECTOR, '.product-price span.woocommerce-Price-amount')))

# Shop: работа в корзине
# 1 Откроем страницу http://practice.automationtesting.in/
driver.get("http://practice.automationtesting.in/")
# Реализация неявного ожидания поиска элементов
driver.implicitly_wait(3) # говорим WebDriver искать каждый элемент в течение 3 секунд

# 2 Нажмём на вкладку "Shop"
driver.find_element_by_css_selector('[href="http://practice.automationtesting.in/shop/"]').click()

# 3 Добавим в корзину книги "HTML5 WebApp Development" и "JS Data Structures and Algorithm"
driver.execute_script("window.scrollBy(0, 300);") 	# эта команда проскроллит страницу на 300 пикселей вниз
driver.find_element_by_css_selector('[href="/shop/?add-to-cart=182"]').click()
time.sleep(3)
driver.find_element_by_css_selector('[href="/shop/?add-to-cart=165"]').click()

# 4 Перейдём в корзину
driver.find_element_by_css_selector('[href="http://practice.automationtesting.in/basket/"]').click()

# 5 Удалим первую книгу
time.sleep(3)
driver.find_element_by_css_selector('.cart_item:nth-child(1) .product-remove').click()

# 6 Нажмём на Undo (отмена удаления)
driver.find_element_by_css_selector('.woocommerce-message >a').click()

# 7 В Quantity увеличим количесто товара до 3 шт для "JS Data Structures and Algorithm“
quantity = driver.find_element_by_name("cart[9766527f2b5d3e95d4a733fcfb77bd7e][qty]")
quantity.clear()
quantity.send_keys("3")

# 8 Нажмём на кнопку "UPDATE BASKET"
driver.find_element_by_name("update_cart").click()

# 9 Добавим тест, что value элемента quantity для "JS Data Structures and Algorithm" равно 3		# используйте assert
quantity_value = quantity.get_attribute("value")
print("quantity_value = ",quantity_value)
assert quantity_value=="3"
print("value элемента quantity для JS Data Structures and Algorithm равно 3")

# 10 Нажмём на кнопку "APPLY COUPON"
time.sleep(3)
driver.find_element_by_css_selector('[value="Apply Coupon"]').click()

# 11 Добавим тест, что возникло сообщение: "Please enter a coupon code."
error = driver.find_element_by_css_selector('.woocommerce-error >li')
error_text = error.text
print(error_text)
assert "Please enter a coupon code." in error_text
print("Возникло сообщение: Please enter a coupon code.")

# Shop: покупка товара
# 1 Откроем страницу http://practice.automationtesting.in/
driver.get("http://practice.automationtesting.in/")
# Реализация неявного ожидания поиска элементов
driver.implicitly_wait(3) # говорим WebDriver искать каждый элемент в течение 3 секунд

# 2 Нажмём на вкладку "Shop" и проскроллим на 300 пикселей вниз
driver.find_element_by_css_selector('[href="http://practice.automationtesting.in/shop/"]').click()
driver.execute_script("window.scrollBy(0, 300);") 	# эта команда проскроллит страницу на 300 пикселей вниз

# 3 Добавим в корзину книги "HTML5 WebApp Development"
driver.find_element_by_css_selector('[href="/shop/?add-to-cart=182"]').click()

# 4 Перейдём в корзину
driver.find_element_by_css_selector('[href="http://practice.automationtesting.in/basket/"]').click()

# 5 Нажмём "PROCEED TO CHECKOUT"
# Перед нажатием, добавим явное ожидание
checkout = WebDriverWait(driver, 3).until(
      EC.element_to_be_clickable((By.CSS_SELECTOR, '[href="http://practice.automationtesting.in/checkout/"]')))
driver.find_element_by_css_selector('[href="http://practice.automationtesting.in/checkout/"]').click()

# 6 Заполним все обязательные поля
# Перед заполнением first name, добавим явное ожидание
firstname_wait = WebDriverWait(driver, 3).until(
      EC.element_to_be_clickable((By.ID, "billing_first_name")))

driver.find_element_by_id("billing_first_name").send_keys("Nady")
driver.find_element_by_id("billing_last_name").send_keys("Golub")
driver.find_element_by_id("billing_email").send_keys("nadez.anikina@gmail.com")
driver.find_element_by_id("billing_phone").send_keys("89277397626")
# Для заполнения country нужно: нажать на селектор - > ввести название в поле ввода - > нажать на вариант который отобразится ниже ввода
driver.find_element_by_id("select2-chosen-1").click()
driver.find_element_by_class_name("select2-input").send_keys("Russia")
driver.find_element_by_id('select2-results-1').click()
driver.find_element_by_id("billing_address_1").send_keys("Ligovskii prospect 101")
driver.find_element_by_id("billing_address_2").send_keys("101")
driver.find_element_by_id("billing_city").send_keys("Sankt Petersburg")
driver.find_element_by_name("billing_state").send_keys("Russia")
driver.find_element_by_css_selector('#billing_postcode.input-text').send_keys("191119")

# 7 Выберем способ оплаты "Check Payments"
# Перед выбором, проскроллим на 600 пикселей вниз и добавим sleep
driver.execute_script("window.scrollBy(0, 300);") 	# эта команда проскроллит страницу на 300 пикселей вниз
time.sleep(3)
driver.find_element_by_id("payment_method_cheque").click()

# 8 Нажмём PLACE ORDER
driver.find_element_by_name("woocommerce_checkout_place_order").click()

# 9 Используя явное ожидание, проверим что отображается надпись "Thank you. Your order has been received."
done = WebDriverWait(driver,10).until_not(
      EC.text_to_be_present_in_element_value((By.CSS_SELECTOR, '.woocommerce-thankyou-order-received'),"Thank you. Your order has been received."))

print("На экране отображается надпись Thank you. Your order has been received.")

# 10 Используя явное ожидание, проверьте что в Payment Method отображается текст "Check Payments"
pay = WebDriverWait(driver, 3).until_not(
      EC.text_to_be_present_in_element_value((By.CSS_SELECTOR, '.page-content.entry-content:nth-child(1) tfoot>tr:nth-child(3) >td'),"Check Payments"))

print("В Payment Method отображается текст Check Payments")

driver.quit() 		# закроем драйвер в конце теста




