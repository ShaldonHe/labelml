import os
from flask import Flask
from flask_cors import CORS
from flask import Response, request, abort,jsonify, send_from_directory, send_file
from io import StringIO
import libs.common.files as libfi
import libs.image.io as im_io
import libs.image.ops as im_ops
import json

import config as cfg
import data


def create_app(**kwargs):
    app = Flask(__name__)
    CORS(app, supports_credentials=True, resources={r'/*': {'origins': '*'}})
    return app

application = create_app()
app = application

def save_json(filepath,j):
    with open(filepath,'w',encoding='utf-8') as json_file:
        data = json.loads(j)
        data['flags'] = {}

        json.dump(data, json_file)
    

def getParms(request):
    if request.method=='POST':
        return request.form
    elif request.method=='GET':
        return request.args
    else:
        return {}

@app.route('/img/<projectID>/<dsID>/<imgID>')
def image(projectID,dsID, imgID):
    img_dir = cfg.MEDIA_PATH
    print('img_dir,project,filename:',projectID,dsID,imgID)
    return send_from_directory(img_dir, imgID+'.bmp')

@app.route('/annotation/<projectID>/<dsID>/<imgID>')
def annotation(projectID, dsID, imgID):
    ds_dir = cfg.DATASET_PATH
    print(ds_dir)
    print('img_dir,project,filename:',projectID,dsID,imgID)
    f_path = f'{ds_dir}/{projectID}/labels/{imgID}.a.json'
    if libfi.exist(f_path):
        return send_file(f_path)
    else:
        return jsonify({})

@app.route('/save/<projectID>/<dsID>/<imgID>',methods=['POST'])
def save_annotation(projectID, dsID, imgID):
    ds_dir = cfg.DATASET_PATH
    print(ds_dir)
    parms = getParms(request)
    print(parms)
    print('save img_dir,project,filename:',projectID,dsID,imgID)
    f_path = f'{ds_dir}/{projectID}/labels/{imgID}.a.json'
    save_json(f_path,parms['annotations'])

    return jsonify({})


@app.route('/thumbnail/<projectID>/<dsID>/<imgID>')
def thumbnail(projectID, dsID, imgID):
    img_dir = cfg.THUMB_PATH
    print('thumbnail: img_dir,project,filename:',projectID,dsID,imgID)
    tar_file = img_dir +'/' + imgID+'.jpg'
    def gen_thumbnail(src_file,tar_file,max_length=256):
        img = im_io.imread(src_file)
        ratio = max_length/max(img.shape)
        img = im_ops.ratio_resize(img,ratio=ratio)
        im_io.imwrite(tar_file,img)

        
    if not libfi.exist(tar_file):
        src_file = cfg.MEDIA_PATH + '/' + imgID+'.bmp'
        if not libfi.exist(src_file):
            abort(404)
        else:
            gen_thumbnail(src_file,tar_file)
    return send_file(tar_file)

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
