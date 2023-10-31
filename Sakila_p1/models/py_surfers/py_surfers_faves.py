import pandas

def model(dbt, session):
    # Must be either table or incremental (view is not currently supported)
    dbt.config(materialized = "table")

    # DataFrame representing an upstream model
    #df = dbt.ref("my_first_dbt_model")
    data = {
    'Surfer': ['KellyS','KellyA', 'Tommy', 'Ed', 'Jon'],
    'Rating': ['A', 'B', 'C', 'D', 'E'],
    'Waves': [10.5, 20.3, 15.2, 8.7, 12.0]
    }

    # Create a DataFrame
    df = pandas.DataFrame(data)
 
    return df
    