import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State

import re

from app import app

from apps import Compte

layout = html.Div(children=[
    html.Header(children=[
        html.Meta(charSet="utf-8"),
        html.Meta(name="viewport", content="width=device-width, initial-scale=1"),
        html.Link(rel="stylesheet", href="./assets/css/libs.bundle.css"),
        html.Link(rel="stylesheet", href="./assets/css/index.bundle.css"),
        html.Title("Register"),
    ]),
    html.Section(className="bg-black overflow-hidden", children=[
        html.Div(className="py-15 py-xl-20 d-flex flex-column container level-3 min-vh-100", children=[
            html.Div(className="row align-items-center justify-content-center my-auto", children=[
                html.Div(className="col-md-10 col-lg-8 col-xl-5", children=[
                    html.Div(className="card", children=[
                        html.Div(className="card-header bg-white text-center pb-0", children=[
                            html.H5(className="fs-4", children="Register"),
                        ]),
                        html.Div(className="card-body bg-white", children=[
                            html.Div(id="wrong_register", children=[]),
                            html.Form(children=[
                                html.Div(className="form-floating mb-2", children=[
                                    dcc.Input(type="text", className="form-control", id="floatinglastname", placeholder="Lastname"),
                                    html.Label(htmlFor = "floatinglastname", children = "Lastname"),
                                ]),
                                html.Div(className="form-floating mb-2", children=[
                                    dcc.Input(type="text", className="form-control", id="floatingfirstname", placeholder="Firstname"),
                                    html.Label(htmlFor ="floatingfirstname", children="Firstname"),
                                ]),
                                html.Div(className="form-floating mb-2", children=[
                                    dcc.Input(type="text", className="form-control", id="floatingpseudo", placeholder="Pseudo"),
                                    html.Label(htmlFor ="floatingpseudo", children="Pseudo"),
                                ]),
                                html.Div(className="form-floating mb-2", children=[
                                    dcc.Input(type="email", className="form-control", id="floatingemail", placeholder="Email", style={}),
                                    html.Label(htmlFor ="floatingemail", children="E-mail"),
                                ]),
                                html.Div(className="form-floating mb-2", children=[
                                    dcc.Input(type="password", className="form-control", id="floatingPassword", placeholder="Password"),
                                    html.Label(htmlFor="floatingPassword", children="Password"),
                                ]),
                                html.Div(className="form-floating mb-2", children=[
                                    dcc.Input(type="password", className="form-control", id="floatingConfirmationPassword", placeholder="Confirmation Password", style={}),
                                    html.Label(htmlFor="floatingConfirmationPassword", children="Confirmation Password"),
                                ]),
                                html.Div(className="d-grid mb-2", children=[
                                    html.A(className="btn btn-lg btn-primary", children="Create Account", id="btn_register"),
                                ]),
                            ]),
                        ]),
                        html.Div(className="card-footer bg-opaque-black inverted text-center", children=[
                            html.P(className="text-secondary", children="Already have an account?"),
                            html.A(href="sign-in", className="underline", children="Sign In"),
                        ]),
                    ]),
                ]),
            ]),
        ]),
        html.Figure(className="background background-overlay", style={"background-image": "url('./assets/images/small-3.jpg')"}),
    ]),
    html.Script(src="../assets/js/vendor.bundle.js"),
    html.Script(src="../assets/js/index.bundle.js"),
])


@app.callback(Output("wrong_register", 'children'),
              Input(component_id='btn_register', component_property='n_clicks'),
              State('floatinglastname', 'value'),
              State('floatingfirstname', 'value'),
              State('floatingpseudo', 'value'),
              State('floatingemail', 'value'),
              State('floatingPassword', 'value'),
              Input('floatingConfirmationPassword', 'value'))
def regsiter(click, lastname, firstname, pseudo, email, password, cmdp):
    if click is not None:
        print(lastname, firstname, pseudo, email, password)
        if lastname is None or lastname == '':
            html_output_register = []
            html_output_register.append(
                html.Div(className="alert alert-danger", role="alert",
                         children="Création du compte impossible, merci de renseigner votre nom"))
            return html_output_register
        elif firstname is None or firstname == '':
            html_output_register = []
            html_output_register.append(
                html.Div(className="alert alert-danger", role="alert",
                         children="Création du compte impossible, merci de renseigner votre prénom"))
            return html_output_register
        elif pseudo is None or pseudo == '':
            html_output_register = []
            html_output_register.append(
                html.Div(className="alert alert-danger", role="alert",
                         children="Création du compte impossible, merci de renseigner votre pseudo"))
            return html_output_register
        elif email is None or not re.match("^[a-z0-9-_]+[\._]?[a-z0-9]+[@][a-z0-9-_]+[.]\w{2,3}$", email,):
            html_output_register = []
            html_output_register.append(
                html.Div(className="alert alert-danger", role="alert",
                         children="Création du compte impossible, e-mail incorrect"))
            return html_output_register
        elif password is None or cmdp is None or password != cmdp:
            html_output_register = []
            html_output_register.append(
                html.Div(className="alert alert-danger", role="alert",
                         children="Création du compte impossible, mot de passes différents"))
            return html_output_register
        elif not Compte.creation_de_compte(lastname, firstname, pseudo, email, password):
            html_output_register = []
            html_output_register.append(
                html.Div(className="alert alert-danger", role="alert", children="Création du compte impossible, Pseudo déjà utilisé"))
            print(html_output_register)
            print("Je passe dans le click")
            return html_output_register
        else:
            html_output_register = []
            html_output_register.append(
                html.Div(className="alert alert-success", role="alert", children=[
                    html.H4(className="alert-heading", children="Compte Créé"),
                    html.A(href="sign-in", className="underline", children="Connectez-vous")
                ]))
            print(html_output_register)
            return html_output_register


@app.callback(Output('floatingConfirmationPassword', 'style'),
            Input(component_id='floatingPassword', component_property='value'),
            Input(component_id='floatingConfirmationPassword', component_property='value'))
def verif_mdp(mdp, cmdp):
    if mdp is not None and mdp == cmdp:
        html_output_mdp = {"border":"3px solid green"}
        print("je passe dans le mot de passe(identique)")
        return html_output_mdp
    elif mdp is not None and cmdp is not None:
        html_output_mdp = {"border": "3px solid red"}
        print("Mot de passe non identique")
        return html_output_mdp


@app.callback(Output('floatingemail', 'style'),
              Input('floatingemail', 'value'))
def verif_adresse_mail(mail):
    if mail is not None and re.match("^[a-z0-9-_]+[\._]?[a-z0-9]+[@][a-z0-9-_]+[.]\w{2,3}$", mail,):
        html_output_email = {"border": "3px solid green"}
        return html_output_email
    elif mail is not None:
        html_output_email = {"border": "3px solid red"}
        return html_output_email
