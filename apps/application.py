import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State
import re

from app import app
from apps import connexion, Compte


layout = html.Div(id='div_page', children=[
    html.Header(children=[
        html.Meta(charSet="utf-8"),
        html.Meta(name="viewport", content="width=device-width, initial-scale=1"),
        html.Link(rel="stylesheet", href="./assets/css/libs.bundle.css"),
        html.Link(rel="stylesheet", href="./assets/css/index.bundle.css"),
        html.Title("Compte")
    ]),
    html.Div(className="bg-light", children=[
        html.Div(className="offcanvas-wrap", children=[
            html.Section(className="split", children=[
                html.Div(className="container", children=[
                    html.Div(className="row justify-content-between", children=[
                        html.Div(className="col-lg-9 split-content", children=[
                            html.Div(className="row", children=[
                                html.Div(className="col-lg-10", children=[
                                    html.H1(children="Welcome", id='titre'),
                                ]),
                            ]),
                            html.Div(id="info_changement", children=[]),
                            #debut DIV Profile
                            html.Section(children=[
                                html.Div(className="row", children=[
                                    html.H3(className="fs-4", children="Profile"),
                                    html.Div(className="col-lg-8", children=[
                                        html.Div(className="card bg-opaque-white", children=[
                                            html.Div(className="card-body bg-white", children=[
                                                html.Form(className="row g-2 g-lg-3", children=[
                                                    html.Div(className="col-md-6", children=[
                                                        html.Label(htmlFor="Firstname", className="form-label", children="Firstname"),
                                                        dcc.Input(type="text", className="form-control", id="Firstname", placeholder="Firstname"),
                                                    ]),
                                                    html.Div(className="col-md-6", children=[
                                                        html.Label(htmlFor="Lastname", className="form-label", children="Lastname"),
                                                        dcc.Input(type="text", className="form-control", id="Lastname", placeholder="Lastname"),
                                                    ]),
                                                    html.Div(className="col-md-12", children=[
                                                        html.Label(htmlFor="Pseudo", className="form-label", children="Pseudo"),
                                                        dcc.Input(type="text", className="form-control", id="Pseudo", placeholder="Pseudo", disabled="disabled"),
                                                    ]),
                                                    html.Div(className="col-md-12", children=[
                                                        html.Label(htmlFor="E-mail", className="form-label", children="E-mail"),
                                                        dcc.Input(type="text", className="form-control", id="E-mail", placeholder="E-mail", style={}),
                                                    ]),
                                                    html.Div(className="col-md-12", children=[
                                                        html.A(className="btn btn-primary", children="Update information", id="btn_update_information"),
                                                    ]),
                                                ]),
                                            ]),
                                        ]),
                                    ]),
                                    html.Div(className="col-lg-4", children=[
                                        html.Div(className="card border bg-white", children=[
                                            html.Div(className="card-body", children=[
                                                html.H5(className="card-title", children="Information"),
                                                html.Div(className="card-text", children="Nombre de connexion : ", style={"text-align":"center"}),
                                                html.Div(className="card-text", children=[], id="log_nb_connexion", style={"text-align":"center"}),
                                                html.Div(className="card-text", children="Dernière connexion le :  ", style={"text-align":"center"}),
                                                html.Div(className="card-text", children=[], id="log_derniere_connexion", style={"text-align":"center"}),
                                            ]),
                                         ]),
                                    ]),
                                ]),
                            ]),
                            html.Div(id="info_changement_mdp", children=[]),
                            #Debut DIV Password
                            html.Section(children=[
                                html.Div(className="row", children=[
                                    html.Div(className="col-lg-8", children=[
                                        html.H3(className="fs-4", children="Password"),
                                        html.Div(className="card bg-opaque-white", children=[
                                            html.Div(className="card-body bg-white", children=[
                                                html.Form(className="row g-2 g-lg-3", children=[
                                                    html.Div(className="col-md-12", children=[
                                                        html.Label(htmlFor="inputCurrentPass", className="form-label", children="Current Password"),
                                                        dcc.Input(type="password", className="form-control", id="inputCurrentPass"),
                                                    ]),
                                                    html.Div(className="col-md-12", children=[
                                                        html.Label(htmlFor="inputNewPass", className="form-label", children="New Password"),
                                                        dcc.Input(type="password", className="form-control", id="inputNewPass"),
                                                    ]),
                                                    html.Div(className="col-md-12", children=[
                                                        html.Label(htmlFor="inputRepeatNewPass", className="form-label", children="Repeat New Password"),
                                                        dcc.Input(type="password", className="form-control", id="inputRepeatNewPass"),
                                                    ]),
                                                    html.Div(className="col-md-12", children=[
                                                        html.A(className="btn btn-primary", children="Change Password", id="btn_change_pwd"),
                                                    ]),
                                                ]),
                                            ]),
                                        ]),
                                    ]),
                                ]),
                            ]),
                            html.Div(className="row", children=[
                                html.Div(className="col-md-6", children=[
                                    html.A(className="btn btn-danger", children="Delete Account",
                                           style={"margin-top": "10px"}, id='btn_delete_account', href="sign-in"),
                                ]),
                                html.Div(className="col-md-4", children=[
                                    html.A(className="btn btn-danger", children="Sign-out", style={"margin-top":"10px"}, id='btn_sign_out', href="sign-in"),
                                ]),
                            ]),
                        ]),
                    ]),
                ]),
            ]),
        ]),
    ]),
    #Javascript
    html.Script(src="../assets/js/vendor.bundle.js"),
    html.Script(src="../assets/js/index.bundle.js"),
])


@app.callback(Output('Firstname', 'placeholder'),
              Output('Lastname', 'placeholder'),
              Output('Pseudo', 'placeholder'),
              Output('E-mail', 'placeholder'),
              Output('refresh', 'data'),
              Output('div_page', 'children'),
              Output('info_changement', 'children'),
              Output('log_nb_connexion', 'children'),
              Output('log_derniere_connexion', 'children'),
              Input('div_page', 'children'),
              Input('btn_update_information', 'n_clicks'),
              State('pseudo', 'data'),
              State('refresh', 'data'),
              State('Firstname', 'value'),
              State('Lastname', 'value'),
              State('E-mail', 'value'))
def chargement_info(input, click, pseudo, refresh, firstname, lastname, mail):
    print("le pseudo :", pseudo)
    if pseudo is None or pseudo == '':
        print('Je suis dans le none')
        html_output = []
        html_output.append(html.Div(children=[
            html.Header(children=[
                html.Meta(charSet="utf-8"),
                html.Meta(name="viewport", content="width=device-width, initial-scale=1"),
                html.Link(rel="stylesheet", href="./assets/css/libs.bundle.css"),
                html.Link(rel="stylesheet", href="./assets/css/index.bundle.css"),
                html.Title("Compte")
            ]),
            html.Div(className='bg-red', children=[
                html.Section(className="inverted", children=[
                    html.Div(className="d-flex flex-column container min-vh-100 py-20", children=[
                        html.Div(
                            className="row align-items-center justify-content-center justify-content-lg-between my-auto",
                            children=[
                                html.Div(className="col-lg-6 order-lg-2", children=[
                                    html.Img(className="img-fluid", src="./assets/images/svg/404.svg", alt="Figure"),
                                ]),
                                html.Div(className="col-md-8 col-lg-5 order-lg-1 text-center text-lg-start", children=[
                                    html.H1(className="display-2", children=["Sorry, page not found"]),
                                    html.A(href="sign-in", className="btn btn-rounded btn-outline-white rounded-pill",
                                           children=["Go back to homepage"]),
                                ]),
                            ]),
                    ]),
                ]),
            ]),
            # Javascript
            html.Script(src="../assets/js/vendor.bundle.js"),
            html.Script(src="../assets/js/index.bundle.js")
        ])
        )
        return dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, html_output, dash.no_update
    else :
        nb_connection, last_connection = connexion.statconnexion(pseudo)
        last_connection = re.sub(":\d{2}.\d{6}", '', last_connection)
        print(last_connection)
        if click is not None:
            print("Je viens de clicquer sur le bouton mise à jour des infos")
            list = []
            if lastname is None or lastname == '':
                list.append(None)
            else:
                list.append(lastname)

            if firstname is None or firstname == '':
                list.append(None)
            else:
                list.append(firstname)

            if mail is None or mail == '':
                list.append(None)
            else:
                if mail is not re.match("^[a-z0-9-_]+[\._]?[a-z0-9]+[@][a-z0-9-_]+[.]\w{2,3}$", mail, ):
                    html_output_register = []
                    html_output_register.append(
                        html.Div(className="alert alert-danger", role="alert",
                                 children="Mise à jour de l'e-mail impossible, e-mail incorrect"))
                    return dash.no_update, dash.no_update,dash.no_update,dash.no_update,dash.no_update,dash.no_update,html_output_register, dash.no_update, dash.no_update
                else:
                    list.append(mail)
            if list.count(None) == 3:
                html_output = []
                return dash.no_update,dash.no_update,dash.no_update,dash.no_update,dash.no_update,dash.no_update,html_output, dash.no_update, dash.no_update
            else:
                if Compte.mis_a_jour_compte(list, pseudo) is True:
                    print(list, pseudo)
                    html_output = []
                    html_output.append(
                        html.Div(className="alert alert-success", role="alert", children=[
                            html.H4(className="alert-heading", children="Confirmation"),
                            html.P(children="Les informations ont été mise à jour")
                        ]))
                    info_user = connexion.infos_user(pseudo)
                    return info_user[1], info_user[0], info_user[3], info_user[2], dash.no_update, dash.no_update, html_output, nb_connection, last_connection
                else:
                    html_output = []
                    html_output.append(
                        html.Div(className="alert alert-danger", role="alert",
                                 children="Informations non mise à jour"))
                    return dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, html_output, dash.no_update, dash.no_update
        else:
            if refresh == 0 and pseudo is not None:
                info_user = connexion.infos_user(pseudo)
                return info_user[1], info_user[0], info_user[3], info_user[2], 1, dash.no_update, dash.no_update, nb_connection, last_connection
            else:
                print('je suis dans le else')
                return 'Firstname', 'Lastname', 'Pseudo', 'E-mail', dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update


@app.callback(Output('pseudo', 'clear_data'),
              Input('btn_sign_out', 'n_clicks'),
              State('pseudo', 'data'))
def deconnexion(click, pseudo):
    if click is not None:
        print('Je clear la data', pseudo)
        return True
    else:
        return dash.no_update


@app.callback(Output('info_changement_mdp', 'children'),
              Input('btn_change_pwd', 'n_clicks'),
              State('pseudo', 'data'),
              State('inputCurrentPass', 'value'),
              State('inputNewPass', 'value'),
              State('inputRepeatNewPass', 'value'))
def change_password(click, pseudo, pwd, npwd, cnpwd):
    if click is not None:
        print('Le click password fonctionne')
        print(pseudo, pwd, npwd, cnpwd)
        if pseudo is None or pseudo == '':
            print('Je suis dans le none')
            html_output = []
            html_output.append(html.Div(children=[
                html.Header(children=[
                    html.Meta(charSet="utf-8"),
                    html.Meta(name="viewport", content="width=device-width, initial-scale=1"),
                    html.Link(rel="stylesheet", href="./assets/css/libs.bundle.css"),
                    html.Link(rel="stylesheet", href="./assets/css/index.bundle.css"),
                    html.Title("Compte")
                ]),
                html.Div(className='bg-red', children=[
                    html.Section(className="inverted", children=[
                        html.Div(className="d-flex flex-column container min-vh-100 py-20", children=[
                            html.Div(
                                className="row align-items-center justify-content-center justify-content-lg-between my-auto",
                                children=[
                                    html.Div(className="col-lg-6 order-lg-2", children=[
                                        html.Img(className="img-fluid", src="./assets/images/svg/404.svg",
                                                 alt="Figure"),
                                    ]),
                                    html.Div(className="col-md-8 col-lg-5 order-lg-1 text-center text-lg-start",
                                             children=[
                                                 html.H1(className="display-2", children=["Sorry, page not found"]),
                                                 html.A(href="sign-in",
                                                        className="btn btn-rounded btn-outline-white rounded-pill",
                                                        children=["Go back to homepage"]),
                                             ]),
                                ]),
                        ]),
                    ]),
                ]),
                # Javascript
                html.Script(src="../assets/js/vendor.bundle.js"),
                html.Script(src="../assets/js/index.bundle.js")
            ])
            )
            return html_output
        elif npwd is None or cnpwd is None or cnpwd != npwd:
            html_output = []
            html_output.append(
                html.Div(className="alert alert-danger", role="alert",
                         children="Changement de mot de passe impossible, les nouveaux de passes ne sont pas identiques"))
            return html_output
        elif pwd is None or pwd == npwd:
            html_output = []
            html_output.append(
                html.Div(className="alert alert-danger", role="alert",
                         children="Changement de mot de passe impossible, ancien et nouveau mot de passe identique"))
            return html_output
        elif(pseudo is not None or pseudo != '') and Compte.changement_de_mot_passe(pseudo, pwd, npwd) is True:
            html_output = []
            html_output.append(
                html.Div(className="alert alert-success", role="alert", children=[
                    html.H4(className="alert-heading", children="Confirmation"),
                    html.P(children="Le mot de passe a été changé")
                ]))
            return html_output
        else:
            html_output = []
            html_output.append(
                html.Div(className="alert alert-danger", role="alert",
                         children="Changement de mot de passe impossible, erreur dans le mot de passe original"))
            return html_output
    else:
        print('Le click password fonctionne pas')
        return dash.no_update


@app.callback(Output('inputRepeatNewPass', 'style'),
                  Input(component_id='inputNewPass', component_property='value'),
                  Input(component_id='inputRepeatNewPass', component_property='value'))
def verif_mdp(mdp, cmdp):
    if mdp is not None and mdp == cmdp:
        html_output_mdp = {"border": "3px solid green"}
        print("je passe dans le mot de passe(identique)")
        return html_output_mdp
    elif mdp is not None and cmdp is not None:
        html_output_mdp = {"border": "3px solid red"}
        print("Mot de passe non identique")
        return html_output_mdp


@app.callback(Output('titre', 'children'),
              Input('btn_delete_account', 'n_clicks'),
              State('pseudo', 'data'))
def delete_account(click, pseudo):
    if click is not None:
        print("Click Suppresion compte")
        if Compte.supression_de_compte(pseudo) is True:
            print('Suppression du compte')
            return dash.no_update
        else:
            print('Erreur lors de la suppression du compte')
            print("Suppression du compte")
            return dash.no_update
    else:
        print("Non Suppression du compte")
        return dash.no_update


"""@app.callback(Output('info_changement', 'children'),
              Input('btn_update_information', 'n_clicks'),
              State('pseudo', 'data'),
              State('Firstname', 'value'),
              State('Lastname', 'value'),
              State('E-mail', 'value'))
def maj_information(click, pseudo, firstname, lastname, mail):
    if click is not None:
        list = []
        if lastname is None or lastname == '':
            list.append(None)
        else:
            list.append(lastname)

        if firstname is None or firstname == '':
            list.append(None)
        else:
            list.append(firstname)

        if mail is None or mail == '':
            list.append(None)
        else :
            if mail is not re.match("^[a-z0-9-_]+[\._]?[a-z0-9]+[@][a-z0-9-_]+[.]\w{2,3}$", mail,):
                html_output_register = []
                html_output_register.append(
                    html.Div(className="alert alert-danger", role="alert",
                             children="Création du compte impossible, e-mail incorrect"))
                return html_output_register
            else:
                list.append(mail)
        if list.count(None) == 3:
            html_output = []
            return html_output
        else:
            if Compte.mis_a_jour_compte(list, pseudo) is True:
                print(list, pseudo)
                html_output = []
                html_output.append(
                    html.Div(className="alert alert-success", role="alert", children=[
                        html.H4(className="alert-heading", children="Confirmation"),
                        html.P(children="Les informations ont été mise à jour")
                    ]))
                return html_output
            else:
                html_output = []
                html_output.append(
                    html.Div(className="alert alert-danger", role="alert",
                             children="Informations non mise à jour"))
                return html_output"""


@app.callback(Output('E-mail', 'style'),
              Input('E-mail', 'value'))
def verif_adresse_mail(mail):
    if mail is not None and re.match("^[a-z0-9-_]+[\._]?[a-z0-9]+[@][a-z0-9-_]+[.]\w{2,3}$", mail,):
        html_output_email = {"border": "3px solid green"}
        return html_output_email
    elif mail is not None:
        html_output_email = {"border": "3px solid red"}
        return html_output_email
