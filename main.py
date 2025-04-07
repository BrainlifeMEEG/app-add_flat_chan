# Copyright (c) 2020 brainlife.io
#
# This file is a MNE python-based brainlife.io App
#
# Author: Kami Salibayeva
# Indiana University

# set up environment
import os
import json
import mne
import numpy as np

# Current path
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

# Populate mne_config.py file with brainlife config.json
with open(__location__+'/config.json') as config_json:
    config = json.load(config_json)

fname = config['raw']
ch_name = config['ch_name']
ch_type = config['ch_type']

# Read the raw data and info
raw = mne.io.read_raw_fif(fname)

nu_data = np.zeros((1, raw.n_times))
nu_info = mne.create_info(ch_names=[ch_name], sfreq=raw.info['sfreq'], ch_types=[ch_type])
stim_raw = mne.io.RawArray(nu_data, nu_info)

raw.load_data()
raw.add_channels([stim_raw])
# save the modified raw file
raw.save(os.path.join('out_dir','raw.fif'), overwrite=True)



# create a product.json file to show the output
dict_json_product = {'brainlife': []}

info = str(raw.info)
dict_json_product['brainlife'].append({'type': 'info', 'msg': info})

with open('product.json', 'w') as outfile:
    json.dump(dict_json_product, outfile)