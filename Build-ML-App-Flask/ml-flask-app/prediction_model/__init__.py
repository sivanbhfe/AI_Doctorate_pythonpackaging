import os
from prediction_model.config import config
with open(os.path.join(config.PACKAGE_ROOT,'version')) as f:
    __version__=f.read().strip()