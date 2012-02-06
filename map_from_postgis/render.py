#!/usr/bin/env python2

from mapnik import *

longlat = Projection('+proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs')
merc = Projection('+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0 +k=1.0 +units=m +nadgrids=@null +no_defs +over')

mapfile = 'mapnik_style.xml'
map_output = 'canberra.png'

m = Map(4*1024,4*1024,"+proj=latlong +datum=WGS84")
load_map(m, mapfile)
# lon, lat , lon , lat

bbox=(Envelope( 149.00,-35.21,149.21,-35.39 ))

# Our bounds above are in long/lat, but our map
# is in spherical mercator, so we need to transform
# the bounding box to mercator to properly position
# the Map when we call `zoom_to_box()`
transform = ProjTransform(longlat,merc)
merc_bbox = transform.forward(bbox)

# Mapnik internally will fix the aspect ratio of the bounding box
# to match the aspect ratio of the target image width and height
# This behavior is controlled by setting the `m.aspect_fix_mode`
# and defaults to GROW_BBOX, but you can also change it to alter
# the target image size by setting aspect_fix_mode to GROW_CANVAS
#m.aspect_fix_mode = mapnik.GROW_CANVAS
# Note: aspect_fix_mode is only available in Mapnik >= 0.6.0
m.zoom_to_box(merc_bbox)


print "Scale = " , m.scale()
render_to_file(m, map_output)
