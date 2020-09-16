import plotly.graph_objects as go
import pandas as pd 

import plotly.express as px  # (version 4.7.0)
import plotly.graph_objects as go

import json
import dash
from urllib.request import urlopen
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output

#with open('datos.csv') as cali_json:
#   datos = cali_json.read_
cali =  "https://raw.githubusercontent.com/spencerlawrence36/basic/master/places.csv"

#with urlopen('https://gist.githubusercontent.com/john-guerra/43c7656821069d00dcbc/raw/be6a6e239cd5b5b803c6e7c2ec405b793a9064dd/Colombia.geo.json') as response:
#    counties = json.load(response)
#cali = json.loads('map_cali.geojson')
#locs = ['VALLE DEL CAUCA']
#for loc in counties['features']:
#    loc['id'] = loc['properties']['NOMBRE_DPT']
#-----------------------------------------------------
app = dash.Dash(__name__)
df = pd.read_csv("datos.csv")

df = df.groupby(['Id_barrio', 'Cod_barrio', 'Cod_comuna', 'Nombre', 'Perimetro (m)'])[['Area (ha)']].mean()
df.reset_index(inplace=True)
print(df[:5])

app.layout = html.Div([

##------------------------------------------------------------


    html.H1("heat map politicians Cali hbtn ", style={'text-align': 'center'}),

    dcc.Dropdown(id="demo-dropdown",
                 options=[
                     {"label": "Armitage", "value": "Armitage"},
                     {"label": "Ospina", "value": "ospina"},
                     {"label": "Eder", "value": "Eder"},
                     {"label": "Chonto", "value": "Chontico"}],
                 multi=False,
                 value="Barrios",
                 style={'width': "40%"}
                 ),

    html.Div(id='output_container', children=[]),
    html.Br(),

    dcc.Graph(id='datos', figure={})

])

##------------------------------------------------------------

##----------------------------------------------------

@app.callback(
    [Output(component_id='output_container', component_property='children'),
     Output(component_id='datos', component_property='figure')],
    [Input(component_id='demo-dropdown', component_property='value')]
)
def update_graph(option_slctd):
    print(option_slctd)
    print(type(option_slctd))

    container = "elige: {}".format(option_slctd)

    dff = df.copy()
    dff = dff[dff["Nombre"] == option_slctd]
    dff = dff[dff["Nombre"] == "Cod_comuna"]
    
#------------------------------------------------------

#----------------------------------------------------------
    #this is my map working
    fig = go.Figure(data=[go.Scattermapbox(
                        #lon=datos[lng],
                        #lat=datos[lat],
                        lat=[3.4616, 3.4716, 3.4728, 3.4730, 3.4745], # tabla_candidato[lat]
                        lon=[-76.5520, -76.5600, -76.5540, -76.5560, -76.5550],  # tabla_candidado[lon]
                        mode='markers + text',
                        marker=dict(size=15, color=['red', 'orange', 'yellow', 'orange', 'red'], opacity=0.5),
                        text='aquí está nuestro politico'
                        
                        ##----- get color scale here ------
                        
                        # se debe relacionar las columnas lat y long vs el valor a comparar 
                        # ese valor debe estar entre la escala min y max y apartir de ahi
                        # se distribuye la tonalidad 
                        
                        #color =tabla_candidato['votos'],
                        #colorscale= 'YlOrRd',
                        #showscale=True,
                        #cmax=200,
                        #cmin=0,
                        ##------------
                        
    )])
    name="aquí"

    fig.update_layout(
        margin={"r":100,"t":80,"l":100,"b":100},
        hovermode='closest',
        #hoverinfo = "Barrio",
        #color_discrete_sequence=["fuchsia"],
        #hover_name="Barrio",
        #hover_data=["State", "Population"],
        mapbox=go.layout.Mapbox(
            style="stamen-terrain", 
            zoom=12, 
            center_lat = 3.4516,
            center_lon = -76.5320,
            layers=[{
                'sourcetype': 'geojson',
                'source': cali,
                'type': 'line', 
            }]
    
        )
    
    )
    #--------------------------------------------------------------
    #fig.show()
    
    return container, fig

if __name__ == '__main__':
   app.run_server(debug=True)
