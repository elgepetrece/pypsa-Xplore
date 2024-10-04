

import pandas as pd
import geopandas as gpd



def fun_gdf_network_generators(carrier, n, file_regions, path_regions):
    """
    This function provides a gdf of a network with some generation features 
    for a specific carrier.

    An appropriate region file is required.

    Columns:
      - geometry
      - bus
      - carrier
      - area
      - p_nom               : installed capacity [MW]
      - p_nom_density       : ratio between p_nom and area [MW/km2]
      - p_nom_max           : potential according to land availability [MW]
      - p_nom_max_density   : ratio between p_nom_max and area [MW/km2]
      - p_nom_max_ratio     : ration between p_nom and p_nom_max [-]
      - p_nom_opt           : optimal capacity [MW]
      - p_nom_opt_density   : ratio between p_nom_opt and area [MW/km2]
      - p_nom_opt_max_ratio : ration between p_nom_opt and p_nom_max [-]

    The gdf is provided in Plate Carrée crs('4036')    
    """

    ##### Get df with generators info
    gg = n.generators
    # filter carrier
    df = gg[gg['carrier']==carrier]
    # remove zero_capacities
    df = df.loc[ df['p_nom']>0 , ['carrier', 'bus', 'p_nom', 'p_nom_max', 'p_nom_opt']]



    ##### Get gdf with regions 
    gdf = gpd.read_file(path_regions+file_regions)

    gdf.rename(columns={'name': 'bus'}, inplace=True)


    ##### Select just some columns
    gdf = gdf[['bus', 'geometry']]


    # Add area [km2]
    gdf_area = gdf.to_crs(3035)
    gdf['area'] = gdf_area.area/1e6

 
    ##### Merge df and gdf
    gdf_network_generators =  pd.merge(gdf,df, on='bus')

    ##### Add p_nom_density 
    gdf_network_generators['p_nom_density'] = gdf_network_generators['p_nom'] / gdf_network_generators['area']

    ##### Add p_nom_max_density
    gdf_network_generators['p_nom_max_density'] = gdf_network_generators['p_nom_max'] / gdf_network_generators['area']

    ##### Add p_nom_max_ratio
    gdf_network_generators['p_nom_max_ratio'] = gdf_network_generators['p_nom'] / gdf_network_generators['p_nom_max']

    ##### Add p_nom_opt_density 
    gdf_network_generators['p_nom_opt_density'] = gdf_network_generators['p_nom_opt'] / gdf_network_generators['area']

    ##### Add p_nom_opt_max_ratio
    gdf_network_generators['p_nom_opt_max_ratio'] = gdf_network_generators['p_nom_opt'] / gdf_network_generators['p_nom_max']



    return gdf_network_generators



