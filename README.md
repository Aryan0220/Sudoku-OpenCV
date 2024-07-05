# Sudoku Solver using OpenCV and Python

This project is a Sudoku solver that utilizes OpenCV for image processing and Tesseract OCR for number recognition. It also includes a backtracking algorithm to solve the Sudoku puzzle.

## Features

- **Image Processing**: Converts the Sudoku puzzle image to a grayscale and applies contour detection to identify the puzzle grid.
- **OCR**: Uses Tesseract OCR to extract numbers from the puzzle image.
- **Sudoku Solver**: Implements a backtracking algorithm to solve the extracted Sudoku puzzle.

## Requirements

- Python 3.x
- OpenCV
- Tesseract OCR
- pytesseract

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/sudoku-solver.git
    cd sudoku-solver
    ```

2. Install the required packages:
    ```sh
    pip install opencv-python pytesseract
    ```

3. Download and install [Tesseract OCR](https://github.com/tesseract-ocr/tesseract). Make sure to add Tesseract to your system's PATH.

## Usage

1. Place your Sudoku puzzle image in the project directory and rename it to `sudo.png`.

2. Update the `pytesseract.pytesseract.tesseract_cmd` path in the code to the location of your Tesseract executable:
    ```python
    pytesseract.pytesseract.tesseract_cmd = r'your_system_path_for_tesseract.exe'
    ```

3. Run the script:
    ```sh
    python sudoku_solver.py
    ```

Feel free to adjust the content as per your project specifics and preferences.
