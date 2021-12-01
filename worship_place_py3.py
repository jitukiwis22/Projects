from overpass import API
from time import sleep
from sys import exc_info
from urllib.request import urlopen
from xmltodict import parse

api = API()
worship=[]

#locations=[(18.5295805, 73.9450703)]
#locations=[(19.3718386,72.8613908)]
locations=[(28.6161112, 77.3905778)]
for loc in locations:
	xx,yy=loc[0],loc[1]
	try:
		response = api.Get('node["amenity"="place_of_worship"](around:10000,{0},{1});'.format(loc[0],loc[1])) 
		print "For location with coordinates {0}, {1} found way IDs:".format(loc[0],loc[1])
		if len(response['features'])>0:
			for way in response['features']:
				print(way['id'])
				worship.append(way['id'])
				
		else:
			print "No ways"
		sleep(1)
	except:
		print "Got error: {0}".format(exc_info())[0]

print("\n")
name=[]
religion=[]
for nodes in worship:

	response1=urlopen('https://www.openstreetmap.org/api/0.6/node/'+str(nodes))
	s=response1.read()
	d=parse(s)
	#print(nodes)

	tag=d['osm']['node']['tag']
	j=0
	k=0
	print(nodes)
	try:
		for i in range(len(tag)):
			if (tag[i]['@k']=='name' or tag[i]['@k']=='name:en'):
				j=i
					#print(j)
			if (tag[i]['@k']=='religion'):
					k=i
					#print(k)
		if (tag[j]['@k']=='name' or tag[j]['@k']=='name:en'):
			name.append(tag[j]['@v'])
		else:
			name.append("NaN")
		if (tag[k]['@k']=='religion'):
			religion.append(tag[k]['@v'])
		else:
			religion.append("NaN")
	except:
		print("No More Info")

temple=0
church=0
mosque=0
gurudwara=0
other=0
for i in range(len(name)):
	print(name[i], religion[i])
for i in range(len(name)):
	if ("Temple" in name[i] or "temple" in name[i] or "Mandir" in name[i] or "mandir" in name[i] or "hindu" in religion[i]):
		temple=temple+1
	elif ("Church" in name[i] or "church" in name[i] or "christian" in religion[i]):
		church=church+1
	elif ("Mosque" in name[i] or "masjid" in name[i] or "mosque" in name[i] or "Masjid" in name[i] or "muslim" in religion[i]):
		mosque=mosque+1
	elif ("Gurudwara" in name[i] or "gurudwara" in name[i] or "sikh" in religion[i] or "Sahib" in name[i]):
		gurudwara=gurudwara+1
	else:
		other=other+1

print("Temple: ", temple)
print("Church: ", church)
print("Mosque: ", mosque)
print("Gurudwara: ", gurudwara)
print("Others: ", other)
print("\n")


