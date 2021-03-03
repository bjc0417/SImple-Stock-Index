from tkinter import *
import tkinter.font as tkFont
from selenium import webdriver
import time

import os

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

root = Tk()
root.title('Stock Market Index')
root. geometry('210x200')
root.resizable(False, False)
root.configure(background='black')

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('headless')
chrome_options.add_argument('--disable-gpu')

driver = webdriver.Chrome('chromedriver',options=chrome_options)
driver.implicitly_wait(1)
driver.get("https://www.marketwatch.com/investing/bond/tmubmusd10y?countrycode=bx")

i = 1

''' 각종 함수 '''

font = tkFont.Font(family='Gadugi', size=10)#, weight='bold')
font_color = '#01ceec'
bg_color = 'black'

# index 불러오기
def get_index():
    # dow
    dow = driver.find_element_by_xpath('/html/body/section/div[2]/div/div[2]/div/div[1]/table/tbody/tr[1]/td[3]/bg-quote')
    dow_per = driver.find_element_by_xpath('/html/body/section/div[2]/div/div[2]/div/div[1]/table/tbody/tr[1]/td[5]/bg-quote')
    time.sleep(1)
    dow_lbl_2 = Label(root, text=dow.text, font=font, fg='white', bg=bg_color).grid(row=i+1, column=1)
    #dow_lbl_3 = Label(root, text=dow_per.text).grid(row=1, column=2)
    ''' 인덱스 체크 '''
    if '-' in dow_per.text:
        dow_lbl_3 = Label(root, text=dow_per.text, fg='#A4193D', font=font, bg='#2d0d0b').grid(row=i+1, column=2, sticky=W+E)
    else:
        dow_lbl_3 = Label(root, text=dow_per.text, fg='#009d64', font=font, bg='#003322').grid(row=i+1, column=2, sticky=W+E)
    print('Dow : ', dow.text, dow_per.text)

    # snp
    snp = driver.find_element_by_xpath('/html/body/section/div[2]/div/div[2]/div/div[1]/table/tbody/tr[2]/td[3]/bg-quote')
    snp_per = driver.find_element_by_xpath('/html/body/section/div[2]/div/div[2]/div/div[1]/table/tbody/tr[2]/td[5]/bg-quote')
    time.sleep(1)
    snp_lbl_2 = Label(root, text=snp.text, font=font, fg='white', bg=bg_color).grid(row=i+2, column=1)
    #snp_lbl_3 = Label(root, text=snp_per.text).grid(row=2, column=2)
    ''' 인덱스 체크 '''
    if '-' in snp_per.text:
        snp_lbl_3 = Label(root, text=snp_per.text, fg='#A4193D', font=font, bg='#2d0d0b').grid(row=i+2, column=2, sticky=W+E)
    else:
        snp_lbl_3 = Label(root, text=snp_per.text, fg='#009d64', font=font, bg='#003322').grid(row=i+2, column=2, sticky=W+E)
    print('S&P : ', snp.text, snp_per.text)

    # Nasdaq
    nas = driver.find_element_by_xpath('/html/body/section/div[2]/div/div[2]/div/div[1]/table/tbody/tr[3]/td[3]/bg-quote')
    nas_per = driver.find_element_by_xpath('/html/body/section/div[2]/div/div[2]/div/div[1]/table/tbody/tr[3]/td[5]/bg-quote')
    nas_lbl_2 = Label(root, text=nas.text, font=font, fg='white', bg=bg_color).grid(row=i+3, column=1)
    #nas_lbl_3 = Label(root, text=nas_per.text).grid(row=3, column=2)
    ''' 인덱스 체크 '''
    if '-' in nas_per.text:
        nas_lbl_3 = Label(root, text=nas_per.text, fg='#A4193D', font=font, bg='#2d0d0b').grid(row=i+3, column=2, sticky=W+E)
    else:
        nas_lbl_3 = Label(root, text=nas_per.text, fg='#009d64', font=font, bg='#003322').grid(row=i+3, column=2, sticky=W+E)
    print('Nasdaq : ', nas.text, nas_per.text)

    # Gold
    gold = driver.find_element_by_xpath('/html/body/section/div[2]/div/div[2]/div/div[1]/table/tbody/tr[5]/td[3]/bg-quote')
    gold_per = driver.find_element_by_xpath('/html/body/section/div[2]/div/div[2]/div/div[1]/table/tbody/tr[5]/td[5]/bg-quote')
    time.sleep(1)
    gold_lbl_2 = Label(root, text=gold.text, font=font, fg='white', bg=bg_color).grid(row=i+4, column=1)
    #gold_lbl_3 = Label(root, text=gold_per.text).grid(row=4, column=2)
    ''' 인덱스 체크 '''
    if '-' in gold_per.text:
        gold_lbl_3 = Label(root, text=gold_per.text, fg='#A4193D', font=font, bg='#2d0d0b').grid(row=i+4, column=2, sticky=W+E)
    else:
        gold_lbl_3 = Label(root, text=gold_per.text, fg='#009d64', font=font, bg='#003322').grid(row=i+4, column=2, sticky=W+E)
    
    print('Gold : ', gold.text, gold_per.text)

    # US 10 Year Treasury Note
    yt_10 = driver.find_elements_by_tag_name('bg-quote')[45]
    yt_10_per = driver.find_elements_by_tag_name('bg-quote')[47]
    yt_10_lbl_2 = Label(root, text=yt_10.text, font=font, fg='white', bg=bg_color).grid(row=i+5, column=1)
    #yt_10_lbl_3 = Label(root, text=yt_10_per.text).grid(row=5, column=2)
    ''' 인덱스 체크 '''
    if '-' in yt_10_per.text:
        yt_10_lbl_3 = Label(root, text=yt_10_per.text, fg='#A4193D', font=font, bg='#2d0d0b').grid(row=i+5, column=2, sticky=W+E)
    else:
        yt_10_lbl_3 = Label(root, text=yt_10_per.text, fg='#009d64', font=font, bg='#003322').grid(row=i+5, column=2, sticky=W+E)
    print('US 10 Year Treasury : ', yt_10.text, '% ', yt_10_per.text)

get_index()


name_lbl = Label(root, text='SIMPLE INDEX', fg='white', bg=bg_color, font=tkFont.Font(family='Gadugi', size=15,weight='bold')).grid(row=i-1, column=i-1, columnspan=3, sticky=W+E)

btn_index = Button(root, text='Refresh',fg=font_color, bg='#001518', command=get_index)
btn_index.grid(row=i, column=i, sticky=W+E)

dow_lbl = Label(root, text='Dow : ', font=font, fg=font_color, bg=bg_color).grid(row=i+1, column=0, sticky=W)
snp_lbl = Label(root, text='S&P : ', font=font, fg=font_color, bg=bg_color).grid(row=i+2, column=0, sticky=W) 
nas_lbl = Label(root, text='NASDAG : ', font=font, fg=font_color, bg=bg_color).grid(row=i+3, column=0, sticky=W) 
gold_lbl = Label(root, text='Gold : ', font=font, fg=font_color, bg=bg_color).grid(row=i+4, column=0, sticky=W) 
yt_10_lbl = Label(root, text='10YT : ', font=font, fg=font_color, bg=bg_color).grid(row=i+5, column=0, sticky=W) 
james_lbl = Label(root, text='made by james', font=font, fg='white', bg=bg_color, justify='center').grid(row=i+6, column=0, sticky=W+E) 

#driver.quit()
root.mainloop()