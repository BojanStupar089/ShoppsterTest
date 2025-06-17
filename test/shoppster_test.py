import pytest
from selenium import webdriver
from selenium.common import TimeoutException, ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by  import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time




@pytest.fixture()
def driver():
    ch_driver = webdriver.Chrome(service=Service('C:/Windows/chromedriver-win64/chromedriver.exe'))
    ch_driver.maximize_window()
    ch_driver.get('https://shoppster.rs')
    time.sleep(20)
    yield ch_driver
    ch_driver.quit()

def login(driver):
    driver.find_element(By.CSS_SELECTOR, '[data-cy="mini-login-link"]').click()
    time.sleep(3)

    driver.find_element(By.XPATH, "//input[@formcontrolname='loginId']").send_keys("bojanstupar1989+shop448@gmail.com")
    time.sleep(2)
    driver.find_element(By.XPATH, "//input[@formcontrolname='password']").send_keys("Celarevo44!")
    time.sleep(3)

    driver.find_element(By.XPATH, "//button[text()=' Uloguj se ']").click()


def close_gift_popup(driver):
    time.sleep(2)
    try:
        close_button = driver.find_element(By.ID, "wps-overlay-close-button")
        close_button.click()
        print("Popup closed.")
    except NoSuchElementException:
        print("No popup found, continuing.")


def add_shoes_to_korpa(driver):
    time.sleep(5)

    login(driver)

    time.sleep(5)

    driver.find_element(By.CSS_SELECTOR, "input[aria-label='search']").send_keys("Muške patike")
    time.sleep(3)

    driver.find_element(By.CSS_SELECTOR, "svg.searchbox__icon").click()
    time.sleep(5)

    driver.find_element(By.XPATH, "//label[contains(., 'Brooks')]").click()
    time.sleep(5)

    driver.find_element(By.XPATH, "//a[@href='/p/1968095']").click()
    time.sleep(5)

    driver.find_element(By.CSS_SELECTOR, '[data-cy="cypress-addToCardBtn"]').click()
    time.sleep(5)


def test_open_google_and_go_to_shoppster(driver):
    time.sleep(2)

    logo=driver.find_element(By.XPATH,"//img[@alt='Shoppster']")

    expected_src = "https://www.shoppster.rs/medias/shoppster-logo.svg"
    actual_src = logo.get_attribute("src")

    assert actual_src.startswith(expected_src), f"Logo src mismatch! Actual: {actual_src}"

def test_register_successful_on_shopster(driver):

    time.sleep(2)
    close_gift_popup(driver)
    time.sleep(2)

    login_link = driver.find_element(By.CSS_SELECTOR, '[data-cy="mini-login-link"]')
    login_link.click()

    time.sleep(2)
    register_btn = driver.find_element(By.CSS_SELECTOR, "a.btn-register")

    driver.execute_script("arguments[0].scrollIntoView(true);", register_btn)
    time.sleep(2)
    register_btn.click()

    time.sleep(2)

    red_korisnik = driver.find_element(By.XPATH, "//span[contains(text(), 'Učlani se kao redovni korisnik')]")
    red_korisnik.click()

    time.sleep(2)

    driver.find_element(By.NAME,"firstName").send_keys("Bojan")
    time.sleep(2)
    driver.find_element(By.NAME, "lastName").send_keys("Stupar")
    time.sleep(2)
    driver.find_element(By.NAME, "email").send_keys("bojanstupar1989+shop448@gmail.com")
    time.sleep(2)
    driver.find_element(By.NAME, "password").send_keys("Celarevo44!")
    time.sleep(2)
    driver.find_element(By.NAME, "confirmpassword").send_keys("Celarevo44!")
    time.sleep(2)
    driver.find_element(By.NAME, "birthDay").send_keys("10")
    time.sleep(2)
    driver.find_element(By.XPATH, "//ng-select[@formcontrolname='birthMonth']").click()

    time.sleep(2)

    driver.find_element(By.XPATH, "//div[@role='option']//span[contains(text(), 'Februar')]").click()

    driver.find_element(By.NAME,"birthYear").send_keys("1989")
    time.sleep(2)
    driver.find_element(By.XPATH, "//input[@formcontrolname='gender']").click()
    time.sleep(2)
    driver.find_element(By.NAME, "consent").click()
    time.sleep(2)
    driver.find_element(By.NAME, "newsletter").click()
    time.sleep(2)

    driver.find_element(By.XPATH, "//button[contains(text(), 'Registruj se')]").click()

    time.sleep(2)
    moj_nalog = driver.find_element(By.CSS_SELECTOR, 'div.footer__headline--desktop').text
    assert "Podrška" in moj_nalog.replace(" ", ""), "Error"

def test_register_required_fields_validation(driver):

    time.sleep(2)
    close_gift_popup(driver)
    time.sleep(2)
    login_link = driver.find_element(By.CSS_SELECTOR, '[data-cy="mini-login-link"]')
    login_link.click()

    time.sleep(2)
    register_btn = driver.find_element(By.CSS_SELECTOR, "a.btn-register")

    driver.execute_script("arguments[0].scrollIntoView(true);", register_btn)
    time.sleep(2)
    register_btn.click()

    time.sleep(2)

    red_korisnik = driver.find_element(By.XPATH, "//span[contains(text(), 'Učlani se kao redovni korisnik')]")
    red_korisnik.click()

    time.sleep(2)
    driver.find_element(By.NAME, "firstName").send_keys("")
    time.sleep(2)
    driver.find_element(By.NAME, "lastName").send_keys("")
    time.sleep(2)
    driver.find_element(By.NAME, "email").send_keys("")
    time.sleep(2)
    driver.find_element(By.NAME, "password").send_keys("Celarevo44!")
    time.sleep(2)
    driver.find_element(By.NAME, "confirmpassword").send_keys("Celarevo44!")
    time.sleep(2)
    driver.find_element(By.NAME, "birthDay").send_keys("10")
    time.sleep(2)
    driver.find_element(By.XPATH, "//ng-select[@formcontrolname='birthMonth']").click()


    time.sleep(2)


    driver.find_element(By.XPATH, "//div[@role='option']//span[contains(text(), 'Februar')]").click()

    driver.find_element(By.NAME, "birthYear").send_keys("1989")

    time.sleep(2)
    driver.find_element(By.NAME, "newsletter").click()
    time.sleep(2)

    driver.find_element(By.XPATH, "//button[contains(text(), 'Registruj se')]").click()

    time.sleep(2)

    assert "*Polje je obavezno" in driver.find_element(By.CLASS_NAME,"form-error-message").text,"Error"

def test_register_password_invalid_format(driver):
    time.sleep(2)
    close_gift_popup(driver)
    time.sleep(2)
    login_link = driver.find_element(By.CSS_SELECTOR, '[data-cy="mini-login-link"]')
    login_link.click()

    time.sleep(2)

    register_btn = driver.find_element(By.CSS_SELECTOR, "a.btn-register")

    driver.execute_script("arguments[0].scrollIntoView(true);", register_btn)
    time.sleep(2)
    register_btn.click()

    time.sleep(2)

    red_korisnik = driver.find_element(By.XPATH, "//span[contains(text(), 'Učlani se kao redovni korisnik')]")
    red_korisnik.click()

    time.sleep(2)

    driver.find_element(By.NAME, "firstName").send_keys("Bojan")
    time.sleep(2)
    driver.find_element(By.NAME, "lastName").send_keys("Stupar")
    time.sleep(2)
    driver.find_element(By.NAME, "email").send_keys("bojanstupar1989@gmail.com")
    time.sleep(2)
    driver.find_element(By.NAME, "password").send_keys("abc")
    time.sleep(2)
    driver.find_element(By.NAME, "confirmpassword").send_keys("abc")
    time.sleep(2)

    password_text=driver.find_element(By.XPATH, "//div[contains(text(),'Lozinka mora sadržati minimum 6 karaktera')]").text
    assert "Lozinka mora sadržati minimum 6 karaktera, od toga jedno veliko slovo i jedan broj" in password_text,"Error"

def test_register_password__mismatch_error(driver):

    time.sleep(2)
    close_gift_popup(driver)
    time.sleep(2)
    login_link = driver.find_element(By.CSS_SELECTOR, '[data-cy="mini-login-link"]')
    login_link.click()

    time.sleep(2)

    register_btn = driver.find_element(By.CSS_SELECTOR, "a.btn-register")

    driver.execute_script("arguments[0].scrollIntoView(true);", register_btn)
    time.sleep(2)
    register_btn.click()
    time.sleep(2)

    red_korisnik= driver.find_element(By.XPATH, "//span[contains(text(), 'Učlani se kao redovni korisnik')]")
    red_korisnik.click()

    time.sleep(2)

    driver.find_element(By.NAME, "firstName").send_keys("Bojan")
    time.sleep(2)
    driver.find_element(By.NAME, "lastName").send_keys("Stupar")
    time.sleep(2)
    driver.find_element(By.NAME, "email").send_keys("bojanstupar1989@gmail.com")
    time.sleep(2)
    driver.find_element(By.NAME, "password").send_keys("Celarevo44!")
    time.sleep(2)
    driver.find_element(By.NAME, "confirmpassword").send_keys("abc")
    time.sleep(2)

    password_mismatch_text=driver.find_element(By.XPATH,"//div[contains(text(),'Lozinke moraju biti iste')]").text
    assert "Lozinke moraju biti iste" in password_mismatch_text,"Error"

def test_register_date_invalid_format(driver):

    time.sleep(2)
    close_gift_popup(driver)
    time.sleep(3)

    login_link = driver.find_element(By.CSS_SELECTOR, '[data-cy="mini-login-link"]')
    login_link.click()
    time.sleep(2)

    register_btn = driver.find_element(By.CSS_SELECTOR, "a.btn-register")
    driver.execute_script("arguments[0].scrollIntoView(true);", register_btn)
    time.sleep(2)
    register_btn.click()
    time.sleep(2)

    red_korisnik =driver.find_element(By.XPATH, "//span[contains(text(), 'Učlani se kao redovni korisnik')]")
    red_korisnik.click()
    time.sleep(2)

    driver.find_element(By.NAME, "firstName").send_keys("Bojan")
    time.sleep(2)
    driver.find_element(By.NAME, "lastName").send_keys("Stupar")
    time.sleep(2)
    driver.find_element(By.NAME, "email").send_keys("bojanstupar1989@gmail.com")
    time.sleep(2)
    driver.find_element(By.NAME, "password").send_keys("Celarevo44!")
    time.sleep(2)
    driver.find_element(By.NAME, "confirmpassword").send_keys("Celarevo44!")
    time.sleep(2)
    driver.find_element(By.NAME, "birthDay").send_keys("")
    time.sleep(2)
    driver.find_element(By.XPATH, "//ng-select[@formcontrolname='birthMonth']").click()
    time.sleep(2)

    driver.find_element(By.XPATH, "//div[@role='option']//span[contains(text(), 'Februar')]").click()

    driver.find_element(By.NAME, "birthYear").send_keys("")
    time.sleep(2)
    driver.find_element(By.XPATH, "//input[@formcontrolname='gender']").click()
    time.sleep(2)
    driver.find_element(By.NAME, "consent").click()
    time.sleep(2)
    driver.find_element(By.NAME, "newsletter").click()
    time.sleep(2)

    button=driver.find_element(By.XPATH, "//button[contains(text(), 'Registruj se')]")
    driver.execute_script("arguments[0].click();", button)
    time.sleep(2)



    date_invalid_text=driver.find_element(By.CLASS_NAME, "invalid-feedback").text
    assert "Pogrešan format datuma, pokušajte ponovo" in date_invalid_text,"Error"

def test_register_email_already_exists(driver):

    time.sleep(2)
    close_gift_popup(driver)
    time.sleep(2)

    login_link = driver.find_element(By.CSS_SELECTOR, '[data-cy="mini-login-link"]')
    login_link.click()

    time.sleep(2)

    register_btn = driver.find_element(By.CSS_SELECTOR, "a.btn-register")
    driver.execute_script("arguments[0].scrollIntoView(true);", register_btn)
    time.sleep(2)
    register_btn.click()
    time.sleep(2)

    button = driver.find_element(By.XPATH, "//span[contains(text(), 'Učlani se kao redovni korisnik')]")
    button.click()

    time.sleep(2)

    driver.find_element(By.NAME, "firstName").send_keys("Bojan")
    time.sleep(2)
    driver.find_element(By.NAME, "lastName").send_keys("Stupar")
    time.sleep(2)
    driver.find_element(By.NAME, "email").send_keys("bojanstupar1989+shop12@gmail.com")
    time.sleep(2)
    driver.find_element(By.NAME, "password").send_keys("Celarevo44!")
    time.sleep(2)
    driver.find_element(By.NAME, "confirmpassword").send_keys("Celarevo44!")
    time.sleep(2)
    driver.find_element(By.NAME, "birthDay").send_keys("10")
    time.sleep(2)
    driver.find_element(By.XPATH, "//ng-select[@formcontrolname='birthMonth']").click()
    time.sleep(2)

    driver.find_element(By.XPATH, "//div[@role='option']//span[contains(text(), 'Februar')]").click()
    driver.find_element(By.NAME, "birthYear").send_keys("1989")
    time.sleep(2)

    driver.find_element(By.XPATH, "//input[@formcontrolname='gender']").click()
    time.sleep(2)

    driver.find_element(By.NAME, "consent").click()
    time.sleep(2)
    driver.find_element(By.NAME, "newsletter").click()
    time.sleep(2)

    driver.find_element(By.XPATH, "//button[contains(text(), 'Registruj se')]").click()
    time.sleep(2)

    assert "E-mail već u upotrebi" in driver.page_source

def test_login_successful(driver):

    time.sleep(2)
    close_gift_popup(driver)
    time.sleep(2)

    login(driver)
    time.sleep(5)

    moj_nalog_text = driver.find_element(By.CSS_SELECTOR, 'div.footer__headline--desktop').text
    assert "Moj nalog" in moj_nalog_text, "Moj nalog was not displayed after login."

def test_login_required_fields_validation(driver):

    time.sleep(2)
    close_gift_popup(driver)
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, '[data-cy="mini-login-link"]').click()
    time.sleep(2)

    driver.find_element(By.XPATH, "//input[@formcontrolname='loginId']").send_keys("")
    time.sleep(2)
    driver.find_element(By.XPATH, "//input[@formcontrolname='password']").send_keys("")
    time.sleep(2)

    driver.find_element(By.XPATH, "//button[text()=' Uloguj se ']").click()

    time.sleep(1)

    login_required_fields_text=driver.find_element(By.CLASS_NAME,"form-error-message").text
    assert "*Polje je obavezno" in login_required_fields_text,"Error"

def test_login_email_invalid_format(driver):

    time.sleep(2)
    close_gift_popup(driver)
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, '[data-cy="mini-login-link"]').click()
    time.sleep(2)

    driver.find_element(By.XPATH, "//input[@formcontrolname='loginId']").send_keys("bkjkjk")
    time.sleep(2)
    driver.find_element(By.XPATH, "//input[@formcontrolname='password']").send_keys("Celarevo44!")
    time.sleep(2)

    driver.find_element(By.XPATH, "//button[text()=' Uloguj se ']").click()

    email_invalid_format_text=driver.find_element(By.CLASS_NAME, "form-error-message").text
    assert "E-mail format nije validan." in email_invalid_format_text,"Error"

def test_login_invalid_credentials(driver):

    time.sleep(2)
    close_gift_popup(driver)
    time.sleep(2)

    driver.find_element(By.CSS_SELECTOR, '[data-cy="mini-login-link"]').click()
    time.sleep(2)

    driver.find_element(By.XPATH, "//input[@formcontrolname='loginId']").send_keys("bojanstupar1989@gmail.com")
    time.sleep(2)
    driver.find_element(By.XPATH, "//input[@formcontrolname='password']").send_keys("Celar")
    time.sleep(2)

    driver.find_element(By.XPATH, "//button[text()=' Uloguj se ']").click()
    time.sleep(2)


    assert "Pogrešni kredencijali. Molimo ulogujte se ponovo." in driver.page_source

def test_login_forgot_password_link_redirects_to_reset_page(driver):

    time.sleep(2)
    close_gift_popup(driver)
    time.sleep(2)

    driver.find_element(By.CSS_SELECTOR, '[data-cy="mini-login-link"]').click()
    time.sleep(2)

    driver.find_element(By.XPATH, "//input[@formcontrolname='loginId']").send_keys("bojanstupar1989@gmail.com")
    time.sleep(2)
    driver.find_element(By.XPATH, "//input[@formcontrolname='password']").send_keys("Celar")
    time.sleep(2)

    driver.find_element(By.LINK_TEXT, "Zaboravljena lozinka?").click()

    time.sleep(2)

    driver.find_element(By.XPATH, "//input[@formcontrolname='userEmail']").send_keys("bojanstupar1989@gmail.com")
    time.sleep(1)

    driver.find_element(By.XPATH, "//button[text()=' Pošalji ']").click()
    time.sleep(2)

    assert "" in driver.find_element(By.CLASS_NAME, "login__header").text, "Error"

def test_youtube_link_redirects_to_shoppster_channel(driver):

    time.sleep(2)
    close_gift_popup(driver)
    time.sleep(2)

    youtube_link= driver.find_element(By.LINK_TEXT, "Shoppster YouTube")
    youtube_link.click()
    time.sleep(5)

    assert youtube_link.is_displayed()
    assert youtube_link.get_attribute("href") == "https://www.youtube.com/@ShoppsterSrbija"

def test_shoppster_search_dvoriste(driver):

    time.sleep(2)
    close_gift_popup(driver)
    time.sleep(2)

    driver.find_element(By.CSS_SELECTOR,"input[aria-label='search']").send_keys("dvoriste")
    time.sleep(2)

    driver.find_element(By.CSS_SELECTOR, "svg.searchbox__icon").click()
    time.sleep(3)

    result_text=driver.find_element(By.CSS_SELECTOR, "div[class='plp__title']").text
    assert"dvoriste" in result_text.lower(),"Error"

def test_shoppster_sidebar_navigation_click_bela_tehnika(driver):

    time.sleep(2)
    close_gift_popup(driver)
    time.sleep(2)

    driver.find_element(By.CSS_SELECTOR, 'a.main-navigation__item-link[href="/c/F01"]').click()
    time.sleep(3)

    assert "Bela tehnika" in driver.find_element(By.CLASS_NAME, "category-page-title").text, "Error"

def test_shoppster_search_odeca_in_moda_category(driver):

    time.sleep(2)
    close_gift_popup(driver)
    time.sleep(2)

    drop_down = driver.find_element(By.CLASS_NAME, "ng-value-container")
    drop_down.click()

    time.sleep(2)
    moda_option = driver.find_element(By.XPATH, "//div[contains(@class,'ng-option')]//span[text()='Moda']")
    moda_option.click()

    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "input[aria-label='search']").send_keys("odeća")
    time.sleep(2)

    driver.find_element(By.CSS_SELECTOR, "svg.searchbox__icon").click()
    time.sleep(2)

    result_text = driver.find_element(By.CSS_SELECTOR, "div[class='plp__title']").text
    assert "odeća" in result_text,"Error"

def test_shoppster_o_nama_page_opens_correctly(driver):

    time.sleep(2)
    close_gift_popup(driver)
    time.sleep(2)

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

    element=driver.find_element(By.XPATH,"//a[@href='/o-nama']")
    driver.execute_script("arguments[0].scrollIntoView(true);", element)
    time.sleep(2)

    driver.execute_script("arguments[0].click();", element)
    time.sleep(2)

    o_nama_title_text = driver.find_element(By.XPATH, "//h2[contains(text(), 'Shoppster - sve na jednom mestu')]").text

    assert "Shoppster - sve na jednom mestu" in o_nama_title_text, "Error"

def test_shoppster_add_shoes_to_cart(driver):

    time.sleep(2)
    close_gift_popup(driver)
    time.sleep(2)

    add_shoes_to_korpa(driver)

    add_shoes_to_cart_text = driver.find_element(By.CLASS_NAME, "dialog__title").text


    assert add_shoes_to_cart_text.strip() == "Moja korpa", "Error"

def test_shoppster_remove_shoes_from_cart(driver):

    time.sleep(2)
    close_gift_popup(driver)
    time.sleep(2)

    add_shoes_to_korpa(driver)
    element = driver.find_element(By.XPATH, "//u[text()='Ukloni proizvod']")
    element.click()

    time.sleep(2)

def test_shoppster_cart_link(driver):
        time.sleep(2)
        close_gift_popup(driver)
        time.sleep(2)

        add_shoes_to_korpa(driver)
        time.sleep(2)

        img = driver.find_element(By.CSS_SELECTOR, "picture img[alt='Shoppster']")
        img.click()
        time.sleep(2)
        korpa_link = driver.find_element(By.XPATH, "//a[@class='mini-cart__link']")
        korpa_link.click()

        time.sleep(2)

        cart_link_text = driver.find_element(By.CLASS_NAME, "dialog__title").text

        assert cart_link_text.strip() == "Moja korpa", "Error"

def test_shoppster_order_product_with_home_address(driver):

    time.sleep(2)
    close_gift_popup(driver)
    time.sleep(2)

    add_shoes_to_korpa(driver)
    time.sleep(2)

    order_product=driver.find_element(By.XPATH,"//button[span[contains(text(),'Naruči odmah')]]")
    order_product.click()
    time.sleep(2)

    order_button=driver.find_element(By.XPATH,"//button[contains(text(),' Naruči ')]")
    order_button.click()
    time.sleep(5)

    radio_button= driver.find_element(By.NAME, "selectedDeliveryMode")
    radio_button.click()
    time.sleep(10)


    street_input = driver.find_element(By.CSS_SELECTOR, "ung-dynamic-dropdown#streetName input")
    street_input.send_keys("Bulevar oslobođenja")
    time.sleep(2)
    street_input.send_keys("\n")
    time.sleep(2)

    driver.find_element(By.ID,"streetNumber").send_keys("11")
    time.sleep(2)
    driver.find_element(By.ID, "building").send_keys("12")
    time.sleep(2)
    driver.find_element(By.ID, "floor").send_keys("1")
    time.sleep(5)

    grad_input = driver.find_element(By.CSS_SELECTOR, "ung-dynamic-dropdown#town input")
    grad_input.send_keys("Novi Sad")
    time.sleep(2)
    grad_input.send_keys("\n")
    time.sleep(2)

    zip_input = driver.find_element(By.CSS_SELECTOR, "ung-dynamic-dropdown#postalCode input")
    zip_input.send_keys("21000")
    time.sleep(1)
    zip_input.send_keys("\n")
    time.sleep(2)

    driver.find_element(By.NAME,"number").send_keys("65123456")
    time.sleep(2)

    nastavi_btn = driver.find_element(By.CSS_SELECTOR, "button[data-cy='cypress-delivery-step__ship-to-btn']")
    nastavi_btn.click()


    time.sleep(3)

    order_product_text=driver.find_element(By.XPATH, "//div[contains(text(), 'Način plaćanja')]").text
    assert "Način plaćanja" in order_product_text, "Error"

def test_shoppster_moji_podaci_display_correctly(driver):

    time.sleep(2)
    close_gift_popup(driver)
    time.sleep(2)
    login(driver)
    time.sleep(3)

    moj_nalog = driver.find_element(By.CSS_SELECTOR, 'div.footer__headline--desktop')
    actions = ActionChains(driver)
    actions.move_to_element(moj_nalog).perform()
    time.sleep(2)

    moji_podaci= driver.find_element(By.LINK_TEXT, "Moji podaci")
    moji_podaci.click()
    time.sleep(2)

    moji_podaci_text=driver.find_element(By.CLASS_NAME,"ung-section-title").text
    assert "Promena e-mail adrese" in moji_podaci_text,"Error"

def test_shoppster_click_bosch_and_plavi_alat_displays_correctly(driver):

    time.sleep(2)
    close_gift_popup(driver)
    time.sleep(2)
    bosch = driver.find_element(By.XPATH, "//a[@href='/bosch-ponuda']")
    driver.execute_script("arguments[0].scrollIntoView(true);", bosch)
    time.sleep(5)

    driver.execute_script("arguments[0].click();", bosch)

    time.sleep(5)

    plavi_alat = driver.find_element(By.XPATH, "//a[@href='/bosch-plavi-alat']")
    plavi_alat.click()

    time.sleep(2)

    plavi_alat_title = driver.find_element(By.CLASS_NAME, "ung-breadcrumb-content")
    text = driver.execute_script("return arguments[0].textContent;", plavi_alat_title)
    assert "Bosch plavi alat" in text

def test_shoppster_reklamacije_i_povrati_display_correctly(driver):

     time.sleep(2)
     close_gift_popup(driver)
     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
     time.sleep(3)


     link_btn = driver.find_element(By.XPATH, "//cx-generic-link//a[@href='/reklamacije-i-povrati']")
     driver.execute_script("arguments[0].scrollIntoView(true);", link_btn)
     time.sleep(2)
     driver.execute_script("arguments[0].click();", link_btn)

     time.sleep(5)
     reklamacije_i_povrati_text=driver.find_element(By.TAG_NAME,"h2").text

     assert "Reklamacije i povrati" in reklamacije_i_povrati_text,"Nije dobro"

def test_shoppster_logout(driver):

    time.sleep(2)
    close_gift_popup(driver)
    time.sleep(2)

    login(driver)
    time.sleep(3)

    moj_nalog = driver.find_element(By.CSS_SELECTOR, 'div.footer__headline--desktop')
    actions = ActionChains(driver)
    actions.move_to_element(moj_nalog).perform()
    time.sleep(2)


    odjavi_se = driver.find_element(By.LINK_TEXT, "Odjavi se")
    odjavi_se.click()
    time.sleep(2)

    assert "Uloguj se" in driver.page_source

def test_shoppster_delete_my_account_successfully(driver):

    time.sleep(2)
    close_gift_popup(driver)

    time.sleep(2)
    login(driver)
    time.sleep(3)

    moj_nalog = driver.find_element(By.CSS_SELECTOR, 'div.footer__headline--desktop')
    actions = ActionChains(driver)
    actions.move_to_element(moj_nalog).perform()
    time.sleep(2)

    moji_podaci = driver.find_element(By.LINK_TEXT, "Moji podaci")
    moji_podaci.click()
    time.sleep(5)

    obrisi_nalog = driver.find_element(By.XPATH, "//button[text()=' Obriši moj nalog ']")
    obrisi_nalog.click()

    time.sleep(3)

    obrisi_button = driver.find_element(By.XPATH,
                                        "//button[contains(@class, 'close-account-btn') and normalize-space(text())='Da, obriši']")
    obrisi_button.click()

    time.sleep(3)

    obrisi_moj_nalog=driver.find_element(By.XPATH,"//button[text()=' Obriši moj nalog ']")
    obrisi_moj_nalog.click()
    time.sleep(2)

    assert "Nalog uspešno obrisan" in driver.page_source
