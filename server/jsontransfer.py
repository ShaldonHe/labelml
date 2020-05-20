import libs.common.files as libfi
import json
import random
s_cache = '0123456789abcdefghijklmnopqrstuvwxyz'
def random_str(l = 10):
    s = ''
    for _ in range(l):
        s+= s_cache[random.randint(0,35)]
    return s

if __name__ == "__main__":
    files = libfi.get_files('./server/dataset/skin/labels','json')
    for f_json in files:
        if f_json[-7:-4]=='.a.':
            continue
        with open(f_json,encoding='utf-8') as f:
            annotation = json.load(f)
            print(annotation)
            new_annotation = {}
            new_annotation['flags'] = annotation['flags']
            new_annotation['annotations'] = []
            for shape in annotation['shapes']:
                print(shape)
                new_shape = {}
                new_shape['id'] = random_str()
                new_shape['label'] = shape['label']
                new_shape['polygon'] = {
                    'annoId':new_shape['id'],
                    'id':random_str(),
                    'label':shape['label'],
                    'points':[]
                    }
                for p in shape['points']:
                    new_p = {
                        'id':random_str(),
                        'x': p[0],
                        'y': p[1]
                        }
                    new_shape['polygon']['points'].append(new_p)
                new_annotation['annotations'].append(new_shape)

        p_dir , filename, _ = libfi.get_details(f_json)
        tar_json = f'{p_dir}/{filename}.a.json'
        with open(tar_json, encoding='utf-8',mode='w+') as f:
            json.dump(new_annotation,f)



