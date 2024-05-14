# GDAL2Tiles-Server
> gdal2tiles.py wrapped in a server that also hosts the tiles
## Usage
* Create the volume that holds your processed tilesets `docker volume create gdal_tiles`
* Start  The server
  * Production: `docker-compose up -d`
  * Development: `docker-compose -f docker-compose.dev.yml -f docker-compose.yml up -d`
* Make a post request with your map to http://localhost:8000/upload with the image in the body.
  *  Take a look at `scripts/http/upload-map.http`
*  That image is now available as a tileset at `http://localhost:8000/tiles/image-name/{zoom}/{x}/{y}.png`
## Special Thanks
* I use this gdal2tiles from https://github.com/commenthol/gdal2tiles-leaflet/tree/master
because I'm using leaflet. 
* Used the base stuff from the Dockerfile here https://github.com/thinkWhere/GDAL-Docker
* ChatGPT (I love you lol)

## Licenses
* See license in gdal2tiles.py
* probably others
* All other Code MIT License
