import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QTextEdit, QGridLayout
from PyQt5.QtCore import Qt


class AddressBook(QWidget):
    def __init__(self, parent=None):
        super(AddressBook, self).__init__(parent)

        # 新建标签和行编辑框
        namelabel = QLabel("Name:")
        self.nameline = QLineEdit()

        # 新建标签和文本编辑框
        addresslabel = QLabel("Address")
        self.addresstext = QTextEdit()

        # 主体布局设置控件位置
        mainlayout = QGridLayout()
        mainlayout.addWidget(namelabel, 0, 0)
        mainlayout.addWidget(self.nameline, 0, 1)
        mainlayout.addWidget(addresslabel, 1, 0, Qt.AlignTop)  # 设置顶部对齐
        mainlayout.addWidget(self.addresstext, 1, 1)

        # 主体布局生效
        self.setLayout(mainlayout)

        # 设置窗体标题
        self.setWindowTitle("Simple Address Book")


if __name__ == '__main__':
    """创建行编辑框和文本编辑框"""

    # 新建一个应用
    app = QApplication(sys.argv)

    # 新建一个窗体
    addressbook = AddressBook()

    # 窗体显示
    addressbook.show()

    # 应用执行
    sys.exit(app.exec_())
