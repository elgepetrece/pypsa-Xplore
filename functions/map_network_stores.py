

from .gdf_network_stores import gdf_network_stores



def map_network_stores(carrier, n, feature, ax, gdf_regions, params, params_local):
    """
    This function plots store features for a specific carrier
    in the geometry of a network.

    Features:
      - area
      - e_nom_opt           : optimal energy capacity [GWh]
    """

    gdf = gdf_network_stores(carrier, n, gdf_regions)



    ##### Fix params_local
    if not params_local['vmin']:
        params_local['vmin'] = gdf[feature].min()

    if not params_local['vmax']:
        params_local['vmax'] = gdf[feature].max()



    ##### Plot in map
    gdf.plot(ax=ax, column=feature, 
             cmap=params['cmap'], edgecolor=params['edgecolor'],
             vmin=params_local['vmin'], vmax=params_local['vmax'], 
             legend=True)


    if feature=='area':
        total = gdf[feature].sum()
        ax.set_title(f'Area. Total: {total:.2f} km2')

    if feature=='e_nom_opt':
        total = gdf[feature].sum()
        ax.set_title(f'{carrier} : Optimal energy storage. Total: {total:.2f} GWh')        

