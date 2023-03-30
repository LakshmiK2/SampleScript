import pytest
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time

#pip freeze > requirements.txt
#pip install -r requirements.txt

driver = webdriver.Chrome()
driver.get("https://carepossible-app-preprod.azurewebsites.net/")
