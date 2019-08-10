# Scooter-Usage-Oslo
Gathering and analyzing electrical scooter movements in Oslo

# How to use
## Data collection
Download from https://www.kaggle.com/amirahmed/oslo-scooter-movement-end-of-july-2019

OR 

1. Run scripts in /scrapers on a regular basis. 
## Data processing
Download from https://www.kaggle.com/amirahmed/oslo-scooter-movement-end-of-july-2019

OR

2. Merge output into one file for easier processing with data-merger.ipynb
3. Round data to every X minutes with data-merger.ipynb
4. Calculate distance moved with distance-measure-and-dateparser.ipynb
5. Use ScooterMapperAndGridMaker.rmd to create grids on maps or to plot (recommend using gis instead, grids are also outputted as shapefiles) 

## Maps and Shapefiles
For detailed shapefiles and maps on Norway
https://www.kartverket.no/data/

For coastline and land shapefiles:
https://osmdata.openstreetmap.de/data/land-polygons.html

## APIs
A description of how to connect to several operator APIs
https://github.com/ubahnverleih/WoBike/

An from Entur API that is supposed to gather data on scooter activity in Norway in one place:
https://developer.entur.org/pages-mobility-docs-scooters
