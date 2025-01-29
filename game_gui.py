import random
from tkinter import *
from tkinter import messagebox as msg
from tkinter.font import families
from PIL import Image, ImageTk

    # menüablak létrehozása
ablak= Tk()
ablak.title ("Kő, Papír, Olló by:Andika")
ablak.geometry("800x1200+10+10")
ablak.config(bg='PeachPuff3')
ablak.resizable( False, False)

menu_frame = Frame(ablak, bg='PeachPuff3')
menu_frame.pack(fill="both", expand=True)

game_frame = Frame(ablak, bg='PeachPuff3')
help_frame = Frame(ablak, bg="PeachPuff3")

btn_back =Button (game_frame,command= lambda:newpanel(menu_frame), bg= "PeachPuff4", text= "Vissza",borderwidth=5, relief="raised",width=40, fg= 'lightblue',)
btn_back.place(x=220, y=600)
btn_back2 =Button (help_frame,command= lambda:newpanel(menu_frame), bg= "PeachPuff4", text= "Vissza",borderwidth=5, relief="raised",width=40, fg= 'lightblue',)
btn_back2.place(x= 220, y= 600)

help_text = Text(help_frame,bg="PeachPuff3", height=15, width=65, borderwidth=5, relief="raised", fg= 'maroon', font= ("Constantian", 14))
help_text.place(x=30, y=30)

# Kép betöltése
image1 = Image.open("/home/lovequinn/Asztal/python/images/ko.jpg")  # A kép elérési útvonala
image1 = image1.resize((100, 100))  # Átméretezés
photo1 = ImageTk.PhotoImage(image1) # – Átalakítja Tkinter-kompatibilis formátumra.

image2 = Image.open("/home/lovequinn/Asztal/python/images/papir.jpg") 
image2 = image2.resize((100, 100))  
photo2 = ImageTk.PhotoImage(image2)

image3 = Image.open("/home/lovequinn/Asztal/python/images/ollo.jpg")  
image3 = image3.resize((100, 100))  
photo3 = ImageTk.PhotoImage(image3) 


help_text.insert("1.0","A játék célja, hogy legyőzd a számítógépet Kő, Papír vagy Olló választásával.\n\n"
                      "- Kő legyőzi az Ollót\n"
                      "- A papír legyőzi a Követ\n"
                      "- Az olló legyőzi a papírt!\n")

help_text.image_create(END, image=photo1)  # Kő képe
help_text.insert(END, "  (Kő) \n")
help_text.image_create(END, image=photo2)  # Papír képe
help_text.insert(END, "  (Papír) \n")
help_text.image_create(END, image=photo3)  # Olló képe
help_text.insert(END, "  (Olló) \n")

help_text.photo1 = photo1
help_text.photo2 = photo2
help_text.photo3 = photo3


help_text.config(state=DISABLED)  # Csak olvashatóvá tesszük



lbl_menu = Label (menu_frame, text= ("Szia! Játszunk egyet! \n Kő, papír, olló!"),fg="maroon" ,bg= "PeachPuff3", font= ('Constantia', 30))
lbl_menu.place(x=200, y=50)

btn_new = Button( menu_frame, text= "Új Játék",borderwidth=5, relief="raised",width=40, fg= 'lightblue', bg= 'PeachPuff4', font= ("Arial"),
                 command=lambda: newpanel(game_frame))

btn_new.place(x=200, y=300)

btn_help = Button( menu_frame, text= "Segítség", borderwidth=5, relief="raised",width=40, fg= 'lightblue', bg= 'PeachPuff4', font= ("Arial"),
command=lambda: newpanel(help_frame))

btn_help.place(x=200, y=350)

btn_exit = Button( menu_frame, text= "Kilépés", borderwidth=5, relief="raised",width=40, fg= 'lightblue', bg= 'PeachPuff4', font= ("Arial"),
                 command=ablak.quit)

btn_exit.place(x=200, y=400)

lbl = Label(game_frame, text= "Kő, papír, vagy olló?", bg='PeachPuff3', fg='maroon', font=("Constantia", 30), width=30)
lbl.place(x=80, y=50)

comp = 0
user = 0

comp_scoore = StringVar()
comp_scoore.set(f"Gép: {comp}")

lbl_c = Label(game_frame, textvariable=comp_scoore, borderwidth=5, relief="raised",bg= 'PeachPuff4', fg='snow', font=("Arial", 12))
lbl_c.place(x=30, y=30)

usr_scoore = StringVar()
usr_scoore.set(f"Játékos: {user}")

lbl_u = Label(game_frame, textvariable=usr_scoore, bg= 'PeachPuff4',borderwidth=5, relief="raised",fg='snow', font=("Arial", 12))
lbl_u.place(x=700, y=30)

ko_btn = Button(game_frame, command=lambda: klikk("Kő"), image=photo1, width=150, height=150, borderwidth=5, relief="groove", bg="PeachPuff4")
ko_btn.place(x=50, y= 300)

papir_btn = Button(game_frame,command=lambda: klikk("Papír"), image=photo2, width=150, height=150, borderwidth=5, relief="groove", bg="PeachPuff4")
papir_btn.place(x=300, y= 300)

ollo_btn = Button(game_frame, image=photo3,command=lambda: klikk("Olló"), width=150, height=150, borderwidth=5, relief="groove", bg="PeachPuff4")
ollo_btn.place(x=550, y= 300)

def newpanel(frame):
    menu_frame.pack_forget()
    game_frame.pack_forget()
    help_frame.pack_forget()
    frame.pack(fill="both", expand= True)

def klikk(jatekos_valasztas):
    global comp, user


    valaszt = ["Kő", "Papír", "Olló"]  # 1: kő, 2: papír, 3: olló
    gpu_valasztas = random.choice(valaszt)  # Gép véletlen választása

    # Ki nyert?
    if jatekos_valasztas == gpu_valasztas:
        eredmeny = "Döntetlen!"
    elif (jatekos_valasztas == "Kő" and gpu_valasztas == "Olló") or \
         (jatekos_valasztas == "Olló" and gpu_valasztas == "Papír") or \
         (jatekos_valasztas == "Papír" and gpu_valasztas == "Kő"):
        user += 1
        eredmeny = "Nyertél!"
    else:
        comp += 1
        eredmeny = "Vesztettél!"

    # Frissítjük a pontszámokat
    comp_scoore.set(f"Gép: {comp}")
    usr_scoore.set(f"Játékos: {user}")

    # Kiírjuk az eredményt egy üzenetablakba
    msg.showinfo("Eredmény", f"Te: {jatekos_valasztas}, Gép: {gpu_valasztas}\n{eredmeny}")
    




menu_frame.pack(fill="both", expand=True)



ablak.mainloop()