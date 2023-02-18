from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time
import os

# get chrome browser driver
driver = webdriver.Chrome(executable_path='C:\\Users\\Siarhei_Puiman\\Downloads\\chromedriver.exe')

# open start url
PATH = 'https://104.196.114.118/spuiman/'
driver.get(PATH)

# get environment variables
log = os.environ.get('LOGIN')
pas = os.environ.get('PASS')


try:

    # pass warning page
    element = WebDriverWait(driver, 10).until(
        ec.presence_of_element_located((By.ID, 'details-button'))
    )
    element.click()

    time.sleep(5)

    element = WebDriverWait(driver, 10).until(
        ec.presence_of_element_located((By.ID, 'proceed-link'))
    )
    element.click()

    # click EPAM SSO button
    element = WebDriverWait(driver, 10).until(
        ec.presence_of_element_located((By.ID, 'zocial-epam-idp'))
    )
    element.click()

    # enter login and password and click "Enter"
    login = driver.find_element_by_id("userNameInput")
    login.send_keys(log)
    password = driver.find_element_by_id("passwordInput")
    password.send_keys(pas)
    password.send_keys(Keys.RETURN)

    # go to the notebook
    notebook = 'https://projectby.trainings.dlabanalytics.com/spuiman/notebooks/final_task.ipynb'
    driver.get(notebook)
    time.sleep(15)

    # run all cells in the notebook
    element = WebDriverWait(driver, 10).until(
        ec.presence_of_element_located((By.ID, 'celllink'))
    )
    element.click()

    element = WebDriverWait(driver, 10).until(
        ec.presence_of_element_located((By.ID, 'run_all_cells'))
    )
    element.click()

except ValueError:
    driver.quit()
