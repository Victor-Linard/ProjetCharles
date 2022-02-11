import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output


from app import app
from app import server

from apps import register, login, application

app.layout = html.Div(children=[
    dcc.Location(id='url', refresh=False),
    dcc.Store(id='pseudo', storage_type='local', clear_data=False),
    dcc.Store(id='refresh', data=0, storage_type='memory'),
    html.Div(id="page-content", children=[])
])


@app.callback(Output(component_id="page-content", component_property='children'),
                Input(component_id='url', component_property='pathname'),)
def display_page(pathname):
    if pathname == '/login':
        return login.layout
    if pathname == '/register':
        return register.layout
    if pathname == '/compte':
        return application.layout
    else:
        return login.layout

if __name__ == '__main__':
    app.run_server(debug=True)