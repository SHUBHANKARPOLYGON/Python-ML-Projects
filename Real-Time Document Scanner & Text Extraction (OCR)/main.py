import cv2
import numpy as np
import pytesseract
from PIL import Image

# Download Tesseract OCR (install via https://github.com/UB-Mannheim/tesseract/wiki)
pytesseract.pytesseract.tesseract_cmd = r'tesseract-ocr-w64-setup-5.5.0.20241111.exe'  # Windows path (adjust for Linux/Mac)


def scan_document():
    cap = cv2.VideoCapture(0)  # Webcam

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # 1. Preprocess (resize, grayscale, blur)
        frame_resized = cv2.resize(frame, (800, 600))
        gray = cv2.cvtColor(frame_resized, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (5, 5), 0)

        # 2. Edge detection + contour finding
        edges = cv2.Canny(blur, 50, 150)
        contours, _ = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # 3. Find document contour (largest rectangle)
        doc_contour = None
        max_area = 0
        for contour in contours:
            peri = cv2.arcLength(contour, True)
            approx = cv2.approxPolyDP(contour, 0.02 * peri, True)
            if len(approx) == 4:  # Check if quadrilateral
                area = cv2.contourArea(contour)
                if area > max_area:
                    max_area = area
                    doc_contour = approx

        # 4. Apply perspective transform if document found
        if doc_contour is not None:
            warped = four_point_transform(gray, doc_contour.reshape(4, 2))
            cv2.drawContours(frame_resized, [doc_contour], -1, (0, 255, 0), 2)

            # 5. OCR on the scanned document
            text = pytesseract.image_to_string(warped)
            print("Extracted Text:\n", text)

        # Display
        cv2.imshow("Document Scanner", frame_resized)
        key = cv2.waitKey(1)
        if key == 27:  # Press ESC to exit
            break

    cap.release()
    cv2.destroyAllWindows()


def four_point_transform(image, pts):
    # Order points: top-left, top-right, bottom-right, bottom-left
    rect = order_points(pts)
    (tl, tr, br, bl) = rect

    # Compute new width and height
    widthA = np.sqrt((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2),
    widthB = np.sqrt((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2),
    maxWidth = max(int(widthA), int(widthB)),

    heightA = np.sqrt((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2),
    heightB = np.sqrt((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2),
    maxHeight = max(int(heightA), int(heightB)),

    # Destination points for transform
    dst = np.array([
        [0, 0],
        [maxWidth - 1, 0],
        [maxWidth - 1, maxHeight - 1],
        [0, maxHeight - 1]], dtype="float32"),

    # Apply perspective transform
    M = cv2.getPerspectiveTransform(rect, dst),
    warped = cv2.warpPerspective(image, M, (maxWidth, maxHeight))
    return warped


def order_points(pts):
    # Initialize a list of coordinates in order: [tl, tr, br, bl]
    rect = np.zeros((4, 2), dtype="float32")
    s = pts.sum(axis=1)
    rect[0] = pts[np.argmin(s)]  # Top-left (smallest sum)
    rect[2] = pts[np.argmax(s)]  # Bottom-right (largest sum)

    diff = np.diff(pts, axis=1)
    rect[1] = pts[np.argmin(diff)]  # Top-right (smallest diff)
    rect[3] = pts[np.argmax(diff)]  # Bottom-left (largest diff)
    return rect


if __name__ == "__main__":
    scan_document()