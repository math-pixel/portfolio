from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


from speech_recognition import Recognizer, Microphone
import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 200)
engine.setProperty('volume',1.0)




#browser_navigation_panel_height = browser.execute_script('return window.outerHeight - window.innerHeight;')

def pronote():
        browser = webdriver.Firefox()
        #browser.maximize_window()
        browser_location = browser.get_window_position()
        print(browser_location)
        browser.get('https://0740006e.index-education.net/pronote/eleve.html?identifiant=PjaSWrRzAYhHwXuh')#ouvre acces a pronote ( site rhone alpe )
        element = WebDriverWait(browser, 10).until(
                EC.presence_of_element_located((By.XPATH, "/html/body/main/div/div/div[1]/div/div/form/fieldset[1]/legend/button"))
        )

        element.click()

        element = WebDriverWait(browser, 10).until(
                EC.presence_of_element_located((By.XPATH, "/html/body/main/div/div/div[1]/div/div/form/fieldset[1]/ul/li[2]/div/label"))
        )

        element.click()

        element = WebDriverWait(browser, 10).until(
                EC.presence_of_element_located((By.ID, 'button-submit'))
        )
        element.click()


        browser.find_element_by_name("username").send_keys("your username")
        browser.find_element_by_name("password").send_keys("your password")

        element = WebDriverWait(browser, 10).until(
                EC.presence_of_element_located((By.ID, 'button-submit'))
        )
        element.click()

        time.sleep(5)
        element = WebDriverWait(browser, 5000).until(
                EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div/div[2]/div/div/div[1]/div/div/div[2]/div[1]/article[1]/div/div/ul"))

        )

        all_children = element.find_elements_by_xpath(".//*")
        for yey in all_children:
                if yey.tag_name == "h4":# pour les jours
                        print(yey.text)
                        engine.say(yey.text)
                        engine.runAndWait()
                if yey.tag_name == "h5":# pour les matiere
                        print(yey.text)
                        engine.say(yey.text)
                        engine.runAndWait()
                if yey.get_attribute("class") == "descriptif":# contenue des devoirs
                        print(yey.text)
                        engine.say(yey.text)
                        engine.runAndWait()


#pronote()


'''

from speech_recognition import Recognizer, Microphone
import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 200)

volume = engine.getProperty('volume')
print(volume)
engine.setProperty('volume',1.0)


engine.say("mathieu yehhhhhh")
engine.runAndWait()

aaa = " wesh comment cv ?"
for l in aaa.split(" "):
    print(l)

recognizer = Recognizer()

# On enregistre le son

with Microphone() as source:
    print("Réglage du bruit ambiant... Patientez...")
    recognizer.adjust_for_ambient_noise(source)
    print("Vous pouvez parler...")
    recorded_audio = recognizer.listen(source)
    # print("Enregistrement terminé !")

# Reconnaissance de l'audio

try:
    print("Traduction en cours...")
    text = recognizer.recognize_google(
            recorded_audio,
            language="fr-FR"
        )
    print("Vous avez dit : {}".format(text))

except Exception as ex:
    print(ex)
'''
