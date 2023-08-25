from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

# # Initialize the driver
driver = webdriver.Chrome()

# # Open the URL
driver.get('https://www.pgatour.com/stats/detail/02675')
# Wait for the first button to be clickable and click it
wait = WebDriverWait(driver, 10)
first_button = wait.until(EC.element_to_be_clickable((By.ID, 'menu-button-:r55:')))
first_button.click()

# Wait for the menu to be visible
wait.until(EC.visibility_of_element_located((By.ID, 'menu-list-:r4f:')))

# Find all buttons with the role 'menuitem' inside the menu
menu_buttons = driver.find_elements_by_xpath("//button[@role='menuitem']")

# Click on the last button
last_button = menu_buttons[-1]
last_button.click() 

# Wait for 10 seconds
time.sleep(10)

# Close the browser
driver.quit()

# for i in range(7):
#     driver.switch_to.frame(i)
#     # Count the elements with the given XPath within the iframe
#     try:
#         first_button = wait.until(EC.element_to_be_clickable((By.ID, 'menu-list-:r4f:')))
#         first_button.click()

#         # Wait for the second button to be clickable and click it
#         second_button = wait.until(EC.element_to_be_clickable((By.ID, 'menu-list-:re:-menuitem-:rg:')))
#         second_button.click()

#         # Wait for 10 seconds
#         time.sleep(10)
#     except:
#         print('not found')

#     # Switch back to the main content
#     driver.switch_to.default_content()



# driver.get("https://www.selenium.dev/selenium/web/inputs.html")

# # Click on the element 
# driver.find_element(By.NAME, "color_input").click()