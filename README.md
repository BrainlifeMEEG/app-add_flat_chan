# app-add_flat_chan

[![Abcdspec-compliant](https://img.shields.io/badge/ABCD_Spec-v1.1-green.svg)](https://github.com/brain-life/abcd-spec)

## Description

Adds artificial flat (zero-valued) channels to MNE raw data files. This app is useful for:
- Adding stimulus or trigger channels that were not originally recorded in the data
- Standardizing channel layouts across datasets by adding placeholder channels
- Preparing data for analyses that require specific channel configurations

## Inputs

- **raw**: MNE raw data file in `.fif` format

## Outputs

- **out_dir/raw.fif**: Modified raw data file with the new flat channel added
- **out_dir/report.html**: QC report containing raw data summary and updated channel information
- **product.json**: Metadata with channel information and data summary

## Configuration Parameters

### Required

- `raw`: Path to the input MNE raw data file (`.fif` format)
- `ch_name`: Name for the new flat channel (e.g., "STI 014", "STIM")
- `ch_type`: Type of the new channel. Common types include:
  - `stim`: For stimulus/trigger channels
  - `misc`: For miscellaneous channels
  - `eeg`: For EEG channels (if adding EEG data)
  - `meg`: For MEG channels (if adding MEG data)

## Usage

The app reads a raw MNE data file, adds a flat channel with the specified name and type, and outputs the modified file.

Example configuration:
```json
{
    "raw": "path/to/raw.fif",
    "ch_name": "STI 014",
    "ch_type": "stim"
}
```

## Technical Details

- **Execution**: Python with MNE-Python and shared brainlife_utils library
- **Data format**: MNE `.fif` format (compatible with all downstream Brainlife.io apps)
- **Channel addition**: Uses `mne.create_info()` and `raw.add_channels()` for consistent channel handling
- **Report generation**: Automatic HTML report with channel visualization

## Authors

- [Kami Salibayeva](https://github.com/KSalibay), Indiana University

## Citations

We kindly ask that you cite the following articles when publishing papers and code using this app:

**brainlife.io: A decentralized and open source cloud platform to support neuroscience research**. Hayashi, S., Caron, B. A., et al. & Pestilli, F. (2023). ArXiv. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10274934/

**MEG and EEG data analysis with MNE-Python**. Gramfort A, et al. & Hämäläinen MS. (2013). Frontiers in Neuroscience, 7(267):1–13. https://doi.org/10.3389/fnins.2013.00267

## Funding Acknowledgement

brainlife.io is publicly funded and for the sustainability of the project we kindly ask that you acknowledge the following funding sources:

[![NSF-BCS-1734853](https://img.shields.io/badge/NSF_BCS-1734853-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1734853)
[![NSF-BCS-1636893](https://img.shields.io/badge/NSF_BCS-1636893-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1636893)
[![NSF-ACI-1916518](https://img.shields.io/badge/NSF_ACI-1916518-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1916518)
[![NSF-IIS-1912270](https://img.shields.io/badge/NSF_IIS-1912270-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1912270)
[![NIH-NIBIB-R01EB030896](https://img.shields.io/badge/NIH_NIBIB-R01EB030896-green.svg)](https://grantome.com/grant/NIH/R01-EB030896-01)

#### MIT Copyright (c) 2021 brainlife.io The University of Texas at Austin and Indiana University
