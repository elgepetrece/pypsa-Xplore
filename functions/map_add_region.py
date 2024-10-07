
import geopandas as gpd


def map_add_region(ax, gdf_regions, params, is_offshore=False):
    
    
    if is_offshore:
        color = params['color_offshore']
    else:
        color = params['color_onshore']

    gdf_regions.plot(ax=ax, color=color, edgecolor=params['edgecolor'], lw=params['lw'])

