
import geopandas as gpd


def map_add_region(ax, file, path, params):
    

    if 'on' in file:
        color = params['color_onshore']
    
    if 'off' in file:
        color = params['color_offshore']

    gpd.read_file(path+file).plot(ax=ax,color=color,edgecolor=params['edgecolor'],lw=params['lw'])

