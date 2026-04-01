# 🔬 Cell Counter using Watershed Algorithm

A Python-based tool for automated cell counting in microscopy images using OpenCV's Watershed segmentation algorithm.

## 📋 Overview

This project uses image processing techniques to accurately count cells in microscopy images. It leverages:
- **Gaussian Blur** for noise reduction
- **Adaptive Thresholding** for binarization
- **Morphological Operations** to clean the image
- **Distance Transform** to identify cell centers
- **Watershed Algorithm** for accurate cell segmentation

## 🛠️ Requirements

- Python 3.7+
- OpenCV
- NumPy

Install dependencies:
```bash
pip install -r requirements.txt
```

## 🚀 Usage

1. Place your microscopy image in the project directory and name it `cells.jpg`  
   *(or update `IMAGE_PATH` in `cell_counter.py`)*

2. Run the script:
```bash
python cell_counter.py
```

3. The script will:
   - Display the cell count in the terminal
   - Show the result image with red boundary lines drawn around detected cells

## 📁 Project Structure

```
cell-counter/
├── cell_counter.py     # Main script
├── requirements.txt    # Python dependencies
├── README.md           # Project documentation
├── .gitignore          # Git ignore rules
└── cells.jpg           # Your input image (add your own)
```

## 🔧 How It Works

| Step | Description |
|------|-------------|
| 1 | Load the image |
| 2 | Convert to grayscale |
| 3 | Apply Gaussian Blur to reduce noise |
| 4 | Adaptive thresholding (binary inverse) |
| 5 | Morphological opening to remove small noise |
| 6 | Dilate to get sure background |
| 7 | Distance transform to find cell centers |
| 8 | Threshold distance map for sure foreground |
| 9 | Determine unknown region |
| 10 | Label connected components as markers |
| 11 | Apply Watershed segmentation |
| 12 | Count unique markers (excluding borders/bg) |
| 13 | Draw red boundaries on detected cells |

## 📌 Notes

- Works best with grayscale or brightfield microscopy images
- For best results, ensure cells are well-separated and in focus
- Tweak `adaptiveThreshold` block size or distance transform threshold for different cell types

## 📄 License

MIT License
