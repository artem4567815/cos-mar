import time
from tkinter import *
from tkinter import ttk
import random
from PIL import Image, ImageTk
import math
import json
import pygame
from objects.bullet import Bullet
from objects.block import Block
from operator import itemgetter
# import os
# import sys
# os.chdir(sys._MEIPASS)
from pyPS4Controller.controller import Controller
from threading import Thread

tk = Tk()
style = ttk.Style()
style.configure("BW.TLabel", foreground="white", background="black")
style.map('BW.TLabel', background=[('selected', 'white')], foreground=[('selected', 'black')])
tk.geometry("1280x1070")
tk.attributes("-fullscreen", True)
c = Canvas(tk, width=1280, height=1024, bg="white")
c.grid(row=2, columnspan=20)
tk["bg"] = "black"

is_playing = False

time0 = 0
vy = 136
count = 0
count2 = 0
life = 5
random_var = StringVar()
blocks = []

color = {"red": ImageTk.PhotoImage(Image.open("images/cannon_red_new.png")),
         "blue": ImageTk.PhotoImage(Image.open("images/blue_new.png")),
         "green": ImageTk.PhotoImage(Image.open("images/green_new.png"))}


#----------------------music!!!-----------------------------------------------------------------------------------------
pygame.init()
pygame.mixer.init()

STOPPED_PLAYING = pygame.USEREVENT + 1
pygame.mixer.music.set_endevent(STOPPED_PLAYING)
music = "one"
arr = ["musik/хакатон_1.wav", "musik/3музыка.wav", "musik/4musik.wav", "musik/musik5.wav"]
rand = random.choice(arr)

print("Playing ", rand)

pygame.mixer.music.load(rand)
pygame.mixer.music.play()
pygame.mixer.music.set_volume(0.1)
arr.remove(str(rand))

#-------------------------------------------------------------------------------------------------------------

#------------------------------------------Background-------------------------------------------------------------------
back_purple_phon = ImageTk.PhotoImage(Image.open("Background/purple.png"))
back_purple_phon2 = c.create_image(0, 0, image=back_purple_phon, anchor=NW)

star1 = ImageTk.PhotoImage(Image.open("Background/star1.png"))
star1_1 = c.create_image(0, 0, image=star1, anchor=NW)
star2 = ImageTk.PhotoImage(Image.open("Background/star2.png"))
star2_1 = c.create_image(0, 0, image=star2, anchor=NW)
star3 = ImageTk.PhotoImage(Image.open("Background/star3.png"))
star3_1 = c.create_image(0, 0, image=star3, anchor=NW)


star1_2 = c.create_image(0, -1024, image=star1, anchor=NW)

star2_2 = c.create_image(0, -1024, image=star2, anchor=NW)

star3_2 = c.create_image(0, -1024, image=star3, anchor=NW)

planet_red = ImageTk.PhotoImage(Image.open("Background/planet_red.png"))
planet_red1 = c.create_image(50, 80, image=planet_red, anchor=NW)
planet_green = ImageTk.PhotoImage(Image.open("Background/planet_green.png"))
planet_green1 = c.create_image(680, 100, image=planet_green, anchor=NW)
planet_purple_light = ImageTk.PhotoImage(Image.open("Background/planet_purple_light.png"))
planet_purple_light1 = c.create_image(1040, 50, image=planet_purple_light, anchor=NW)
planet_purple_dark = ImageTk.PhotoImage(Image.open("Background/planet_purple_dark.png"))
planet_purple_dark1 = c.create_image(400, 200, image=planet_purple_dark, anchor=NW)
planet_orange = ImageTk.PhotoImage(Image.open("Background/palnet_orange.png"))
planet_orange1 = c.create_image(500, 760, image=planet_orange, anchor=NW)

sb = ImageTk.PhotoImage(Image.open("Background/хзхзхзхзхзхзхзхзхзхз.png"))
sb1 = c.create_image(0, 0, image=sb, anchor=NW)

planet_green_dark = ImageTk.PhotoImage(Image.open("Background/planet_green_dark.png"))
planet_green_dark1 = c.create_image(30, 550, image=planet_green_dark, anchor=NW)
planet_top = ImageTk.PhotoImage(Image.open("Background/planet_top.png"))
planet_top1 = c.create_image(740, 520, image=planet_top, anchor=NW)
vx = 0.04
vx2 = 0.012
vx3 = 0.1
vx4 = 0.12
vx5 = 0.016
vx6 = 0.014
vx7 = 0.2
#-----------------------------------------------------------------------------------------------------------------------

images = {
    "base": ImageTk.PhotoImage(Image.open("images/baza.png")),
    "cannon_create_green": ImageTk.PhotoImage(Image.open("images/new_green.png")),
    "cannon_create_blue": ImageTk.PhotoImage(Image.open("images/new_blue.png")),
    "cannon_create_red": ImageTk.PhotoImage(Image.open("images/new_red.png")),
    "bullet_create_green": ImageTk.PhotoImage(Image.open("images/bullet.png")),
    "bullet_create_blue": ImageTk.PhotoImage(Image.open("images/bullet_blue.png")),
    "bullet_create_red": ImageTk.PhotoImage(Image.open("images/red_bullet.png")),
    "aim": ImageTk.PhotoImage(Image.open("images/aim2.png")),
    "red_aim": ImageTk.PhotoImage(Image.open("images/red_aim.png")),
    "black_hp": ImageTk.PhotoImage(Image.open("images/black_color.png")),
    "red_hp": ImageTk.PhotoImage(Image.open("images/red_color.png")),
    "select_green_cannon": ImageTk.PhotoImage(Image.open("images/yellow_green.png")),
    "select_blue_cannon": ImageTk.PhotoImage(Image.open("images/yellow_blue.png")),
    "select_red_cannon": ImageTk.PhotoImage(Image.open("images/yellow_red.png")),
    "1.5x": ImageTk.PhotoImage(Image.open("images/15x.png")),
    "2x": ImageTk.PhotoImage(Image.open("images/2x.png")),
    "3x": ImageTk.PhotoImage(Image.open("images/3x.png")),
    "sound": ImageTk.PhotoImage(Image.open("images/sound.png")),
    "not sound": ImageTk.PhotoImage(Image.open("images/not_sound.png")),
    "info": ImageTk.PhotoImage(Image.open("images/info3.png"))
}
game_objects = {

}
bonus = []
black_life = {}
time5 = 50
users = []
a = 15000
t = 0
list_count = []
columns = ("№", "name", "count")

def show_message():
    global count, flag9, users, leb3, flag16, tree, num
    if flag9:
        ax = entry.get()
        leb3 = Label(tk, font=("Ariel", 25), foreground="white", background="black")
        leb3.grid(row=3, column=4)
        try:
            with open("users.txt", "r") as file:
                users = json.load(file)
        except:
            users = []

        has_user = False
        for user in users:
            if user["name"] == ax:
                has_user = True
                break

        if not has_user:
            users.append({"name": ax, "count": count})
            users.sort(key=itemgetter('count'), reverse=True)

        art = users.index({"name": ax, "count": count})
        with open("users.txt", "w") as file:
            json.dump(users, file, indent=1)
        if len(users) >= 101:
            users.remove(users[-1])
        tree.destroy()
        num = 0
        tree = ttk.Treeview(columns=columns, show="headings", height=45, style="BW.TLabel")
        scrollbar = ttk.Scrollbar(orient='vertical', command=tree.yview)
        scrollbar.grid(row=4, column=21, sticky=NS)

        tree['yscrollcommand'] = scrollbar.set
        for person in users:
            if len(users) >= 101:
                users.remove(users[-1])
                leb3.configure(
                    text="Твои очки: " + str(count) + '\n' + "Твой ник: " + str(ax) + '\n' + "Твоё место: " + str(
                        num))
            num += 1
            leb3.configure(
                text="Твои очки: " + str(count) + '\n' + "Твой ник: " + str(ax) + '\n' + "Твоё место: " + str(
                    art + 1))
            tree.insert("", END, values=(num, person["name"], person["count"]), tags="tree")
            tree.tag_configure("tree", font=("Ariel", 13))
        flag9 = False


game_btn = ImageTk.PhotoImage(Image.open("Background/KPNF2945.PNG"))
restart = ImageTk.PhotoImage(Image.open("images/restart.png"))
tab_lid = ImageTk.PhotoImage(Image.open("images/tabl_new.png"))
bullets = []

state = "green"
flag = "True"
flag2 = True
flag5 = False
flag6 = False
flag7 = False
flag8 = True
flag9 = True
flag10 = True
flag11 = False
flag12 = False
flag13 = False
flag14 = False
flag15 = False
flag16 = True


time2 = 3240
objects = []
station = "menu"
time4 = 0


def clear():
    for object in objects:
        c.delete(object)


def draw_menu():
    if is_playing == False:
        objects.append(c.create_image(200, 650, image=game_btn, anchor=NW))
        objects.append(c.create_image(50, 0, image=images["info"], anchor=NW))

def menn():
    global station, leb, btn4, entry, tree, flag7, btn, lab, lab2, leb2, leb3
    if station == "menu3":
        station = "menu2"
        flag7 = False
        c.config(width=1280, height=1024)
        leb.destroy()
        leb2.destroy()
        leb3.destroy()
        btn4.destroy()
        entry.destroy()
        tree.destroy()
        btn.destroy()
        lab = Label(tk, text="Счёт:", font=("Comic Sans MS", 25), bg="black", fg="white")
        lab.grid(row=0, column=0)
        lab2 = Label(tk, textvariable=random_var, font=("Comic Sans MS", 25), fg="black")
        lab2.grid(row=0, column=1)

def draw_menu2():
    global station, entry, leb, leb2, num, btn4, lab, lab2, leb3
    if not is_playing:
        objects.append(c.create_image(150, 130, image=restart, anchor=NW))
        objects.append(c.create_image(100, 469, image=tab_lid, anchor=NW))
        if flag7:
            station = "menu3"
            lab.destroy()
            lab2.destroy()
            btn4.grid(row=0, column=0)
            leb.grid(row=0, column=1)
            leb2.grid(row=1, column=1)
            entry.grid(row=3, column=1)
            c.config(width=0, height=0)
            tree.grid(row=4, columnspan=20)
            btn.grid(row=3, column=2)

            tree.heading("№", text="№", anchor=NW)
            tree.heading("name", text="Имя", anchor=NW)
            tree.heading("count", text="count", anchor=NW)

            tree.column("#1", stretch=NO, width=100)
            tree.column("#2", stretch=NO, width=820)
            tree.column("#3", stretch=NO, width=200)

            clear()


def draw_images():
    game_objects["sound"] = c.create_image(1210, 954, image=images["sound"], anchor=NW)
    game_objects["not sound"] = c.create_image(1210, 954, image=images["not sound"], anchor=NW)
    game_objects["base1"] = c.create_image(0, 956, image=images["base"], anchor=NW)
    game_objects["aim2"] = c.create_image(30, -136, image=images["aim"], anchor=NW)
    game_objects["aim"] = c.create_image(30, -136, image=images["red_aim"], anchor=NW)
    game_objects["cannon_green"] = c.create_image(50, 810, image=images["cannon_create_green"], anchor=NW)
    game_objects["cannon_blue"] = c.create_image(490, 810, image=images["cannon_create_blue"], anchor=NW)
    game_objects["cannon_red"] = c.create_image(1074, 815, image=images["cannon_create_red"], anchor=NW)
    game_objects["selected1"] = c.create_image(50, 810, image=images["select_green_cannon"], anchor=NW)
    game_objects["selected2"] = c.create_image(490, 810, image=images["select_blue_cannon"], anchor=NW)
    game_objects["selected3"] = c.create_image(1074, 815, image=images["select_red_cannon"], anchor=NW)
    c.tag_raise(game_objects["cannon_green"])
    c.tag_raise(game_objects["cannon_red"])
    c.tag_raise(game_objects["cannon_blue"])
    c.tag_raise(game_objects["aim2"])
    c.tag_raise(game_objects["base1"])
    c.tag_raise(game_objects["sound"], game_objects["base1"])
    game_objects["hp5"] = c.create_image(5, 960, image=images["red_hp"], tag='down', anchor=NW)
    game_objects["hp4"] = c.create_image(85, 960, image=images["red_hp"], tag='down', anchor=NW)
    game_objects["hp3"] = c.create_image(165, 960, image=images["red_hp"], tag='down', anchor=NW)
    game_objects["hp2"] = c.create_image(245, 960, image=images["red_hp"], tag='down', anchor=NW)
    game_objects["hp"] = c.create_image(325, 960, image=images["red_hp"], tag='down', anchor=NW)
    c.tag_raise(game_objects["hp"])
    c.tag_raise(game_objects["hp2"])
    c.tag_raise(game_objects["hp3"])
    c.tag_raise(game_objects["hp4"])
    c.tag_raise(game_objects["hp5"])
    game_objects["dead_line"] = c.create_line(0, 810, 1280, 810, fill="red", width=2)


def click(event):
    global station, is_playing, time0, flag9, time2
    if 200 < event.x < 1102 and 650 < event.y < 837 and is_playing == False and station != "menu2":
        clear()
        flag9 = True
        if station == "menu":
            station = "game"
            draw_images()
        else:
            station = "menu"


def click2(event):
    global station, is_playing, time0, flag, life, tree, flag5, flag6, flag7, flag9, flag10, time4, a, t, tree, leb, entry, btn4, btn, num, users, count, count2, tree2, tree3, leb2, leb3, flag16, time2, entry2
    if 150 < event.x < 1134 and 130 < event.y < 320 and is_playing == False and station == "menu2":
        clear()
        if station == "menu2":
            life = 5
            time0 = 0
            count = 0
            count2 = 0
            time4 = 0
            a = 15000
            t = 0
            time2 = 3240
            flag = "True"
            station = "game"
            draw_images()
        else:
            station = "menu2"
    if 100 < event.x < 1176 and 469 < event.y < 894 and not is_playing and station == "menu2":
        flag7 = True
        flag9 = True
        num = 0
        entry = ttk.Entry(width=30, font=("Ariel", 20))
        leb = Label(tk, text="Топ 120 лучших игроков!", font=("Ariel", 25), foreground="white", background="black")
        leb2 = Label(tk, text="Введите ник ниже:", font=("Ariel", 25), foreground="white", background="black")
        leb3 = Label(tk, font=("Ariel", 25), foreground="white", background="black")
        btn4 = Button(tk, text="<", command=menn, width=10, height=3, foreground="white", background="black")
        tree = ttk.Treeview(columns=columns, show="headings", height=45, style="BW.TLabel")
        scrollbar = ttk.Scrollbar(orient='vertical', command=tree.yview)
        scrollbar.grid(row=4, column=21, sticky=NS)
        tree['yscrollcommand'] = scrollbar.set
        btn = Button(tk, text="Enter", command=show_message, foreground="white", background="black", font=("Ariel", 20))

        try:
            with open("users.txt", "r") as file:
                users = json.load(file)
        except:
            users = []

        for person in users:
            num += 1
            if len(users) >= 101:
                users.remove(users[-1])
            else:
                tree.insert("", END, values=(num, person["name"], person["count"]), tags="tree")
                tree.tag_configure("tree", font=("Ariel", 13))
        if station == "menu3":
            station = "game"
        else:
            station = "menu3"

frame = 0
count3 = 0
count4 = 0
count5 = 0
mxstate = 0


def gameloop():
    global station, is_playing, time0, frame
    global arr, music, vy
    global time5, flag15, flag, life
    global count, time2, time4, a, t, count2, time5, flag15, count3, count4, count5, flag, is_playing
    global is_playing, count, station, life, flag, time0, bonus, entry2, mxstate
    frame += 20
    should_delete = []
    neightboor2 = []
    counter = []
    time4 += 5
    cor = []
    if station == "menu":
        is_playing = False
        draw_menu()
    if station == "menu2":
        is_playing = False
        time0 = 0
    if station == "menu3":
        is_playing = False
        draw_menu2()
    if station == "game":
        is_playing = True
        time0 += 20

    if len(arr) == 0:
        arr = ["musik/хакатон_1.wav", "3musik/музыка.wav", "musik/4musik.wav", "musik/musik5.wav"]
    for event in pygame.event.get():
        rand = random.choice(arr)

        if STOPPED_PLAYING == event.type:
            print("New music ", rand)

        if STOPPED_PLAYING == event.type and music == "one":
            pygame.mixer.music.load(rand)
            arr.remove(rand)
            pygame.mixer.music.play()
            music = "two"
            continue
        if STOPPED_PLAYING == event.type and music == "two":
            pygame.mixer.music.load(rand)
            arr.remove(rand)
            pygame.mixer.music.play()
            music = "three"
            continue
        if STOPPED_PLAYING == event.type and music == "three":
            pygame.mixer.music.load(rand)
            arr.remove(rand)
            pygame.mixer.music.play()
            music = "four"
            continue
        if STOPPED_PLAYING == event.type and music == "four":
            pygame.mixer.music.load(rand)
            arr.remove(rand)
            pygame.mixer.music.play()
            music = "one"
            continue

    if flag == "False":
        is_playing = False
        station = "menu2"
        entry2.grid(row=0, column=4)
        c.delete(game_objects["base1"])
        c.delete(game_objects["aim2"])
        c.delete(game_objects["aim"])
        c.delete(game_objects["cannon_green"])
        c.delete(game_objects["cannon_blue"])
        c.delete(game_objects["cannon_red"])
        c.delete(game_objects["selected1"])
        c.delete(game_objects["selected2"])
        c.delete(game_objects["selected3"])
        c.delete(game_objects["hp5"])
        c.delete(game_objects["hp4"])
        c.delete(game_objects["hp3"])
        c.delete(game_objects["hp2"])
        c.delete(game_objects["hp"])
        if "life1" in black_life:
            c.delete(black_life["life1"])
        if "life2" in black_life:
            c.delete(black_life["life2"])
        if "life3" in black_life:
            c.delete(black_life["life3"])
        if "life4" in black_life:
            c.delete(black_life["life4"])
        if "life5" in black_life:
            c.delete(black_life["life5"])
        c.delete(game_objects["dead_line"])
        for block in blocks[:]:
            delete_block(block)
        for bullet in bullets[:]:
            delete_bullet(bullet.image)
            bullets.remove(bullet)
    if station == "menu2":
        is_playing = False
        time0 = 0
        draw_menu2()

    if is_playing:
        if frame % time2 == 0:
            x, y = c.coords(game_objects["aim2"])
            if y < 600:
                c.move(game_objects["aim2"], 0, vy)
                c.move(game_objects["aim"], 0, vy)
            x = 30
            for _ in range(9):
                cc = random.choice(list(color))
                block1 = Block(c, c.create_image(x, -136, image=color[cc], anchor=NW), cc, True)
                x += 136
                blocks.append(block1)
            for i in blocks:
                res1 = i.image
                c.tag_raise(game_objects["aim2"], res1)
                c.move(res1, 0, vy)
            for j in bullets:
                j.ty += vy

        for i in bullets:
            s = (i.tx - i.x) ** 2 + (i.y - i.ty) ** 2
            s2 = math.sqrt(s)
            coef = 1600 / (s2 + 0.000000000000000000000000001)
            dy = -int((i.y - i.ty)) * coef
            c.move(i.image, int((i.tx - i.x) * coef), dy)
            if s2 < 1600:
                c.coords(i.image, i.tx, i.ty)
            for block in blocks:
                if i.tx == block.x and i.ty == block.y and same_color(i, block):
                    block.is_bullet = False

        for block in blocks[:]:
            if block.y + 136 > 820:
                flag = "False"
        c.tag_raise("down")
        c.tag_raise("down2")
        if life == 5:
            c.tag_raise(game_objects["aim2"], game_objects["aim2"])
        if time5 != 0 and flag15:
            time5 -= 5
        if time5 == 0:
            c.tag_raise(game_objects["aim2"], game_objects["aim"])
            flag15 = False
            time5 = 50



        if time4 == 1000:
            t += 1
            time4 = 0
            a = a + (a * (t / 6000))
        for bullet in bullets[:]:
            if not bullet.is_finished():
                continue
            for block in blocks[:]:
                if bullet_intersects_block(bullet, block):
                    if not same_color(bullet, block):
                        life_funk()
                        block.is_bullet = True
                        bullets.remove(bullet)
                        delete_bullet(bullet.image)
                        break
                    else:
                        if block not in should_delete:
                            should_delete.append(block)
                            counter.append(block)
                        bullets.remove(bullet)
                        delete_bullet(bullet.image)
                        break

        while len(should_delete) != 0:
            for block in should_delete[:]:
                for neightboor in blocks[:]:
                    if is_neightboor(block, neightboor) and same_color(block, neightboor):
                        if neightboor not in should_delete and neightboor not in neightboor2:
                            neightboor2.append(neightboor)
                            counter.append(neightboor)
                cor.append({"x": block.x, "y": block.y})
                delete_block(block)
                rand = random.randint(100, 501)
                (len(counter))
                count += rand
                count3 += rand
                count4 += rand
                count5 += rand
                list_count.append(rand)
                for i in range(len(list_count)):
                    count2 += list_count[i]
                    if len(counter) >= 4:
                        count -= sum(list_count[0:3])
                        count2 -= sum(list_count[0:3])
                    list_count.remove(list_count[i])
                if count2 >= a:
                    count2 = 0
                    time2 -= 400

            should_delete = neightboor2
            neightboor2 = []
        if 4 <= len(counter) <= 7:
            count3 *= 1.5
            count += count3
            count2 += count3
            bonus.append({"bonus": c.create_image(cor[0]["x"], cor[0]["y"] + 40, image=images["1.5x"], anchor=NW),
                          "time": time.time()})
        if 8 <= len(counter) <= 10:
            count4 *= 2
            count += count4
            count2 += count4
            bonus.append({"bonus": c.create_image(cor[0]["x"], cor[0]["y"] + 40, image=images["2x"], anchor=NW),
                          "time": time.time()})
        if len(counter) >= 11:
            count5 *= 3
            count += count5
            count2 += count5
            bonus.append({"bonus": c.create_image(cor[0]["x"], cor[0]["y"] + 40, image=images["3x"], anchor=NW),
                          "time": time.time()})

        for k in bonus[:]:
            if time.time() - k["time"] > 3:
                bonus.remove(k)
                delete_bullet(k["bonus"])
            if flag == "False":
                bonus.remove(k)
                delete_bullet(k["bonus"])
        count3 = 0
        count4 = 0
        count5 = 0
        random_var.set(str(count))

        if mxstate == 0:
            c.tag_raise(game_objects["sound"], game_objects["base1"])
        if mxstate == 1:
            c.tag_raise(game_objects["not sound"], game_objects["base1"])

    c.after(20, gameloop)


c.after(20, gameloop)




def Move_aim(key):
    if is_playing:
        x, y = c.coords(game_objects["aim2"])
        if (key.char == "d" or key.char == "D" or key.char == "в" or key.char == "В") and x < 1118:
            c.move(game_objects["aim2"], 136, 0)
            c.move(game_objects["aim"], 136, 0)
        if (key.char == "a" or key.char == "A" or key.char == "ф" or key.char == "Ф") and x > 30:
            c.move(game_objects["aim2"], -136, 0)
            c.move(game_objects["aim"], -136, 0)
        if (key.char == "w" or key.char == "W" or key.char == "ц" or key.char == "Ц") and y > 0:
            c.move(game_objects["aim2"], 0, -136)
            c.move(game_objects["aim"], 0, -136)
        if (key.char == "s" or key.char == "S" or key.char == "ы" or key.char == "Ы") and y < 600:
            c.move(game_objects["aim2"], 0, 136)
            c.move(game_objects["aim"], 0, 136)

def move_aim_down():
    if is_playing:
        c.move(game_objects["aim2"], 0, 136)
        c.move(game_objects["aim"], 0, 136)

def move_aim_left():
    if is_playing:
        c.move(game_objects["aim2"], -136, 0)
        c.move(game_objects["aim"], -136, 0)

def move_aim_right():
    if is_playing:
        c.move(game_objects["aim2"], 136, 0)
        c.move(game_objects["aim"], 136, 0)
def move_aim_up():
    c.move(game_objects["aim2"], 0, -136)
    c.move(game_objects["aim"], 0, -136)



def spawn_bullet(color):
    coordinates_for_color = {
        "red": (1120, 840),
        "green": (75, 800),
        "blue": (630, 770),
    }

    if is_playing:
        for i in blocks:
            x1, y1 = c.coords(game_objects["aim2"])
            x1 += 68
            y1 += 68
            if i.x < x1 <= i.x + 136 and i.y <= y1 <= i.y + 136 and i.is_bullet:
                print(x1, y1, i.y)
                bullet1 = Bullet(c, x1, y1,
                                 c.create_image(*coordinates_for_color[state], image=images[f"bullet_create_{color}"],
                                                anchor=NW), color)
                c.tag_raise(bullet1.image)
                bullets.append(bullet1)


def Move_two_bul(event):
    if is_playing:
        spawn_bullet(state)


tk.bind("<space>", Move_two_bul)



def bullet_intersects_block(bullet, block):
    return block.x < bullet.x + 40 < block.x + 136 and block.y < bullet.y + 20 < bullet.y + 136


def bullet_intersects_block_blue(bullet, block):
    return block.x < bullet.x + 26 < block.x + 136 and block.y < bullet.y + 44 < bullet.y + 136


def bullet_intersects_block_red(bullet, block):
    return block.x < bullet.x < block.x + 136 and block.y < bullet.y < bullet.y + 136


def should_hit(bullet, block):
    x1, y1 = c.coords(bullet.image)

    current_block_img = block.image

    x2, y2 = c.coords(current_block_img)
    if x2 <= x1 < x2 + 136 and y2 <= y1 < y2 + 136:
        return True


def same_color(bullet, block):
    current_bullet = bullet.color
    res2 = block.color
    if res2 == current_bullet:
        return True


def is_neightboor(block, neightboor):
        if abs(neightboor.x - block.x) == 136 and neightboor.y == block.y:
            return True
        if neightboor.x == block.x and abs(neightboor.y - block.y) == 136:
            return True


def life_funk():
    global life, flag, flag15
    life -= 1
    if life == 4:
        black_life["life1"] = c.create_image(325, 960, image=images["black_hp"], tag='down2',
                                             anchor=NW)
        c.tag_raise(game_objects["aim"], game_objects["aim2"])
        flag15 = True
    if life == 3:
        black_life["life2"] = c.create_image(245, 960, image=images["black_hp"], tag='down2',
                                             anchor=NW)
        c.tag_raise(game_objects["aim"], game_objects["aim2"])
        flag15 = True
    if life == 2:
        black_life["life3"] = c.create_image(165, 960, image=images["black_hp"], tag='down2',
                                             anchor=NW)
        c.tag_raise(game_objects["aim"], game_objects["aim2"])
        flag15 = True
    if life == 1:
        black_life["life4"] = c.create_image(85, 960, image=images["black_hp"], tag='down2',
                                             anchor=NW)
        c.tag_raise(game_objects["aim"], game_objects["aim2"])
        flag15 = True
    if life == 0:
        black_life["life5"] = c.create_image(5, 960, image=images["black_hp"], tag='down2',
                                             anchor=NW)
        flag = "False"


def delete_block(block):
    r1 = block.image
    blocks.remove(block)
    c.delete(r1)
    del block


def delete_bullet(bullet):
    b1 = bullet
    del bullet
    c.delete(b1)




def selected_green_cannon(event):
    global state, flag14, flag5, flag6
    if is_playing:
        state = "green"
        c.tag_raise(game_objects["hp4"], game_objects["selected1"])
        c.tag_raise(game_objects["selected1"], game_objects["cannon_green"])
        if "life4" in black_life:
            c.tag_raise(black_life["life4"], game_objects["selected1"])
        flag14 = True
        if flag5:
            c.tag_raise(game_objects["cannon_blue"], game_objects["selected2"])
        if flag6:
            c.tag_lower(game_objects["cannon_red"], game_objects["sound"])
            c.tag_lower(game_objects["cannon_red"], game_objects["not sound"])
            c.tag_raise(game_objects["cannon_red"], game_objects["selected3"])

def selected_blue_cannon(event):
    global state, flag5, flag14, flag6
    if is_playing:
        state = "blue"
        c.tag_raise(game_objects["selected2"], game_objects["cannon_blue"])
        flag5 = True
        if flag14:
            c.tag_raise(game_objects["cannon_green"], game_objects["selected1"])

        if flag6:
            c.tag_lower(game_objects["cannon_red"], game_objects["sound"])
            c.tag_lower(game_objects["cannon_red"], game_objects["not sound"])
            c.tag_raise(game_objects["cannon_red"], game_objects["selected3"])

def selected_red_cannon(event):
    global state, flag5, flag14, flag6
    if is_playing:
        state = "red"
        c.tag_lower(game_objects["selected3"], game_objects["sound"])
        c.tag_lower(game_objects["selected3"], game_objects["not sound"])
        c.tag_raise(game_objects["selected3"], game_objects["cannon_red"])
        flag6 = True
        if flag14:
            c.tag_raise(game_objects["cannon_green"], game_objects["selected1"])
        if flag5:
            c.tag_raise(game_objects["cannon_blue"], game_objects["selected2"])

tk.bind('<Left>', selected_green_cannon)
tk.bind('<Up>', selected_blue_cannon)
tk.bind('<Right>', selected_red_cannon)


def TK_PRESS(key):
    Move_aim(key)


entry2 = ttk.Entry(width=15, font=("Ariel", 20))

tk.bind("<KeyPress>", TK_PRESS)


def invisible(event):
    print("Pausing music")
    pygame.mixer.music.pause()


def ff(event):
    print("resuming music")
    pygame.mixer.music.unpause()



def provoke_sound(event):
    global mxstate
    if 1210 <= event.x <= 1280 and 954 <= event.y <= 1024 and mxstate == 0:
        c.tag_raise(game_objects["sound"], game_objects["not sound"])
        ff(event)
        mxstate = 1
        return
    if 1210 <= event.x <= 1280 and 954 <= event.y <= 1024 and mxstate == 1:
        c.tag_raise(game_objects["not sound"], game_objects["sound"])
        invisible(event)
        mxstate = 0
        return
    if station == "menu":
        click(event)
    if station == "menu2":
        click2(event)


c.bind("<Button-1>", provoke_sound)
tk.bind('<Unmap>', invisible)
tk.bind('<Map>', ff)

lab = Label(tk, text="Счёт:", font=("Comic Sans MS", 25), bg="black", fg="white")
lab.grid(row=0, column=0)
lab2 = Label(tk, textvariable=random_var, font=("Comic Sans MS", 25), fg="black")
lab2.grid(row=0, column=1)

flag30 = True
flag31 = True

class MyControoler(Controller):
    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)
    def on_x_press(self):
        selected_blue_cannon(None)
    def on_square_press(self):
        selected_green_cannon(None)
    def on_circle_press(self):
        selected_red_cannon(None)
    def on_R2_release(self):
        Move_two_bul(None)
    def on_L3_down(self, value):
        global flag30, flag31
        x, y = c.coords(game_objects["aim2"])
        if flag30 and y < 600:
            move_aim_down()
            flag30 = False
    def on_L3_y_at_rest(self):
        global flag30
        flag30 = True
    def on_L3_x_at_rest(self):
        global flag31
        flag31 = True
    def on_L3_left(self, value):
        global flag31
        if flag31:
            move_aim_left()
            flag31 = False
    def on_L3_right(self, value):
        global flag31
        if flag31:
            move_aim_right()
            flag31 = False
    def on_L3_up(self, value):
        global flag30
        if flag30:
            move_aim_up()
            flag30 = False


controller = MyControoler(interface="/dev/input/js0", connecting_using_ds4drv=False)
spam_thread = Thread(target=lambda: controller.listen(timeout=60))
spam_thread.start()
mainloop()