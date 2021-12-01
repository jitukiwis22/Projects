from overpass import API
from time import sleep
from sys import exc_info
from xmltodict import parse
from urllib.request import urlopen
 
api = API()
road_id=[]
Highway=[]
Name=[]
#locations=[(18.5295805, 73.9450703)]
locations=[(19.3718386,72.8613908)]
#locations=[(24.2126953,83.2405929)]
for loc in locations:
    xx,yy=loc[0],loc[1]
    try:
        response = api.Get('way["highway"](around:50,{0},{1});'.format(loc[0],loc[1])) 
        print ("For location with coordinates {0}, {1} found way IDs:".format(loc[0],loc[1]))
        if len(response['features'])>0:
            for way in response['features']:
                print(way['id'])
                road_id.append(way['id'])
        else:
            print ("No ways")
        sleep(1)
    except:
        print ("Got error: {0}".format(exc_info())[0])

print(road_id)

for i in road_id:
    response = urlopen('http://www.openstreetmap.org/api/0.6/way/'+str(i)+'/full')
    s=response.read()
    d=parse(s)

    try:
        for tags in d['osm']['way']['tag']:
            print (u'key = {0}, value = {1}'.format(tags['@k'], tags['@v']))
            if (tags['@k']=='highway'):
                Highway.append(tags['@v'])
            elif (tags['@k']=='name'):
                Name.append(tags['@v'])

    except:
        print (u'key = {0}, value = {1}'.format(d['osm']['way']['tag']['@k'], d['osm']['way']['tag']['@v']))
        Highway.append(d['osm']['way']['tag']['@v'])
        Name.append("NaN")

print(Highway)
print(Name)
