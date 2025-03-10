
import geopandas as gpd


def map_add_region(ax, gdf_regions, params, is_offshore=False):
    '''
    This function is to just plot the regions provided in 'gdf_regions' in axes 'ax'.
    Colors are provided by the 'params' (use 'none' in there for no colors).
    Specify in boolean 'is_offshore' the type of regions.
    '''
    
    if is_offshore:
        color = params['color_offshore']
    else:
        color = params['color_onshore']

    gdf_regions.plot(ax=ax, color=color, edgecolor=params['edgecolor'], lw=params['lw'])

