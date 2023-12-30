AutoHighlight Visionary
===

## Abstract
AutoHighlight Visionary is a tool to help the user to create a highlight video from a long video. The tool will automatically detect the highlight moments in the video and create a highlight video from those moments.

## Basic Idea
- Shot Detection
- Ball and Rim Detection
- Ball Tracking

## Application Showcase
### Shot Detection
![Shot Detection](./src/shot_detection.gif)

### Ball and Rim Detection
![Ball and Rim Detection](./src/ball_rim_detection.gif)

### Ball Tracking
![Ball Tracking](./src/ball_tracking.gif)

## Results
The result combine the three steps above. The result is not perfect but it is good enough to be used as a highlight video.
![Score](./src/scoring.gif)

## Installation

- create conda environment
```bash
conda create -n autohighlight-visionary python=3.10
```

- activate conda environment
```bash
conda activate autohighlight-visionary
```

- install requirements
```bash
pip install -r requirements.txt
```

## Usage
- run the main file
```bash
python main.py
```