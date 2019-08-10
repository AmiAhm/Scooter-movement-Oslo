# Scooter-Usage-Oslo
Gathering and analyzing electrical scooter movements in Oslo

# How to use
## Data collection
1. Run scripts in /scrapers on a regular basis. 
## Data processing
2. Merge output into one file for easier processing with data-merger.ipynb
3. Round data to every X minutes with data-merger.ipynb
4. Calculate distance moved with distance-measure-and-dateparser.ipynb
5. Use ScooterMapperAndGridMaker.rmd to create grids on maps or to plot (recommend using gis instead, grids are also outputted as shapefiles) 
