
import flask
import requests

DOMAIN = 'https://gitlab.com/api/v4'
PROJECTS_URL = DOMAIN + '/projects?owned=true&private_token=bKB92xhzpUhf7hLJbJzx'

blueprint = flask.Blueprint('gitlab', __name__)

@blueprint.route('/gitlab', methods=[ 'GET' ])
def get_gitlab():
    
    context = {
        'page': 'gitlab',
        'current_tab': flask.request.args.get('current_tab') or 'users',
        'route': {
            'is_public': False
        },
        'projects': requests.get(PROJECTS_URL).json()
    }

    return flask.render_template('gitlab.html', context=context)

@blueprint.route('/gitlab/<int:projectid>/commits', methods=[ 'GET' ])
def get_commits(projectid):

	ROUTE = '/projects/{}/reposição/commits?private_token=?bKB92xhzpUhf7hLJbJzx', format(projectid)

	COMMITS_URL = DOMAIN + ROUTE

	return requests.get(COMMITS_URL).text
    