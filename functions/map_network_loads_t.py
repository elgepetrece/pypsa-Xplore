

from .gdf_network_loads_t import gdf_network_loads_t



def map_network_loads_t(n, feature, ax, gdf_regions, params, params_local):
    """
    This function plots load features in the geometry of a network.

    Features:
      - area
      - annual_load         : [TWh]
      - annual_load_density : [GWh/km2]      
    """

    gdf = gdf_network_loads_t(n, gdf_regions)



    ##### Fix params_local
    if params_local['vmin']=='':
        params_local['vmin'] = gdf[feature].min()

    if params_local['vmax']=='':
        params_local['vmax'] = gdf[feature].max()



    ##### Plot in map
    gdf.plot(ax=ax, column=feature, 
             cmap=params['cmap'], edgecolor=params['edgecolor'], lw=params['lw'],
             vmin=params_local['vmin'], vmax=params_local['vmax'], 
             legend=True)


    if feature=='area':
        total = gdf[feature].sum()
        ax.set_title(f'Area. Total: {total:.2f} km2')

    if feature=='annual_load':
        total = gdf[feature].sum()
        ax.set_title(f'Annual load. Total: {total:.2f} TWh')        

    if feature=='annual_load_density':
        ax.set_title(f'Annual load density [GWh/km2]')



