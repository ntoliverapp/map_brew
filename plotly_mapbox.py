import plotly.express as px

import pandas as pd
bmp_data = "...map.csv"
bmp_df = pd.read_csv(bmp_data)
bmp_df

api_token =''

fig = px.scatter_mapbox(bmp_df, hover_name='Name', hover_data=['Address', 'City', 'State', 'Zip','Website', 'Phone' ],lat='Latitude', lon="Longitude", zoom=3.5, center = {"lat": 38.8880671, "lon": -98.8539725}, color_continuous_scale=['red', 'black'], color="State",size_max=30, height=700, width=1350, title='Breweries across the US',
                       )
fig.update_layout(font_size=16,  title={'xanchor': 'center','yanchor': 'top', 'y':0.95, 'x':0.5,}, title_font_size = 24, mapbox_accesstoken=api_token, mapbox_style = "mapbox://styles/ntoliverapp/ckwu41ke5748m14oyacujuiqb")
fig.update_traces(marker=dict(size=6))
fig.write_image('map_brew.png')
# # fig.write_image('map_brew.pdf')
fig.write_html('map_brew.html')
# fig.show()