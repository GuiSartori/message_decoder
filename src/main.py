# Import the libraries needed to find elements and manipulate the browser
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
from dotenv import load_dotenv
from utils.aa_login import login_aa

# Import exceptions
from selenium.common.exceptions import *

# Import custom log function
from utils.custom_log import *

# Loads the .env file variables to login on AA Community
load_dotenv()
login = os.getenv('login')
senha = os.getenv('senha')

def main():
    
    # Tries to create the log, open the web browser and start the Message Decoder Challenge
    try:

        # Creates the log
        log_create()
        log_append("Início do desafio Message Decoder")

        # Initializes the driver (in this case, Edge)
        edge_driver = r"src\utils\msedgedriver.exe"
        driver = webdriver.Edge(edge_driver)

        # Opens the desired page and maximizes the window
        driver.get("https://pathfinder.automationanywhere.com/challenges/AutomationAnywhereLabs-Translate.html")
        driver.maximize_window()
        log_append("Navegador inicializado na página do desafio Message Decoder")
        
        # The login_aa function performs the login for Automation Anywhere Community
        login_aa(driver,login,senha)
        
        # Captures the text to be translated
        bulgarian_text_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//section//h2')) # Awaits to the presence of the element to execute the capture
        )
        bulgarian_string = bulgarian_text_element.text.replace("Text to Decode: ", "") # Cut the english stretch of the string
        log_append('Texto em búlgaro capturado com sucesso') 
        
        # Saves the original tab identifier
        message_decoder_tab = driver.current_window_handle

        # Opens a new tab with the translator link
        driver.execute_script("window.open('https://translate.glosbe.com/bg-en', '_blank');")
        log_append('Nova aba aberta com o tradutor de búlgaro para inglês')

        # Get the identifiers of all open tabs
        tabs = driver.window_handles

        # Alternates the focus of the driver for the new tab (the last in the tab list)
        driver.switch_to.window(tabs[-1])
        log_append('Aba do tradutor ativa')

        # Fills in the field of the text to be translated with the original text
        bulgarian_input = driver.find_element(By.XPATH, '//textarea[@placeholder="Type or paste your text here..."]')
        bulgarian_input.send_keys(bulgarian_string)
        bulgarian_input.send_keys(Keys.ENTER)
        log_append('Texto original em búlgaro inserido no tradutor')
       
        time.sleep(5) # Awaits the appearance of the text translated into English
        
        # Capture the translated text
        english_text_element = driver.find_element(By.XPATH, '//app-page-translator-translation-output/div')
        english_string = english_text_element.text
        log_append('Texto traduzido para o inglês e capturado')

        # Returns to the Message Decoder tab
        driver.switch_to.window(message_decoder_tab)
        log_append('Aba do Message Decoder ativa')
        
        # Insert the text translated into Input Field
        text_input = driver.find_element(By.XPATH, '//*[@id="message_input"]')
        text_input.send_keys(english_string)
        log_append('Texto traduzido inserido no input field')

        # Clicks the submit button
        submit_btn = driver.find_element(By.XPATH, '//a[text()="Submit"]')
        submit_btn.click()
        log_append('Realizado click no botão "Submit"')
        
        # Capturing the results of the bot execution
        time.sleep(1)
        success_message = driver.find_element(By.XPATH, '//*[@id="success-title"]').text
        processing_time = driver.find_element(By.XPATH, '//*[@id="processing-time"]').text
        accuracy = driver.find_element(By.XPATH, '//*[@id="accuracy"]').text
        log_append(f"Mensagem: {success_message} | Tempo de processamento: {processing_time} | Acurácia: {accuracy}")
        
    except Exception as e:
            log_append(f"Ocorreu um erro - {e.__class__.__name__}")

    log_append("Finalizando execução do bot")

# Performs the main function
main()