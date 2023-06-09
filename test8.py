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
#from pyPS4Controller.controller import Controller
from threading import Thread

tk = Tk()
style = ttk.Style()
style.configure("BW.TLabel", foreground="white", background="black")
style.map('BW.TLabel', background=[('selected', 'white')], foreground=[('selected', 'black')])
tk.geometry("1024x820")
#tk.attributes("-fullscreen", True)
c = Canvas(tk, width=1024, height=768, bg="white")
c.grid(row=2, columnspan=20)
tk["bg"] = "black"

is_playing = False
is_deleted = False
time0 = 0
vy = 102
count = 0
count2 = 0
life = 30
random_var = StringVar()
blocks = []

color = {"red": ImageTk.PhotoImage(Image.open("images/cannon_red_new.png").resize((108, 102), Image.LANCZOS)),
         "blue": ImageTk.PhotoImage(Image.open("images/blue_new.png").resize((108, 102), Image.LANCZOS)),
         "green": ImageTk.PhotoImage(Image.open("images/green_new.png").resize((108, 102), Image.LANCZOS))}

top_name = ["ShadowBlade", "FrostFury", "Thunderbolt", "Nightshade", "Dragonfire", "Stormbringer", "DarkPhoenix",
            "Steelheart", "IceQueen", "MysticMage", "FlameKnight", "PhantomAssassin", "BloodRaven", "Thunderstorm",
            "Shadowhunter", "SoulReaper", "LunarWraith", "CrimsonBlade", "ElectricSoul", "GoldenEagle", "IronFist",
            "ToxicVenom", "Iceberg", "MysticSorcerer", "Firefly", "PhantomBlade", "Bloodhound", "Thunderboltz",
            "ShadowWarrior", "Frostbite", "CelestialSiren", "Nightcrawler", "EmberKnight", "Frostnova", "Thunderstrike",
            "DarkKnight", "Dragonheart", "SteelStorm", "IceFang", "MysticGoddess", "PhoenixFlame", "PhantomEnigma",
            "Bloodmoon", "ThunderousRoar", "ShadowStalker", "SpectralBlade", "Moonshadow", "Emberfire", "FrostbiteX",
            "DragonBreath", "SteelSavior", "IcePhoenix", "MysticDragon", "PhoenixAshes", "DragonBreath",
            "PhantomGhost", "Bloodseeker", "ThunderboltzZ", "ShadowStorm", "SpectralBlade", "Moonshadow", "Emberfire",
            "FrostbiteX", "ThunderboltzX", "DarkWidow", "SteelSavior", "IcePhoenix", "MysticDragon", "PhoenixAshes",
            "PhantomGhost", "Bloodseeker", "ThunderboltzZ", "ShadowStorm", "CuddlyKitten", "FurryFox", "HappyHamster",
            "BouncyBunny", "DaringDragonfly", "MagicMermaid", "FunkyFrog", "WackyWalrus", "CheekyChipmunk", "SillySeal",
            "PlayfulPenguin", "QuirkyQuetzal", "ZippyZebra", "SpunkySquirrel", "GigglyGorilla", "WigglyWorm", "GigglyGnome",
            "SpunkySquid", "DizzyDolphin", "SillySnake", "ChirpyChicken", "BouncyButterfly", "FurryFerret", "JollyJellyfish",
            "HappyHedgehog", "FunkyFlamingo", "MagicMonkey", "ZanyZebra", "QuirkyQuesadilla", "HilariousHippopotams"
]
with open("users3.txt", "r") as file:
    dell = json.load(file)
for delll in dell:
    top_name.remove(delll["name"])

#----------------------music!!!-----------------------------------------------------------------------------------------
pygame.init()
pygame.mixer.init()

STOPPED_PLAYING = pygame.USEREVENT + 1
pygame.mixer.music.set_endevent(STOPPED_PLAYING)
music = "one"
arr = ["musik/хакатон_1.wav", "musik/3музыка.wav", "musik/4musik.wav", "musik/musik5.wav"]
rand = random.choice(arr)
pygame.mixer.music.load(rand)
pygame.mixer.music.play()
pygame.mixer.music.set_volume(0.1)
arr.remove(str(rand))

#-------------------------------------------------------------------------------------------------------------

#------------------------------------------Background-------------------------------------------------------------------
back_purple_phon = ImageTk.PhotoImage(Image.open("Background/purple.png").resize((1024, 768), Image.LANCZOS))
back_purple_phon2 = c.create_image(0, 0, image=back_purple_phon, anchor=NW)

star1 = ImageTk.PhotoImage(Image.open("Background/star1.png").resize((1024, 768), Image.LANCZOS))
star1_1 = c.create_image(0, 0, image=star1, anchor=NW)
star2 = ImageTk.PhotoImage(Image.open("Background/star2.png").resize((1024, 768), Image.LANCZOS))
star2_1 = c.create_image(0, 0, image=star2, anchor=NW)
star3 = ImageTk.PhotoImage(Image.open("Background/star3.png").resize((1024, 768), Image.LANCZOS))
star3_1 = c.create_image(0, 0, image=star3, anchor=NW)


star1_2 = c.create_image(0, -1024, image=star1, anchor=NW)

star2_2 = c.create_image(0, -1024, image=star2, anchor=NW)

star3_2 = c.create_image(0, -1024, image=star3, anchor=NW)

planet_red = ImageTk.PhotoImage(Image.open("Background/planet_red.png").resize((104, 98), Image.LANCZOS))
planet_red1 = c.create_image(50, 80, image=planet_red, anchor=NW)
planet_green = ImageTk.PhotoImage(Image.open("Background/planet_green.png").resize((56, 53), Image.LANCZOS))
planet_green1 = c.create_image(680, 100, image=planet_green, anchor=NW)
planet_purple_light = ImageTk.PhotoImage(Image.open("Background/planet_purple_light.png").resize((139, 131), Image.LANCZOS))
planet_purple_light1 = c.create_image(1040, 50, image=planet_purple_light, anchor=NW)
planet_purple_dark = ImageTk.PhotoImage(Image.open("Background/planet_purple_dark.png").resize((184, 173), Image.LANCZOS))
planet_purple_dark1 = c.create_image(400, 200, image=planet_purple_dark, anchor=NW)
planet_orange = ImageTk.PhotoImage(Image.open("Background/palnet_orange.png").resize((82, 77), Image.LANCZOS)),
planet_orange1 = c.create_image(500, 760, image=planet_orange, anchor=NW)

sb = ImageTk.PhotoImage(Image.open("Background/хзхзхзхзхзхзхзхзхзхз.png").resize((1024, 768), Image.LANCZOS))
sb1 = c.create_image(0, 0, image=sb, anchor=NW)

planet_green_dark = ImageTk.PhotoImage(Image.open("Background/planet_green_dark.png").resize((224, 210), Image.LANCZOS))
planet_green_dark1 = c.create_image(30, 550, image=planet_green_dark, anchor=NW)
planet_top = ImageTk.PhotoImage(Image.open("Background/planet_top.png").resize((389, 365), Image.LANCZOS)),
planet_top1 = c.create_image(740, 520, image=planet_top, anchor=NW)
vx = 0.04
vx2 = 0.012
vx3 = 0.1
vx4 = 0.12
vx5 = 0.016
vx6 = 0.014
vx7 = 0.2

def Move_star():
    global arr, music
    if len(arr) == 0:
        arr = ["musik/хакатон_1.wav", "3musik/музыка.wav", "musik/4musik.wav", "musik/musik5.wav"]
    for event in pygame.event.get():
        rand = random.choice(arr)
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

    c.after(50, Move_star)


c.after(50, Move_star)

#-----------------------------------------------------------------------------------------------------------------------

images = {
    "base": ImageTk.PhotoImage(Image.open("images/baza.png").resize((1024, 51), Image.LANCZOS)),
    "cannon_create_green": ImageTk.PhotoImage(Image.open("images/new_green.png").resize((108, 120), Image.LANCZOS)),
    "cannon_create_blue": ImageTk.PhotoImage(Image.open("images/new_blue.png").resize((256, 120), Image.LANCZOS)),
    "cannon_create_red": ImageTk.PhotoImage(Image.open("images/new_red.png").resize((123, 117), Image.LANCZOS)),
    "bullet_create_green": ImageTk.PhotoImage(Image.open("images/bullet.png").resize((64, 15), Image.LANCZOS)),
    "bullet_create_blue": ImageTk.PhotoImage(Image.open("images/bullet_blue.png").resize((42, 66), Image.LANCZOS)),
    "bullet_create_red": ImageTk.PhotoImage(Image.open("images/red_bullet.png").resize((74, 11), Image.LANCZOS)),
    "aim": ImageTk.PhotoImage(Image.open("images/aim2.png").resize((108, 102), Image.LANCZOS)),
    "red_aim": ImageTk.PhotoImage(Image.open("images/red_aim.png").resize((108, 102), Image.LANCZOS)),
    "black_hp": ImageTk.PhotoImage(Image.open("images/black_color.png").resize((56, 45), Image.LANCZOS)),
    "red_hp": ImageTk.PhotoImage(Image.open("images/red_color.png").resize((56, 45), Image.LANCZOS)),
    "select_green_cannon": ImageTk.PhotoImage(Image.open("images/yellow_green.png").resize((108, 120), Image.LANCZOS)),
    "select_blue_cannon": ImageTk.PhotoImage(Image.open("images/yellow_blue.png").resize((256, 120), Image.LANCZOS)),
    "select_red_cannon": ImageTk.PhotoImage(Image.open("images/yellow_red.png").resize((123, 117), Image.LANCZOS)),
    "1.5x": ImageTk.PhotoImage(Image.open("images/15x.png").resize((108, 41), Image.LANCZOS)),
    "2x": ImageTk.PhotoImage(Image.open("images/2x.png").resize((69, 41), Image.LANCZOS)),
    "3x": ImageTk.PhotoImage(Image.open("images/3x.png").resize((64, 41), Image.LANCZOS)),
    "sound": ImageTk.PhotoImage(Image.open("images/sound.png").resize((56, 53), Image.LANCZOS)),
    "not sound": ImageTk.PhotoImage(Image.open("images/not_sound.png").resize((56, 53), Image.LANCZOS)),
    "info": ImageTk.PhotoImage(Image.open("images/info3.png").resize((950, 416), Image.LANCZOS)),
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

game_btn = ImageTk.PhotoImage(Image.open("Background/KPNF2945.PNG"))
restart = ImageTk.PhotoImage(Image.open("images/restart.png").resize((630, 107), Image.LANCZOS))
tab_lid = ImageTk.PhotoImage(Image.open("images/tabl_new.png").resize((732, 239), Image.LANCZOS))
NEW_GAME = ImageTk.PhotoImage(Image.open("images/new_game.png").resize((594, 316), Image.LANCZOS))
restart_yel = ImageTk.PhotoImage(Image.open("images/restart_yellow.png").resize((630, 107), Image.LANCZOS))
tab_lid_yel = ImageTk.PhotoImage(Image.open("images/tab_lid_yellow.png").resize((732, 239), Image.LANCZOS))
NEW_GAME_yel = ImageTk.PhotoImage(Image.open("images/new_game_yellow.png").resize((594, 316), Image.LANCZOS))
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
flag16 = False


time2 = 8000
objects = []
station = "menu"
time4 = 0


def clear():
    for object in objects:
        c.delete(object)


def draw_menu():
    if is_playing == False:
        objects.append(c.create_image(55, 420, image=game_btn, anchor=NW))
        objects.append(c.create_image(40, 0, image=images["info"], anchor=NW))

def menn():
    global station, leb, btn4, tree, flag7, btn, lab, lab2, leb2, leb3
    if station == "menu3":
        station = "menu2"
        flag7 = False
        c.config(width=1280, height=1024)
        leb.destroy()
        leb3.destroy()
        btn4.destroy()
        tree.destroy()
        lab = Label(tk, text="Счёт:", font=("Comic Sans MS", 25), bg="black", fg="white")
        lab.grid(row=0, column=0)
        lab2 = Label(tk, textvariable=random_var, font=("Comic Sans MS", 25), fg="black")
        lab2.grid(row=0, column=1)

def draw_menu2():
    global station, leb, leb2, num, btn4, lab, lab2, leb3, one, two, th, notone, nottwo, noth, f6, f7, f8
    if not is_playing:
        one = c.create_image(195, 35, image=restart_yel, anchor=NW)
        two = c.create_image(150, 180, image=tab_lid_yel, anchor=NW)
        th = c.create_image(225, 470, image=NEW_GAME_yel, anchor=NW)
        notone = c.create_image(195, 35, image=restart, anchor=NW)
        nottwo = c.create_image(150, 180, image=tab_lid, anchor=NW)
        noth = c.create_image(225, 470, image=NEW_GAME, anchor=NW)
        objects.append(notone)
        objects.append(nottwo)
        objects.append(noth)
        objects.append(one)
        objects.append(two)
        objects.append(th)
        if f6:
            c.tag_lower(notone)
        if f7:
            c.tag_lower(nottwo)
        if f8:
            c.tag_lower(noth)
        if flag7:
            station = "menu3"
            lab.destroy()
            lab2.destroy()
            leb.grid(row=0, column=1)
            c.config(width=0, height=0)
            tree.grid(row=4, columnspan=20)

            tree.heading("№", text="№", anchor=NW)
            tree.heading("name", text="Имя", anchor=NW)
            tree.heading("count", text="count", anchor=NW)

            tree.column("#1", stretch=NO, width=100)
            tree.column("#2", stretch=NO, width=820)
            tree.column("#3", stretch=NO, width=200)

            clear()


def draw_images():
    game_objects["sound"] = c.create_image(954, 610, image=images["sound"], anchor=NW)
    game_objects["not sound"] = c.create_image(954, 610, image=images["not sound"], anchor=NW)
    game_objects["base1"] = c.create_image(0, 620, image=images["base"], anchor=NW)
    game_objects["aim2"] = c.create_image(30, -102, image=images["aim"], anchor=NW)
    game_objects["aim"] = c.create_image(30, -102, image=images["red_aim"], anchor=NW)
    game_objects["cannon_green"] = c.create_image(40, 510, image=images["cannon_create_green"], anchor=NW)
    game_objects["cannon_blue"] = c.create_image(400, 510, image=images["cannon_create_blue"], anchor=NW)
    game_objects["cannon_red"] = c.create_image(860, 515, image=images["cannon_create_red"], anchor=NW)
    game_objects["selected1"] = c.create_image(40, 510, image=images["select_green_cannon"], anchor=NW)
    game_objects["selected2"] = c.create_image(400, 510, image=images["select_blue_cannon"], anchor=NW)
    game_objects["selected3"] = c.create_image(860, 515, image=images["select_red_cannon"], anchor=NW)
    c.tag_raise(game_objects["cannon_green"])
    c.tag_raise(game_objects["cannon_red"])
    c.tag_raise(game_objects["cannon_blue"])
    c.tag_raise(game_objects["aim2"])
    c.tag_raise(game_objects["base1"])
    c.tag_raise(game_objects["sound"], game_objects["base1"])
    game_objects["hp5"] = c.create_image(5, 620, image=images["red_hp"], tag='down', anchor=NW)
    game_objects["hp4"] = c.create_image(85, 620, image=images["red_hp"], tag='down', anchor=NW)
    game_objects["hp3"] = c.create_image(165, 620, image=images["red_hp"], tag='down', anchor=NW)
    game_objects["hp2"] = c.create_image(245, 620, image=images["red_hp"], tag='down', anchor=NW)
    game_objects["hp"] = c.create_image(325, 620, image=images["red_hp"], tag='down', anchor=NW)
    c.tag_raise(game_objects["hp"])
    c.tag_raise(game_objects["hp2"])
    c.tag_raise(game_objects["hp3"])
    c.tag_raise(game_objects["hp4"])
    c.tag_raise(game_objects["hp5"])
    game_objects["dead_line"] = c.create_line(0, 510, 1280, 510, fill="red", width=2)


def click(event):
    global station, is_playing, time0, flag9, time2, name, is_deleted
    if 70 < event.x < 972 and 420 < event.y < 657 and is_playing == False and station != "menu2":
        clear()
        name = random.choice(top_name)
        print(name)
        flag9 = True
        if station == "menu":
            station = "game"
            draw_images()
        else:
            station = "menu"


def click2(event):
    global station, is_playing, time0, flag, life, tree, flag5, flag6, flag7, flag9, flag10, time4, a, t, tree, leb, entry, btn, num, users, count, count2, tree2, tree3, leb3, flag16, time2, name, btn4, f4, art
    if 195 < event.x < 825 and 35 < event.y < 142 and is_playing == False and station == "menu2":
        clear()
        if station == "menu2":
            life = 5
            time0 = 0
            count = 0
            count2 = 0
            time4 = 0
            a = 15000
            t = 0
            time2 = 8000
            flag = "True"
            station = "game"
            draw_images()
        else:
            station = "menu2"
    if 150 < event.x < 882 and 239 < event.y < 419 and not is_playing and station == "menu2":
        flag7 = True
        f4 = False
        try:
            with open("users3.txt", "r") as file:
                users = json.load(file)
        except:
            users = []

        has_user = False
        for user in users:
            if user["name"] == name and user["count"] > count:
                has_user = True
                print(8)
                break
            if user["name"] == name and user["count"] < count:
                ind = users.index({"name": user["name"], "count": user["count"]})
                print(user["name"])
                users.remove(users[ind])

        if not has_user:
            users.append({"name": name, "count": count})
            users.sort(key=itemgetter('count'), reverse=True)
            art = users.index({"name": name, "count": count})

        with open("users3.txt", "w") as file:
            json.dump(users, file, indent=1)


        num = 0
        leb = Label(tk, text="Топ 100 лучших игроков!", font=("Ariel", 25), foreground="white", background="black")
        leb3 = Label(tk, font=("Ariel", 25), foreground="white", background="black")
        leb3.grid(row=3, column=1)
        btn4 = Button(tk, text="<", command=menn, width=10, height=3, foreground="white", background="black")
        btn4.grid(row=0, column=0)
        tree = ttk.Treeview(columns=columns, show="headings", height=40, style="BW.TLabel")
        scrollbar = ttk.Scrollbar(orient='vertical', command=tree.yview)
        scrollbar.grid(row=4, column=21, sticky=NS)
        tree['yscrollcommand'] = scrollbar.set


        for person in users:
            num += 1
            leb3.configure(text="Твои очки: " + str(count) + '\n' + "! Важно в таблицу сохраняется лучший резульат!" + '\n' + "Твой ник: " + str(name) + '\n' + "Твоё место: " + str(art+1))
            if len(users) >= 101:
                name_old = users[-1]["name"]
                top_name.append(name_old)
                users.remove(users[-1])

            else:
                tree.insert("", END, values=(num, person["name"], person["count"]), tags="tree")
                tree.tag_configure("tree", font=("Ariel", 13))
        if station == "menu3":
            station = "game"
        else:
            station = "menu3"
    if 150 <= event.x <= 882 and 470 <= event.y <= 749:
        station = "menu"
        life = 5
        time0 = 0
        count = 0
        count2 = 0
        time4 = 0
        a = 15000
        t = 0
        time2 = 8000
        flag = "True"
        draw_menu()
        clear()

#  границы, кнопка играть джостиком
def gameloop():
    global station, is_playing, time0
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
    c.after(20, gameloop)


c.after(20, gameloop)


def Move_aim_down():
    global time2
    if is_playing:
        x, y = c.coords(game_objects["aim2"])
        if y < 600:
            c.move(game_objects["aim2"], 0, vy)
            c.move(game_objects["aim"], 0, vy)
    c.after(time2, Move_aim_down)


c.after(time2, Move_aim_down)


def Move_aim(key):
    if is_playing:
        x, y = c.coords(game_objects["aim2"])
        if (key.char == "d" or key.char == "D" or key.char == "в" or key.char == "В") and x < 1118:
            c.move(game_objects["aim2"], 108, 0)
            c.move(game_objects["aim"], 108, 0)
        if (key.char == "a" or key.char == "A" or key.char == "ф" or key.char == "Ф") and x > 30:
            c.move(game_objects["aim2"], -108, 0)
            c.move(game_objects["aim"], -108, 0)
        if (key.char == "w" or key.char == "W" or key.char == "ц" or key.char == "Ц") and y > 0:
            c.move(game_objects["aim2"], 0, -102)
            c.move(game_objects["aim"], 0, -102)
        if (key.char == "s" or key.char == "S" or key.char == "ы" or key.char == "Ы") and y < 600:
            c.move(game_objects["aim2"], 0, 102)
            c.move(game_objects["aim"], 0, 102)

def move_aim_down():
    if is_playing:
        c.move(game_objects["aim2"], 0, 102)
        c.move(game_objects["aim"], 0, 102)

def move_aim_left():
    if is_playing:
        c.move(game_objects["aim2"], -108, 0)
        c.move(game_objects["aim"], -108, 0)

def move_aim_right():
    if is_playing:
        c.move(game_objects["aim2"], 108, 0)
        c.move(game_objects["aim"], 108, 0)
def move_aim_up():
    c.move(game_objects["aim2"], 0, -102)
    c.move(game_objects["aim"], 0, -102)

def spawn_squ():
    global time2
    x = 30
    if is_playing:
        for _ in range(9):
            cc = random.choice(list(color))
            block1 = Block(c, c.create_image(x, -102, image=color[cc], anchor=NW), cc, True)
            x += 108
            blocks.append(block1)
    c.after(time2, spawn_squ)


c.after(time2, spawn_squ)


def Move_squ():
    global vy, time2
    if is_playing:
        for i in blocks:
            res1 = i.image
            c.tag_raise(game_objects["aim2"], res1)
            c.move(res1, 0, vy)
        for j in bullets:
            j.ty += vy
    c.after(time2, Move_squ)


c.after(time2, Move_squ)


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
            if i.x < x1 <= i.x + 108 and i.y <= y1 <= i.y + 102 and i.is_bullet:
                bullet1 = Bullet(c, x1, y1,
                                 c.create_image(*coordinates_for_color[state], image=images[f"bullet_create_{color}"],
                                                anchor=NW), color)
                c.tag_raise(bullet1.image)
                bullets.append(bullet1)


def Move_two_bul(event):
    if is_playing:
        spawn_bullet(state)


tk.bind("<space>", Move_two_bul)


def Move_bullet():
    if is_playing:
        for i in bullets:
            s = (i.tx - i.x) ** 2 + (i.y - i.ty) ** 2
            s2 = math.sqrt(s)
            coef = 3200 / (s2 + 0.000000000000000000000000001)
            dy = -int((i.y - i.ty)) * coef
            c.move(i.image, int((i.tx - i.x) * coef), dy)
            if s2 < 3200:
                c.coords(i.image, i.tx, i.ty)
            for block in blocks:
                if should_hit(i, block) and same_color(i, block):
                    i.is_bullet = False
    c.after(5, Move_bullet)


c.after(5, Move_bullet)


def Layer():
    global time5, flag15, flag, life
    if is_playing:
        for block in blocks[:]:
            if block.y + 102 > 530:
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
    c.after(5, Layer)


c.after(5, Layer)


def bullet_intersects_block(bullet, block):
    return block.x < bullet.x < block.x + 108 and block.y < bullet.y < bullet.y + 102


def should_hit(bullet, block):
    x1, y1 = c.coords(bullet.image)

    current_block_img = block.image

    x2, y2 = c.coords(current_block_img)
    if x2 <= x1 < x2 + 108 and y2 <= y1 < y2 + 102:
        return True


def same_color(bullet, block):
    current_bullet = bullet.color
    res2 = block.color
    if res2 == current_bullet:
        return True


def is_neightboor(block, neightboor):
        if abs(neightboor.x - block.x) == 108 and neightboor.y == block.y:
            return True
        if neightboor.x == block.x and abs(neightboor.y - block.y) == 102:
            return True


def life_funk():
    global life, flag, flag15
    life -= 1
    if life == 24:
        black_life["life1"] = c.create_image(325, 620, image=images["black_hp"], tag='down2',
                                             anchor=NW)
        c.tag_raise(game_objects["aim"], game_objects["aim2"])
        flag15 = True
    if life == 18:
        black_life["life2"] = c.create_image(245, 620, image=images["black_hp"], tag='down2',
                                             anchor=NW)
        c.tag_raise(game_objects["aim"], game_objects["aim2"])
        flag15 = True
    if life == 12:
        black_life["life3"] = c.create_image(165, 620, image=images["black_hp"], tag='down2',
                                             anchor=NW)
        c.tag_raise(game_objects["aim"], game_objects["aim2"])
        flag15 = True
    if life == 6:
        black_life["life4"] = c.create_image(85, 620, image=images["black_hp"], tag='down2',
                                             anchor=NW)
        c.tag_raise(game_objects["aim"], game_objects["aim2"])
        flag15 = True
    if life <= 0:
        black_life["life5"] = c.create_image(5, 620, image=images["black_hp"], tag='down2',
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


count3 = 0
count4 = 0
count5 = 0


def Player():
    global count, time2, time4, a, t, count2, time5, flag15, count3, count4, count5, flag, is_playing
    should_delete = []
    neightboor2 = []
    counter = []
    time4 += 5
    cor = []
    if time4 == 1000:
        t += 1
        time4 = 0
        a = a + (a * (t / 6000))
    if is_playing:
        for bullet in bullets[:]:
            if not bullet.is_finished():
                continue
            for block in blocks[:]:
                if bullet_intersects_block(bullet, block):
                    if not same_color(bullet, block):
                        life_funk()
                        bullets.remove(bullet)
                        delete_bullet(bullet.image)
                        break
                    else:
                        #block.is_bullet = True
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

                # print(" Счет: " + str(count) + '\n', "Теорема времени: " + str(a) + '\n', "Время: " + str(t) +
                #       '\n', "Время игры: " + str(time4) + '\n', "time2: " + str(time2) + '\n',
                #       "----------------------------------")
            should_delete = neightboor2
            neightboor2 = []
        if 4 <= len(counter) <= 7:
            count3 *= 1.5
            count += count3
            count2 += count3
            bonus.append({"bonus": c.create_image(cor[0]["x"], cor[0]["y"] + 40, image=images["1.5x"], anchor=NW), "time": time.time()})
        if 8 <= len(counter) <= 10:
            count4 *= 2
            count += count4
            count2 += count4
            bonus.append({"bonus": c.create_image(cor[0]["x"], cor[0]["y"] + 40, image=images["2x"], anchor=NW), "time": time.time()})
        if len(counter) >= 11:
            count5 *= 3
            count += count5
            count2 += count5
            bonus.append({"bonus": c.create_image(cor[0]["x"], cor[0]["y"] + 40, image=images["3x"], anchor=NW), "time": time.time()})

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

    c.after(5, Player)


c.after(5, Player)


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

def you_lose():
    global is_playing, count, station, life, flag, time0, bonus, entry2, f4
    if flag == "False":
        is_playing = False
        station = "menu2"
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

    c.after(50, you_lose)


c.after(50, you_lose)

tk.bind("<KeyPress>", TK_PRESS)


def provoke_for_time_sound():
    global mxstate
    if is_playing:
        if mxstate == 0:
            c.tag_raise(game_objects["sound"], game_objects["base1"])
            mxstate = 1
            return
        if mxstate == 1:
            c.tag_raise(game_objects["not sound"], game_objects["base1"])
            mxstate = 0
            return
    c.after(5, provoke_for_time_sound)


c.after(5, provoke_for_time_sound)


def invisible(event):
    pygame.mixer.music.pause()


def ff(event):
    pygame.mixer.music.unpause()


mxstate = 0


def provoke_sound(event):
    global mxstate
    if 954 <= event.x <= 1024 and 610 <= event.y <= 680 and mxstate == 0:
        c.tag_raise(game_objects["sound"], game_objects["not sound"])
        ff(event)
        mxstate = 1
        return
    if 954 <= event.x <= 1024 and 610 <= event.y <= 680 and mxstate == 1:
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


def onr(event):
    global f6, f7, f8, one, nottwo, noth, notone, s
    if station == "menu2":
        c.tag_raise(one)
        c.tag_lower(notone, notone)
        s += 1
        f6 = True
        return
        # if f7:
        #     c.tag_raise(nottwo)
        # if f8:
        #     c.tag_raise(noth)

def ont(event):
    global state, f6, f7, f8, two, notone, noth, nottwo, s
    if station == "menu2":
        c.tag_raise(two, nottwo)
        f7 = True
        s += 1
        return
        # if f6:
        #     c.tag_raise(notone)
        #
        # if f8:
        #     c.tag_raise(noth)

def onn(event):
    global f8, f7, f6, th, notone, nottwo, noth, s
    if station == "menu2":
        c.tag_raise(th, noth)
        f8 = True
        s += 1
        return
        # if f6:
        #     c.tag_raise(notone)
        # if f7:
        #     c.tag_raise(nottwo)


def joystick_controller():
    global f, f1, f2, f3, state, one, two, f6, f7, f8, notone, nottwo, noth, s, f9
    pygame.joystick.init()
    f = True
    f1 = True
    clock = pygame.time.Clock()
    f2 = True
    f3 = True
    f6 = True
    f7 = False
    f8 = False
    f9 = True
    r = 0
    s = 1
    while True:
        joystick_count = pygame.joystick.get_count()
        for i in range(joystick_count):
            joystick = pygame.joystick.Joystick(i)
            joystick.init()
            if station != "menu":
                if round(joystick.get_axis(0)) == 1:
                    if f:
                        move_aim_right()
                        f = False
                if round(joystick.get_axis(0)) == -1:
                    if f:
                        move_aim_left()
                        f = False
                if joystick.get_axis(1) > 0:
                    print(s)
                    if f1:
                        move_aim_down()
                        f1 = False
                    if s % 3 == 1 and f9:
                        onr(None)
                        f8 = False
                        f7 = False
                        f9 = False
                        break
                    if s % 3 == 2 and f9:
                        ont(None)
                        f6 = False
                        f8 = False
                        f9 = False
                        break
                    if s % 3 == 0 and f9:
                        onn(None)
                        f7 = False
                        f6 = False
                        f9 = False
                        print(989999999)
                        break
                if round(joystick.get_axis(1)) == 0:
                    f9 = True
                    print(joystick.get_axis(1))

                if round(joystick.get_axis(1)) == -1:
                    if f1:
                        move_aim_up()
                        f1 = False
                if round(joystick.get_axis(0)) == 0:
                    f = True
                if joystick.get_axis(1) == 0:
                    f1 = True
            if joystick.get_button(3) == 1:
                selected_blue_cannon(None)
            if joystick.get_button(1) == 1:
                selected_green_cannon(None)
            if joystick.get_button(4) == 1:
                selected_red_cannon(None)
            if joystick.get_button(0) == 1:
                if f3:
                    try:
                        spawn_bullet(state)
                        #print(22323232323232)
                        f3 = False
                        r += 1
                        continue
                    except:
                        pass
            if joystick.get_button(1) == 0:
                #print(r)
                if r % 1 ==0:
                    f3 = True

        clock.tick(120)
spam_thread = Thread(target=joystick_controller)
spam_thread.start()
mainloop()