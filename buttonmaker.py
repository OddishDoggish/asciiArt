def hexcode(i):
    colors = ("00", "5F", "87", "AF", "D7", "FF")
    return colors[i]


row = 0
for g in range(6):
    for b in range(6):
        for r in range(6):
            #print('self.btn' + str(r) + str(g) + str(b) + ' = Button(self.colorgrid, text="' + str(r) + str(g) + str(b) +
            #      '", fg="white", bg="#' + hexcode(r) + hexcode(g) + hexcode(b) + '", command=partial(self.color, "'
            #                                                                      + str(r) + str(g) + str(b) + '"))')
            #print('self.btn' + str(r) + str(g) + str(b) + '.grid(row=' + str(row) + ', column=' + str(r) +
            #      ', sticky="ew", padx=2)')
            print('self.writing.tag_configure("' + str(r) + str(g) + str(b) + '", foreground="#' + hexcode(r) + hexcode(g)
                  + hexcode(b) + '")')
#        row = row+1

