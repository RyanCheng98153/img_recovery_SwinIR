## SwiniR
It is an image recovery model that can convert an image from low resolution to high resolution

### Preparation
1. Create a new virtual environment
   - `python -m venv .venv`
2. Activate the virtual environment
   - Windows
     - `.\.venv\Scripts\Activate.ps1`
   - MacOS/Linux
     - `source ./.venv/Scripts/activate`
3. install the python dependency
   - `pip install -r requirements.txt`
4. download the weight
   - `sh download-weights.sh`

### Usage
- `python app.py`

Then you can use it on gradio, 
when the image is recovered the data will be saved in "results/data.png"