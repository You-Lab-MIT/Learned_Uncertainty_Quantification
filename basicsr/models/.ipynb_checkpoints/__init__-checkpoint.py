# ------------------------------------------------------------------------
# Copyright (c) 2022 megvii-model. All Rights Reserved.
# ------------------------------------------------------------------------
# Modified from BasicSR (https://github.com/xinntao/BasicSR)
# Copyright 2018-2020 BasicSR Authors
# ------------------------------------------------------------------------
import importlib
from os import path as osp
import torch

from basicsr.utils import get_root_logger, scandir
from basicsr.utils.options import parse

# automatically scan and import model modules
# scan all the files under the 'models' folder and collect files ending with
# '_model.py'
model_folder = osp.dirname(osp.abspath(__file__))
model_filenames = [
    osp.splitext(osp.basename(v))[0] for v in scandir(model_folder)
    if v.endswith('_model.py')
]
# import all the model modules
_model_modules = [
    importlib.import_module(f'basicsr.models.{file_name}')
    for file_name in model_filenames
]


def create_model(opt):
    """Create model.

    Args:
        opt (dict): Configuration. It constains:
            model_type (str): Model type.
    """
    model_type = opt['model_type']

    # dynamic instantiation
    for module in _model_modules:
        model_cls = getattr(module, model_type, None)
        if model_cls is not None:
            break
    if model_cls is None:
        raise ValueError(f'Model {model_type} is not found.')
#     print("\n")
#     print("opt = ", opt)
#     print("\n")
#     print('model_cls = ', model_cls)
    model = model_cls(opt)
    

    logger = get_root_logger()
    logger.info(f'Model [{model.__class__.__name__}] is created.')
    return model


def load_finetuned_model(weight_path, config_path):
    """
    Loads finetuned weights into the NAFNet model.

    Args:
        weight_path (str): Path to the finetuned weights file (.pth).
        config_path (str): Path to the model configuration file (.yml).
        device (str or torch.device, optional): Device to load the model on (default: auto-detect).

    Returns:
        torch.nn.Module: The finetuned NAFNet model.
    """
    device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')

    finetuned_model_weights = torch.load(weight_path, map_location=device)

    opt = parse(config_path, is_train=False)
    opt['dist'] = False

    NAFNET_model = create_model(opt)
    NAFNET_model = NAFNET_model.net_g
    NAFNET_model.load_state_dict(finetuned_model_weights['params'])

    print("Finetuned weights loaded successfully!")
    return NAFNET_model