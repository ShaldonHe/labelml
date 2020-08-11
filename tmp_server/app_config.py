
import os

# #HOST = '24.5.150.30'
# HOST = '10.0.0.21'
# HOST = 'localhost'

import libs.common.files as libfi

PROJECT_NAME = 'skin' #'VOC2007' #'oxfordpets'
# BASE_PATH = '/home/sheldon/Document/code/beyes/labelml/server' #'/bigguy/data' #'/Users/bfortuner/data'
cw_dir = libfi.folder(__file__)
print('当前工作目录:',cw_dir)
BASE_PATH = '{}'.format(cw_dir) #'/bigguy/data' #'/Users/bfortuner/data'
DATASET_PATH = os.path.join(BASE_PATH,'dataset')
IMAGE_PATH = os.path.join(BASE_PATH,'dataset', PROJECT_NAME, 'images')
THUMB_PATH = os.path.join(BASE_PATH,'dataset', PROJECT_NAME, 'thumbnail')
print(IMAGE_PATH)
ENDIP = '0.0.0.0'
ENDPORT = 5000
# ENDPOINT = 'http://0.0.0.0:5000'
# IMG_ENDPOINT = ENDPOINT + '/getimage'
# print("IMG", IMG_ENDPOINT)
projects = {
    'skin':
        {
            'name':'浅层皮肤病理标注项目',
            'description':"浅层皮肤病理标注项目",
            # 'id':'skin',
            # 'dataset':'skin',
            'labels':['角质层','棘层','真皮乳头层','真皮网状层','真皮浅层血管周围炎症细胞浸润','角化过度','棘层增厚'],
            'colors':{'角质层':'#00FFFF','棘层':'#FFFFFF','真皮乳头层':'#FF00FF','真皮网状层':'#FFFF00','真皮浅层血管周围炎症细胞浸润':'#0000FF','角化过度':'#FF0000','棘层增厚':'#FF00FF'}
    },
}