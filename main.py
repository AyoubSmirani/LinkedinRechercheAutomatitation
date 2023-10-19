# This is a sample Python script.
import time
from tkinter import *
from selenium.webdriver import Keys
import sys
from _socket import timeout
from selenium import webdriver
from selenium.webdriver.chrome.service import service, Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
class emploie:
    def __init__(self, emploi, emploiDesc ,url):
        self.emploi = emploi
        self.emploiDesc = emploiDesc
        self.url = url
    def affiche(self):
        print(str(self.emploi.text)
              +
              '\n --------------------------------------------------------------------------------------------'
              +
              str(self.emploiDesc.text))

def submit():
   email = email_entry.get()
   password = password_entry.get()


    # You can perform actions with email, password, and keyword here
    # For example, print them to the console
   print(f"Email: {email}")


   ser = Service("C:\\Users\\azizh\Desktop\\build\\chromedriver.exe")

   driver = webdriver.Chrome(service=ser)
   seConnecter(driver,email,password)

   timeout(2)
   print(driver.current_url[0:35])
   if driver.current_url[0:35] == 'https://www.linkedin.com/checkpoint':
       driver.quit()
       print("Linkedin refuse robot !! restart please")
   else :

      offreemploi = driver.find_element(By.XPATH, "//*[@id='global-nav']/div/nav/ul/li[3]/a")
      offreemploi.click()
      time.sleep(3)
      time.sleep(3)
      search = driver.find_element(By.XPATH, "/html/body/div[5]/header/div/div/div/div[2]/div[2]/div/div/input[1]")
      search.send_keys(Keys.ENTER)
      time.sleep(3)
      section1 = driver.find_element(By.XPATH, "/html/body/div[5]/div[3]/div[4]/div/div/main/div/div[1]/div/ul")
      li = section1.find_elements(By.TAG_NAME, "li")

      Poste = []

      for div in li:
          time.sleep(3)
          url = driver.current_url
          desc = driver.find_element(By.CLASS_NAME,"jobs-description__container")
          Poste.append(emploie(div.text, desc, url))
          div.click()

      filename = "f6.html"
      try:
          # Open the file in write mode
          with open(filename, "w") as html_file:
              # Write the HTML content to the file
              html_file.write("<h1>Offre d'emploie Linkedin</h1>")
              html_file.write("<ul>")
              for obj in Poste:
                  html_file.write(f"<li><a href='{obj.url}' >{obj.emploi}</a></li>")
              html_file.write("</ul>")
          print(f"HTML file '{filename}' created successfully.")
      except Exception as e:
          print(f"Error: {str(e)}")
          sys.exit(1)

      driver.quit()


def seConnecter(driver,email,password,):
    driver.get('https://fr.linkedin.com/')
    driver.maximize_window()
    timeout(2)
    # main = driver.find_element(By.XPATH, "/html/body/main")
    # print(main.text)
    session_key = driver.find_element(By.NAME, "session_key")
    session_key.send_keys(email)
    session_password = driver.find_element(By.NAME, "session_password")
    session_password.send_keys(password)
    btn = driver.find_element(By.XPATH, "//*[@id='main-content']/section[1]/div/div/form/div[2]/button")
    btn.click()

# Create the main window
root = Tk()
root.title("User Information")

# Create labels and entry fields
email_label = Label(root, text="Email:")
email_label.pack()
email_entry = Entry(root)
email_entry.pack()

password_label = Label(root, text="Password:")
password_label.pack()
password_entry = Entry(root, show="*")  # Use 'show' to hide the password
password_entry.pack()



# Create a button to submit the information
submit_button = Button(root, text="Submit", command=submit)
submit_button.pack()

root.mainloop()


















