# Music Recommendation Based on Emotion

## Description
As part of the 2024 SUTD Computational Data Science Module, we decided to explore Music Emotion Recognition and Retrieval to better understand how audio processing works and how we could develop models that can recommend songs that are emotionally similar.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)

## Installation
The following project requires OpenSMILE (required for `dashboard` directory) and Essentia to run the project.

1. Refer to the [OpenSMILE Documentation](https://audeering.github.io/opensmile/get-started.html#compiling-on-linux-mac) to compile the OpenSMILE package from source.
2. Refer to the [Essentia Documentation](https://essentia.upf.edu/installing.html#installing-essentia) to install the Essentia library.
3. Git clone this repository to the desktop
4. Set up a Python Virtual Environment inside the root directory of the GitHub Repository
5. Activate the virtual environment and install the package dependencies using the following command `pip install -r requirements.txt`

## Usage
The project is composed of 2 main directories - `dashboard` and `research`
The `dashboard` directory consists of files to run the Streamlit Web Application Demo while the `research` directory consists of files, mainly notebooks, in which we conducted our experimentation and analysis.

### Running the Streamlit Web Application
- Run the Streamlit demo via the following command `streamlit run ./dashboard/UI/app.py`

## Contributions
The following project was completed by
- Lim Fuo En
- Anthony Lim
- Issac Jose Ignatius
- Koh Jia Jun
- Timothy Wee
