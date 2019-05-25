
import flask
import docker

blueprint = flask.Blueprint('docker', __name__)

connection = docker.DockerClient()

@blueprint.route('/docker', methods=[ 'GET' ])
def get_docker():

	container = connection.containers.get('13f8eb19f45e')

	if not container:
		flask.flash('container nao encontrado', 'danger')

	elif container.status = 'running':
		container.stop()
		flask.flash('container iniciado', 'succes')

	else:

		flask.flash('container já está parado', 'info')

	return flask.redirect('/docker')    
																		
	context = {
		'page': 'docker',
		'route': {
			'is_public': False
		},
		'container': container
	}

	return flask.render_template('docker.html', context=context)

@blueprint.route('/docker/start', methods=[ 'GET' ])
def start_docker():
	return 'start docker'

@blueprint.route('/docker/stop', methods=[ 'GET' ])
def stop_docker():
	return 'stop docker'

