import json
import sys
import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

try:  # To allow for python 2 and 3 compatability
    reload(sys)
    sys.setdefaultencoding("utf8")
except:
    pass

CHANNEL = sys.argv[1].lower()

url = "https://beta.nightbot.tv/t/{channel}/commands".format(
    channel=CHANNEL)

commands = []

with open("test.html", "r") as f:  # read changes.json
    html = f.read()


def init_driver():
    # Choose your preferred driver
    driver = webdriver.Firefox()
    # driver = webdriver.PhantomJS()
    driver.wait = WebDriverWait(driver, 5)
    return driver


def extract(soup, CONTINUE=True, STOP=False):
    tbody = soup.find("tbody")
    rows = tbody.find_all("tr", role="row")
    for row in rows:
        sub_rows = row.find_all("td")
        command = {}
        command["action"] = sub_rows[0].get_text().lstrip("!")
        command["response"] = sub_rows[1].get_text()
        command["user_level"] = sub_rows[2].get_text()
        commands.append(command)
    next_button_li = driver.find_element_by_id("DataTables_Table_0_next")
    next_button_a = next_button_li.find_elements_by_tag_name("a")
    next_button_a[0].click()
    soup = BeautifulSoup(str(driver.page_source), "html.parser")
    if (soup.find("li", class_="paginate_button next disabled")
            is None and CONTINUE is True):
        extract(soup)
    elif CONTINUE is True and STOP is False:
        extract(soup, CONTINUE=False, STOP=True)


def lookup(driver, query):
    driver.get(url)
    try:
        driver.wait.until(EC.presence_of_element_located(
            (By.ID, "DataTables_Table_0")))
        limit = driver.wait.until(EC.element_to_be_clickable(
            (By.NAME, "DataTables_Table_0_length")))
        limit.click()
        for i in range(3):
            limit.send_keys(Keys.DOWN)
        limit.send_keys(Keys.RETURN)
        soup = BeautifulSoup(str(driver.page_source), "html.parser")
        extract(soup)  # first page
        output = json.dumps({"commands": commands}, indent=2)
        print(output)
        print(len(commands))
        with open("saved_data/" + CHANNEL + ".json", "w") as f:  # write to file
            f.write(output)
    except TimeoutException:
        print("I don't think they have Nightbot enabled DansGame")

if __name__ == "__main__":
    driver = init_driver()
    lookup(driver, "Selenium")
    driver.quit()
