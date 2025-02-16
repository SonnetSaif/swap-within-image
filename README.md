# Swap Within Image

This repository provides a Python script designed to perform data augmentation by swapping objects within an image. It's particularly useful for enhancing datasets in computer vision tasks.

## Features

- **Data Augmentation**: Enhance your dataset by swapping objects within images to create new variations.
- **XML Parsing**: Utilizes XML files (e.g., Pascal VOC format) to identify and manipulate object annotations.

## Requirements

- Python 3.x
- Required libraries: `xml.etree.ElementTree`, `PIL` (Pillow)

## Usage

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/SonnetSaif/swap-within-image.git
   cd swap-within-image
   ```

2. **Install Dependencies**:
    Ensure you have the required libraries installed:
   ```bash
   pip install pillow
   ```

3. **Prepare Your Data**:
    - Place your images and corresponding XML annotation files in the `data/` directory.
   
4. **Run the Script**:
   ```bash
   python data_augmentation.py
   ```
   This will generate new images with swapped objects and save them in the augmented_data/ directory.
