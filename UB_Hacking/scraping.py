from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Function to extract main article text from a given URL
def extract_article_text(url):
    # Set up the Chrome driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    article_text = []

    try:
        # Open the article page
        driver.get(url)
        
        # Wait until the main content is present - targetting common article tags
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "article"))
        )

        # Try various common tags or classes to extract the article content
        # First, try the <article> tag if it's available
        try:
            content = driver.find_element(By.TAG_NAME, "article")
        except:
            # Fallback to a common class used for article content in <div>
            content = driver.find_element(By.CLASS_NAME, "main-content")

        # Extract text from all <p> tags within the selected content
        paragraphs = content.find_elements(By.TAG_NAME, "p")
        for paragraph in paragraphs:
            text = paragraph.text.strip()
            if text:
                article_text.append(text)

        # Print the extracted text
        print("Extracted Article Content:")
        for line in article_text:
            print(line)

    except Exception as e:
        print(f"An error occurred: {str(e)}")

    finally:
        driver.quit()

    return article_text

# Test the function with an example URL
url = 'https://www.reuters.com/world/us/republicans-brink-clinching-us-house-control-2024-11-09/'
article_content = extract_article_text(url)