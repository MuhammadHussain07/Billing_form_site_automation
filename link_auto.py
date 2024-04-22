from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time


# Setup the Edge WebDriver with the path to your 'msedgedriver'
edge_driver_path = 'D:\\proj\\Automation\\msedgedriver.exe'
service = Service(executable_path=edge_driver_path)
driver = webdriver.Edge(service=service)

# Load the Excel file
file_path = 'D:\\proj\\Automation\\Test Leads.xlsx'
df = pd.read_excel(file_path)

# Function to execute the first set of actions
def execute_first_code(row):
    try:
        driver.get(row['Web Name'])
        
        form_container_xpath = '//*[@id="medicare_leads"]'
        WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, form_container_xpath))
        )
        print(f"Form container found for URL: {row['Web Name']}")

        form_fields = {
            'first-name': row['First Name'],
            'last-name': row['Last Name'],
            'street-address': row['Address'],
            'city': row['City'],
            'state': row['State'],
            'zip': row['Zip'],
            'email': row['Email'],
            'phone': row['Phone'],
            'dob': row['DOB'],
            'age': str(row['Age']),
        }

        for field_name, value in form_fields.items():
            time.sleep(1)  # Is line ko add kiya hai form fields ko slowly fill karne ke liye.
            field = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.NAME, field_name)))
            field.clear()
            field.send_keys(value)
            print(f"{field_name} field filled.")

        submit_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.ID, 'btnsbt')))
        submit_button.click()
        print("Form submitted.")
        time.sleep(3)
    except Exception as e:
        print(f"Error processing URL: {row['Web Name']}, Error: {e}")

# Function to execute the second set of actions
def execute_second_code(row):
    try:
        driver.get(row['Web Name'])
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'form')))

        form_fields = {
            'first_name': row['First Name'],
            'last_name': row['Last Name'],
            'address': row['Address'],
            'city': row['City'],
            'state': row['State'],
            'zip': row['Zip'],
            'phone': row['Phone'],
            'email': row['Email'],
            'dob': row['DOB'],
            'age': str(row['Age']),
        }

        for field_name, value in form_fields.items():
            time.sleep(1)  # Yeh line added for slow form filling.    
            element = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.NAME, field_name)))
            element.clear()
            element.send_keys(value)

        try:
            agree_button_xpath = '//*[@id="contactForm"]/div/div[11]/a/div/button'
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, agree_button_xpath))).click()
        except:
            agree_button = driver.find_element(By.NAME, 'Agree')
            driver.execute_script("arguments[0].click();", agree_button)
        
        print(f"Form submitted for URL: {row['Web Name']}")
        time.sleep(3)
    except Exception as e:
        print(f"Error processing URL: {row['Web Name']}, Error: {e}")


# Iterate over each row in the DataFrame
for index, row in df.iterrows():
    try:
        # Depending on your link structure, determine how to distinguish between the two types
        # For demonstration, let's say if a link contains a specific keyword it should use the first code
        # Otherwise, use the second code. Adjust the condition based on your actual requirements
        if "leadyards.com" in row['Web Name']:
            execute_first_code(row)
        else:
            execute_second_code(row)
        
    except Exception as e:
        print(f"Error processing URL: {row['Web Name']}, Error: {e}")
        error_screenshot_path = f"D:\\proj\\Automation\\error_screenshot_{index}.png"
        driver.save_screenshot(error_screenshot_path)
        print(f"Screenshot saved to {error_screenshot_path}")
        continue

# Close the WebDriver
driver.quit()
