import libs.common.files as libfi
import json
if __name__ == "__main__":
    files = libfi.get_files('./server/dataset/skin/labels','json')
    for f_json in files:
        with open(f_json,encoding='utf-8') as f:
            annotation = json.load(f)
            print(annotation)
            new_annotation = {}
            new_annotation['flags'] = annotation['flags']
            new_annotation['annotations'] = []
            for shape in annotation['shapes']:
                print(shape)
                new_shape = {}
                new_shape['id'] = shape['label']
                new_shape['label'] = shape['label']
                new_annotation['annotations'].append(new_shape)


