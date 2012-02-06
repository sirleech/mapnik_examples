#!/usr/bin/env python2

from mapnik import *

mapfile = 'mapnik_style.xml'
map_output = 'canberra.png'

m = Map(4*1024,4*1024)
load_map(m, mapfile)
# lon, lat , lon , lat
bbox=(Envelope( 149.00,-35.21,149.21,-35.39 ))

m.zoom_to_box(bbox)
print "Scale = " , m.scale()
render_to_file(m, map_output)
