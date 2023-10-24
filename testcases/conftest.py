import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.core.os_manager import ChromeType
# from selenium.webdriver.chrome.service import Service as BraveService
# from selenium.webdriver.edge.service import Service as EdgeService
# from webdriver_manager.microsoft import EdgeChromiumDriverManager
# from selenium.webdriver.firefox.service import Service as FirefoxService
# from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get(url='https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Faccounts.google.com%2F&followup=https%3A%2F%2Faccounts.google.com%2F&ifkv=AVQVeyyxR9-FNBpXL5iL4HwGnzi1hPWDWhdU_D-VNK6dPa_DPaTs0A2e7TjeJb72iFrVu09a31WE5&passive=1209600&flowName=GlifWebSignIn&flowEntry=ServiceLogin&dsh=S-1442592184%3A1698150008071214&theme=glif')
    driver.maximize_window()
    request.cls.driver = driver
    # request.cls.wait = wait
    yield
    driver.close()