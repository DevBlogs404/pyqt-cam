# import sys
# import cv2
# from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QLabel, QMessageBox, QSizePolicy
# from PyQt6.QtGui import QImage, QPixmap,QCursor
# from PyQt6.QtCore import QTimer, QDir, Qt

# class CameraApp(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         self.setWindowTitle("Camera App")
#         self.setGeometry(100, 100, 800, 600)
        

#         self.is_mirrored = False

#         # Create a main widget and layout
#         main_widget = QWidget()
#         main_layout = QVBoxLayout(main_widget)
#         main_layout.setContentsMargins(0, 0, 0, 0)
#         main_layout.setSpacing(0)

#         # Create a label to display the video stream
#         self.video_label = QLabel(self)
#         self.video_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
#         # self.video_label.setScaledContents(True)
#         self.video_label.setSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Ignored)
#         self.video_label.adjustSize()
#         self.video_label.setStyleSheet('background-color:black;')
#         main_layout.addWidget(self.video_label,9)  # 80% height

#         # Create a layout for the buttons
#         button_layout = QHBoxLayout()

#         # Create a button to capture images
#         self.capture_button = QPushButton("Capture Image", self)
#         self.capture_button.clicked.connect(self.capture_image)
#         self.capture_button.setStyleSheet("border-radius: 10px; padding: 10px; background-color: blue; color: white;")
#         self.capture_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
#         button_layout.addWidget(self.capture_button)

#         # Create a button to mirror the video stream
#         self.mirror_button = QPushButton("Mirror Image", self)
#         self.mirror_button.clicked.connect(self.toggle_mirror)
#         self.mirror_button.setStyleSheet("border-radius: 10px; padding: 10px; background-color: blue; color: white;")
#         self.mirror_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
#         button_layout.addWidget(self.mirror_button)

#         button_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

#         # Create a widget for the buttons to set its background color
#         button_widget = QWidget()
#         button_widget.setLayout(button_layout)
#         button_widget.setStyleSheet("background-color: rgba(0,0,0,0.3); border: 1px solid black;")
#         button_widget.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
#         main_layout.addWidget(button_widget, 1)  # 20% height

#         # Set the main widget as the central widget
#         self.setCentralWidget(main_widget)

#         # Initialize the video capture
#         self.cap = cv2.VideoCapture(0)

#         # Create a timer to update the video stream
#         self.timer = QTimer()
#         self.timer.timeout.connect(self.update_frame)
#         self.timer.start(30)

#     def update_frame(self):
#         ret, frame = self.cap.read()
#         if ret:
#             if self.is_mirrored:
#                 frame = cv2.flip(frame, 1)
#             # Convert the frame to QImage
#             frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#             image = QImage(frame, frame.shape[1], frame.shape[0], frame.strides[0], QImage.Format.Format_RGB888)
#             self.video_label.setPixmap(QPixmap.fromImage(image).scaled(self.video_label.size(), Qt.AspectRatioMode.KeepAspectRatio))

#     def capture_image(self):
#         ret, frame = self.cap.read()
#         if ret:
#             if self.is_mirrored:
#                 frame = cv2.flip(frame, 1)
#             filename = QDir.currentPath() + "/captured_image.jpg"
#             saved = cv2.imwrite(filename, frame)
#             if saved:
#                 QMessageBox.information(self, "Image Saved", "Image saved successfully at " + filename)
#             else:
#                 QMessageBox.warning(self, "Save Failed", "Failed to save the image.")

#     def toggle_mirror(self):
#         self.is_mirrored = not self.is_mirrored

       

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = CameraApp()
#     window.show()
#     window.showMaximized()
#     sys.exit(app.exec())




import sys
import cv2
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QLabel, QMessageBox, QSizePolicy
from PyQt6.QtGui import QImage, QPixmap, QCursor
from PyQt6.QtCore import QTimer, QDir, Qt

class CameraApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Camera App")
        self.setGeometry(100, 100, 800, 600)
        self.setStyleSheet("background-color: black;")

        self.is_mirrored = False

        # Create a main widget and layout
        main_widget = QWidget()
        main_layout = QVBoxLayout(main_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # Create a label to display the video stream
        self.video_label = QLabel(self)
        self.video_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # screen = QApplication.primaryScreen()  # Returns a QRect object
        # size = screen.availableGeometry()
        # width = size.width()
        # height = size.height()
        # print(width,height)
        # self.video_label.width = width
        # self.video_label.height = 800;
        self.video_label.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        main_layout.addWidget(self.video_label,9)  # 80% height

        # Create a layout for the buttons
        button_layout = QHBoxLayout()

        # Create a button to capture images
        self.capture_button = QPushButton("Capture Image", self)
        self.capture_button.clicked.connect(self.capture_image)
        self.capture_button.setStyleSheet("""
            border-radius: 10px;
            padding: 10px;
            background-color: blue;
            color: white;
        """)
        # Set cursor for capture_button
        self.capture_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        button_layout.addWidget(self.capture_button)

        # Create a button to mirror the video stream
        self.mirror_button = QPushButton("Mirror Image", self)
        self.mirror_button.clicked.connect(self.toggle_mirror)
        self.mirror_button.setStyleSheet("""
            border-radius: 10px;
            padding: 10px;
            background-color: blue;
            color: white;
        """)
        # Set cursor for mirror_button
        self.mirror_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        button_layout.addWidget(self.mirror_button)

        button_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Create a widget for the buttons to set its background color and border
        button_widget = QWidget()
        button_widget.setLayout(button_layout)
        button_widget.setStyleSheet("""
            background-color: rgba(0,0,0,0.3);
            border: 1px solid gray;
        """)
        button_widget.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        main_layout.addWidget(button_widget, 1)  # 20% height

        # Set the main widget as the central widget
        self.setCentralWidget(main_widget)

        self.cap = None
        self.timer = None
        self.start_capture()

    def start_capture(self):
        if self.cap:
            self.stop_capture()  # Ensure any existing capture is stopped

        self.cap = cv2.VideoCapture(0)
        if not self.cap.isOpened():
            QMessageBox.warning(self, "Camera Error", "Unable to access the camera.")
            return

        # Create a timer to update the video stream
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(30)

    def stop_capture(self):
        if self.timer:
            self.timer.stop()
        if self.cap:
            if self.cap.isOpened():
                self.cap.release()
            self.cap = None

    def update_frame(self):
        if self.cap is None or not self.cap.isOpened():
            return

        ret, frame = self.cap.read()
        if ret:
            if self.is_mirrored:
                frame = cv2.flip(frame, 1)
            # Convert the frame to QImage
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image = QImage(frame, frame.shape[1], frame.shape[0], frame.strides[0], QImage.Format.Format_RGB888)
            self.video_label.setPixmap(QPixmap.fromImage(image).scaled(self.video_label.size(), Qt.AspectRatioMode.KeepAspectRatio))

    def capture_image(self):
        if self.cap is None or not self.cap.isOpened():
            QMessageBox.warning(self, "Capture Error", "Camera is not available.")
            return

        ret, frame = self.cap.read()
        if ret:
            if self.is_mirrored:
                frame = cv2.flip(frame, 1)
            filename = QDir.currentPath() + "/captured_image.jpg"
            saved = cv2.imwrite(filename, frame)
            if saved:
                QMessageBox.information(self, "Image Saved", "Image saved successfully at " + filename)
            else:
                QMessageBox.warning(self, "Save Failed", "Failed to save the image.")

    def toggle_mirror(self):
        self.is_mirrored = not self.is_mirrored

    def showEvent(self, event):
        super().showEvent(event)
        self.start_capture()  # Start the video capture when the window is shown

    def hideEvent(self, event):
        super().hideEvent(event)
        self.stop_capture()  # Stop the video capture when the window is hidden

   

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CameraApp()
    window.show()
    sys.exit(app.exec())

