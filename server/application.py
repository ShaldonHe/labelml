import os
from flask import Flask
from flask_cors import CORS
from flask_graphql import GraphQLView
from schema import Schema
from flask import Response, request, abort,jsonify, send_from_directory
from io import StringIO

import config as cfg
import data


def create_app(**kwargs):
    app = Flask(__name__)
    CORS(app, supports_credentials=True, resources={r'/*': {'origins': '*'}})
    app.add_url_rule(
        '/graphql',
        view_func=GraphQLView.as_view('graphql', schema=Schema, **kwargs)
    )
    return app

application = create_app(graphiql=True)
app = application


@app.route('/img/<project>/<filename>')
def image(project, filename):
    img_dir = cfg.MEDIA_PATH
    print('img_dir,project,filename:',img_dir,project,filename)
    return send_from_directory(img_dir, filename)

@app.route('/project/dataset/list/<dsname>')
def dataset_list(dsname):
    img_dir = cfg.MEDIA_PATH
    
    return jsonify({})



if __name__ == '__main__':
    application.run(host='localhost')
