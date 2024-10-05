
import geopandas as gpd


def map_add_region(ax, file_regions, path_regions, params):
    

    if 'on' in file_regions:
        color = params['color_onshore']
    
    if 'off' in file_regions:
        color = params['color_offshore']

    gpd.read_file(path_regions+file_regions).plot(ax=ax, color=color, edgecolor=params['edgecolor'], lw=params['lw'])

