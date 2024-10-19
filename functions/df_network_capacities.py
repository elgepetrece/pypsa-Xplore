

import pandas as pd


def df_network_capacities(n):
    """
    This function provides a df with 2 columns, "Initial_capacity" and "Optimal_capacity".
    
    The rows cover all the carriers included in:
      - n.generators
      - n.links
      - n.storage_units

    For some link carriers ('CCGT', 'OCGT', 'H2 Fuel Cell', 'battery discharger'), the capacity 
    was multiplied by the efficiency to reflect the 'electrical' capacity (for these links, the
    end point of the link).
    """

    ##### Generators
    gg = n.generators

    gg_summary = gg.groupby('carrier').agg(
                    Initial_capacity=pd.NamedAgg(column='p_nom', aggfunc='sum'),
                    Optimal_capacity=pd.NamedAgg(column='p_nom_opt', aggfunc='sum'),
                    )


    ##### Links
    lk = n.links

    lk_summary = lk.groupby('carrier').agg(
                    Initial_capacity=pd.NamedAgg(column='p_nom', aggfunc='sum'),
                    Optimal_capacity=pd.NamedAgg(column='p_nom_opt', aggfunc='sum'),
                    )

    for carrier in ['CCGT', 'OCGT', 'H2 Fuel Cell', 'battery discharger']:
        if carrier in lk_summary.index:
            eff = lk.loc[lk['carrier']==carrier, 'efficiency'].unique()[0]
            lk_summary.loc[carrier, 'Initial_capacity'] = lk_summary.loc[carrier, 'Initial_capacity']*eff
            lk_summary.loc[carrier, 'Optimal_capacity'] = lk_summary.loc[carrier, 'Optimal_capacity']*eff


    ##### Storage units
    su = n.storage_units


    su_summary = su.groupby('carrier').agg(
                    Initial_capacity=pd.NamedAgg(column='p_nom', aggfunc='sum'),
                    Optimal_capacity=pd.NamedAgg(column='p_nom_opt', aggfunc='sum'),
    )


    ##### Join
    df = pd.concat([gg_summary, lk_summary, su_summary])


    return df
