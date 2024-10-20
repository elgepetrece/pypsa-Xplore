
import xarray as xr
import numpy as np
import pandas as pd



def xd_csv_prices(rootpath, dic_lists):

    """ This function is a draft, it wouldn't work with more complex csv files"""
    
    ##### Unwrap dic_lists
    prefix_list = dic_lists['prefix_list']
    name_list = dic_lists['name_list']
    simpl_list = dic_lists['simpl_list']
    clusters_list = dic_lists['clusters_list']
    ll_list = dic_lists['ll_list']
    opts_list = dic_lists['opts_list']
    sector_opts_list = dic_lists['sector_opts_list']
    horizons_list = dic_lists['horizons_list']


    ##### Initial values
    initial_values = np.zeros([len(prefix_list),
                               len(name_list),
                               len(simpl_list),
                               len(clusters_list),
                               len(ll_list),
                               len(opts_list),
                               len(sector_opts_list),
                               len(horizons_list),
                               ])


    ##### Create xd array
    xd = xr.Dataset(
        {
        #'AC':               (['prefix', 'name', 'simpl', 'clusters', 'll',
        #                      'opts', 'sector_opts', 'horizons'], 
        #                      initial_values),
        'co2':              (['prefix', 'name', 'simpl', 'clusters', 'll',
                              'opts', 'sector_opts', 'horizons'], 
                              initial_values),
        #'co2 stored':       (['prefix', 'name', 'simpl', 'clusters', 'll',
        #                      'opts', 'sector_opts', 'horizons'], 
        #                      initial_values),
        #'co2 sequestered':  (['prefix', 'name', 'simpl', 'clusters', 'll',
        #                      'opts', 'sector_opts', 'horizons'], 
        #                      initial_values),    
        #'gas':              (['prefix', 'name', 'simpl', 'clusters', 'll',
        #                      'opts', 'sector_opts', 'horizons'], 
        #                      initial_values),   
        #'H2':               (['prefix', 'name', 'simpl', 'clusters', 'll',
        #                      'opts', 'sector_opts', 'horizons'], 
        #                      initial_values),    
        #'battery':          (['prefix', 'name', 'simpl', 'clusters', 'll',
        #                      'opts', 'sector_opts', 'horizons'], 
        #                      initial_values),                                                                                                                     
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
        }
    )
        
        
    ##### Add values
    
    for prefix in prefix_list:
        
        for name in name_list:

            ### Load csv
            file = f'prices.csv'
            path = f'{rootpath}/results/{prefix}/{name}/csvs/'

            df = pd.read_csv(path+file, index_col=0, header=None, names=['var', 'Value'])


            
            for simpl in simpl_list:
                
                for clusters in clusters_list:
                    
                    for ll in ll_list:
                        
                        for opts in opts_list:
                            
                            for sector_opts in sector_opts_list:
                                
                                for horizons in horizons_list:

                                    ### Introduce data
                                    #for variable in list(xd.data_vars):
                                    #    print(f'1: {variable}')
                                    #    value = pd.to_numeric(df.loc[variable, 'Value'])
                                    #    print(f'2: {value}')
                                    #    xd[variable].loc[prefix, name, simpl, clusters, ll, opts, sector_opts, horizons] = value
                                    #    print(f'3: {xd.values}')
                                    value = pd.to_numeric(df.loc['co2', 'Value'])
                                    xd['co2'].loc[prefix, name, simpl, clusters, ll, opts, sector_opts, horizons] = value
                                    


    ##### Remove dimensions with one single value
    xd = np.squeeze(xd)


    ##### Remove coordinates with one single value
    for coord in xd.coords:        
        unique_values = xd.coords[coord].values    
        if len(np.unique(unique_values)) == 1:
            xd = xd.drop_vars(coord)


    return xd





   


