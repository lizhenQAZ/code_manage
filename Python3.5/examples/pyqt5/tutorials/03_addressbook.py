import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QTextEdit, QGridLayout, QPushButton, QVBoxLayout, QMessageBox, QHBoxLayout
from PyQt5.QtCore import Qt


class SortedDict(dict):
    class Iterator(object):
        def __init__(self, sorted_dict):
            self._dict = sorted_dict
            self._keys = sorted(self._dict.keys())
            self._nr_items = len(self._keys)
            self._idx = 0

        def __iter__(self):
            return self

        def next(self):
            if self._idx >= self._nr_items:
                raise StopIteration
            key = self._keys[self._idx]
            value = self._dict[key]
            self._idx += 1
            return key, value

        __next__ = next

    def __iter__(self):
        return SortedDict.Iterator(self)

    iterkeys = __iter__


class AddressBook(QWidget):
    def __init__(self, parent=None):
        super(AddressBook, self).__init__(parent)

        self.contacts = SortedDict()  # 设置通讯录
        self.oldname = ''  # 设置名字
        self.oldaddress = ''  # 设置地址

        # 新建标签和编辑框
        namelabel = QLabel("Name:")  # 设置标签
        self.nameline = QLineEdit()  # 设置行编辑框
        self.nameline.setReadOnly(True)  # 设置行编辑框为只读
        addresslabel = QLabel("Address")
        self.addresstext = QTextEdit()  # 设置文本编辑框
        self.addresstext.setReadOnly(True)  # 设置文本编辑框为只读

        # 新建按钮对象
        self.addbutton = QPushButton('&Add')  # 设置新建按钮对象
        self.addbutton.show()  # 设置按钮对象显示
        self.submitbutton = QPushButton('&Submit')  # 设置提交按钮对象
        self.submitbutton.hide()  # 设置按钮对象隐藏
        self.cancelbutton = QPushButton('&Cancel')  # 设置取消按钮对象
        self.cancelbutton.hide()
        self.nextbutton = QPushButton('&Next')  # 设置向下翻页按钮
        self.nextbutton.setEnabled(False)
        self.previousbutton = QPushButton('&Previous')  # 设置向上翻页按钮
        self.previousbutton.setEnabled(False)

        # 按钮对象绑定事件
        self.addbutton.clicked.connect(self.addcontact)  # 设置增加事件
        self.submitbutton.clicked.connect(self.submitcontact)  # 设置提交事件
        self.cancelbutton.clicked.connect(self.cancel)  # 设置取消事件
        self.nextbutton.clicked.connect(self.nextpage)  # 设置向下翻页事件
        self.previousbutton.clicked.connect(self.previouspage)  # 设置向上翻页事件

        # VB布局设置按钮位置
        buttonlayout1 = QVBoxLayout()
        buttonlayout1.addWidget(self.addbutton, Qt.AlignTop)
        buttonlayout1.addWidget(self.submitbutton)
        buttonlayout1.addWidget(self.cancelbutton)
        buttonlayout1.addStretch()  # VB布局生效

        # HB布局设置按钮位置
        buttonlayout2 = QHBoxLayout()
        buttonlayout2.addWidget(self.previousbutton)
        buttonlayout2.addWidget(self.nextbutton)

        # 网状布局设置标签、行编辑框、文本框、按钮位置
        mainlayout = QGridLayout()
        mainlayout.addWidget(namelabel, 0, 0)
        mainlayout.addWidget(self.nameline, 0, 1)
        mainlayout.addWidget(addresslabel, 1, 0, Qt.AlignTop)  # 设置顶部对齐
        mainlayout.addWidget(self.addresstext, 1, 1)

        mainlayout.addLayout(buttonlayout1, 1, 2)  # 增加VB布局按钮
        mainlayout.addLayout(buttonlayout2, 3, 1)  # 增加HB布局按钮
        self.setLayout(mainlayout)  # 主体布局生效
        self.setWindowTitle("Simple Address Book")  # 设置窗体标题

    def addcontact(self):
        self.oldname = self.nameline.text()  # 设置行编辑框值
        self.oldaddress = self.addresstext.toPlainText()  # 设置文本编辑框值

        self.nameline.clear()  # 设置行编辑框为初始值
        self.addresstext.clear()  # 设置文本编辑框为初始值

        self.nameline.setReadOnly(False)  # 设置行编辑框不可用
        self.nameline.setFocus(Qt.OtherFocusReason)
        self.addresstext.setReadOnly(False)  # 设置文本编辑框不可用

        self.addbutton.setEnabled(False)  # 设置新增按钮不可用
        self.nextbutton.setEnabled(False)  # 设置向下翻页按钮不可用
        self.nextbutton.setEnabled(False)  # 设置向上翻页按钮不可用
        self.submitbutton.show()  # 设置提交按钮显示
        self.cancelbutton.show()  # 设置取消按钮显示

    def submitcontact(self):
        name = self.nameline.text()  # 获取行编辑框值
        address = self.addresstext.toPlainText()  # 获取文本编辑框值

        if name == "" or address == "":  # 行编辑框值为空时设置提醒
            QMessageBox.information(self, "Empty Field", "Please enter a name and address.")
            return

        if name not in self.contacts:  # 行编辑框值不在列表中时存入通讯录
            self.contacts[name] = address
            QMessageBox.information(self, "Add Successful", "\"%s\" has been added to your address book." % name)
        else:  # 否则，设置提醒不能存入通讯录
            QMessageBox.information(self, "Add Unsuccessful", "Sorry, \"%s\" is already in your address book." % name)
            return

        if not self.contacts:  # 通讯录空时，清空编辑框值
            self.nameline.clear()  # 设置行编辑框初始值
            self.addresstext.clear()  # 设置文本编辑框为初始值

        self.nameline.setReadOnly(True)  # 设置行编辑框为可读
        self.addresstext.setReadOnly(True)  # 设置文本编辑框为可读
        self.addbutton.setEnabled(True)  # 设置新增按钮可用

        number = len(self.contacts)  # 通讯录的记录个数决定是否可以翻页
        self.nextbutton.setEnabled(number > 1)
        self.previousbutton.setEnabled(number > 1)
        self.submitbutton.hide()  # 设置提交按钮隐藏
        self.cancelbutton.hide()  # 设置取消按钮隐藏

    def cancel(self):
        self.nameline.setText(self.oldname)  # 设置行编辑框为初始值
        self.addresstext.setText(self.oldaddress)  # 设置文本编辑框为初始值

        if not self.contacts:
            self.nameline.clear()
            self.address.clear()
        self.nameline.setReadOnly(True)
        self.addresstext.setReadOnly(True)
        self.addbutton.setEnabled(True)  # 设置新增按钮为可用

        number = len(self.contacts)
        self.nextbutton.setEnabled(number > 1)
        self.previousbutton.setEnabled(number > 1)
        self.submitbutton.hide()  # 设置提交按钮隐藏
        self.cancelbutton.hide()  # 设置取消按钮隐藏

    def nextpage(self):
        name = self.nameline.text()
        it = iter(self.contacts)

        try:
            while True:
                this_name, _ = it.next()

                if this_name == name:
                    next_name, next_address = it.next()
                    break
        except StopIteration:
            next_name, next_address = iter(self.contacts).next()

        self.nameline.setText(next_name)
        self.addresstext.setText(next_address)

    def previouspage(self):
        name = self.nameline.text()

        prev_name = prev_address = None
        for this_name, this_address in self.contacts:
            if this_name == name:
                break

            prev_name = this_name
            prev_address = this_address
        else:
            self.nameline.clear()
            self.address.clear()
            return

        if prev_name is None:
            for prev_name, prev_addreess in self.contacts:
                pass

        self.nameline.setText(prev_name)
        self.addresstext.setText(prev_address)


if __name__ == '__main__':
    """新增通讯录得上下翻页功能"""

    # 新建一个应用
    app = QApplication(sys.argv)

    # 新建一个窗体
    addressbook = AddressBook()

    # 窗体显示
    addressbook.show()

    # 应用执行
    sys.exit(app.exec_())
