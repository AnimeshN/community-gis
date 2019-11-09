CommunityGIS is a platform for community  for a spatial data infrastructure. 
This consists of frontend described below and backend which is geonode ( see www.geonode.org) 
Primary objective of communitygis is to provide educational platform for learners to learn about spatial information and learn how these modern tools can be used to solve real life problems. As a platform it is for people who range from those who can contribute data ( mobile based point data collection to digitization of published maps) to those who can analyse the data to infer useful social knowledge. It is a digital contraption needed to collect, aggregate , access and analyse data finally provide decision support for to manipulate reality. Since all source code is published hereby (for frontend) , under GPL, any one can reproduce the technology , without any permission from makerGHAT. This has been created by volunteers and coordinated by www.makerghat.org 
This is inspired by ideas as in 'p2p governance' of Bowens ( https://blog.p2pfoundation.net/about ) and Third Pillar of Dr Raghuram Rajan  (https://www.penguinrandomhouse.com/books/566369/the-third-pillar-by-raghuram-rajan/9780525558316/ )



# Build using

* Geonode 2.10
* Python 2.7
* Django 1.11.22
* PostgreSQL 11.5
* Leaflet 1.5

# How to setup for development

* Go through the link to setup geonode
http://docs.geonode.org/en/2.10.x/install/project/index.html

* clone this repository 

* rename it to my_geonode

* stop paver 

* replace /opt/geonode_custom/my_geonode with community-gis(my_geonode)

* download following folder and copy geoserver and downloaded folder inside my_geonode folder
https://drive.google.com/open?id=1tEgBTgk3ovWdrfecLAbMVRIPDxeHpmm1

* start paver
