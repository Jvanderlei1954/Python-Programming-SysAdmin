import flask
import ldap3

blueprint = flask.Blueprint('auth', __name__)

@blueprint.route('/sign-in', methods=[ 'GET' ])
def get_sign_in():    

    context = {
        'page': 'sign-in',
        'route': {
            'is_public': True
        },
    }

    return flask.render_template('sign-in.html', context=context)


@blueprint.route('/sign-up', methods=[ 'GET' ])
def get_sign_up():
    context = {
        'page': 'sign-up',
        'route': {
            'is_public': True
        },
    }

    return flask.render_template('sign-up.html', context=context)


@blueprint.route('/sign-up', methods=[ 'POST' ])
def post_sign_up():
    server = ldap3.Server('ldap://0.0.0.0:389')
    connection = ldap3.Connection(
        server,
        'cn=admin,dc=dexter,dc=com,dc=br',
        '4linux'
    )

    try:
        connection.bind()
    except:
        flask.flash('Sem conexão com o LDAP', 'danger')
        return flask.redirect('/sign-up')

    name = flask.request.form['name']
    surname = flask.request.form['surname']
    email = flask.request.form['email']
    password = flask.request.form['password']

    object_class = [
        'top',
        'person',
        'organizationalPerson',
        'inetOrgPerson',
    ]

    user = {
        'cn': name,
        'sn': surname,
        'mail': email,
        'uid': email,
        'userPassword': password
    }

    cn = 'uid={},dc=dexter,dc=com,dc=br'.format(email)

    if connection.add(cn, object_class, user):
        return flask.redirect('/sign-in')
    flask.flash('Erro ao cadastrar usuário', 'danger')
    return flask.redirect('sign-up')

    return ''


@blueprint.route('/sign-in', methods=[ 'POST' ])
def post_sign_in():
       
    server = ldap3.Server('ldap://0.0.0.0:389')
    connection = ldap3.Connection(
        server,
        'cn=admin,dc=dexter,dc=com,dc=br',
        '4linux'
    )

    try:
        connection.bind()
    except:
        flask.flash('Sem conexão com o LDAP', 'danger')
        return flask.redirect('/sign-up')

    email = flask.request.form['email']
    password = flask.request.form['password']

    connection.search(
        'uid={},dc=dexter,dc=com,dc=br'.format(email),
        '(objectClass=person)',
        attributes=['userPassword']
    )

    try:
        user = connection.entries[0]
        saved_password = user.userPassword.value.decode()
        if saved_password == password:
            flask.session[ 'email' ] = email
            flask.flash('Login com sucesso', 'success')
            return flask.redirect('/')
    except:
        flask.flash('Email não está cadastrado na base de dados', 'danger')

    return ''


@blueprint.route('/sign-out', methods=[ 'POST' ])
def post_sign_out():
    return ''