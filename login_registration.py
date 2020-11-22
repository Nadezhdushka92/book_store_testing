# Registration_login: регистрация аккаунта
from selenium import webdriver
driver = webdriver.Chrome()

# 1 Откроем страницу http://practice.automationtesting.in/
driver.get("http://practice.automationtesting.in/")
# Реализация неявного ожидания поиска элементов
driver.implicitly_wait(3) # говорим WebDriver искать каждый элемент в течение 3 секунд

# 2 Нажмём на вкладку "My Account Menu"
driver.find_element_by_css_selector('[href="http://practice.automationtesting.in/my-account/"]').click()

# 3 В разделе "Register", введём email для регистрации
regemail = driver.find_element_by_id("reg_email")
regemail.send_keys("nadez.anikina@gmail.com")

# 4 В разделе "Register", введём пароль для регистрации
regpassword = driver.find_element_by_id("reg_password")
regpassword.send_keys("@Admin#123654!^")

# 5 Нажмиём на кнопку "Register"
driver.find_element_by_css_selector('[name="register"]').click()

# логин в систему
# 1 Откроем страницу http://practice.automationtesting.in/
driver.get("http://practice.automationtesting.in/")

# 2 Нажмём на вкладку "My Account Menu"
driver.find_element_by_css_selector('[href="http://practice.automationtesting.in/my-account/"]').click()

# 3 В разделе "Login", введём email для логина 		# данные можно взять из предыдущего теста
email = driver.find_element_by_id("username")
email.send_keys("nadez.anikina@gmail.com")

# 4 В разделе "Login", введём пароль для логина 	# данные можно взять из предыдущего теста
password = driver.find_element_by_id("password")
password.send_keys("@Admin#123654!^")

# 5 Нажмём на кнопку "Login"
driver.find_element_by_css_selector('[name="login"]').click()

# 6 Добавим проверку, что на странице есть элемент "Logout"
logout = driver.find_element_by_css_selector('[href="http://practice.automationtesting.in/my-account/customer-logout/"]')
logout_text = logout.text
assert "Logout" in logout_text
print("На странице есть элемент Logout")
driver.quit() 		# закроем драйвер в конце теста
