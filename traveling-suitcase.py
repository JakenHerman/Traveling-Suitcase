import urllib
import webbrowser

u = urllib.urlopen('http://ctabustracker.com/bustime/map/getBusesForRoute.jsp?route=22')
data = u.read()
f = open('rt22.xml', 'wb')
f.write(data)
f.close()

from xml.etree.ElementTree import *
doc = parse('rt22.xml')
for bus in doc.findall('bus'):
    d = bus.findtext('d')
    lat = float(bus.findtext('lat'))
    lon = float(bus.findtext('lon'))
    direction = bus.findtext('d')
#Lat = N/S
if direction.startswith('North'):
    busid = bus.findtext('id')
    print busid, lat, lon
    
    webbrowser.open("https://www.google.com/maps/place/@"+str(lat)+","+str(lon)+","
                    "19z")

else:
    print "No buses."