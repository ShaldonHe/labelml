# Project Types
CLASSIFICATION = 'classification'
SEGMENTATION = 'segmentation'
PROJECT_TYPES = [CLASSIFICATION, SEGMENTATION]

METRICS_FNAME = 'metrics.json'
FOLD_FNAME = 'labels.json'
PREDS_FNAME = 'predictions.json'

# Datasets
TRAIN = 'trn'
VAL = 'val'
TEST = 'tst'
FULL = 'full'
UNLABELED = 'unlabeled'
DSETS = [TRAIN, VAL, TEST, FULL]

# Transforms
JOINT = 'joint'
UPSAMPLE = 'upsample'
TARGET = 'target'
TENSOR = 'tensor'
MASK = 'mask'

# File
JPG = 'jpg'
TIF = 'tif'
PNG = 'png'
GIF = 'gif'
BCOLZ = 'bc'
JPG_EXT = '.'+JPG
TIF_EXT = '.'+TIF
PNG_EXT = '.'+PNG
GIF_EXT = '.'+GIF
BCOLZ_EXT = '.'+BCOLZ
IMG_EXTS = [JPG_EXT, TIF_EXT, PNG_EXT, GIF_EXT, BCOLZ_EXT]
CHECKPOINT_EXT = '.th'
EXPERIMENT_CONFIG_FILE_EXT = '.json'
EXPERIMENT_CONFIG_FNAME = 'config.json'
EXPERIMENT_HISTORY_FILE_EXT = '.csv'
EXP_FILE_EXT = '.zip'
PRED_FILE_EXT = '.bc'
SUBMISSION_FILE_EXT = '.csv'
ENSEMBLE_FILE_EXT = '.bc'
DSET_FOLD_FILE_EXT = '.json'
MODEL_EXT = '.mdl'
WEIGHTS_EXT = '.th'
OPTIM_EXT = '.th'

# Postfix
INPUT_POSTFIX = JPG_EXT
TARGET_POSTFIX = '_mask'+GIF_EXT

# Metrics
LOSS = 'Loss'
SCORE = 'Score'
ACCURACY = 'Accuracy'
F2_SCORE = 'F2'
ENSEMBLE_F2 = 'EnsembleF2'
DICE_SCORE = 'Dice'
MEAN = 'mean'
GMEAN = 'gmean'
VOTE = 'vote'
STD_DEV = 'std'
ENSEMBLE_METHODS = [MEAN, GMEAN]

# File Regex
WEIGHTS_FNAME_REGEX = r'weights-(\d+)\.pth$'
OPTIM_FNAME_REGEX = r'optim-(\d+)\.pth$'
WEIGHTS_OPTIM_FNAME_REGEX = r'(weights|optim)-(\d+)\.th$'
LATEST_WEIGHTS_FNAME = 'latest_weights.th'
LATEST_OPTIM_FNAME = 'latest_optim.th'
LATEST = 'latest'


# Predictions
SINGLE_MODEL_PRED = 'single-basic'
SINGLE_MODEL_TTA_PRED = 'single-tta'
PREDICTION_TYPES = [SINGLE_MODEL_PRED, SINGLE_MODEL_TTA_PRED]
SINGLE_MODEL_ENSEMBLE = 'single-ens'
SINGLE_MODEL_TTA_ENSEMBLE = 'single-ens-tta'
ENSEMBLE_TYPES = [SINGLE_MODEL_ENSEMBLE, SINGLE_MODEL_TTA_ENSEMBLE]
DEFAULT_BLOCK_NAME = 'preds'

# Ensembles
MEGA_ENSEMBLE = 'mega-ens'
MEGA_ENSEMBLE_TYPES = [MEGA_ENSEMBLE]


# Experiments
INITIALIZED = 'INITIALIZED'
RESUMED = 'RESUMED'
COMPLETED = 'COMPLETED'
IN_PROGRESS = 'IN_PROGRESS'
FAILED = 'FAILED'
MAX_PATIENCE_EXCEEDED = 'MAX_PATIENCE_EXCEEDED'
EXPERIMENT_STATUSES = [INITIALIZED, RESUMED, COMPLETED,
    IN_PROGRESS, FAILED, MAX_PATIENCE_EXCEEDED]
EXP_ID_FIELD = 'exp_id'
ES_EXP_KEY_FIELD = 'key'
LATEST_WEIGHTS_FNAME = 'latest_weights{:s}'.format(WEIGHTS_EXT)
LATEST_OPTIM_FNAME = 'latest_optim{:s}'.format(OPTIM_EXT)
MODEL_FNAME = 'model{:s}'.format(MODEL_EXT)
OPTIM_FNAME = 'optim{:s}'.format(OPTIM_EXT)


# Data Aug
IMAGENET_MEAN = [0.485, 0.456, 0.406]
IMAGENET_STD = [0.229, 0.224, 0.225]
