import tkinter as tk
import requests

window = tk.Tk()
window.title("Burç Yorumu App")
window.resizable(False, False)

FONT = ("Roboto", 9, "bold")
mode = "default"

def button_selected(buttonName):
    global mode
    if(buttonName == "gunluk"):
        gunluk_button.config(bg="Light Green")
        haftalik_button.config(bg="White")
        aylik_button.config(bg="White")
        yillik_button.config(bg="White")
        mode = ""
    elif (buttonName == "haftalik"):
        gunluk_button.config(bg="White")
        haftalik_button.config(bg="Light Green")
        aylik_button.config(bg="White")
        yillik_button.config(bg="White")
        mode = "haftalik"
    elif (buttonName == "aylik"):
        gunluk_button.config(bg="White")
        haftalik_button.config(bg="White")
        aylik_button.config(bg="Light Green")
        yillik_button.config(bg="White")
        mode = "aylik"
    elif (buttonName == "yillik"):
        gunluk_button.config(bg="White")
        haftalik_button.config(bg="White")
        aylik_button.config(bg="White")
        yillik_button.config(bg="Light Green")
        mode = "yillik"

def yorumu_goruntule(yorum, burc):
    global mode
    secondary_window = tk.Toplevel()
    secondary_window.title(f"{burc}")
    secondary_window.config(bg="White")
    if mode == "aylik" or mode == "yillik":
        yorumLabel = tk.Label(secondary_window, text=f"{yorum}",wraplength=1250,bg="White")
    else:
        yorumLabel = tk.Label(secondary_window, text=f"{yorum}",wraplength=600,bg="White")
    yorumLabel.grid(row=0, column=0, padx=10, pady=10)
    button_close = tk.Button(secondary_window,font=FONT,text="KAPAT", command=secondary_window.destroy,cursor="hand2",bg="Orange",width=10)
    button_close.grid(row=1, column=0, pady=10)

def yorumu_getir(burc):
    global url
    if mode != "default":
        if mode != "":
            url = f"https://burc-yorumlari.vercel.app/get/{burc}/{mode}"
            response = requests.get(url)
            for yorum in response.json():
                text = yorum["Yorum"]
            yorumu_goruntule(text,burc)
        else:
            url = f"https://burc-yorumlari.vercel.app/get/{burc}/"
            response = requests.get(url)
            for yorum in response.json():
                text = yorum["GunlukYorum"]
            yorumu_goruntule(text,burc)

# Tkinter items
koc_image = tk.PhotoImage(file="images/koc.png").subsample(2)
koc_button = tk.Label(window, image=koc_image, cursor="hand2")
koc_button.bind("<Button-1>", lambda event, burc="Koç": yorumu_getir(burc))

boga_image = tk.PhotoImage(file="images/boga.png").subsample(2)
boga_button = tk.Label(window, image=boga_image, cursor="hand2")
boga_button.bind("<Button-1>", lambda event, burc="Boğa": yorumu_getir(burc))

ikizler_image = tk.PhotoImage(file="images/ikizler.png").subsample(2)
ikizler_button = tk.Label(window, image=ikizler_image, cursor="hand2")
ikizler_button.bind("<Button-1>", lambda event, burc="İkizler": yorumu_getir(burc))

yengec_image = tk.PhotoImage(file="images/yengec.png").subsample(2)
yengec_button = tk.Label(window, image=yengec_image, cursor="hand2")
yengec_button.bind("<Button-1>", lambda event, burc="Yengeç": yorumu_getir(burc))

aslan_image = tk.PhotoImage(file="images/aslan.png").subsample(2)
aslan_button = tk.Label(window, image=aslan_image, cursor="hand2")
aslan_button.bind("<Button-1>", lambda event, burc="Aslan": yorumu_getir(burc))

basak_image = tk.PhotoImage(file="images/basak.png").subsample(2)
basak_button = tk.Label(window, image=basak_image, cursor="hand2")
basak_button.bind("<Button-1>", lambda event, burc="Başak": yorumu_getir(burc))

terazi_image = tk.PhotoImage(file="images/terazi.png").subsample(2)
terazi_button = tk.Label(window, image=terazi_image, cursor="hand2")
terazi_button.bind("<Button-1>", lambda event, burc="Terazi": yorumu_getir(burc))

akrep_image = tk.PhotoImage(file="images/akrep.png").subsample(2)
akrep_button = tk.Label(window, image=akrep_image, cursor="hand2")
akrep_button.bind("<Button-1>", lambda event, burc="Akrep": yorumu_getir(burc))

yay_image = tk.PhotoImage(file="images/yay.png").subsample(2)
yay_button = tk.Label(window, image=yay_image, cursor="hand2")
yay_button.bind("<Button-1>", lambda event, burc="Yay": yorumu_getir(burc))

oglak_image = tk.PhotoImage(file="images/oglak.png").subsample(2)
oglak_button = tk.Label(window, image=oglak_image, cursor="hand2")
oglak_button.bind("<Button-1>", lambda event, burc="Oğlak": yorumu_getir(burc))

kova_image = tk.PhotoImage(file="images/kova.png").subsample(2)
kova_button = tk.Label(window, image=kova_image, cursor="hand2")
kova_button.bind("<Button-1>", lambda event, burc="Kova": yorumu_getir(burc))

balik_image = tk.PhotoImage(file="images/balik.png").subsample(2)
balik_button = tk.Label(window, image=balik_image, cursor="hand2")
balik_button.bind("<Button-1>", lambda event, burc="Balık": yorumu_getir(burc))

gunluk_button = tk.Button(text="GÜNLÜK", cursor="hand2", bg="White", width=13, font=FONT, command=lambda: button_selected("gunluk"))
haftalik_button = tk.Button(text="HAFTALIK", cursor="hand2", bg="White", width=13, font=FONT, command=lambda: button_selected("haftalik"))
aylik_button = tk.Button(text="AYLIK", cursor="hand2", bg="White", width=13, font=FONT, command=lambda: button_selected("aylik"))
yillik_button = tk.Button(text="YILLIK", cursor="hand2", bg="White", width=13, font=FONT, command=lambda: button_selected("yillik"))

# Layout
koc_button.grid(column=0, row=0)
boga_button.grid(column=1, row=0)
ikizler_button.grid(column=2, row=0)
yengec_button.grid(column=3, row=0)
aslan_button.grid(column=0, row=1)
basak_button.grid(column=1, row=1)
terazi_button.grid(column=2, row=1)
akrep_button.grid(column=3, row=1)
yay_button.grid(column=0, row=2)
oglak_button.grid(column=1, row=2)
kova_button.grid(column=2, row=2)
balik_button.grid(column=3, row=2)
gunluk_button.grid(column=0,row=3)
haftalik_button.grid(column=1,row=3)
aylik_button.grid(column=2,row=3)
yillik_button.grid(column=3,row=3)

window.eval('tk::PlaceWindow . center')
window.mainloop()