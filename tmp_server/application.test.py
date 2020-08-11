import os
from flask import Flask
from flask_cors import CORS
from flask import Response, request, abort,jsonify, send_from_directory, send_file
from io import StringIO
import libs.common.files as libfi
import libs.image.io as im_io
import libs.image.ops as im_ops
import json

import app_config as cfg
# import data


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

@app.route('/image/<imgID>')
def image(imgID):
    print('Image ID:',imgID)
    return send_from_directory(cfg.IMAGE_PATH, imgID+'.bmp')

@app.route('/label/<imgID>')
def annotation(imgID):
    print('Image ID:',imgID)
    f_path = f'{cfg.DATASET_PATH}/skin/labels/{imgID}.json'
    if libfi.exist(f_path):
        return send_file(f_path)
    else:
        return jsonify({})

@app.route('/updatelabel/<imgID>',methods=['POST'])
def save_annotation(imgID):
    parms = getParms(request)
    print('updatelabel:',imgID, parms)
    f_path = f'{cfg.DATASET_PATH}/skin/labels/{imgID}.json'
    save_json(f_path,parms['newlabel'])
    return jsonify({"success":True})


@app.route('/exportlabel/<imgID>')
def export_annotation(imgID):
    print('exportlabel:',imgID)
    f_path = f'{cfg.DATASET_PATH}/skin/labels/{imgID}.json'
    if libfi.exist(f_path):
        return send_file(f_path)
    else:
        return jsonify({})



@app.route('/thumbnail/<imgID>')
def thumbnail(imgID):
    print('thumbnail: ',imgID)
    tar_file = cfg.THUMB_PATH +'/' + imgID+'.jpg'
    def gen_thumbnail(src_file,tar_file,max_length=256):
        img = im_io.imread(src_file)
        ratio = max_length/max(img.shape)
        img = im_ops.ratio_resize(img,ratio=ratio)
        im_io.imwrite(tar_file,img)

        
    if not libfi.exist(tar_file):
        src_file = cfg.IMAGE_PATH + '/' + imgID+'.bmp'
        if not libfi.exist(src_file):
            abort(404)
        else:
            gen_thumbnail(src_file,tar_file)
    return send_file(tar_file)

@app.route('/labellist')
def project():
    return jsonify( cfg.projects['skin'])

@app.route('/imagelist')
def dataset_list():
    img_dir = cfg.IMAGE_PATH
    print('imagelist')
    files = libfi.get_files(img_dir,'bmp')
    dslist = [ {'id':libfi.filename(x)} for x in files]
    return jsonify(dslist)


@app.route('/imageinfo/<imgID>')
def imageinfo(imgID):
    print('imageinfo:', imgID)
    tar_file = f'{cfg.IMAGE_PATH}/{imgID}.bmp'
    if libfi.exist(tar_file):
        img = im_io.imread(tar_file)
        result = {'name':libfi.filename(tar_file),'width':img.shape[0],'height':img.shape[1],'id':imgID}
        return jsonify(result)
    else:
        abort(404)

if __name__ == '__main__':
    application.run(host='localhost',debug=True)
