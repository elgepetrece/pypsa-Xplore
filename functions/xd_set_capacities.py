
import pypsa
import xarray as xr
import numpy as np
from .df_network_capacities import df_network_capacities



def xd_set_capacities(rootpath, dic_lists):
    
    ##### Unwrap dic_lists
    prefix_list = dic_lists['prefix_list']
    name_list = dic_lists['name_list']
    simpl_list = dic_lists['simpl_list']
    clusters_list = dic_lists['clusters_list']
    ll_list = dic_lists['ll_list']
    opts_list = dic_lists['opts_list']
    sector_opts_list = dic_lists['sector_opts_list']
    horizons_list = dic_lists['horizons_list']
    carrier_list = dic_lists['carrier_list']


    ##### Initial values
    initial_values = np.zeros([len(prefix_list),
                               len(name_list),
                               len(simpl_list),
                               len(clusters_list),
                               len(ll_list),
                               len(opts_list),
                               len(sector_opts_list),
                               len(horizons_list),
                               len(carrier_list),
                               ])


    ##### Create xd array
    xd = xr.Dataset(
        {
        'Initial_capacity': (['prefix', 'name', 'simpl', 'clusters', 'll',
                              'opts', 'sector_opts', 'horizons', 'carrier'], 
                              initial_values),
        'Optimal_capacity': (['prefix', 'name', 'simpl', 'clusters', 'll',
                              'opts', 'sector_opts', 'horizons', 'carrier'], 
                              initial_values),
        },
        coords={
            'prefix': prefix_list,
            'name': name_list,
            'simpl': simpl_list,
            'clusters': clusters_list,
            'll': ll_list,
            'opts': opts_list,
            'sector_opts': sector_opts_list,
            'horizons': horizons_list,
            'carrier': carrier_list
        }
    )
        
        
    ##### Add values
    
    for prefix in prefix_list:
        
        for name in name_list:
            
            for simpl in simpl_list:
                
                for clusters in clusters_list:
                    
                    for ll in ll_list:
                        
                        for opts in opts_list:
                            
                            for sector_opts in sector_opts_list:
                                
                                for horizons in horizons_list:
                                    

                                    ### Load network
                                    file = f'elec_s{simpl}_{clusters}_l{ll}_{opts}_{sector_opts}_{horizons}.nc'
                                    path = f'{rootpath}/results/{prefix}/{name}/postnetworks/'

                                    n = pypsa.Network(path+file)


                                    ### Get capacities            
                                    df = df_network_capacities(n)

                                    for carrier in carrier_list:

                                        xd['Initial_capacity'].loc[prefix, name, simpl, clusters, ll, opts, sector_opts, horizons, carrier] = df.loc[carrier, 'Initial_capacity']
                                        xd['Optimal_capacity'].loc[prefix, name, simpl, clusters, ll, opts, sector_opts, horizons, carrier] = df.loc[carrier, 'Optimal_capacity']


    ##### Remove dimensions with one single value
    xd = np.squeeze(xd)


    ##### Remove coordinates with one single value
    for coord in xd.coords:        
        unique_values = xd.coords[coord].values    
        if len(np.unique(unique_values)) == 1:
            xd = xd.drop_vars(coord)

    return xd





   


