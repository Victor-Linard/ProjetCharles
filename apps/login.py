# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State

from app import app
from apps import connexion
#Creation de la page WEB Login, creation de la variable layout qui prend toutes les variables de la page HTML
layout = html.Div(children=[
    #En-tête de la page HTML
    html.Header(children=[
        html.Meta(charSet="utf-8"),
        html.Meta(name="viewport", content="width=device-width, initial-scale=1"),
        html.Link(rel="stylesheet", href="./assets/css/libs.bundle.css"),
        html.Link(rel="stylesheet", href="./assets/css/index.bundle.css"),
        html.Title("Sign in")
    ]),
    #section de la page qui contient toutes les DIV de la page Login permettant ainsi d'organiser la page et d'appliquer les classes du bootstrap
    html.Section(className="bg-black overflow-hidden", children=[
        html.Div(className="py-15 py-xl-20 d-flex flex-column container level-3 min-vh-100", children=[
            html.Div(className="row align-items-center justify-content-center my-auto", children=[
                html.Div(className="col-md-10 col-lg-8 col-xl-5", children=[
                    html.Div(className="card", children=[
                        html.Div(className="card-header bg-white text-center pb-0", children=[
                            html.H5(className="fs-4 mb-1", children="Sign In", id='titre_page'),
                        ]),
                        html.Div(className="card-body bg-white", children=[
                            #Div qui est utilisé ensuite lors des callback plus loin pour mettre à jour la page en fonction du retour des fonctions de connexions
                            html.Div(id="wrong_info", children=[]),
                            #Div qui permet de mettre en forme le premier input de la page login (le pseudo)
                            html.Div(children=[
                                html.Div(className="form-floating mb-2", children=[
                                    dcc.Input(type="text", className="form-control", id="floatingpseudosignin", placeholder="Pseudo"),
                                    html.Label(htmlFor="floatingpseudosignin", children="Pseudo"),
                                ]),
                                #Div qui met en place le second input avec le mot de passe.
                                html.Div(className="form-floating mb-2", children=[
                                    dcc.Input(type="password", className="form-control", id="floatingPassword", placeholder="Password"),
                                    html.Label(htmlFor="floatingPassword", children="Password"),
                                ]),
                                 html.Div(className="d-grid mb-2", children=[
                                    html.A(className="btn btn-lg btn-primary", id="btn_login", children="Sign In"),
                                ]),
                                #pas mis en place encore
                                #html.Div(className="row", children=[
                                    #html.Div(className="col text-end", children=[
                                        #html.A(href="forgot-password.html", className="underline small", children="Forgot Password"),
                                    #]),
                                #]),
                            ]),
                        ]),
                        #permet de faire apparaitre la petite div en bas de la page qui permet à l'utilisateur de se connecter si besoin
                        html.Div(className="card-footer bg-opaque-black inverted text-center", children=[
                            html.P(className="text-secondary", children="Don't have an account yet?"),
                            html.A(href="register", className="underline", children="Register"),
                        ]),
                    ]),
                ]),
            ]),
        ]),
        #affiche la photo en background.
        html.Figure(className="background background-overlay", style={"background-image": "url('./assets/images/small-5.jpg')"}),
    ]),
    html.Script(src="../assets/js/vendor.bundle.js"),
    html.Script("./assets/js/index.bundle.js"),
])

#Partie callback : Cette partie permet de gérer les événements qui se passe sur la page :
# - le click sur le bouton Sign in


@app.callback(Output(component_id="wrong_info", component_property='children'),
              Output("url", "pathname"),
              Output('pseudo', 'data'),
              Input(component_id='btn_login', component_property='n_clicks'),
              State('floatingpseudosignin', 'value'),
              State('floatingPassword', 'value'),
              State('pseudo', 'data'))
def sign_in(click, pseudo, password, pseudo_state):
    if click is not None:
        if connexion.verification_compte_avant_connexion(pseudo, password) is False or connexion.verification_compte_avant_connexion(pseudo, password) == 0:
            html_output = []
            html_output.append(
                html.Div(className="alert alert-danger", role="alert", children="Wrong Username or Password"))
            return html_output, dash.no_update, dash.no_update

        else:
            return dash.no_update, "/compte", pseudo
    else:
        print("Sign in remise à zéro de pseudo store")
        return dash.no_update, dash.no_update, None

