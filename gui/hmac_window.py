from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit, QFileDialog, QMessageBox
)
from PyQt5.QtCore import Qt
from HMAC_File_Authenticator.HMACFileAuthenticator import FileHMAC

class FileHMACApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("File HMAC Generator & Verifier")
        self.setGeometry(100, 100, 600, 400)
        self.setStyleSheet("""
            QMainWindow {
                background-color: #2E3440;
            }
            QLabel {
                color: #D8DEE9;
                font-size: 14px;
            }
            QLineEdit {
                background-color: #3B4252;
                color: #ECEFF4;
                border: 1px solid #4C566A;
                padding: 5px;
                font-size: 14px;
            }
            QPushButton {
                background-color: #5E81AC;
                color: #ECEFF4;
                border: none;
                padding: 10px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #81A1C1;
            }
            QMessageBox {
                background-color: #3B4252;
            }
            QMessageBox QLabel {
                color: #ECEFF4;
                font-size: 14px;
            }
            QMessageBox QPushButton {
                background-color: #5E81AC;
                color: #ECEFF4;
                border: none;
                padding: 10px;
                font-size: 14px;
            }
            QMessageBox QPushButton:hover {
                background-color: #81A1C1;
            }
        """)

        # Central Widget
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        # File Path Input
        self.file_path_label = QLabel("File Path:")
        self.layout.addWidget(self.file_path_label)
        self.file_path_input = QLineEdit()
        self.file_path_input.setPlaceholderText("Select a file...")
        self.layout.addWidget(self.file_path_input)
        self.browse_file_button = QPushButton("Browse File")
        self.browse_file_button.clicked.connect(self.browse_file)
        self.layout.addWidget(self.browse_file_button)

        # Secret Key Input
        self.secret_key_label = QLabel("Secret Key:")
        self.layout.addWidget(self.secret_key_label)
        self.secret_key_input = QLineEdit()
        self.secret_key_input.setPlaceholderText("Enter your secret key...")
        self.layout.addWidget(self.secret_key_input)

        # HMAC Output Path Input
        self.hmac_output_label = QLabel("HMAC Output Path:")
        self.layout.addWidget(self.hmac_output_label)
        self.hmac_output_input = QLineEdit()
        self.hmac_output_input.setPlaceholderText("Select a location to save HMAC...")
        self.layout.addWidget(self.hmac_output_input)
        self.browse_hmac_output_button = QPushButton("Browse HMAC Output")
        self.browse_hmac_output_button.clicked.connect(self.browse_hmac_output)
        self.layout.addWidget(self.browse_hmac_output_button)

        # Buttons for Actions
        self.generate_hmac_button = QPushButton("Generate HMAC")
        self.generate_hmac_button.clicked.connect(self.generate_hmac)
        self.layout.addWidget(self.generate_hmac_button)

        self.verify_hmac_button = QPushButton("Verify HMAC")
        self.verify_hmac_button.clicked.connect(self.verify_hmac)
        self.layout.addWidget(self.verify_hmac_button)

    def browse_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select File", "", "All Files (*)")
        if file_path:
            self.file_path_input.setText(file_path)

    def browse_hmac_output(self):
        hmac_output_path, _ = QFileDialog.getSaveFileName(self, "Save HMAC", "", "HMAC Files (*.hmac)")
        if hmac_output_path:
            self.hmac_output_input.setText(hmac_output_path)

    def generate_hmac(self):
        file_path = self.file_path_input.text()
        secret_key = self.secret_key_input.text()
        hmac_output_path = self.hmac_output_input.text()

        if not file_path or not secret_key or not hmac_output_path:
            self.show_message("Input Error", "Please fill in all fields.", QMessageBox.Warning)
            return

        try:
            hmac_value = FileHMAC.generate_hmac(file_path, secret_key)
            FileHMAC.save_hmac(hmac_value, hmac_output_path)
            self.show_message("Success", "HMAC generated and saved successfully!", QMessageBox.Information)
        except Exception as e:
            self.show_message("Error", f"An error occurred: {str(e)}", QMessageBox.Critical)

    def verify_hmac(self):
        file_path = self.file_path_input.text()
        secret_key = self.secret_key_input.text()
        hmac_output_path = self.hmac_output_input.text()

        if not file_path or not secret_key or not hmac_output_path:
            self.show_message("Input Error", "Please fill in all fields.", QMessageBox.Warning)
            return

        try:
            is_verified = FileHMAC.verify_hmac(file_path, secret_key, hmac_output_path)
            if is_verified:
                self.show_message("Verification", "File Integrity: VERIFIED", QMessageBox.Information)
            else:
                self.show_message("Verification", "File Integrity: NOT VERIFIED", QMessageBox.Warning)
        except Exception as e:
            self.show_message("Error", f"An error occurred: {str(e)}", QMessageBox.Critical)

    def show_message(self, title, message, icon):
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.setIcon(icon)
        msg_box.exec_()

