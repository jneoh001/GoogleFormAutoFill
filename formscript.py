from selenium import webdriver
from random import randint
import time
from selenium.webdriver.common.by import By


def runScript():

    #declare variables & obtain essential data
    link = input("Enter Form Link: \n")
    answersArray = []
    extraChoicesArray = []
    noAnswers = int(input("How many options you want to click (Counts  for Radio Buttons & Check Boxes) :) \n"))

    for i in range(noAnswers):
        answersArray.append(int(input("Radio Button Number: ")))
    
    extraChoices = input("Any Extra XPATH Choices? (e.g 1 to 5 rating e.t.c) Y/N ")

    if(extraChoices == 'Y'):
        extraChoicesNumber = int(input("How many extra choices? "))
        for i in range(extraChoicesNumber):
            extraChoicesXPATH = input("XPATH: ")
            extraChoicesArray.append(extraChoicesXPATH)
    
    submitXPath = input("Submit Button XPath: ")

    numberOfEntries = int(input("How many times do you want to run this script? "))
    for i in range(numberOfEntries):
        #start scripting --------------------------------------------------------------
        print("Running Script..." + str(i+1))
        driver = webdriver.Chrome()
        driver.get(link)

        # We get an array of all radio buttons.& checkboxes
        radiobuttons = driver.find_elements(By.CLASS_NAME, "docssharedWizToggleLabeledContainer")

        # CLick Radio Buttons
        for i in range(len(answersArray)):
            radiobuttons[answersArray[i]].click()
        #Click Extra Choices

        for i in range(len(extraChoicesArray)):
            (driver.find_element(By.XPATH, extraChoicesArray[i])).click()


        submitbutton = driver.find_element(By.XPATH, submitXPath)
        print(str(i+1) + "Script Completed.")
        submitbutton.click()
        
        




# Main
print("""
    -----------------------WELCOME TO GOOGLE FORM AUTO FILL ------------------------------ SCRIPT BY JAVIER NEOH 
    Things to prepare before using
    1. Google Form Link
    2. Number of the Radio buttons/Check Boxes you want to click. ( Start counting from 0)
    4. XPath for Special Buttons. ( e.g 1 to 5)
    3. Submit Button XPath
     """)

runScript()








# no_Qns = int(input("How many questions are there: \n"))

# choicesPerQn = []
# xpathArray = []

# submitXPath = input("Enter Submit Button Xpath: \n")
# for i in range(no_Qns):
#     print("For Question " + str(i+1))
#     qnXpath = input("Enter XPath of Desired Option ")
#     xpathArray.append(qnXpath)





# # Click all options
# for i in range(len(xpathArray)):
#     (driver.find_element(By.XPATH, xpathArray[i])).click()

# # Click Submit
# (driver.find_element(By.XPATH, submitXPath)).click()



# for number_of_runs in range(no_Qns):
#     #driver = webdriver.Chrome()

#     driver = webdriver.Chrome()
#     driver.get(link)

#     time.sleep(1)
#     #Question 1
#     # q1choice = randint(1,5)
#     # while( q1choice not in [1,2,5]):
#     #     q1choice = randint(1,5)

#     # if (q1choice == 1):
#     #     q1 = driver.find_element(By.XPATH,'//*[@id="i5"]/div[3]/div')
#     # if (q1choice == 2):
#     #     q1 = driver.find_element(By.XPATH,'//*[@id="i8"]/div[3]/div')
#     # if (q1choice == 5):
#     #     q1 = driver.find_element(By.XPATH,'//*[@id="i17"]/div[3]/div')
#     q1 = driver.find_element(By.XPATH,'//*[@id="i5"]/div[3]/div')
#     q1.click()


#     #question 2
#     q2choice = randint(1,5)
#     # while( q2choice not in [1,2,5]):
#     #     q2choice = randint(1,5)

#     # if (q2choice == 1):
#     #     q2 = driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div[1]/span/div/label[1]/div[2]/div/div/div[3]/div')
#     # if (q2choice == 2):
#     #     q2 = driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div[1]/span/div/label[1]/div[2]/div/div/div[3]/div')
#     # if (q2choice == 5):
#     #     q2 = driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div[1]/span/div/label[5]/div[2]/div/div/div[3]/div')
#     q2 = driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div[1]/span/div/label[4]/div[2]/div/div/div[3]/div')
#     q2.click()

#     # question 3
#     q3choice = randint(1,5)

#     # if (q3choice == 1):
#     #     q3 = driver.find_element(By.XPATH,'//*[@id="i28"]/div[3]/div')
#     # if (q3choice == 2):
#     #     q3 = driver.find_element(By.XPATH,'//*[@id="i31"]/div[3]/div ')
#     # if (q3choice == 3):
#     #     q3 = driver.find_element(By.XPATH,'//*[@id="i34"]/div[3]/div')
#     # if (q3choice == 4):
#     #     q3 = driver.find_element(By.XPATH,'//*[@id="i37"]/div[3]/div')
#     # if (q3choice == 5):
#     #     q3 = driver.find_element(By.XPATH,'//*[@id="i40"]/div[3]/div')
    
#     q3 = driver.find_element(By.XPATH,'//*[@id="i19"]/div[3]/div')
    
#     q3.click()


#     #question 4
#     q4 = driver.find_element(By.XPATH,'///*[@id="i35"]/div[3]/div')
#     q4.click()

#     #question 5#
#     q5choice = randint(1,5)

#     # if (q5choice == 1):
#     #     q5 = driver.find_element(By.XPATH,'//*[@id="i57"]/div[3]/div')
#     # if (q5choice == 2):
#     #     q5 = driver.find_element(By.XPATH,'//*[@id="i60"]/div[3]/div')
#     # if (q5choice == 3):
#     #     q5 = driver.find_element(By.XPATH,'//*[@id="i63"]/div[3]/div')
#     # if (q5choice == 4):
#     #     q5 = driver.find_element(By.XPATH,'//*[@id="i66"]/div[3]/div')
#     # if (q5choice == 5):
#     q5 = driver.find_element(By.XPATH,'//*[@id="i45"]/div[3]/div')
#     q5.click()

#      #question 6#
#     # q6choice = randint(1,5)

#     # if (q6choice == 1):
#     #     q6 = driver.find_element(By.XPATH,'//*[@id="i76"]/div[3]/div')
#     # if (q6choice == 2):
#     #     q6 = driver.find_element(By.XPATH,'//*[@id="i79"]/div[3]/div')
#     # if (q6choice == 3):
#     #     q6 = driver.find_element(By.XPATH,'//*[@id="i82"]/div[3]/div')
#     # if (q6choice == 4):
#     #     q6 = driver.find_element(By.XPATH,'//*[@id="i85"]/div[3]/div')
#     # if (q6choice == 5):
#     #     q6 = driver.find_element(By.XPATH,'//*[@id="i88"]/div[3]/div')
#     # q6.click()


#     #SUBMISSION 
#     submit = driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[3]/div/div[1]/div/span/span')
#     submit.click()


#     driver.close()
