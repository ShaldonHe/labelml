from flask import Flask, request, abort, make_response, render_template, url_for, jsonify,send_file
import os
from optparse import OptionParser
from threading import Lock
from libs.common.hash import object_md5,string_md5
from libs.common.files import get_files,get_details
from libs.image.io import imread
import json
app = Flask(__name__)
app.config.from_object(__name__)
app.config['JSON_AS_ASCII'] = False

dataset_dir = '/media/xiaodonghe/data/data/Skin/New-Annotation/'
# dataset_dir = '/home/sheldon/Document/data/银屑/'

projects = {}
datasets = {}
images = {}
image_paths = {}
labels = {}
def build_images():
    files = get_files(dataset_dir,ext='jpg|jpeg|bmp|png')
    for p_file in files:
        _,subfolder,filename,ext = get_details(p_file,root_path=dataset_dir)
        abs_p = f'{subfolder}/{filename}.{ext}'
        img = imread(p_file)
        image_key = object_md5(img)
        hash_key = string_md5(abs_p)
        if image_key not in image_paths:
            image_paths[image_key] = abs_p
        else:
            image_paths[image_key].append(abs_p)

        images[hash_key] = image_key

def build_labels():
    files = get_files(dataset_dir,ext='json')
    for p_file in files:
        _,subfolder,filename,ext = get_details(p_file,root_path=dataset_dir)
        json_label = json.load(open(p_file))
        image_name = json_label['imagePath']
        if image_name.split('.')[0] != filename:
            raise IOError(p_file)
        abs_p = f'{subfolder}/{image_name}'# filename.ext
        hash_key = string_md5(abs_p)
        print(hash_key)
        labels[hash_key] = p_file
        json_label['label_id'] = hash_key
        json_label['image_id'] = images[hash_key]
        json_label['imageData'] = None
        json.dump(json_label,open(p_file,'w'),ensure_ascii=False)


def build_dataset():
    datasets['SkinLesion'] = {'id':'SkinLesion','images':[{'label_id':k,'image_id':images[k],'path':image_paths[images[k]]} for k in images.keys()]}

def build_project():
    projects['SkinLesion'] = {'id':'SkinLesion','dataset_id':'SkinLesion'}

build_images()
build_labels()
build_dataset()
build_project()

def getParms(request):
    if request.method=='POST':
        return request.form
    elif request.method=='GET':
        return request.args
    else:
        return {}

def save_json_to(file_path,json_data):
    with open(file_path,"w") as f:
        json.dump(json_data,f,ensure_ascii=False)


@app.route('/')
def index():
    return jsonify(list(projects.keys())) 


@app.route('/projects')
def project_list():
    return jsonify(list(projects.keys())) 

@app.route('/project/<project_id>')
def project(project_id):
    if project_id in projects:
        return jsonify(projects[project_id])
    else:
        return abort(403)

@app.route('/dataset/<dataset_id>')
def dataset(dataset_id):
    if dataset_id in dataset_id:
        return jsonify(datasets[dataset_id])
    else:
        return abort(403)


@app.route('/image/<image_id>')
def image(image_id):
    if image_id in image_paths:
        img_path = f'{dataset_dir}{image_paths[image_id]}'
        return send_file(img_path)
    else:
        return abort(403)



@app.route('/label/<label_id>',methods=['GET','POST'])
def label(label_id):
    if label_id in labels:
        label_path = labels[label_id]
        if request.method == 'POST':
            parms = getParms(request)
            label_json = json.loads(parms['label_json'])
            save_json_to(label_path,label_json)

        # if request.
        return send_file(label_path)
    else:
        return abort(403)



@app.route('/file/<file_id>',methods=['GET','POST'])
def remote_file(file_id):
    if file_id in labels:
        return jsonify({'image_id':images[file_id],'label_id':file_id})
    else:
        return abort(403)


if __name__ == '__main__':
    app.run(host = '0.0.0.0', port =10000,threaded=True, debug=True)
