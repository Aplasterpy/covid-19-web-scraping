import requests 
import bs4
import tkinter as tk
import plyer
import time
import datetime
import threading

def get_html_data(url):
    data = requests.get(url)
    return data
#persing html data

def get_corona_details_in_india():
    url = "https://www.mohfw.gov.in/"
    html_data = get_html_data(url)
    bs = bs4.BeautifulSoup(html_data.text, 'html.parser')
    info_div = bs.find("div", class_="information_row").find_all("div", class_="iblock")
    all_details = ""
    for block in info_div:
        count = block.find("span", class_="icount").get_text()
        text = block.find("div", class_="info_label").get_text()
        all_details = all_details + text + " : " + count + "\n"
    return all_details

def refresh():
    newData = get_corona_details_in_india()
    print("Refresh...")
    print("please wait....")
    mainLabel['text'] = newData
    
    def notify_me():
        while True:
            plyer.notification.notify(
                title = "COVID 19 cases of INDIA",
                timeout = 10,
                app_icon = 'icon.ico'

            )
            time.sleep(30)
            
            
root =tk.Tk()
root.geometry ("900x800")
root.iconbitmap("icon.ico")
root.title("CORORNA DATA TRACKER - INDIA")
root.configure(background = 'white')
f = ("poppins", 25, "bold")
banner =  tk.PhotoImage(file = "banner.png")
bannerLABEL = tk.Label(root,image = banner)
bannerLABEL.pack()
#mainLabel = tk.Label(root, text=get_corona_details_in_india)
mainLabel = tk.Label(root, text=get_corona_detail_of_india(), font=f, bg='white')
mainLabel.pack()

reBtn = tk.Button(root, text="REFRESH", font=f, relief='solid', command=refresh)
reBtn.pack()

# create a new thread
th1 = threading.Thread(target=notify_me)
th1.setDaemon(True)
th1.start()

root.mainloop()