from tkinter import filedialog
from tkinter import *

from selenium.webdriver.common.action_chains import ActionChains
import tkinter as tk
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from pynput.keyboard import Key, Controller


import os
import keyboard
from keyboard import press
import sys
import time
from datetime import datetime
from datetime import timedelta

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(executable_path="chromedriver.exe",options=chrome_options)


global total_content
global path_file
global uservalue
global passvalue
global timevalue
global userDiscriptions
global userLink
global time_uploading
flag = 0
keyboard = Controller()
global indexList
indexList=0
global List
List=[]
# to run bot
def run_ALl():
    
    open_Browser()
    media_post_upload()


# open browser
def open_Browser():
    # go to website twitter login page
    URL = "https://twitter.com/i/flow/login"
    driver.maximize_window()
    tweetUSer = uservalue.get()
    tweetPass = passvalue.get()
    driver.get(URL)
    us_xpath = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, "//input[@name='text']")))
    us_xpath.send_keys(tweetUSer)
    us_xpath.send_keys(Keys.ENTER)
    # keyboard = Controller()
    # keyboard.type(tweetUSer)
    # keyboard.press(Key.enter)
    # keyboard.release(Key.enter)
    # time.sleep(1)

    #pass value

    pas_xpath = WebDriverWait(driver,15).until(EC.presence_of_element_located((By.XPATH,"//input[@name='password']")))
    pas_xpath.send_keys(tweetPass)
    pas_xpath.send_keys(Keys.ENTER)

    # keyboard = Controller()
    # time.sleep(3)
    # keyboard.type(tweetPass)
    # keyboard.press(Key.enter)
    # keyboard.release(Key.enter)

def media_post_upload():
    time.sleep(5)
    wait_time_of_upload = time_uploading.get()
    wait_sec = int(wait_time_of_upload)
    keyboard = Controller()
    driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't')
    driver.get('https://studio.twitter.com/library')
    # print(directory)
    media_click = driver.find_element_by_xpath('//button [@class = "Button" ]')
    for filename in os.listdir(directory):
        print(filename + "  Uploading....")
        f = os.path.join(directory, filename)
        f = f.replace('/','\\')
        # print(f)
        if os.path.isfile(f):
            print(f)
            media_click.click()
            time.sleep(5)
            keyboard.type(f)
            keyboard.press(Key.enter)
            time.sleep(2)
            keyboard.release(Key.enter)
            time.sleep(wait_sec)
            print("DOne ")
            schedule_post()
    print("Done")
def schedule_post():
    global flag
    global privous_time
    global indexList

    keyboard = Controller()
    tweet_discriptions = userDiscriptions.get()
    tweet_link = userLink.get()
    tweet_time_gap = timevalue.get()



    # tweet_vide_click= driver.find_element_by_xpath("//p[@class='_1QcFWTUe']")
    tweet_vide_click= driver.find_element_by_xpath("(//div[@class='_25qJQmz6'])[1]")
    tweet_vide_click.click()

    #discriptions click
    tweet_Desriptions_click = driver.find_element_by_xpath("//textarea[@label='Description'][@name='media.metadata.description']")
    tweet_Desriptions_click.click()
    keyboard.type(tweet_discriptions)

    #link click and type
    tweet_url = driver.find_element_by_xpath("//input[@name='media.metadata.cta_link'][@class='FormInput']")
    tweet_url.click()
    keyboard.type(tweet_link)
    #twitt button

    twitt_post_elm = driver.find_element_by_xpath("//span[@class='Button-label'][text() = 'Tweet']")
    twitt_post_elm.click()
    #text conatent
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//textarea[@placeholder=\"What's happening?\"]"))).send_keys(List[indexList])
    if(indexList>=total_content-1):
        print("Rotating content")
        indexList=0
    else:
        indexList+=1
    #twiit schedule posthey
    time.sleep(3)
    twiit_sechedule_elm = driver.find_element_by_xpath("//span[@class='Button-label'][text() = 'Schedule']")
    twiit_sechedule_elm.click()
    time_int_val = int(tweet_time_gap)


    if(flag<1):
        current_time_info = datetime.today()
        current_time_info = current_time_info + timedelta(minutes=time_int_val)
        privous_time = current_time_info

        day = str(privous_time.day)
        change_month = datetime.today()
        month = int(change_month.month)
        prMonth= int(privous_time.month)
        if prMonth > month or prMonth > 12:
            mclick = driver.find_element_by_xpath("//button[@title='Next']")
            mclick.click()
        else:
            pass
        day_xpath = "(//span[normalize-space()='" + day + "'])[2]"
        try:
            date_select = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "(//span[normalize-space()='" + day + "'])[1]")))
            date_select.click()
        except:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, day_xpath))).click()



        time_post = current_time_info.strftime("%I:%M %p")
        # time_input_schedule = driver.find_element_by_xpath("//input[@class='w-wEIeIn']")
        time_input_schedule = driver.find_element_by_xpath("//input[@class='_2qlDr6oK']")
        time_input_schedule.click()
        time_input_schedule.send_keys(Keys.CONTROL, 'a')
        keyboard.type(time_post)

        # inputs

        flag = 1
        print(time_post)
    else:
        privous_time = privous_time + timedelta(minutes=time_int_val)

        day = str(privous_time.day)
        change_month = datetime.today()
        month = int(change_month.month)
        pMonth = int(privous_time.month)
        if pMonth > month or pMonth > 12:
            mclick = driver.find_element_by_xpath("//button[@title='Next']")
            mclick.click()
        else:
            pass
        day_xpath = "(//span[normalize-space()='" + day + "'])[2]"
        try:
            date_select = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "(//span[normalize-space()='" + day + "'])[1]")))
            date_select.click()
        except:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, day_xpath))).click()



        time_post_twitter = privous_time.strftime("%I:%M %p")
        # time_input_schedule = driver.find_element_by_xpath("//input[@class='w-wEIeIn']")
        time_input_schedule = driver.find_element_by_xpath("//input[@class='_2qlDr6oK']")
        time_input_schedule.click()
        time_input_schedule.send_keys(Keys.CONTROL, 'a')
        keyboard.type(time_post_twitter)



        print(time_post_twitter)




    time_save_post = driver.find_element_by_xpath("//span[@class='Button-label'][text()='Save' ]")
    time_save_post.click()
    Send_done_post = driver.find_element_by_xpath("//span[@class='Button-label'][text()='Done' ]")
    Send_done_post.click()

def displayText(path):
    global Counter
    global total_content
    Counter = 0
    file = open(path, "r")
    # Reading from file
    content=file.read()
    CoList = content.split("##")
    for i in CoList:
        if i:
            List.append(i)
            Counter += 1
    sizelist = len(List) - 1
    total_content=sizelist
    return Counter

# browse button
def browse_text():
    global textdirect
    # Allow user to select a directory and store it in global var
    # called folder_path

    textdirect = filedialog.askopenfilename(filetypes=(("content", "*.txt"), ("All files", "*")))
    # directory.repalce('/','\')
    folder_p.set(textdirect)
    print("total contents",displayText(textdirect))


def browse_button():
    global directory
    # Allow user to select a directory and store it in global var
    # called folder_path

    directory = filedialog.askdirectory()
    # directory.repalce('/','\')
    folder_path.set(directory)






root = Tk()
root.geometry("1200x500")
root.title("Bot By Deepak")
root['background'] = '#8C65D3'

# credential

user = Label(root, text="UserName", font="Roboto,14,bold", bg="#8C65D3", fg="white")
password = Label(root, text="Password", font="Roboto,14,bold", bg="#8C65D3", fg="white")
browsefolder = Label(root, text="Browse media", font="Roboto,14,bold", bg="#8C65D3", fg="white")
discriptions = Label(root, text="Discriptions", font="Roboto,14,bold", bg="#8C65D3", fg="white")
timeDelay = Label(root, text="Time delay", font="Roboto,14,bold", bg="#8C65D3", fg="white")
link = Label(root, text="links ", font="Roboto,14,bold", bg="#8C65D3", fg="white")
uploading_time_wait = Label(root, text="Uploading Media time wait in sec", font="Roboto,14,bold", bg="#8C65D3", fg="white")


# alignment of layout
user.grid()
password.grid(row=1)
browsefolder.grid(row=2)
timeDelay.grid(row=3)
uploading_time_wait.grid(row=4)
discriptions.grid(row=5)
link.grid(row=6)
Label(root, text="add content text ", font="Roboto,14,bold", bg="#8C65D3", fg="white").grid(row=7)

# entry
uservalue = StringVar()
passvalue = StringVar()
timevalue = StringVar()
userDiscriptions = StringVar()
userLink = StringVar()
time_uploading = StringVar()


# data
userentry = Entry(root, textvariable=uservalue)
passentry = Entry(root, textvariable=passvalue)
timeentry = Entry(root, textvariable=timevalue)
DiscriptionEntry = Entry(root, textvariable=userDiscriptions, width=50)
linkEntry = Entry(root, textvariable= userLink, width = 55)
upload_entry = Entry(root, textvariable=time_uploading)


userentry.grid(row=0, column=1)
passentry.grid(row=1, column=1)
timeentry.grid(row=3, column=1)
DiscriptionEntry.grid(row=5, column=1)
linkEntry.grid(row = 6 ,column=1)
upload_entry.grid(row = 4 ,column=1)
folder_path = StringVar()
folder_p=StringVar()

lbl1 = Label(master=root, textvariable=folder_path)
lbl1.grid(row=2, column=2)
lbl2 = Label(master=root, textvariable=folder_p)
lbl2.grid(row=7, column=3)
button2 = Button(text="Browse", command=browse_button).grid(row=2, column=1)
button3 = Button(text="Browse text", command=browse_text).grid(row=7, column=1)

Button(text="Run Bot", command=run_ALl).grid()
root.mainloop()
