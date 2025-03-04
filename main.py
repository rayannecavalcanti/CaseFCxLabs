import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import modules

def automate_checkout():
    driver = webdriver.Chrome()
    driver.get("https://www.advantageonlineshopping.com/#/")
    driver.maximize_window()
    
    wait = WebDriverWait(driver, 10)
    time.sleep(4)


    driver.find_element(By.ID, "menuUser").click()
    create_account_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "CREATE NEW ACCOUNT")))
    time.sleep(2)
    create_account_link.click()

    username = modules.username()
    username_field = wait.until(EC.visibility_of_element_located((By.NAME, "usernameRegisterPage")))
    username_field.send_keys(username)
    time.sleep(2)

    email_field = driver.find_element(By.NAME, "emailRegisterPage")
    email_field.send_keys(modules.email())
    time.sleep(2)

    password = modules.password()
    password_field = driver.find_element(By.NAME, "passwordRegisterPage")
    password_field.send_keys(password)
    time.sleep(2)

    confirm_password_field = driver.find_element(By.NAME, "confirm_passwordRegisterPage")
    confirm_password_field.send_keys(password)
    time.sleep(2)

    first_name_field = driver.find_element(By.NAME, "first_nameRegisterPage")
    first_name_field.send_keys(modules.first_name())
    time.sleep(2)

    last_name_field = driver.find_element(By.NAME, "last_nameRegisterPage")
    last_name_field.send_keys(modules.last_name())
    time.sleep(2)

    phone_number_field = driver.find_element(By.NAME, "phone_numberRegisterPage")
    phone_number_field.send_keys(modules.phone_number())
    time.sleep(2)

    country_field = driver.find_element(By.NAME, "countryListboxRegisterPage")
    country_field.send_keys(modules.country())
    time.sleep(2)

    state = modules.state()
    state_field = driver.find_element(By.NAME, "state_/_province_/_regionRegisterPage")
    state_field.send_keys(state)
    time.sleep(2)

    city_field = driver.find_element(By.NAME, "cityRegisterPage")
    city_field.send_keys(modules.city())
    time.sleep(2)

    address_field = driver.find_element(By.NAME, "addressRegisterPage")
    address_field.send_keys(modules.address())
    time.sleep(2)

    postal_code_field = driver.find_element(By.NAME, "postal_codeRegisterPage")
    postal_code_field.send_keys(modules.postal_code())
    time.sleep(2)

    driver.find_element(By.NAME, "i_agree").click()
    time.sleep(2)

    driver.find_element(By.ID, "register_btn").click()
    time.sleep(5)

    driver.find_element(By.ID, "menuUser").click()
    sign_out_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//label[@class='option roboto-medium ng-scope' and contains(text(), 'Sign out')]")))
    sign_out_button.click()
    time.sleep(3)

    driver.find_element(By.ID, "menuUser").click()
    wait.until(EC.visibility_of_element_located((By.NAME, "username"))).send_keys(username)
    time.sleep(2)

    driver.find_element(By.NAME, "password").send_keys(password)
    time.sleep(2)

    login_button = wait.until(EC.element_to_be_clickable((By.ID, "sign_in_btn")))
    login_button.click()
    time.sleep(3)

    chosen_category = modules.categories()
    category_link = wait.until(EC.element_to_be_clickable((By.ID, chosen_category["id"])))
    category_link.click()
    time.sleep(3)

    items = driver.find_elements(By.XPATH, "//div[contains(@class,'product')]")
    if items:
        random.choice(items).click()
        time.sleep(3)

        add_to_cart_button = wait.until(EC.element_to_be_clickable((By.NAME, "save_to_cart")))
        add_to_cart_button.click()
        time.sleep(3)
    else:
        print("Nenhum item encontrado na categoria!")

    driver.find_element(By.ID, "menuCart").click()
    time.sleep(2)

    checkout_button = wait.until(EC.element_to_be_clickable((By.ID, "checkOutPopUp")))
    checkout_button.click()
    time.sleep(2)

    next_button = wait.until(EC.element_to_be_clickable((By.ID, "next_btn")))
    next_button.click()
    time.sleep(2)

    payment_methods = ["safepay", "mastercredit"]
    chosen_payment = random.choice(payment_methods)
    print(f"Selecionando o método de pagamento: {chosen_payment.upper()}")

    if chosen_payment == "safepay":
        driver.find_element(By.NAME, "safepay").click()
        time.sleep(2)

        driver.find_element(By.NAME, "safepay_username").send_keys(username)
        time.sleep(2)

        driver.find_element(By.NAME, "safepay_password").send_keys(password)
        time.sleep(2)

        pay_now_button = wait.until(EC.element_to_be_clickable((By.ID, f"pay_now_btn_SAFEPAY")))
        pay_now_button.click()
        time.sleep(3)

    elif chosen_payment == "mastercredit":
        driver.find_element(By.NAME, "masterCredit").click()
        time.sleep(2)

        driver.find_element(By.NAME, "card_number").send_keys(modules.card_number())
        time.sleep(2)

        driver.find_element(By.NAME, "cvv_number").send_keys(modules.cvv())
        time.sleep(2)

        driver.find_element(By.NAME, "mmListbox").send_keys(modules.month_exp())
        time.sleep(2)

        driver.find_element(By.NAME, "yyyyListbox").send_keys(modules.year_exp())
        time.sleep(2)

        driver.find_element(By.NAME, "cardholder_name").send_keys(f"{modules.first_name()} {modules.last_name()}")
        time.sleep(2)

        pay_now_button = wait.until(EC.element_to_be_clickable((By.ID, f"pay_now_btn_ManualPayment")))
        pay_now_button.click()
        time.sleep(3)

    driver.quit()

if __name__ == "__main__":
    automate_checkout()