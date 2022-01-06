import plotly.express as px

import pandas as pd
bmp_data = "...maps.csv"
bmp_df = pd.read_csv(bmp_data)
bmp_df

api_token =''

fig = px.scatter_mapbox(bmp_df, hover_name='Name', hover_data=['Address', 'City', 'State', 'Zip','Website', 'Phone' ],lat='Longitude', lon="Latitude", zoom=2, center = {"lat": 37.0902, "lon": -95.7129}, color_continuous_scale=['red', 'black'], color="State",size_max=30,   title='Breweries across the US',
                       )
fig.update_layout(font_size=16,  title={'xanchor': 'center','yanchor': 'top', 'y':0.95, 'x':0.5,}, title_font_size = 24, mapbox_accesstoken=api_token, mapbox_style = "mapbox://styles/ntoliverapp/ckwu41ke5748m14oyacujuiqb")
fig.update_traces(marker=dict(size=6))
# fig.write_image('map_brew.png')
# fig.write_image('map_brew.pdf')
# fig.write_html('map_brew.html')
fig.show()