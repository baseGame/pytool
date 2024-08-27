import sys

from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication, QWidget


class CalculatorWindow(QWidget):
    def __init__(self):
        super().__init__()
        # 加载ui文件
        # 方式1 动态加载UI文件.
        # self.ui = QUiLoader().load('calculator.ui')
        # 方式2. 编译为python文件
        # pyside2-uic ui/calculator.ui > ui_main.py
        # 通常采用动态加载比较方便，因为改动界面后，不需要转化，直接运行，特别方便。
        # 但是，如果你的程序里面有非qt-designer提供的控件，这时候，需要在代码里面加上一些额外的声明，而且可能还会有奇怪的问题。往往就要采用转化Python代码的方法。
        # loader = QUiLoader()
        # ui_file = 'ui/calculator.ui'
        # self.ui = QUiLoader().load(ui_file)
        self.ui = QUiLoader().load('ui/calculator.ui')
        self.ui.text_result.clear()
        self.bind()

    def bind(self):
        self.ui.button_0.clicked.connect(self.append_num)
        self.ui.button_1.clicked.connect(self.append_num)
        self.ui.button_2.clicked.connect(self.append_num)
        self.ui.button_3.clicked.connect(self.append_num)
        self.ui.button_4.clicked.connect(self.append_num)
        self.ui.button_5.clicked.connect(self.append_num)
        self.ui.button_6.clicked.connect(self.append_num)
        self.ui.button_7.clicked.connect(self.append_num)
        self.ui.button_8.clicked.connect(self.append_num)
        self.ui.button_9.clicked.connect(self.append_num)
        self.ui.button_dot.clicked.connect(self.append_num)
        self.ui.button_add.clicked.connect(self.append_num)
        self.ui.button_sub.clicked.connect(self.append_num)
        self.ui.button_mul.clicked.connect(self.append_num)
        self.ui.button_div.clicked.connect(self.append_num)
        self.ui.button_eq.clicked.connect(self.calculate)
        self.ui.button_del.clicked.connect(self.delete)

    def append_num(self):
        sender = self.sender()
        text = sender.text()
        if sender == self.ui.button_mul:
            text = '*'
        elif sender == self.ui.button_div:
            text = '/'
        self.ui.text_result.setPlainText(self.ui.text_result.toPlainText() + text)

    def calculate(self):
        text = self.ui.text_result.toPlainText()
        result = eval(text)
        self.ui.text_result.setPlainText(text + '=' + str(result))

    def delete(self):
        text = self.ui.text_result.toPlainText()
        text = text[:-1]
        self.ui.text_result.setPlainText(text)

    # 打包exe


# pyinstaller script.py --noconsole --hidden-import PySide2.QtXml
# --noconsole指定不要命令行窗口，否则我们的程序运行的时候，还会多一个黑窗口。 但是我建议大家可以先去掉这个参数，等确定运行成功后，再加上参数重新制作exe。因为这个黑窗口可以显示出程序的报错，这样我们容易找到问题的线索。
# --hidden -import PySide2.QtXml参数是因为这个
# --icon="logo.ico"
# QtXml库是动态导入，PyInstaller没法分析出来，需要我们告诉它，
# 最后，别忘了，把程序所需要的ui文件拷贝到打包目录中。


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CalculatorWindow()
    window.ui.show()
    sys.exit(app.exec_())
