from PyQt5.QtWidgets import *
import sys

def main_enchilada():
    window.show()
    sys.exit(app.exec_())


app = QApplication([])
app.setApplicationName("Text Editor")
text = QPlainTextEdit()
window = QMainWindow()
window.setCentralWidget(text)
menu = window.menuBar().addMenu("&File")
open_action = QAction("&Open")


def open_file():
    path = QFileDialog.getOpenFileName(window, "Open")[0]
    if path:
        text.setPlainText(open(path).read())

open_action.triggered.connect(open_file)
menu.addAction(open_action)

close = QAction("&Close")
close.triggered.connect(window.close)
menu.addAction(close)

help_menu = window.menuBar().addMenu("&Help")
about_action = QAction("&About")
help_menu.addAction(about_action)

def show_about_dialog():
    text = "<center>" \
           "<h1>Text Editor</h1>" \
           "&#8291;" \
           "<img src=icon.svg" \
           "</center>" \
           "<p>Version 31.4.159.265358<br/>" \
           "Copyright &copy; Company Inc.</p>"
    QMessageBox.about(window, "About Text Editor", text)


about_action.triggered.connect(show_about_dialog)

main_enchilada()
