#!/usr/bin/env python2

from mapnik import *

mapfile = 'mapnik_style.xml'
map_output = 'canberra.png'

m = Map(4*1024,4*1024)
load_map(m, mapfile)
# lon, lat , lon , lat
bbox=(Envelope( 16424265,-4221489,16796858,-4423753 ))

m.zoom_to_box(bbox)
print "Scale = " , m.scale()
render_to_file(m, map_output)