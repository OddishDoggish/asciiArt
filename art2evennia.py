import tkinter as tk
from tkinter import *
from functools import partial
from tkinter.filedialog import askopenfilename
import os
import pandas as pd
import numpy as np
from PIL import Image
from PIL import ImageTk


class MainWindow:
    def __init__(self, main):

        main.title("ART 2 EVENNIA")
        """
        Application layout: 
        There will be 3 columns. The first is (colorframe -> colorgrid) for the color grid. The second (text_frame) is
        for the text windows. The third (toolbar) is for the photo (if used) and the command buttons.
        """
        main.rowconfigure(0, minsize=200, weight=1)
        main.columnconfigure(1, minsize=400, weight=1)
        main.columnconfigure(2, minsize=200, weight=1)

        self.colorframe = Frame()
        self.colorgrid = Canvas(self.colorframe)
        self.scroll_color_y = Scrollbar(self.colorgrid, orient=VERTICAL, command=self.colorgrid.yview)
        self.colorgrid.configure(yscrollcommand=self.scroll_color_y.set)
        self.btn000 = Button(self.colorgrid, text="000", fg="white", bg="#000000",
                             command=partial(self.color, "000")).grid(row=0, column=0, sticky="ew", padx=2)
        self.btn100 = Button(self.colorgrid, text="100", fg="white", bg="#5F0000",
                             command=partial(self.color, "100")).grid(row=0, column=1, sticky="ew", padx=2)
        self.btn200 = Button(self.colorgrid, text="200", fg="white", bg="#870000",
                             command=partial(self.color, "200")).grid(row=0, column=2, sticky="ew", padx=2)
        self.btn300 = Button(self.colorgrid, text="300", fg="white", bg="#AF0000",
                             command=partial(self.color, "300")).grid(row=0, column=3, sticky="ew", padx=2)
        self.btn400 = Button(self.colorgrid, text="400", fg="white", bg="#D70000",
                             command=partial(self.color, "400")).grid(row=0, column=4, sticky="ew", padx=2)
        self.btn500 = Button(self.colorgrid, text="500", fg="white", bg="#FF0000",
                             command=partial(self.color, "500")).grid(row=0, column=5, sticky="ew", padx=2)
        self.btn001 = Button(self.colorgrid, text="001", fg="white", bg="#00005F",
                             command=partial(self.color, "001")).grid(row=1, column=0, sticky="ew", padx=2)
        self.btn101 = Button(self.colorgrid, text="101", fg="white", bg="#5F005F",
                             command=partial(self.color, "101")).grid(row=1, column=1, sticky="ew", padx=2)
        self.btn201 = Button(self.colorgrid, text="201", fg="white", bg="#87005F",
                             command=partial(self.color, "201")).grid(row=1, column=2, sticky="ew", padx=2)
        self.btn301 = Button(self.colorgrid, text="301", fg="white", bg="#AF005F",
                             command=partial(self.color, "301")).grid(row=1, column=3, sticky="ew", padx=2)
        self.btn401 = Button(self.colorgrid, text="401", fg="white", bg="#D7005F",
                             command=partial(self.color, "401")).grid(row=1, column=4, sticky="ew", padx=2)
        self.btn501 = Button(self.colorgrid, text="501", fg="white", bg="#FF005F",
                             command=partial(self.color, "501")).grid(row=1, column=5, sticky="ew", padx=2)
        self.btn002 = Button(self.colorgrid, text="002", fg="white", bg="#000087",
                             command=partial(self.color, "002")).grid(row=2, column=0, sticky="ew", padx=2)
        self.btn102 = Button(self.colorgrid, text="102", fg="white", bg="#5F0087",
                             command=partial(self.color, "102")).grid(row=2, column=1, sticky="ew", padx=2)
        self.btn202 = Button(self.colorgrid, text="202", fg="white", bg="#870087",
                             command=partial(self.color, "202")).grid(row=2, column=2, sticky="ew", padx=2)
        self.btn302 = Button(self.colorgrid, text="302", fg="white", bg="#AF0087",
                             command=partial(self.color, "302")).grid(row=2, column=3, sticky="ew", padx=2)
        self.btn402 = Button(self.colorgrid, text="402", fg="white", bg="#D70087",
                             command=partial(self.color, "402")).grid(row=2, column=4, sticky="ew", padx=2)
        self.btn502 = Button(self.colorgrid, text="502", fg="white", bg="#FF0087",
                             command=partial(self.color, "502")).grid(row=2, column=5, sticky="ew", padx=2)
        self.btn003 = Button(self.colorgrid, text="003", fg="white", bg="#0000AF",
                             command=partial(self.color, "003")).grid(row=3, column=0, sticky="ew", padx=2)
        self.btn103 = Button(self.colorgrid, text="103", fg="white", bg="#5F00AF",
                             command=partial(self.color, "103")).grid(row=3, column=1, sticky="ew", padx=2)
        self.btn203 = Button(self.colorgrid, text="203", fg="white", bg="#8700AF",
                             command=partial(self.color, "203")).grid(row=3, column=2, sticky="ew", padx=2)
        self.btn303 = Button(self.colorgrid, text="303", fg="white", bg="#AF00AF",
                             command=partial(self.color, "303")).grid(row=3, column=3, sticky="ew", padx=2)
        self.btn403 = Button(self.colorgrid, text="403", fg="white", bg="#D700AF",
                             command=partial(self.color, "403")).grid(row=3, column=4, sticky="ew", padx=2)
        self.btn503 = Button(self.colorgrid, text="503", fg="white", bg="#FF00AF",
                             command=partial(self.color, "503")).grid(row=3, column=5, sticky="ew", padx=2)
        self.btn004 = Button(self.colorgrid, text="004", fg="white", bg="#0000D7",
                             command=partial(self.color, "004")).grid(row=4, column=0, sticky="ew", padx=2)
        self.btn104 = Button(self.colorgrid, text="104", fg="white", bg="#5F00D7",
                             command=partial(self.color, "104")).grid(row=4, column=1, sticky="ew", padx=2)
        self.btn204 = Button(self.colorgrid, text="204", fg="white", bg="#8700D7",
                             command=partial(self.color, "204")).grid(row=4, column=2, sticky="ew", padx=2)
        self.btn304 = Button(self.colorgrid, text="304", fg="white", bg="#AF00D7",
                             command=partial(self.color, "304")).grid(row=4, column=3, sticky="ew", padx=2)
        self.btn404 = Button(self.colorgrid, text="404", fg="white", bg="#D700D7",
                             command=partial(self.color, "404")).grid(row=4, column=4, sticky="ew", padx=2)
        self.btn504 = Button(self.colorgrid, text="504", fg="white", bg="#FF00D7",
                             command=partial(self.color, "504")).grid(row=4, column=5, sticky="ew", padx=2)
        self.btn005 = Button(self.colorgrid, text="005", fg="white", bg="#0000FF",
                             command=partial(self.color, "005")).grid(row=5, column=0, sticky="ew", padx=2)
        self.btn105 = Button(self.colorgrid, text="105", fg="white", bg="#5F00FF",
                             command=partial(self.color, "105")).grid(row=5, column=1, sticky="ew", padx=2)
        self.btn205 = Button(self.colorgrid, text="205", fg="white", bg="#8700FF",
                             command=partial(self.color, "205")).grid(row=5, column=2, sticky="ew", padx=2)
        self.btn305 = Button(self.colorgrid, text="305", fg="white", bg="#AF00FF",
                             command=partial(self.color, "305")).grid(row=5, column=3, sticky="ew", padx=2)
        self.btn405 = Button(self.colorgrid, text="405", fg="white", bg="#D700FF",
                             command=partial(self.color, "405")).grid(row=5, column=4, sticky="ew", padx=2)
        self.btn505 = Button(self.colorgrid, text="505", fg="white", bg="#FF00FF",
                             command=partial(self.color, "505")).grid(row=5, column=5, sticky="ew", padx=2)
        self.btn010 = Button(self.colorgrid, text="010", fg="white", bg="#005F00",
                             command=partial(self.color, "010")).grid(row=6, column=0, sticky="ew", padx=2)
        self.btn110 = Button(self.colorgrid, text="110", fg="white", bg="#5F5F00",
                             command=partial(self.color, "110")).grid(row=6, column=1, sticky="ew", padx=2)
        self.btn210 = Button(self.colorgrid, text="210", fg="white", bg="#875F00",
                             command=partial(self.color, "210")).grid(row=6, column=2, sticky="ew", padx=2)
        self.btn310 = Button(self.colorgrid, text="310", fg="white", bg="#AF5F00",
                             command=partial(self.color, "310")).grid(row=6, column=3, sticky="ew", padx=2)
        self.btn410 = Button(self.colorgrid, text="410", fg="white", bg="#D75F00",
                             command=partial(self.color, "410")).grid(row=6, column=4, sticky="ew", padx=2)
        self.btn510 = Button(self.colorgrid, text="510", fg="white", bg="#FF5F00",
                             command=partial(self.color, "510")).grid(row=6, column=5, sticky="ew", padx=2)
        self.btn011 = Button(self.colorgrid, text="011", fg="white", bg="#005F5F",
                             command=partial(self.color, "011")).grid(row=7, column=0, sticky="ew", padx=2)
        self.btn111 = Button(self.colorgrid, text="111", fg="white", bg="#5F5F5F",
                             command=partial(self.color, "111")).grid(row=7, column=1, sticky="ew", padx=2)
        self.btn211 = Button(self.colorgrid, text="211", fg="white", bg="#875F5F",
                             command=partial(self.color, "211")).grid(row=7, column=2, sticky="ew", padx=2)
        self.btn311 = Button(self.colorgrid, text="311", fg="white", bg="#AF5F5F",
                             command=partial(self.color, "311")).grid(row=7, column=3, sticky="ew", padx=2)
        self.btn411 = Button(self.colorgrid, text="411", fg="white", bg="#D75F5F",
                             command=partial(self.color, "411")).grid(row=7, column=4, sticky="ew", padx=2)
        self.btn511 = Button(self.colorgrid, text="511", fg="white", bg="#FF5F5F",
                             command=partial(self.color, "511")).grid(row=7, column=5, sticky="ew", padx=2)
        self.btn012 = Button(self.colorgrid, text="012", fg="white", bg="#005F87",
                             command=partial(self.color, "012")).grid(row=8, column=0, sticky="ew", padx=2)
        self.btn112 = Button(self.colorgrid, text="112", fg="white", bg="#5F5F87",
                             command=partial(self.color, "112")).grid(row=8, column=1, sticky="ew", padx=2)
        self.btn212 = Button(self.colorgrid, text="212", fg="white", bg="#875F87",
                             command=partial(self.color, "212")).grid(row=8, column=2, sticky="ew", padx=2)
        self.btn312 = Button(self.colorgrid, text="312", fg="white", bg="#AF5F87",
                             command=partial(self.color, "312")).grid(row=8, column=3, sticky="ew", padx=2)
        self.btn412 = Button(self.colorgrid, text="412", fg="white", bg="#D75F87",
                             command=partial(self.color, "412")).grid(row=8, column=4, sticky="ew", padx=2)
        self.btn512 = Button(self.colorgrid, text="512", fg="white", bg="#FF5F87",
                             command=partial(self.color, "512")).grid(row=8, column=5, sticky="ew", padx=2)
        self.btn013 = Button(self.colorgrid, text="013", fg="white", bg="#005FAF",
                             command=partial(self.color, "013")).grid(row=9, column=0, sticky="ew", padx=2)
        self.btn113 = Button(self.colorgrid, text="113", fg="white", bg="#5F5FAF",
                             command=partial(self.color, "113")).grid(row=9, column=1, sticky="ew", padx=2)
        self.btn213 = Button(self.colorgrid, text="213", fg="white", bg="#875FAF",
                             command=partial(self.color, "213")).grid(row=9, column=2, sticky="ew", padx=2)
        self.btn313 = Button(self.colorgrid, text="313", fg="white", bg="#AF5FAF",
                             command=partial(self.color, "313")).grid(row=9, column=3, sticky="ew", padx=2)
        self.btn413 = Button(self.colorgrid, text="413", fg="white", bg="#D75FAF",
                             command=partial(self.color, "413")).grid(row=9, column=4, sticky="ew", padx=2)
        self.btn513 = Button(self.colorgrid, text="513", fg="white", bg="#FF5FAF",
                             command=partial(self.color, "513")).grid(row=9, column=5, sticky="ew", padx=2)
        self.btn014 = Button(self.colorgrid, text="014", fg="white", bg="#005FD7",
                             command=partial(self.color, "014")).grid(row=10, column=0, sticky="ew", padx=2)
        self.btn114 = Button(self.colorgrid, text="114", fg="white", bg="#5F5FD7",
                             command=partial(self.color, "114")).grid(row=10, column=1, sticky="ew", padx=2)
        self.btn214 = Button(self.colorgrid, text="214", fg="white", bg="#875FD7",
                             command=partial(self.color, "214")).grid(row=10, column=2, sticky="ew", padx=2)
        self.btn314 = Button(self.colorgrid, text="314", fg="white", bg="#AF5FD7",
                             command=partial(self.color, "314")).grid(row=10, column=3, sticky="ew", padx=2)
        self.btn414 = Button(self.colorgrid, text="414", fg="white", bg="#D75FD7",
                             command=partial(self.color, "414")).grid(row=10, column=4, sticky="ew", padx=2)
        self.btn514 = Button(self.colorgrid, text="514", fg="white", bg="#FF5FD7",
                             command=partial(self.color, "514")).grid(row=10, column=5, sticky="ew", padx=2)
        self.btn015 = Button(self.colorgrid, text="015", fg="white", bg="#005FFF",
                             command=partial(self.color, "015")).grid(row=11, column=0, sticky="ew", padx=2)
        self.btn115 = Button(self.colorgrid, text="115", fg="white", bg="#5F5FFF",
                             command=partial(self.color, "115")).grid(row=11, column=1, sticky="ew", padx=2)
        self.btn215 = Button(self.colorgrid, text="215", fg="white", bg="#875FFF",
                             command=partial(self.color, "215")).grid(row=11, column=2, sticky="ew", padx=2)
        self.btn315 = Button(self.colorgrid, text="315", fg="white", bg="#AF5FFF",
                             command=partial(self.color, "315")).grid(row=11, column=3, sticky="ew", padx=2)
        self.btn415 = Button(self.colorgrid, text="415", fg="white", bg="#D75FFF",
                             command=partial(self.color, "415")).grid(row=11, column=4, sticky="ew", padx=2)
        self.btn515 = Button(self.colorgrid, text="515", fg="white", bg="#FF5FFF",
                             command=partial(self.color, "515")).grid(row=11, column=5, sticky="ew", padx=2)
        self.btn020 = Button(self.colorgrid, text="020", fg="white", bg="#008700",
                             command=partial(self.color, "020")).grid(row=12, column=0, sticky="ew", padx=2)
        self.btn120 = Button(self.colorgrid, text="120", fg="white", bg="#5F8700",
                             command=partial(self.color, "120")).grid(row=12, column=1, sticky="ew", padx=2)
        self.btn220 = Button(self.colorgrid, text="220", fg="white", bg="#878700",
                             command=partial(self.color, "220")).grid(row=12, column=2, sticky="ew", padx=2)
        self.btn320 = Button(self.colorgrid, text="320", fg="white", bg="#AF8700",
                             command=partial(self.color, "320")).grid(row=12, column=3, sticky="ew", padx=2)
        self.btn420 = Button(self.colorgrid, text="420", fg="white", bg="#D78700",
                             command=partial(self.color, "420")).grid(row=12, column=4, sticky="ew", padx=2)
        self.btn520 = Button(self.colorgrid, text="520", fg="white", bg="#FF8700",
                             command=partial(self.color, "520")).grid(row=12, column=5, sticky="ew", padx=2)
        self.btn021 = Button(self.colorgrid, text="021", fg="white", bg="#00875F",
                             command=partial(self.color, "021")).grid(row=13, column=0, sticky="ew", padx=2)
        self.btn121 = Button(self.colorgrid, text="121", fg="white", bg="#5F875F",
                             command=partial(self.color, "121")).grid(row=13, column=1, sticky="ew", padx=2)
        self.btn221 = Button(self.colorgrid, text="221", fg="white", bg="#87875F",
                             command=partial(self.color, "221")).grid(row=13, column=2, sticky="ew", padx=2)
        self.btn321 = Button(self.colorgrid, text="321", fg="white", bg="#AF875F",
                             command=partial(self.color, "321")).grid(row=13, column=3, sticky="ew", padx=2)
        self.btn421 = Button(self.colorgrid, text="421", fg="white", bg="#D7875F",
                             command=partial(self.color, "421")).grid(row=13, column=4, sticky="ew", padx=2)
        self.btn521 = Button(self.colorgrid, text="521", fg="white", bg="#FF875F",
                             command=partial(self.color, "521")).grid(row=13, column=5, sticky="ew", padx=2)
        self.btn022 = Button(self.colorgrid, text="022", fg="white", bg="#008787",
                             command=partial(self.color, "022")).grid(row=14, column=0, sticky="ew", padx=2)
        self.btn122 = Button(self.colorgrid, text="122", fg="white", bg="#5F8787",
                             command=partial(self.color, "122")).grid(row=14, column=1, sticky="ew", padx=2)
        self.btn222 = Button(self.colorgrid, text="222", fg="white", bg="#878787",
                             command=partial(self.color, "222")).grid(row=14, column=2, sticky="ew", padx=2)
        self.btn322 = Button(self.colorgrid, text="322", fg="white", bg="#AF8787",
                             command=partial(self.color, "322")).grid(row=14, column=3, sticky="ew", padx=2)
        self.btn422 = Button(self.colorgrid, text="422", fg="white", bg="#D78787",
                             command=partial(self.color, "422")).grid(row=14, column=4, sticky="ew", padx=2)
        self.btn522 = Button(self.colorgrid, text="522", fg="white", bg="#FF8787",
                             command=partial(self.color, "522")).grid(row=14, column=5, sticky="ew", padx=2)
        self.btn023 = Button(self.colorgrid, text="023", fg="white", bg="#0087AF",
                             command=partial(self.color, "023")).grid(row=15, column=0, sticky="ew", padx=2)
        self.btn123 = Button(self.colorgrid, text="123", fg="white", bg="#5F87AF",
                             command=partial(self.color, "123")).grid(row=15, column=1, sticky="ew", padx=2)
        self.btn223 = Button(self.colorgrid, text="223", fg="white", bg="#8787AF",
                             command=partial(self.color, "223")).grid(row=15, column=2, sticky="ew", padx=2)
        self.btn323 = Button(self.colorgrid, text="323", fg="white", bg="#AF87AF",
                             command=partial(self.color, "323")).grid(row=15, column=3, sticky="ew", padx=2)
        self.btn423 = Button(self.colorgrid, text="423", fg="white", bg="#D787AF",
                             command=partial(self.color, "423")).grid(row=15, column=4, sticky="ew", padx=2)
        self.btn523 = Button(self.colorgrid, text="523", fg="white", bg="#FF87AF",
                             command=partial(self.color, "523")).grid(row=15, column=5, sticky="ew", padx=2)
        self.btn024 = Button(self.colorgrid, text="024", fg="white", bg="#0087D7",
                             command=partial(self.color, "024")).grid(row=16, column=0, sticky="ew", padx=2)
        self.btn124 = Button(self.colorgrid, text="124", fg="white", bg="#5F87D7",
                             command=partial(self.color, "124")).grid(row=16, column=1, sticky="ew", padx=2)
        self.btn224 = Button(self.colorgrid, text="224", fg="white", bg="#8787D7",
                             command=partial(self.color, "224")).grid(row=16, column=2, sticky="ew", padx=2)
        self.btn324 = Button(self.colorgrid, text="324", fg="white", bg="#AF87D7",
                             command=partial(self.color, "324")).grid(row=16, column=3, sticky="ew", padx=2)
        self.btn424 = Button(self.colorgrid, text="424", fg="white", bg="#D787D7",
                             command=partial(self.color, "424")).grid(row=16, column=4, sticky="ew", padx=2)
        self.btn524 = Button(self.colorgrid, text="524", fg="white", bg="#FF87D7",
                             command=partial(self.color, "524")).grid(row=16, column=5, sticky="ew", padx=2)
        self.btn025 = Button(self.colorgrid, text="025", fg="white", bg="#0087FF",
                             command=partial(self.color, "025")).grid(row=17, column=0, sticky="ew", padx=2)
        self.btn125 = Button(self.colorgrid, text="125", fg="white", bg="#5F87FF",
                             command=partial(self.color, "125")).grid(row=17, column=1, sticky="ew", padx=2)
        self.btn225 = Button(self.colorgrid, text="225", fg="white", bg="#8787FF",
                             command=partial(self.color, "225")).grid(row=17, column=2, sticky="ew", padx=2)
        self.btn325 = Button(self.colorgrid, text="325", fg="white", bg="#AF87FF",
                             command=partial(self.color, "325")).grid(row=17, column=3, sticky="ew", padx=2)
        self.btn425 = Button(self.colorgrid, text="425", fg="white", bg="#D787FF",
                             command=partial(self.color, "425")).grid(row=17, column=4, sticky="ew", padx=2)
        self.btn525 = Button(self.colorgrid, text="525", fg="white", bg="#FF87FF",
                             command=partial(self.color, "525")).grid(row=17, column=5, sticky="ew", padx=2)
        self.btn030 = Button(self.colorgrid, text="030", fg="white", bg="#00AF00",
                             command=partial(self.color, "030")).grid(row=18, column=0, sticky="ew", padx=2)
        self.btn130 = Button(self.colorgrid, text="130", fg="white", bg="#5FAF00",
                             command=partial(self.color, "130")).grid(row=18, column=1, sticky="ew", padx=2)
        self.btn230 = Button(self.colorgrid, text="230", fg="white", bg="#87AF00",
                             command=partial(self.color, "230")).grid(row=18, column=2, sticky="ew", padx=2)
        self.btn330 = Button(self.colorgrid, text="330", fg="white", bg="#AFAF00",
                             command=partial(self.color, "330")).grid(row=18, column=3, sticky="ew", padx=2)
        self.btn430 = Button(self.colorgrid, text="430", fg="white", bg="#D7AF00",
                             command=partial(self.color, "430")).grid(row=18, column=4, sticky="ew", padx=2)
        self.btn530 = Button(self.colorgrid, text="530", fg="white", bg="#FFAF00",
                             command=partial(self.color, "530")).grid(row=18, column=5, sticky="ew", padx=2)
        self.btn031 = Button(self.colorgrid, text="031", fg="white", bg="#00AF5F",
                             command=partial(self.color, "031")).grid(row=19, column=0, sticky="ew", padx=2)
        self.btn131 = Button(self.colorgrid, text="131", fg="white", bg="#5FAF5F",
                             command=partial(self.color, "131")).grid(row=19, column=1, sticky="ew", padx=2)
        self.btn231 = Button(self.colorgrid, text="231", fg="white", bg="#87AF5F",
                             command=partial(self.color, "231")).grid(row=19, column=2, sticky="ew", padx=2)
        self.btn331 = Button(self.colorgrid, text="331", fg="white", bg="#AFAF5F",
                             command=partial(self.color, "331")).grid(row=19, column=3, sticky="ew", padx=2)
        self.btn431 = Button(self.colorgrid, text="431", fg="white", bg="#D7AF5F",
                             command=partial(self.color, "431")).grid(row=19, column=4, sticky="ew", padx=2)
        self.btn531 = Button(self.colorgrid, text="531", fg="white", bg="#FFAF5F",
                             command=partial(self.color, "531")).grid(row=19, column=5, sticky="ew", padx=2)
        self.btn032 = Button(self.colorgrid, text="032", fg="white", bg="#00AF87",
                             command=partial(self.color, "032")).grid(row=20, column=0, sticky="ew", padx=2)
        self.btn132 = Button(self.colorgrid, text="132", fg="white", bg="#5FAF87",
                             command=partial(self.color, "132")).grid(row=20, column=1, sticky="ew", padx=2)
        self.btn232 = Button(self.colorgrid, text="232", fg="white", bg="#87AF87",
                             command=partial(self.color, "232")).grid(row=20, column=2, sticky="ew", padx=2)
        self.btn332 = Button(self.colorgrid, text="332", fg="white", bg="#AFAF87",
                             command=partial(self.color, "332")).grid(row=20, column=3, sticky="ew", padx=2)
        self.btn432 = Button(self.colorgrid, text="432", fg="white", bg="#D7AF87",
                             command=partial(self.color, "432")).grid(row=20, column=4, sticky="ew", padx=2)
        self.btn532 = Button(self.colorgrid, text="532", fg="white", bg="#FFAF87",
                             command=partial(self.color, "532")).grid(row=20, column=5, sticky="ew", padx=2)
        self.btn033 = Button(self.colorgrid, text="033", fg="white", bg="#00AFAF",
                             command=partial(self.color, "033")).grid(row=21, column=0, sticky="ew", padx=2)
        self.btn133 = Button(self.colorgrid, text="133", fg="white", bg="#5FAFAF",
                             command=partial(self.color, "133")).grid(row=21, column=1, sticky="ew", padx=2)
        self.btn233 = Button(self.colorgrid, text="233", fg="white", bg="#87AFAF",
                             command=partial(self.color, "233")).grid(row=21, column=2, sticky="ew", padx=2)
        self.btn333 = Button(self.colorgrid, text="333", fg="white", bg="#AFAFAF",
                             command=partial(self.color, "333")).grid(row=21, column=3, sticky="ew", padx=2)
        self.btn433 = Button(self.colorgrid, text="433", fg="white", bg="#D7AFAF",
                             command=partial(self.color, "433")).grid(row=21, column=4, sticky="ew", padx=2)
        self.btn533 = Button(self.colorgrid, text="533", fg="white", bg="#FFAFAF",
                             command=partial(self.color, "533")).grid(row=21, column=5, sticky="ew", padx=2)
        self.btn034 = Button(self.colorgrid, text="034", fg="white", bg="#00AFD7",
                             command=partial(self.color, "034")).grid(row=22, column=0, sticky="ew", padx=2)
        self.btn134 = Button(self.colorgrid, text="134", fg="white", bg="#5FAFD7",
                             command=partial(self.color, "134")).grid(row=22, column=1, sticky="ew", padx=2)
        self.btn234 = Button(self.colorgrid, text="234", fg="white", bg="#87AFD7",
                             command=partial(self.color, "234")).grid(row=22, column=2, sticky="ew", padx=2)
        self.btn334 = Button(self.colorgrid, text="334", fg="white", bg="#AFAFD7",
                             command=partial(self.color, "334")).grid(row=22, column=3, sticky="ew", padx=2)
        self.btn434 = Button(self.colorgrid, text="434", fg="white", bg="#D7AFD7",
                             command=partial(self.color, "434")).grid(row=22, column=4, sticky="ew", padx=2)
        self.btn534 = Button(self.colorgrid, text="534", fg="white", bg="#FFAFD7",
                             command=partial(self.color, "534")).grid(row=22, column=5, sticky="ew", padx=2)
        self.btn035 = Button(self.colorgrid, text="035", fg="white", bg="#00AFFF",
                             command=partial(self.color, "035")).grid(row=23, column=0, sticky="ew", padx=2)
        self.btn135 = Button(self.colorgrid, text="135", fg="white", bg="#5FAFFF",
                             command=partial(self.color, "135")).grid(row=23, column=1, sticky="ew", padx=2)
        self.btn235 = Button(self.colorgrid, text="235", fg="white", bg="#87AFFF",
                             command=partial(self.color, "235")).grid(row=23, column=2, sticky="ew", padx=2)
        self.btn335 = Button(self.colorgrid, text="335", fg="white", bg="#AFAFFF",
                             command=partial(self.color, "335")).grid(row=23, column=3, sticky="ew", padx=2)
        self.btn435 = Button(self.colorgrid, text="435", fg="white", bg="#D7AFFF",
                             command=partial(self.color, "435")).grid(row=23, column=4, sticky="ew", padx=2)
        self.btn535 = Button(self.colorgrid, text="535", fg="white", bg="#FFAFFF",
                             command=partial(self.color, "535")).grid(row=23, column=5, sticky="ew", padx=2)
        self.btn040 = Button(self.colorgrid, text="040", fg="white", bg="#00D700",
                             command=partial(self.color, "040")).grid(row=24, column=0, sticky="ew", padx=2)
        self.btn140 = Button(self.colorgrid, text="140", fg="white", bg="#5FD700",
                             command=partial(self.color, "140")).grid(row=24, column=1, sticky="ew", padx=2)
        self.btn240 = Button(self.colorgrid, text="240", fg="white", bg="#87D700",
                             command=partial(self.color, "240")).grid(row=24, column=2, sticky="ew", padx=2)
        self.btn340 = Button(self.colorgrid, text="340", fg="white", bg="#AFD700",
                             command=partial(self.color, "340")).grid(row=24, column=3, sticky="ew", padx=2)
        self.btn440 = Button(self.colorgrid, text="440", fg="white", bg="#D7D700",
                             command=partial(self.color, "440")).grid(row=24, column=4, sticky="ew", padx=2)
        self.btn540 = Button(self.colorgrid, text="540", fg="white", bg="#FFD700",
                             command=partial(self.color, "540")).grid(row=24, column=5, sticky="ew", padx=2)
        self.btn041 = Button(self.colorgrid, text="041", fg="white", bg="#00D75F",
                             command=partial(self.color, "041")).grid(row=25, column=0, sticky="ew", padx=2)
        self.btn141 = Button(self.colorgrid, text="141", fg="white", bg="#5FD75F",
                             command=partial(self.color, "141")).grid(row=25, column=1, sticky="ew", padx=2)
        self.btn241 = Button(self.colorgrid, text="241", fg="white", bg="#87D75F",
                             command=partial(self.color, "241")).grid(row=25, column=2, sticky="ew", padx=2)
        self.btn341 = Button(self.colorgrid, text="341", fg="white", bg="#AFD75F",
                             command=partial(self.color, "341")).grid(row=25, column=3, sticky="ew", padx=2)
        self.btn441 = Button(self.colorgrid, text="441", fg="white", bg="#D7D75F",
                             command=partial(self.color, "441")).grid(row=25, column=4, sticky="ew", padx=2)
        self.btn541 = Button(self.colorgrid, text="541", fg="white", bg="#FFD75F",
                             command=partial(self.color, "541")).grid(row=25, column=5, sticky="ew", padx=2)
        self.btn042 = Button(self.colorgrid, text="042", fg="white", bg="#00D787",
                             command=partial(self.color, "042")).grid(row=26, column=0, sticky="ew", padx=2)
        self.btn142 = Button(self.colorgrid, text="142", fg="white", bg="#5FD787",
                             command=partial(self.color, "142")).grid(row=26, column=1, sticky="ew", padx=2)
        self.btn242 = Button(self.colorgrid, text="242", fg="white", bg="#87D787",
                             command=partial(self.color, "242")).grid(row=26, column=2, sticky="ew", padx=2)
        self.btn342 = Button(self.colorgrid, text="342", fg="white", bg="#AFD787",
                             command=partial(self.color, "342")).grid(row=26, column=3, sticky="ew", padx=2)
        self.btn442 = Button(self.colorgrid, text="442", fg="white", bg="#D7D787",
                             command=partial(self.color, "442")).grid(row=26, column=4, sticky="ew", padx=2)
        self.btn542 = Button(self.colorgrid, text="542", fg="white", bg="#FFD787",
                             command=partial(self.color, "542")).grid(row=26, column=5, sticky="ew", padx=2)
        self.btn043 = Button(self.colorgrid, text="043", fg="white", bg="#00D7AF",
                             command=partial(self.color, "043")).grid(row=27, column=0, sticky="ew", padx=2)
        self.btn143 = Button(self.colorgrid, text="143", fg="white", bg="#5FD7AF",
                             command=partial(self.color, "143")).grid(row=27, column=1, sticky="ew", padx=2)
        self.btn243 = Button(self.colorgrid, text="243", fg="white", bg="#87D7AF",
                             command=partial(self.color, "243")).grid(row=27, column=2, sticky="ew", padx=2)
        self.btn343 = Button(self.colorgrid, text="343", fg="white", bg="#AFD7AF",
                             command=partial(self.color, "343")).grid(row=27, column=3, sticky="ew", padx=2)
        self.btn443 = Button(self.colorgrid, text="443", fg="white", bg="#D7D7AF",
                             command=partial(self.color, "443")).grid(row=27, column=4, sticky="ew", padx=2)
        self.btn543 = Button(self.colorgrid, text="543", fg="white", bg="#FFD7AF",
                             command=partial(self.color, "543")).grid(row=27, column=5, sticky="ew", padx=2)
        self.btn044 = Button(self.colorgrid, text="044", fg="white", bg="#00D7D7",
                             command=partial(self.color, "044")).grid(row=28, column=0, sticky="ew", padx=2)
        self.btn144 = Button(self.colorgrid, text="144", fg="white", bg="#5FD7D7",
                             command=partial(self.color, "144")).grid(row=28, column=1, sticky="ew", padx=2)
        self.btn244 = Button(self.colorgrid, text="244", fg="white", bg="#87D7D7",
                             command=partial(self.color, "244")).grid(row=28, column=2, sticky="ew", padx=2)
        self.btn344 = Button(self.colorgrid, text="344", fg="white", bg="#AFD7D7",
                             command=partial(self.color, "344")).grid(row=28, column=3, sticky="ew", padx=2)
        self.btn444 = Button(self.colorgrid, text="444", fg="white", bg="#D7D7D7",
                             command=partial(self.color, "444")).grid(row=28, column=4, sticky="ew", padx=2)
        self.btn544 = Button(self.colorgrid, text="544", fg="white", bg="#FFD7D7",
                             command=partial(self.color, "544")).grid(row=28, column=5, sticky="ew", padx=2)
        self.btn045 = Button(self.colorgrid, text="045", fg="white", bg="#00D7FF",
                             command=partial(self.color, "045")).grid(row=29, column=0, sticky="ew", padx=2)
        self.btn145 = Button(self.colorgrid, text="145", fg="white", bg="#5FD7FF",
                             command=partial(self.color, "145")).grid(row=29, column=1, sticky="ew", padx=2)
        self.btn245 = Button(self.colorgrid, text="245", fg="white", bg="#87D7FF",
                             command=partial(self.color, "245")).grid(row=29, column=2, sticky="ew", padx=2)
        self.btn345 = Button(self.colorgrid, text="345", fg="white", bg="#AFD7FF",
                             command=partial(self.color, "345")).grid(row=29, column=3, sticky="ew", padx=2)
        self.btn445 = Button(self.colorgrid, text="445", fg="white", bg="#D7D7FF",
                             command=partial(self.color, "445")).grid(row=29, column=4, sticky="ew", padx=2)
        self.btn545 = Button(self.colorgrid, text="545", fg="white", bg="#FFD7FF",
                             command=partial(self.color, "545")).grid(row=29, column=5, sticky="ew", padx=2)
        self.btn050 = Button(self.colorgrid, text="050", fg="white", bg="#00FF00",
                             command=partial(self.color, "050")).grid(row=30, column=0, sticky="ew", padx=2)
        self.btn150 = Button(self.colorgrid, text="150", fg="white", bg="#5FFF00",
                             command=partial(self.color, "150")).grid(row=30, column=1, sticky="ew", padx=2)
        self.btn250 = Button(self.colorgrid, text="250", fg="white", bg="#87FF00",
                             command=partial(self.color, "250")).grid(row=30, column=2, sticky="ew", padx=2)
        self.btn350 = Button(self.colorgrid, text="350", fg="white", bg="#AFFF00",
                             command=partial(self.color, "350")).grid(row=30, column=3, sticky="ew", padx=2)
        self.btn450 = Button(self.colorgrid, text="450", fg="white", bg="#D7FF00",
                             command=partial(self.color, "450")).grid(row=30, column=4, sticky="ew", padx=2)
        self.btn550 = Button(self.colorgrid, text="550", fg="white", bg="#FFFF00",
                             command=partial(self.color, "550")).grid(row=30, column=5, sticky="ew", padx=2)
        self.btn051 = Button(self.colorgrid, text="051", fg="white", bg="#00FF5F",
                             command=partial(self.color, "051")).grid(row=31, column=0, sticky="ew", padx=2)
        self.btn151 = Button(self.colorgrid, text="151", fg="white", bg="#5FFF5F",
                             command=partial(self.color, "151")).grid(row=31, column=1, sticky="ew", padx=2)
        self.btn251 = Button(self.colorgrid, text="251", fg="white", bg="#87FF5F",
                             command=partial(self.color, "251")).grid(row=31, column=2, sticky="ew", padx=2)
        self.btn351 = Button(self.colorgrid, text="351", fg="white", bg="#AFFF5F",
                             command=partial(self.color, "351")).grid(row=31, column=3, sticky="ew", padx=2)
        self.btn451 = Button(self.colorgrid, text="451", fg="white", bg="#D7FF5F",
                             command=partial(self.color, "451")).grid(row=31, column=4, sticky="ew", padx=2)
        self.btn551 = Button(self.colorgrid, text="551", fg="white", bg="#FFFF5F",
                             command=partial(self.color, "551")).grid(row=31, column=5, sticky="ew", padx=2)
        self.btn052 = Button(self.colorgrid, text="052", fg="white", bg="#00FF87",
                             command=partial(self.color, "052")).grid(row=32, column=0, sticky="ew", padx=2)
        self.btn152 = Button(self.colorgrid, text="152", fg="white", bg="#5FFF87",
                             command=partial(self.color, "152")).grid(row=32, column=1, sticky="ew", padx=2)
        self.btn252 = Button(self.colorgrid, text="252", fg="white", bg="#87FF87",
                             command=partial(self.color, "252")).grid(row=32, column=2, sticky="ew", padx=2)
        self.btn352 = Button(self.colorgrid, text="352", fg="white", bg="#AFFF87",
                             command=partial(self.color, "352")).grid(row=32, column=3, sticky="ew", padx=2)
        self.btn452 = Button(self.colorgrid, text="452", fg="white", bg="#D7FF87",
                             command=partial(self.color, "452")).grid(row=32, column=4, sticky="ew", padx=2)
        self.btn552 = Button(self.colorgrid, text="552", fg="white", bg="#FFFF87",
                             command=partial(self.color, "552")).grid(row=32, column=5, sticky="ew", padx=2)
        self.btn053 = Button(self.colorgrid, text="053", fg="white", bg="#00FFAF",
                             command=partial(self.color, "053")).grid(row=33, column=0, sticky="ew", padx=2)
        self.btn153 = Button(self.colorgrid, text="153", fg="white", bg="#5FFFAF",
                             command=partial(self.color, "153")).grid(row=33, column=1, sticky="ew", padx=2)
        self.btn253 = Button(self.colorgrid, text="253", fg="white", bg="#87FFAF",
                             command=partial(self.color, "253")).grid(row=33, column=2, sticky="ew", padx=2)
        self.btn353 = Button(self.colorgrid, text="353", fg="white", bg="#AFFFAF",
                             command=partial(self.color, "353")).grid(row=33, column=3, sticky="ew", padx=2)
        self.btn453 = Button(self.colorgrid, text="453", fg="white", bg="#D7FFAF",
                             command=partial(self.color, "453")).grid(row=33, column=4, sticky="ew", padx=2)
        self.btn553 = Button(self.colorgrid, text="553", fg="white", bg="#FFFFAF",
                             command=partial(self.color, "553")).grid(row=33, column=5, sticky="ew", padx=2)
        self.btn054 = Button(self.colorgrid, text="054", fg="white", bg="#00FFD7",
                             command=partial(self.color, "054")).grid(row=34, column=0, sticky="ew", padx=2)
        self.btn154 = Button(self.colorgrid, text="154", fg="white", bg="#5FFFD7",
                             command=partial(self.color, "154")).grid(row=34, column=1, sticky="ew", padx=2)
        self.btn254 = Button(self.colorgrid, text="254", fg="white", bg="#87FFD7",
                             command=partial(self.color, "254")).grid(row=34, column=2, sticky="ew", padx=2)
        self.btn354 = Button(self.colorgrid, text="354", fg="white", bg="#AFFFD7",
                             command=partial(self.color, "354")).grid(row=34, column=3, sticky="ew", padx=2)
        self.btn454 = Button(self.colorgrid, text="454", fg="white", bg="#D7FFD7",
                             command=partial(self.color, "454")).grid(row=34, column=4, sticky="ew", padx=2)
        self.btn554 = Button(self.colorgrid, text="554", fg="white", bg="#FFFFD7",
                             command=partial(self.color, "554")).grid(row=34, column=5, sticky="ew", padx=2)
        self.btn055 = Button(self.colorgrid, text="055", fg="white", bg="#00FFFF",
                             command=partial(self.color, "055")).grid(row=35, column=0, sticky="ew", padx=2)
        self.btn155 = Button(self.colorgrid, text="155", fg="white", bg="#5FFFFF",
                             command=partial(self.color, "155")).grid(row=35, column=1, sticky="ew", padx=2)
        self.btn255 = Button(self.colorgrid, text="255", fg="white", bg="#87FFFF",
                             command=partial(self.color, "255")).grid(row=35, column=2, sticky="ew", padx=2)
        self.btn355 = Button(self.colorgrid, text="355", fg="white", bg="#AFFFFF",
                             command=partial(self.color, "355")).grid(row=35, column=3, sticky="ew", padx=2)
        self.btn455 = Button(self.colorgrid, text="455", fg="white", bg="#D7FFFF",
                             command=partial(self.color, "455")).grid(row=35, column=4, sticky="ew", padx=2)
        self.btn555 = Button(self.colorgrid, text="555", fg="white", bg="#FFFFFF",
                             command=partial(self.color, "555")).grid(row=35, column=5, sticky="ew", padx=2)
        self.scroll_color_y.grid(row=0, rowspan=36, column=6, sticky="ns")

        self.text_frame = Frame()
        self.text_frame.rowconfigure(0, minsize=200, weight=1)
        self.text_frame.rowconfigure(1, minsize=100, weight=1)
        self.text_frame.columnconfigure(0, weight=1)
        self.write_frame = Frame(self.text_frame)
        self.write_frame.rowconfigure(0, minsize=200, weight=1)
        self.write_frame.columnconfigure(0, weight=1)
        self.writing = Text(self.write_frame, insertbackground="white", background="black", fg="white", width=100,
                            borderwidth=5, wrap=tk.NONE)
        self.scroll_write_x = Scrollbar(self.write_frame, orient=HORIZONTAL, command=self.writing.xview)
        self.scroll_write_y = Scrollbar(self.write_frame, orient=VERTICAL, command=self.writing.yview)
        self.writing['xscrollcommand'] = self.scroll_write_x.set
        self.writing['yscrollcommand'] = self.scroll_write_y.set
        self.writing.grid(row=0, column=0, sticky="nsew")
        self.scroll_write_y.grid(row=0, column=1, sticky="ns")
        self.scroll_write_x.grid(row=1, column=0, sticky="ew")
        self.encoding = Text(self.text_frame, borderwidth=5)
        self.write_frame.grid(row=0, column=0, sticky="nsew")
        self.encoding.grid(row=1, column=0, sticky="nsew")

        self.toolbar = Frame()
        self.toolbar.rowconfigure(0, minsize=200, weight=1)
        self.toolbar.columnconfigure(0, minsize=200, weight=1)
        self.character = "@"
        self.lbl_char = Label(self.toolbar, text="Character: ")
        self.ent_char = Entry(self.toolbar)
        self.ent_char.insert(0, self.character)
        self.text_size = 40
        self.lbl_size = Label(self.toolbar, text="Width of text: ")
        self.ent_size = Entry(self.toolbar)
        self.ent_size.insert(0, self.text_size)
        self.lbl_file = Label(self.toolbar, text="No file selected.")
        self.btn_file = Button(self.toolbar, text="Select file to process.", command=self.do_pick_file)
        self.btn_go = Button(self.toolbar, text="CONVERT IMAGE!", fg="green", command=self.go_convert_image)
        self.btn_copy = Button(self.toolbar, text="Copy to Clipboard", command=self.copy_to_clipboard)
        self.btn_quit = Button(self.toolbar, text="QUIT", fg="red", command=main.destroy)
        self.encode = Button(self.toolbar, text="ENCODE", background="black", foreground="white", command=self.encode_text)
        self.decode = Button(self.toolbar, text="DECODE", command=self.decode_text)
        self.ascii_mark = Button(self.toolbar, text="Mark as ASCII", command=self.mark_as_ascii)
        self.ascii_toggle = Button(self.toolbar, text="Toggle ASCII view", command=self.toggle_ascii)
        self.btn_color = Button(self.toolbar, text="Get color of selected:", command=self.which_color)
        self.lbl_color = Label(self.toolbar, text="")
        self.display_canvas = Canvas(self.toolbar, height=200, width=200)
        if self.lbl_file["text"] == "No file selected.":
            self.idacat = Image.open(getpath("idacat.gif")).resize((200, 193))
            self.img = ImageTk.PhotoImage(self.idacat)
            self.display_image = self.display_canvas.create_image(0, 0, anchor=NW, image=self.img)

        self.display_canvas.grid(row=0, column=0, columnspan=2)
        self.lbl_char.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
        self.ent_char.grid(row=1, column=1, sticky="ew", padx=5, pady=5)
        self.lbl_size.grid(row=2, column=0, sticky="ew", padx=5)
        self.ent_size.grid(row=2, column=1, sticky="ew", padx=5)
        self.lbl_file.grid(row=3, column=1, sticky="ew", padx=5)
        self.btn_file.grid(row=3, column=0, sticky="ew", padx=5)
        self.btn_go.grid(row=4, column=0, sticky="ew", padx=5)
        self.btn_copy.grid(row=4, column=1, sticky="ew", padx=5)
        self.encode.grid(row=5, column=0, sticky="ew", padx=5)
        self.decode.grid(row=5, column=1, sticky="ew", padx=5)
        self.ascii_mark.grid(row=6, column=0, sticky="ew", padx=5)
        self.ascii_toggle.grid(row=6, column=1, sticky="ew", padx=5)
        self.clr = StringVar()
        self.btn_color.grid(row=6, column=0, sticky="ew", padx=5)
        self.lbl_color.grid(row=6, column=1, sticky="ew", padx=5)
        self.btn_quit.grid(row=7, sticky="ew", padx=5)

        self.colorgrid.grid(row=0, column=0, sticky="nsew")
        self.colorframe.grid(row=0, column=0, sticky="ns")
        self.text_frame.grid(row=0, column=1, sticky="ns")
        self.toolbar.grid(row=0, column=2, sticky="n")

        # All tags listed here:
        self.writing.tag_configure("ascii", background="black")
        self.writing.tag_configure("000", foreground="#000000")
        self.writing.tag_configure("100", foreground="#5F0000")
        self.writing.tag_configure("200", foreground="#870000")
        self.writing.tag_configure("300", foreground="#AF0000")
        self.writing.tag_configure("400", foreground="#D70000")
        self.writing.tag_configure("500", foreground="#FF0000")
        self.writing.tag_configure("001", foreground="#00005F")
        self.writing.tag_configure("101", foreground="#5F005F")
        self.writing.tag_configure("201", foreground="#87005F")
        self.writing.tag_configure("301", foreground="#AF005F")
        self.writing.tag_configure("401", foreground="#D7005F")
        self.writing.tag_configure("501", foreground="#FF005F")
        self.writing.tag_configure("002", foreground="#000087")
        self.writing.tag_configure("102", foreground="#5F0087")
        self.writing.tag_configure("202", foreground="#870087")
        self.writing.tag_configure("302", foreground="#AF0087")
        self.writing.tag_configure("402", foreground="#D70087")
        self.writing.tag_configure("502", foreground="#FF0087")
        self.writing.tag_configure("003", foreground="#0000AF")
        self.writing.tag_configure("103", foreground="#5F00AF")
        self.writing.tag_configure("203", foreground="#8700AF")
        self.writing.tag_configure("303", foreground="#AF00AF")
        self.writing.tag_configure("403", foreground="#D700AF")
        self.writing.tag_configure("503", foreground="#FF00AF")
        self.writing.tag_configure("004", foreground="#0000D7")
        self.writing.tag_configure("104", foreground="#5F00D7")
        self.writing.tag_configure("204", foreground="#8700D7")
        self.writing.tag_configure("304", foreground="#AF00D7")
        self.writing.tag_configure("404", foreground="#D700D7")
        self.writing.tag_configure("504", foreground="#FF00D7")
        self.writing.tag_configure("005", foreground="#0000FF")
        self.writing.tag_configure("105", foreground="#5F00FF")
        self.writing.tag_configure("205", foreground="#8700FF")
        self.writing.tag_configure("305", foreground="#AF00FF")
        self.writing.tag_configure("405", foreground="#D700FF")
        self.writing.tag_configure("505", foreground="#FF00FF")
        self.writing.tag_configure("010", foreground="#005F00")
        self.writing.tag_configure("110", foreground="#5F5F00")
        self.writing.tag_configure("210", foreground="#875F00")
        self.writing.tag_configure("310", foreground="#AF5F00")
        self.writing.tag_configure("410", foreground="#D75F00")
        self.writing.tag_configure("510", foreground="#FF5F00")
        self.writing.tag_configure("011", foreground="#005F5F")
        self.writing.tag_configure("111", foreground="#5F5F5F")
        self.writing.tag_configure("211", foreground="#875F5F")
        self.writing.tag_configure("311", foreground="#AF5F5F")
        self.writing.tag_configure("411", foreground="#D75F5F")
        self.writing.tag_configure("511", foreground="#FF5F5F")
        self.writing.tag_configure("012", foreground="#005F87")
        self.writing.tag_configure("112", foreground="#5F5F87")
        self.writing.tag_configure("212", foreground="#875F87")
        self.writing.tag_configure("312", foreground="#AF5F87")
        self.writing.tag_configure("412", foreground="#D75F87")
        self.writing.tag_configure("512", foreground="#FF5F87")
        self.writing.tag_configure("013", foreground="#005FAF")
        self.writing.tag_configure("113", foreground="#5F5FAF")
        self.writing.tag_configure("213", foreground="#875FAF")
        self.writing.tag_configure("313", foreground="#AF5FAF")
        self.writing.tag_configure("413", foreground="#D75FAF")
        self.writing.tag_configure("513", foreground="#FF5FAF")
        self.writing.tag_configure("014", foreground="#005FD7")
        self.writing.tag_configure("114", foreground="#5F5FD7")
        self.writing.tag_configure("214", foreground="#875FD7")
        self.writing.tag_configure("314", foreground="#AF5FD7")
        self.writing.tag_configure("414", foreground="#D75FD7")
        self.writing.tag_configure("514", foreground="#FF5FD7")
        self.writing.tag_configure("015", foreground="#005FFF")
        self.writing.tag_configure("115", foreground="#5F5FFF")
        self.writing.tag_configure("215", foreground="#875FFF")
        self.writing.tag_configure("315", foreground="#AF5FFF")
        self.writing.tag_configure("415", foreground="#D75FFF")
        self.writing.tag_configure("515", foreground="#FF5FFF")
        self.writing.tag_configure("020", foreground="#008700")
        self.writing.tag_configure("120", foreground="#5F8700")
        self.writing.tag_configure("220", foreground="#878700")
        self.writing.tag_configure("320", foreground="#AF8700")
        self.writing.tag_configure("420", foreground="#D78700")
        self.writing.tag_configure("520", foreground="#FF8700")
        self.writing.tag_configure("021", foreground="#00875F")
        self.writing.tag_configure("121", foreground="#5F875F")
        self.writing.tag_configure("221", foreground="#87875F")
        self.writing.tag_configure("321", foreground="#AF875F")
        self.writing.tag_configure("421", foreground="#D7875F")
        self.writing.tag_configure("521", foreground="#FF875F")
        self.writing.tag_configure("022", foreground="#008787")
        self.writing.tag_configure("122", foreground="#5F8787")
        self.writing.tag_configure("222", foreground="#878787")
        self.writing.tag_configure("322", foreground="#AF8787")
        self.writing.tag_configure("422", foreground="#D78787")
        self.writing.tag_configure("522", foreground="#FF8787")
        self.writing.tag_configure("023", foreground="#0087AF")
        self.writing.tag_configure("123", foreground="#5F87AF")
        self.writing.tag_configure("223", foreground="#8787AF")
        self.writing.tag_configure("323", foreground="#AF87AF")
        self.writing.tag_configure("423", foreground="#D787AF")
        self.writing.tag_configure("523", foreground="#FF87AF")
        self.writing.tag_configure("024", foreground="#0087D7")
        self.writing.tag_configure("124", foreground="#5F87D7")
        self.writing.tag_configure("224", foreground="#8787D7")
        self.writing.tag_configure("324", foreground="#AF87D7")
        self.writing.tag_configure("424", foreground="#D787D7")
        self.writing.tag_configure("524", foreground="#FF87D7")
        self.writing.tag_configure("025", foreground="#0087FF")
        self.writing.tag_configure("125", foreground="#5F87FF")
        self.writing.tag_configure("225", foreground="#8787FF")
        self.writing.tag_configure("325", foreground="#AF87FF")
        self.writing.tag_configure("425", foreground="#D787FF")
        self.writing.tag_configure("525", foreground="#FF87FF")
        self.writing.tag_configure("030", foreground="#00AF00")
        self.writing.tag_configure("130", foreground="#5FAF00")
        self.writing.tag_configure("230", foreground="#87AF00")
        self.writing.tag_configure("330", foreground="#AFAF00")
        self.writing.tag_configure("430", foreground="#D7AF00")
        self.writing.tag_configure("530", foreground="#FFAF00")
        self.writing.tag_configure("031", foreground="#00AF5F")
        self.writing.tag_configure("131", foreground="#5FAF5F")
        self.writing.tag_configure("231", foreground="#87AF5F")
        self.writing.tag_configure("331", foreground="#AFAF5F")
        self.writing.tag_configure("431", foreground="#D7AF5F")
        self.writing.tag_configure("531", foreground="#FFAF5F")
        self.writing.tag_configure("032", foreground="#00AF87")
        self.writing.tag_configure("132", foreground="#5FAF87")
        self.writing.tag_configure("232", foreground="#87AF87")
        self.writing.tag_configure("332", foreground="#AFAF87")
        self.writing.tag_configure("432", foreground="#D7AF87")
        self.writing.tag_configure("532", foreground="#FFAF87")
        self.writing.tag_configure("033", foreground="#00AFAF")
        self.writing.tag_configure("133", foreground="#5FAFAF")
        self.writing.tag_configure("233", foreground="#87AFAF")
        self.writing.tag_configure("333", foreground="#AFAFAF")
        self.writing.tag_configure("433", foreground="#D7AFAF")
        self.writing.tag_configure("533", foreground="#FFAFAF")
        self.writing.tag_configure("034", foreground="#00AFD7")
        self.writing.tag_configure("134", foreground="#5FAFD7")
        self.writing.tag_configure("234", foreground="#87AFD7")
        self.writing.tag_configure("334", foreground="#AFAFD7")
        self.writing.tag_configure("434", foreground="#D7AFD7")
        self.writing.tag_configure("534", foreground="#FFAFD7")
        self.writing.tag_configure("035", foreground="#00AFFF")
        self.writing.tag_configure("135", foreground="#5FAFFF")
        self.writing.tag_configure("235", foreground="#87AFFF")
        self.writing.tag_configure("335", foreground="#AFAFFF")
        self.writing.tag_configure("435", foreground="#D7AFFF")
        self.writing.tag_configure("535", foreground="#FFAFFF")
        self.writing.tag_configure("040", foreground="#00D700")
        self.writing.tag_configure("140", foreground="#5FD700")
        self.writing.tag_configure("240", foreground="#87D700")
        self.writing.tag_configure("340", foreground="#AFD700")
        self.writing.tag_configure("440", foreground="#D7D700")
        self.writing.tag_configure("540", foreground="#FFD700")
        self.writing.tag_configure("041", foreground="#00D75F")
        self.writing.tag_configure("141", foreground="#5FD75F")
        self.writing.tag_configure("241", foreground="#87D75F")
        self.writing.tag_configure("341", foreground="#AFD75F")
        self.writing.tag_configure("441", foreground="#D7D75F")
        self.writing.tag_configure("541", foreground="#FFD75F")
        self.writing.tag_configure("042", foreground="#00D787")
        self.writing.tag_configure("142", foreground="#5FD787")
        self.writing.tag_configure("242", foreground="#87D787")
        self.writing.tag_configure("342", foreground="#AFD787")
        self.writing.tag_configure("442", foreground="#D7D787")
        self.writing.tag_configure("542", foreground="#FFD787")
        self.writing.tag_configure("043", foreground="#00D7AF")
        self.writing.tag_configure("143", foreground="#5FD7AF")
        self.writing.tag_configure("243", foreground="#87D7AF")
        self.writing.tag_configure("343", foreground="#AFD7AF")
        self.writing.tag_configure("443", foreground="#D7D7AF")
        self.writing.tag_configure("543", foreground="#FFD7AF")
        self.writing.tag_configure("044", foreground="#00D7D7")
        self.writing.tag_configure("144", foreground="#5FD7D7")
        self.writing.tag_configure("244", foreground="#87D7D7")
        self.writing.tag_configure("344", foreground="#AFD7D7")
        self.writing.tag_configure("444", foreground="#D7D7D7")
        self.writing.tag_configure("544", foreground="#FFD7D7")
        self.writing.tag_configure("045", foreground="#00D7FF")
        self.writing.tag_configure("145", foreground="#5FD7FF")
        self.writing.tag_configure("245", foreground="#87D7FF")
        self.writing.tag_configure("345", foreground="#AFD7FF")
        self.writing.tag_configure("445", foreground="#D7D7FF")
        self.writing.tag_configure("545", foreground="#FFD7FF")
        self.writing.tag_configure("050", foreground="#00FF00")
        self.writing.tag_configure("150", foreground="#5FFF00")
        self.writing.tag_configure("250", foreground="#87FF00")
        self.writing.tag_configure("350", foreground="#AFFF00")
        self.writing.tag_configure("450", foreground="#D7FF00")
        self.writing.tag_configure("550", foreground="#FFFF00")
        self.writing.tag_configure("051", foreground="#00FF5F")
        self.writing.tag_configure("151", foreground="#5FFF5F")
        self.writing.tag_configure("251", foreground="#87FF5F")
        self.writing.tag_configure("351", foreground="#AFFF5F")
        self.writing.tag_configure("451", foreground="#D7FF5F")
        self.writing.tag_configure("551", foreground="#FFFF5F")
        self.writing.tag_configure("052", foreground="#00FF87")
        self.writing.tag_configure("152", foreground="#5FFF87")
        self.writing.tag_configure("252", foreground="#87FF87")
        self.writing.tag_configure("352", foreground="#AFFF87")
        self.writing.tag_configure("452", foreground="#D7FF87")
        self.writing.tag_configure("552", foreground="#FFFF87")
        self.writing.tag_configure("053", foreground="#00FFAF")
        self.writing.tag_configure("153", foreground="#5FFFAF")
        self.writing.tag_configure("253", foreground="#87FFAF")
        self.writing.tag_configure("353", foreground="#AFFFAF")
        self.writing.tag_configure("453", foreground="#D7FFAF")
        self.writing.tag_configure("553", foreground="#FFFFAF")
        self.writing.tag_configure("054", foreground="#00FFD7")
        self.writing.tag_configure("154", foreground="#5FFFD7")
        self.writing.tag_configure("254", foreground="#87FFD7")
        self.writing.tag_configure("354", foreground="#AFFFD7")
        self.writing.tag_configure("454", foreground="#D7FFD7")
        self.writing.tag_configure("554", foreground="#FFFFD7")
        self.writing.tag_configure("055", foreground="#00FFFF")
        self.writing.tag_configure("155", foreground="#5FFFFF")
        self.writing.tag_configure("255", foreground="#87FFFF")
        self.writing.tag_configure("355", foreground="#AFFFFF")
        self.writing.tag_configure("455", foreground="#D7FFFF")
        self.writing.tag_configure("555", foreground="#FFFFFF")

    def which_color(self):
        self.clr = "555"
        if self.writing.tag_ranges(tk.SEL):
            tags = self.writing.tag_names(tk.SEL_FIRST)
            for tag in tags:
                if (tag != "sel") & (tag != "ascii"):
                    self.clr = tag
        self.lbl_color["text"] = self.clr

    def color(self, code):
        if self.writing.tag_ranges(tk.SEL):
            for c in range(len(self.writing.get(tk.SEL_FIRST, tk.SEL_LAST))):
                tags = self.writing.tag_names("%s+%ic" % (tk.SEL_FIRST, c))
                for tag in tags:
                    if (tag.lower() != "sel") & (tag.lower() != "ascii"):
                        self.writing.tag_remove(tag, tk.SEL_FIRST, tk.SEL_LAST)
            self.writing.tag_add(code, tk.SEL_FIRST, tk.SEL_LAST)

    def mark_as_ascii(self):
        if self.writing.tag_ranges(tk.SEL):
            current_tags = self.writing.tag_names(tk.SEL_FIRST)
            if "ascii" in current_tags:
                self.writing.tag_remove("ascii", tk.SEL_FIRST, tk.SEL_LAST)
            else:
                self.writing.tag_add("ascii", tk.SEL_FIRST, tk.SEL_LAST)
        self.writing.tag_lower("ascii", belowThis="sel")

    def encode_text(self):
        encoded_string = ""
        last_tag = "|555"
        index = 0
        line_index = 1
        is_ascii = False
        for x in self.writing.get("1.0", tk.END):
            tags = self.writing.tag_names(str(line_index) + "." + str(index))
            print(tags)
            if tags.count("ascii") > 0:
                if not is_ascii:
                    encoded_string = encoded_string + "<ascii>"
                    is_ascii = True
                t = list(tags)
                t.remove("ascii")
                tags = tuple(t)
            else:
                if is_ascii:
                    encoded_string = encoded_string + "</ascii>"
                    is_ascii = False
            if tags.count("sel") < 0:
                t = list(tags)
                t.remove("sel")
                tags = tuple(t)
            if x == "\n":
                encoded_string = encoded_string + "|/"
                line_index = line_index + 1
                index = 0
                continue
            if len(tags) == 0:
                current_tag = "|555"
            else:
                current_tag = "|" + "".join(tags[len(tags) - 1])
            if last_tag == current_tag:
                encoded_string = encoded_string + x
            else:
                last_tag = current_tag
                encoded_string = encoded_string + current_tag + x
            if x == "|":
                encoded_string = encoded_string + "|"
            index = index + 1
        self.encoding.delete("1.0", tk.END)
        self.encoding.insert(tk.END, encoded_string)

    def decode_text(self):
        print("Begin decoding.")
        self.writing.delete("1.0", tk.END)
        self.writing.insert("1.0", self.encoding.get("1.0", tk.END))
        start = "1.0"
        code = ""
        count = IntVar()
        location = self.writing.search(r"\|[0-5][0-5][0-5]|\|[=][a-z]", start, regexp=True, count=count)
        if location == "1.0":
            code = self.writing.get("1.1", "1.4")
            self.writing.delete("1.0", "1.4")
        print("Check for Color Tags")
        while True:
            location = self.writing.search(r"\|[0-5][0-5][0-5]|\|[=][a-z]", start, regexp=True, count=count)
            if location == "":
                break
            if count.get() == 0:
                break
            self.writing.tag_add(code, start, location)
            code = self.writing.get("%s+1c" % location, "%s+4c" % location)
            self.writing.delete(location, "%s+4c" % location)
            start = location
        start = "1.0"
        print("Check for line endings")
        while True:
            location = self.writing.search(r"(\|\/)", start, regexp=True, count=count)
            if location == "":
                break
            if count.get() == 0:
                break
            self.writing.delete(location, "%s+2c" % location)
            self.writing.insert(location, "\n")
            start = location
        start = "1.0"
        print("Check for pipes.")
        while True:
            location = self.writing.search(r"\|\|", start, count=count, regexp=True, forwards=True)
            if location == "":
                break
            if self.writing.compare(start, ">", location):
                break
            if count.get() == 0:
                break
            self.writing.delete(location, "%s+2c" % location)
            self.writing.insert(location, "|")
            start = "%s+1c" % location
        print("Check for ascii.")
        while True:
            start = self.writing.search(r"<ascii>", "1.0", count=count, regexp=True, nocase=1)
            print(start)
            if count.get() == 0:
                break
            end = self.writing.search(r"<\/ascii>", "1.0", count=count, regexp=True, nocase=1)
            print(end)
            if count.get() == 0:
                break
            if (start == "") | (end == ""):
                break
            self.writing.tag_add("ascii", start, end)
            self.writing.delete(end, "%s+8c" % end)
            self.writing.delete(start, "%s+7c" % start)

    def do_pick_file(self):
        picked_file_types = [('Image files', '*.jpg *.png *.gif')]
        self.image_name = askopenfilename(initialdir=os.getcwd(), title="Please select an image:",
                                          filetypes=picked_file_types)
        self.lbl_file["text"] = self.image_name
        img_new = Image.open(self.image_name)
        (orig_w, orig_h) = img_new.size
        if orig_w >= orig_h:
            new_w = 200
            new_h = round(orig_h / orig_w * 200)
        else:
            new_h = 200
            new_w = round(orig_w / orig_h * 200)
        self.img = ImageTk.PhotoImage(img_new.resize((new_w, new_h)))
        self.display_canvas.itemconfig(self.display_image, image=self.img)

    def copy_to_clipboard(self):
        clip = pd.DataFrame([self.encoding.get("1.0", "%s-1c" % tk.END)])
        clip.to_clipboard(excel=False, header=False, index=False)

    def go_convert_image(self):
        if self.lbl_file["text"] == "No file selected.":
            self.do_pick_file()
        image_file = Image.open(self.image_name)
        cursor = 2  # ratio of cursor as pixel
        (orig_w, orig_h) = image_file.size
        aspect_ratio = orig_h / (orig_w * cursor)
        new_w = int(self.ent_size.get())
        new_h = round(aspect_ratio * new_w)
        image_array = np.array(image_file.resize((new_w, new_h)))
        (w, h, colors) = image_array.shape
        color_string = ''
        last_color = ''
        for x in range(0, w - 1):
            for y in range(0, h - 1):
                new_color = color_convert(image_array, x, y)
                if new_color != "000":
                    marker = self.ent_char.get()
                else:
                    marker = " "
                if new_color == last_color:
                    color_string = color_string + marker
                else:
                    color_string = color_string + "|" + new_color + marker
                last_color = new_color
            color_string = color_string[0:len(color_string) - 1] + "|/"
        self.encoding.delete("1.0", tk.END)
        self.encoding.insert(tk.END, color_string)
        self.decode_text()

    def toggle_ascii(self):
        current = self.writing.tag_configure("ascii")
        if current["background"][4] == "#484848":
            self.writing.tag_configure("ascii", background="black")
        else:
            self.writing.tag_configure("ascii", background="#484848")


def color_convert(image_array, x, y):
    colors = (0, 95, 135, 175, 215, 255)
    red = str(colors.index(min(colors, key=lambda n: abs(n - image_array[x, y, 0]))))
    grn = str(colors.index(min(colors, key=lambda n: abs(n - image_array[x, y, 1]))))
    blu = str(colors.index(min(colors, key=lambda n: abs(n - image_array[x, y, 2]))))
    color_string = red + grn + blu
    return color_string


def getpath(filename):
    try:
        path = sys._MEIPASS
    except Exception:
        path = os.path.abspath('.')
    return os.path.join(path, filename)


window = Tk()
MainWindow(window)
window.mainloop()
