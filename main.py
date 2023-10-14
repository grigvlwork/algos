import sys
import traceback
import subprocess
import autopep8
import sys
from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox


def run_text(text):
    with open('code.py', 'w') as c:
        c.write(text)
    completed_process = subprocess.run(['python', 'code.py'], capture_output=True, text=True)
    if completed_process.returncode == 0:
        return completed_process.stdout
    else:
        return completed_process.stderr


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('mainwindow.ui', self)
        self.run_btn.clicked.connect(self.run)
        self.pep8_btn.clicked.connect(self.pep8)
        self.clear_btn.clicked.connect(self.clear)

    def clear(self):
        self.source_te.clear()

    def pep8(self):
        text = '<sol1>\n```\n' + self.code1_te.toPlainText() + '\n```\n</sol1>\n\n' + \
               '<sol2>\n```\n' + self.code2_te.toPlainText() + '\n```\n</sol2>\n\n' + \
               '<sol3>\n```\n' + self.code3_te.toPlainText() + '\n```\n</sol3>\n\n' + \
               '<sol4>\n```\n' + self.code4_te.toPlainText() + '\n```\n</sol4>'
        self.source_te.clear()
        self.source_te.appendPlainText(text)

    def run(self):
        t = self.source_te.toPlainText()
        if all(x in t for x in ['<sol1>', '</sol1>']):
            code = t[t.find('<sol1>') + 6:t.find('</sol1>')]
            self.code1_te.clear()
            code = code.replace('```', '').strip()
            code = autopep8.fix_code(code)
            self.code1_te.appendPlainText(code)
            self.result1_lb.setText(run_text(code))
        if all(x in t for x in ['<sol2>', '</sol2>']):
            code = t[t.find('<sol2>') + 6:t.find('</sol2>')]
            self.code2_te.clear()
            code = code.replace('```', '').strip()
            code = autopep8.fix_code(code)
            self.code2_te.appendPlainText(code)
            self.result2_lb.setText(run_text(code))
        if all(x in t for x in ['<sol3>', '</sol3>']):
            code = t[t.find('<sol3>') + 6:t.find('</sol3>')]
            self.code3_te.clear()
            code = code.replace('```', '').strip()
            code = autopep8.fix_code(code)
            self.code3_te.appendPlainText(code)
            self.result3_lb.setText(run_text(code))
        if all(x in t for x in ['<sol4>', '</sol4>']):
            code = t[t.find('<sol4>') + 6:t.find('</sol4>')]
            self.code4_te.clear()
            code = code.replace('```', '').strip()
            code = autopep8.fix_code(code)
            self.code4_te.appendPlainText(code)
            self.result4_lb.setText(run_text(code))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()


    def excepthook(exc_type, exc_value, exc_tb):
        tb = "".join(traceback.format_exception(exc_type, exc_value, exc_tb))
        # tb += '\n'.join(ex.current_rec.get_row())
        print(tb)

        msg = QMessageBox.critical(
            None,
            "Error catched!:",
            tb
        )
        QApplication.quit()


    sys.excepthook = excepthook
    ex.show()
    sys.exit(app.exec_())
