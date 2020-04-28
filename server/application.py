import os
from flask import Flask
from flask_cors import CORS
# from flask_graphql import GraphQLView
# from schema import Schema
from flask import Response, request, abort,jsonify, send_from_directory
from io import StringIO
import libs.common.files as libfi

import config as cfg
import data


def create_app(**kwargs):
    app = Flask(__name__)
    CORS(app, supports_credentials=True, resources={r'/*': {'origins': '*'}})
    # app.add_url_rule(
    #     '/graphql',
    #     view_func=GraphQLView.as_view('graphql', schema=Schema, **kwargs)
    # )
    return app

application = create_app(graphiql=True)
app = application


@app.route('/img/<projectID>/<dsID>/<imgID>')
def image(projectID,dsID, imgID):
    img_dir = cfg.MEDIA_PATH
    print('img_dir,project,filename:',projectID,dsID,imgID)
    return send_from_directory(img_dir, imgID+'.bmp')

@app.route('/project/info/<projectID>')
def project(projectID):
    print('ProjectID: ',projectID)
    if projectID in cfg.projects:
        return jsonify( cfg.projects[projectID])
    else:
        abort(404)

@app.route('/project/dataset/list/<dsname>')
def dataset_list(dsname):
    img_dir = cfg.MEDIA_PATH
    print(img_dir)
    libfi.filename
    files = libfi.get_files(img_dir,'bmp')
    dslist = [ {'id':libfi.filename(x),'filename':libfi.filename(x)+'.bmp'} for x in files]
    return jsonify(dslist)

if __name__ == '__main__':
    application.run(host='localhost',debug=True)
