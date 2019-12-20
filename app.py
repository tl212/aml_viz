import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()
app.layout = html.Div(children=[
    html.H1('Azerbaijani Laundromat Interact Visualization Pilot'),
    dcc.Graph(id='example',
    figure ={
        'data': [
            {'x':[1,2,3,4,5], 'y':[5,6,7,2,1], 'type':'line', 'name':'ML ALERT'},
            {'x':[1,2,3,4,5], 'y':[8,3,2,3,5], 'type':'bar', 'name':'Number of Transactions'},
            ],
        'layout': {
            'title':'Danske EE branch - Metastar Daily Transactions Example'
            }
        })
    ])

if __name__ == '__main__':
    app.run_server(debug=True)

    