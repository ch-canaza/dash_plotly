#!/usr/bin/python3
import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()
app.layout = html.Div([
    dcc.Graph(figure=fig)
])

app.run_server(debug=True, use_reloader=False)  # Turn off reloader if inside Jupyter
# #with open("datos.csv") as f:
#     lis = [line.split(",") for line in f]        # create a list of lists
#     for i, x in enumerate(lis):              #print the list items 
#         #print (x[1])
#         for k in x:
#             print (k)
