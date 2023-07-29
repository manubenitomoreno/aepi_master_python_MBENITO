from PyQt6.QtWidgets import QApplication

from .mainwindow import MainWindow


def main():
    app = QApplication([])
    window = MainWindow()
    window.setStyleSheet(
    """
    QMainWindow {
        background-color: #E6E6FA;
    }

    QListWidget {
        background-color: #E6E6FA;
        alternate-background-color: #ffffff;
        color: #333333;
    }

    QPushButton {
        background-color: #8A2BE2;
        color: #ffffff;
        border: none;
        border-radius: 4px;
        padding: 8px;
    }

    QPushButton:hover {
        background-color: #6A1E9E;
    }

    QPushButton:pressed {
        background-color: #49276D;
    }

    QLineEdit {
        background-color: #ffffff;
        border: 1px solid #8A2BE2;
        border-radius: 4px;
        padding: 4px;
    }
    """
)

    window.show()
    app.exec()


if __name__ == '__main__':
    main()