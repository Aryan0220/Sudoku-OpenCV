import cv2 as cv
import pytesseract
from sudoku import solve, print_board

pytesseract.pytesseract.tesseract_cmd = r'your_system_for_tesseract.exe'

# Map of numbers
numbers = ['1','2','3','4','5','6','7','8','9']

# Load the image
image = cv.imread('sudo.png')
print("Loading image.....")

# Blurring image
blurred = cv.GaussianBlur(image, (5, 5), 0)
print("Blurring image.....")

# RGB to Grayscale
gray = cv.cvtColor(blurred, cv.COLOR_BGR2GRAY)
print("RGB to Grayscale")

# Create Contours
thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY_INV, 11, 2)
print("Creating Contours")

# Counting Contours
cnts, _ = cv.findContours(thresh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
print("Counting Contours")

# Getting maximum count and area
print("Getting maximum count and area")
max_cnt = None
max_area = 0
for cnt in cnts:
    area = cv.contourArea(cnt)
    if area > max_area:
        max_cnt = cnt
        max_area = area

approx = cv.approxPolyDP(max_cnt, 0.05 * cv.arcLength(max_cnt, True), True)

# corners = [x1, y1, x2, y2, x3, y3, x4, y4]
corners = approx.reshape(4, 2).flatten()
print("corners = [x1, y1, x2, y2, x3, y3, x4, y4]")

# Width and Height of each cell
cell_width = int((corners[4] - corners[0]) / 9)
cell_height = int((corners[3] - corners[1]) / 9)
print("Getting Width and Height of each cell")

board = [[]]

# Convert img into Matrix of string
print("Converting img into Matrix of string")
for row in range(9):
    cells = []
    for col in range(9):
        x1, y1 = (corners[0] + (cell_width) * col) + 4, (corners[1] + (cell_height) * row) + 4
        x2, y2 = x1 + cell_width, y1 + cell_height
        cell_image = image[y1:y2, x1:x2]
        height, width, temp = cell_image.shape
        cell_image = cv.resize(cell_image, (width * 2, height * 2), interpolation=cv.INTER_LINEAR)
        val = pytesseract.image_to_string(cell_image, config='--psm 6')
        cell_val = ''
        if len(val) == 0:
            cell_val = str('.')
        else:
            if val[0] in numbers:
                cell_val = val[0]
            else:
                cell_val = str('.')
        cells.append(cell_val)
    board.append(cells)

# Reshpae board for solving
print("Reshaping board for solving")
board = board[1:10]

print("Puzzle")

print_board(board)

# Solving Sudoku Board using Backtracking
print("Solving Sudoku Board using Backtracking")
solve(board)

print("Solution")
print()
print_board(board)