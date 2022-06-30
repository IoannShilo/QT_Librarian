import os.path

import pypyodbc
import PySide2
from PySide2 import QtWidgets, QtSql
from PySide2.QtCore import *
from PySide2.QtGui import *



from Forms.Main_window import Ui_MainWindow
from Forms.Register import Ui_Form as RegForm
from Forms.Readers import Ui_Form as ReadersForm
from Forms.Young_readers import Ui_Form as YoungReadersForm
from Forms.Login import Ui_Form as LoginForm


dirname = os.path.dirname(PySide2.__file__)
plugin_path = os.path.join(dirname, 'plugins', 'platforms')
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.regwin = RegisterWindow()
        self.readerswin = ReadersWindow()
        self.youngreaderswin = YoungReadersWindow()
        self.loginwin = LoginWindow()

        self.timer = QTimer(self)
        self.connect(self.timer, SIGNAL('timeout()'), self.showtime)
        self.timer.start(1000)
        self.showtime()

        self.ui.pushButton_3.clicked.connect(self.open_register)
        self.ui.pushButton.clicked.connect(self.open_readers)
        self.ui.pushButton_2.clicked.connect(self.open_yng_readers)
        self.connect(self.ui.actionLog_in, SIGNAL('triggered()'), self.open_login)


    def showtime(self):
        time = QTime.currentTime()
        text = time.toString('hh:mm')
        if (time.second() % 2) == 0:
            text = text[:2] + ' ' + text[3:]
        self.ui.lcdNumber.display(text)

    def open_register(self):
        self.regwin.show()

    def open_readers(self):
        self.readerswin.show()


    def open_yng_readers(self):
        self.youngreaderswin.show()


    def open_login(self):
        self.loginwin.show()



class RegisterWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = RegForm()
        self.ui.setupUi(self)


class ReadersWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = ReadersForm()
        self.ui.setupUi(self)
        self.abc = self.ui.tableView


    def run(self, username, password):

        if username == 'tsqllogin' and password == 'Pa$$w0rd':

            connection = pypyodbc.connect(
                'Driver={SQL Server};'
                'Server=vpngw.avalon.ru;'
                'Database=DevDB2022_IVASHI;'
                'uid=' + username + ';'
                'pwd=' + password + ';')

            cursor = connection.cursor()
            mySQLQuery = ("""
                                        SELECT *
                                        FROM Library.Author
                                        """)
            cursor.execute(mySQLQuery)
            data_list = cursor.fetchall()
            header = ['Author id', 'Last name', 'First name', 'Country']
            print(data_list)

            table_model = MyTableModel(self, data_list, header)

            self.abc.setModel(table_model)
        else:
            print('error')



class YoungReadersWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = YoungReadersForm()
        self.ui.setupUi(self)


class LoginWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = LoginForm()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.settext)

    def settext(self):
        username = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()
        aaa = ReadersWindow()
        aaa.run(username, password)



class MyTableModel(QAbstractTableModel):
    def __init__(self, parent, mylist, header, *args):
        QAbstractTableModel.__init__(self, parent, *args)
        self.mylist = mylist
        self.header = header
        self.login = LoginWindow()

    def rowCount(self, parent):
        return len(self.mylist)

    def columnCount(self, parent):
        return len(self.mylist[0])

    def data(self, index, role):
        if not index.isValid():
            return None
        elif role != Qt.DisplayRole:
            return None
        return self.mylist[index.row()][index.column()]

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.header[col]
        return None

    def sort(self, col, order):
        """sort table by given column number col"""
        self.emit(SIGNAL("layoutAboutToBeChanged()"))
        self.mylist = sorted(self.mylist,
            key=operator.itemgetter(col))
        if order == Qt.DescendingOrder:
            self.mylist.reverse()
        self.emit(SIGNAL("layoutChanged()"))













if __name__ == '__main__':
    app = QtWidgets.QApplication()

    myapp = MainWindow()
    myapp.show()

    app.exec_()

