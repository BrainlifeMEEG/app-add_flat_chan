"""
Add flat channels to MNE raw data.

This app adds artificial flat (zero-valued) channels to MNE raw data files.
This is useful for adding stimulus or trigger channels that were not originally
recorded in the data, or for standardizing channel layouts across datasets.

Input:
    - raw: Path to MNE raw data file (.fif format)
    - ch_name: Name for the new channel
    - ch_type: Type of the new channel (e.g., 'eeg', 'meg', 'stim', 'misc')

Output:
    - out_dir/raw.fif: MNE raw data file with the new flat channel added
    - out_report/report.html: QC report with channel information
    - product.json: Metadata with updated channel info
"""

# Copyright (c) 2026 brainlife.io
#
# This app adds flat channels to MNE raw data files.
#
# Authors:
# - Kami Salibayeva (https://github.com/KSalibay)
# - Maximilien Chaumon (https://github.com/dnacombo)

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'brainlife_utils'))

# Standard imports
import mne
import numpy as np

# Import shared utilities
from brainlife_utils import (
    load_config,
    setup_matplotlib_backend,
    ensure_output_dirs,
    create_product_json,
    add_info_to_product,
    add_raw_info_to_product
)

# Set up matplotlib for headless execution
setup_matplotlib_backend()

# Ensure output directories exist
ensure_output_dirs('out_dir', 'out_report')

# Load configuration
config = load_config()

# == LOAD DATA ==
fname = config['raw']
ch_name = config['ch_name']
ch_type = config['ch_type']

# Read the raw data
raw = mne.io.read_raw_fif(fname)

# == ADD FLAT CHANNEL ==
# Create a flat (zero-valued) channel
nu_data = np.zeros((1, raw.n_times))
nu_info = mne.create_info(ch_names=[ch_name], sfreq=raw.info['sfreq'], ch_types=[ch_type])
flat_raw = mne.io.RawArray(nu_data, nu_info)

# Load data to memory before concatenating
raw.load_data()
# Add the flat channel to the raw data
raw.add_channels([flat_raw], force_update_info=True)

# == CREATE REPORT ==
report = mne.Report(title='Add Flat Channel Report')
report.add_raw(raw=raw, title='Raw Data with Added Flat Channel')

# Add channel information to report
channel_info_html = '<p><b>Channels in this file:</b></p>' + ', '.join(raw.ch_names)
report.add_html(title='Channels', html=channel_info_html)

# == SAVE DATA ==
raw.save(os.path.join('out_dir', 'raw.fif'), overwrite=True)
report.save(os.path.join('out_report', 'report.html'), overwrite=True)

# == CREATE PRODUCT JSON ==
product_items = []

# Add structured raw info messages
add_raw_info_to_product(product_items, raw)

# Add information about the added channel
msg = f"Added flat channel '{ch_name}' of type '{ch_type}'"
add_info_to_product(product_items, msg)

# Create the product.json file
create_product_json(product_items)