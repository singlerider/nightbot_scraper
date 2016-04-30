from bs4 import BeautifulSoup

commands = []

with open("test.html", "r") as f:  # read changes.json
    html = f.read()

soup = BeautifulSoup(html, "html.parser")
tbody = soup.find("tbody")
paginate_buttons = BeautifulSoup(str(soup.find_all(
    class_="dataTables_paginate paging_full_numbers")), "html.parser")
number_of_pages = paginate_buttons.find_all("li")
print(len(number_of_pages) - 5)
# print(soup.find_all(class_="paginate_button next disabled"))
# rows = tbody.find_all("tr", role="row")
# for row in rows:
#     sub_rows = row.find_all("td")
#     print(sub_rows[0].get_text())
#     command = {}
#     command["action"] = sub_rows[0].get_text()
#     command["response"] = sub_rows[1].get_text()
#     command["user_level"] = sub_rows[2].get_text()
#     commands.append(command)
#
# print(commands)
