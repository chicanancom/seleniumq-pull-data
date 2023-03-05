from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By
website ='https://www.adamchoi.co.uk/bttsresult/detailed'
driver = webdriver.Edge()
driver.get(website)
td = driver.find_element(By.XPATH, '//label[@analytics-event="All matches"]')
td.click()

matches = driver.find_elements(By.TAG_NAME, 'tr')

date = []
hometeam = []
score = []
awayteam = []

for match in matches:
    date.append(match.find_element(By.XPATH, './td[1]' ).text)
    hometeam.append(match.find_element(By.XPATH, './td[2]').text)
    score.append(match.find_element(By.XPATH, './td[3]').text)
    awayteam.append(match.find_element(By.XPATH, './td[4]').text)

# driver.quit()

df = pd.DataFrame({'date': date, 'hometeam': hometeam, 'score': score, 'awayteam': awayteam})
df.to_csv("football_data.csv", index=False)

