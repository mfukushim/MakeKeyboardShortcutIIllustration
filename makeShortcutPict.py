#!/usr/bin/python
import os
import csv
from gimpfu import *
from gimp import pdb


def do_draw(image, layer, pict_path, shortcut_def, key_def_csv, marker_color):
    text_color = (0, 0, 0, 255)  # R,G,B,A
    draw_size = 80
    marker_alpha = 80.0
    # set output dir
    out = os.path.abspath(os.path.join(pict_path, os.pardir, "pictOut"))
    if not os.path.exists(out):
        os.makedirs(out)

    # load key define
    key_def = {}
    rd = open(key_def_csv)
    csv_reader = csv.reader(rd, delimiter='\t')
    for line in csv_reader:
        key_def[line[0]] = (int(line[1]), int(line[2]))

    # load base picture
    img = pdb.gimp_file_load(pict_path, "file")

    # load shortcut def
    rd2 = open(shortcut_def, "r")
    data = rd2.readlines()
    for line2 in data:
        row = line2.split('\t')
        label = ''.join(list(filter(lambda d: d.isalnum(), row[0].replace("/", "Slash").replace("-", "Minus"))))
        print(label)
        base_layer = pdb.gimp_image_get_active_layer(img)
        draw_layer = pdb.gimp_layer_copy(base_layer, True)
        img.add_layer(draw_layer, 0)
        keys = row[0].split("+")
        for key in keys:
            try:
                pos = key_def[key]
            except KeyError:
                gimp.message(str(key))
                break
            point = [pos[0], pos[1]]
            pdb.gimp_context_set_foreground(marker_color)
            pdb.gimp_context_set_brush("1. Pixel")
            pdb.gimp_context_set_brush_size(draw_size)
            pdb.gimp_context_set_opacity(marker_alpha)
            pdb.gimp_context_set_dynamics("Dynamics Off")
            pdb.gimp_paintbrush_default(draw_layer, len(point), point)

        pdb.gimp_context_set_foreground(text_color)
        text_layer = pdb.gimp_text_fontname(img, draw_layer, 20, 20, row[1], 0, False, 52, 0, "Sans-serif Bold")
        pdb.gimp_layer_resize(text_layer, img.width, img.height, 0, 0)
        pdb.gimp_floating_sel_anchor(text_layer)
        pdb.file_png_save_defaults(img, draw_layer, os.path.join(out, label + ".png"), label + ".png")
        img.remove_layer(draw_layer)

    # gimp.Display(img)


register(
    "MakeShortcut",
    "Make Keyboard shortcut illustration",
    "Longer description of doing stuff",
    "MF",
    "MF",
    "2020",
    "<Image>/ExtTool/make shortcut pict",
    "",
    [(PF_FILE, "pict_path", "Keyboard Picture", "keyboard.xcf"),
     (PF_FILE, "shortcut_def", "Shortcut define TSV", "shortcut.csv"),
     (PF_FILE, "key_def", "Key define TSV", "keydef.csv"),
     (PF_COLOR, "marker_color", "Marker Color", (238, 124, 29, 128))
     ],
    [],
    do_draw)

main()
