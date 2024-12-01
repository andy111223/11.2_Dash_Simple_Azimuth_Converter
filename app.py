import dash
from dash import dcc, html
from dash.dependencies import Input, Output

# Create the app
app = dash.Dash()

# Create the layout
app.layout = html.Div(
    style={
        'background-color': '#0d1117',  # Night military theme background
        'color': '#c9d1d9',  # Text color
        'height': '100vh',
        'display': 'flex',
        'flex-direction': 'column',
        'justify-content': 'center',
        'align-items': 'center',
        'font-family': 'Arial, sans-serif'
    },
    children=[
        # Column 1
        html.Div(
            style={
                'width': '60%',
                'border': '2px solid #58a6ff',
                'border-radius': '10px',
                'padding': '20px',
                'text-align': 'center',
                'margin-bottom': '20px'
            },
            children=[
                html.H2(
                    'Topographic to Magnetic',
                    style={'font-size': '30px', 'color': '#58a6ff'}
                ),
                dcc.Input(
                    id='topo-input',
                    type='number',
                    min=0,
                    max=360,
                    placeholder='Enter topographic azimuth',
                    style={
                        'width': '70%',
                        'font-size': '30px',
                        'padding': '10px',
                        'margin-bottom': '10px',
                        'background-color': '#161b22',
                        'color': '#ffffff',
                        'border': '2px solid #58a6ff',
                        'border-radius': '5px',
                        'box-sizing': 'border-box'
                    }
                ),
                html.Label(
                    'minus 6°',
                    style={
                        'font-size': '30px',
                        'color': '#58a6ff',
                        'margin-top': '10px',
                        'display': 'block'
                    }
                ),
                html.Div(style={'height': '10px'}),  # Empty line for spacing
                html.Div(
                    id='mag-output',
                    style={'font-size': '40px', 'margin-top': '10px', 'color': '#ff7b72'}
                )
            ]
        ),
        # Column 2
        html.Div(
            style={
                'width': '60%',
                'border': '2px solid #58a6ff',
                'border-radius': '10px',
                'padding': '20px',
                'text-align': 'center',
                'margin-bottom': '20px'
            },
            children=[
                html.H2(
                    'Magnetic to Topographic',
                    style={'font-size': '30px', 'color': '#58a6ff'}
                ),
                dcc.Input(
                    id='mag-input',
                    type='number',
                    min=0,
                    max=360,
                    placeholder='Enter magnetic azimuth',
                    style={
                        'width': '70%',
                        'font-size': '30px',
                        'padding': '10px',
                        'margin-bottom': '10px',
                        'background-color': '#161b22',
                        'color': '#ffffff',
                        'border': '2px solid #58a6ff',
                        'border-radius': '5px',
                        'box-sizing': 'border-box'
                    }
                ),
                html.Label(
                    'plus 6°',
                    style={
                        'font-size': '30px',
                        'color': '#58a6ff',
                        'margin-top': '10px',
                        'display': 'block'
                    }
                ),
                html.Div(style={'height': '10px'}),  # Empty line for spacing
                html.Div(
                    id='topo-output',
                    style={'font-size': '40px', 'margin-top': '10px', 'color': '#ff7b72'}
                )
            ]
        ),
        # Message below the columns
        html.Div(
            'Valid for Olsztyn areas in 2025',
            style={
                'font-size': '20px',
                'color': '#8b949e',
                'margin-top': '20px',
                'text-align': 'center'
            }
        )
    ]
)


# Callbacks
@app.callback(
    Output('mag-output', 'children'),
    [Input('topo-input', 'value')]
)
def topographic_to_magnetic(topo_azimuth):
    if topo_azimuth is None or topo_azimuth < 0 or topo_azimuth > 360:
        return "Enter a valid azimuth"
    return f"{(topo_azimuth - 6) % 360}°"  # Subtract 6 and wrap around 360 if needed

@app.callback(
    Output('topo-output', 'children'),
    [Input('mag-input', 'value')]
)
def magnetic_to_topographic(mag_azimuth):
    if mag_azimuth is None or mag_azimuth < 0 or mag_azimuth > 360:
        return "Enter a valid azimuth"
    return f"{(mag_azimuth + 6) % 360}°"  # Add 6 and wrap around 360 if needed


# Run the server
if __name__ == '__main__':
    app.run_server()
