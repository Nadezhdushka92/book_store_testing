# Home: добавление комментария
from selenium import webdriver
driver = webdriver.Chrome()

# 1 Откроем страницу http://practice.automationtesting.in/
driver.get("http://practice.automationtesting.in/")

# 2 Проскроллим страницу вниз на 600 пикселей
driver.execute_script("window.scrollBy(0, 600);") 	# эта команда проскроллит страницу на 600 пикселей вниз

# 3 Нажмём на название книги "Selenium Ruby" или на кнопку "READ MORE"
driver.find_element_by_css_selector('.post-160 .woocommerce-LoopProduct-link >h3').click()

# 4 Нажмём на вкладку "REVIEWS"
driver.find_element_by_css_selector('[href="#tab-reviews"]').click()

# 5 Поставим 5 звёзд
star = driver.find_element_by_class_name("star-5")
star.click()

# 6 Заполним поле "Review" сообщением: "Nice book!"
comm = driver.find_element_by_id("comment")
comm.send_keys("Nice book!")

# 7 Заполним поле "Name"
auth = driver.find_element_by_id("author")
auth.send_keys("Nady")

# 8 Заполним "Email"
email = driver.find_element_by_id("email")
email.send_keys("anikinana92@yandex.ru")

# 9 Нажмём на кнопку "SUBMIT"
driver.find_element_by_id("submit").click()

driver.quit() 		# закроем драйвер в конце теста