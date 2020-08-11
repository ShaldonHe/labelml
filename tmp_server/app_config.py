
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

PROJECT_LABELS = (
    'car', 'trafficlight', 'biker'
)

METRICS_FNAME = 'metrics.json'
FOLD_FNAME = 'labels.json'
PREDS_FNAME = 'predictions.json'
RANKINGS_FNAME = 'rankings.csv'


class Config(object):
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    AWS_ACCESS_KEY = os.getenv('AWS_ACCESS_KEY_ID', 'password')
    AWS_SECRET_KEY = os.getenv('AWS_SECRET_ACCESS_KEY', 'password')
    DATABASE_CNNECTION = 'mongodb://writer:beyes0308@localhost:8000'
    AWS_REGION='us-west-1'

class ProductConfig(Config):
    ENDPOINT = 'http://0.0.0.0:80'
    DEBUG = False

class DevConfig(Config):
    ENDPOINT = 'http://localhost:5000'
    DEBUG = True

#config = globals()[os.getenv('LABELML_ENV', 'ProductConfig')]
env = os.getenv('LABELML_ENV', 'dev')
print ("ENV " + env)
if env == 'product':
    ENDPOINT = ProductConfig.ENDPOINT
else:
    ENDPOINT = DevConfig.ENDPOINT

IMG_ENDPOINT = ENDPOINT + '/img'
print("IMG", IMG_ENDPOINT)
projects = {
    'skin':
        {
            'name':'浅层皮肤病理结构标注项目',
            'description':"浅层皮肤病理结构标注项目",
            'id':'skin',
            'dataset':'skin',
            'labels':['角质层','棘层','真皮乳头层','真皮网状层','真皮浅层血管周围炎症细胞浸润','角化过度','棘层增厚'],
            'colors':{'角质层':'#00FFFF','棘层':'#FFFFFF','真皮乳头层':'#FF00FF','真皮网状层':'#FFFF00','真皮浅层血管周围炎症细胞浸润':'#0000FF','角化过度':'#FF0000','棘层增厚':'#FF00FF'}
    },
}