import os.path
from random import randint

import pypyodbc
import PySide2
from PySide2 import QtWidgets
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

        self.db_conn = None

        self.loginwin = LoginWindow()
        self.loginwin.signalConnection.connect(self.setConnection)
        self.loginwin.signalConnectionError.connect(self.errorConnection)

        self.timer = QTimer(self)
        self.connect(self.timer, SIGNAL('timeout()'), self.showtime)
        self.timer.start(1000)
        self.showtime()

        self.ui.pushButton_3.clicked.connect(self.open_register)
        self.ui.pushButton.clicked.connect(self.open_readers)
        self.ui.pushButton_2.clicked.connect(self.open_yng_readers)
        self.connect(self.ui.actionLog_in, SIGNAL('triggered()'), self.open_login)

    def setConnection(self, emit_conn):
        self.db_conn = emit_conn
        QtWidgets.QMessageBox.about(self, "Successfully", "Connected")

    def errorConnection(self, err):
        QtWidgets.QMessageBox.warning(self, "Error", str(err))

    def showtime(self):
        time = QTime.currentTime()
        text = time.toString('hh:mm')
        if (time.second() % 2) == 0:
            text = text[:2] + ' ' + text[3:]
        self.ui.lcdNumber.display(text)

    def open_register(self):
        if self.db_conn is None:
            self.errorConnection("Please log in")
            # Нет подключения
        else:
            self.regwin = RegisterWindow(self.db_conn)
            self.regwin.show()

    def open_readers(self):

        if self.db_conn is None:
            self.errorConnection("Please log in")
            # Нет подключения
        else:
            self.readerswin = ReadersWindow(self.db_conn)
            self.readerswin.show()

    def open_yng_readers(self):
        if self.db_conn is None:
            self.errorConnection("Please log in")
            # Нет подключения
        else:
            self.youngreaderswin = YoungReadersWindow(self.db_conn)
            self.youngreaderswin.show()

    def open_login(self):
        self.loginwin.show()


class RegisterWindow(QtWidgets.QWidget):
    def __init__(self, db_conn, parent=None):
        super().__init__(parent)

        self.ui = RegForm()
        self.ui.setupUi(self)

        self.ui.tabWidget.setCurrentIndex(0)

        self.db_conn = db_conn

        self.cursor = self.db_conn.cursor()

        self.ui.pushButton.clicked.connect(self.reg)
        self.ui.pushButton_3.clicked.connect(self.yng_reg)

    def reg(self):
            mySQLQuery = ("""INSERT INTO Library.Readers (Reader_id, Last_name,
                                                          First_name, Middle_name,
                                                          Address, Phone_number, Passport_id) 
                                                      
                            VALUES (N'%s', N'%s', N'%s', N'%s', N'%s', N'%s', N'%s')""" % (randint(000000, 999999),
                                                                                           self.ui.lineEdit.text(),
                                                                                           self.ui.lineEdit_2.text(),
                                                                                           self.ui.lineEdit_3.text(),
                                                                                           self.ui.lineEdit_4.text(),
                                                                                           self.ui.lineEdit_5.text(),
                                                                                           self.ui.lineEdit_6.text(),
                                                                                           ))

            self.cursor.execute(mySQLQuery)
            self.db_conn.commit()

    def yng_reg(self):
        mySQLQuery = ("""INSERT INTO Library.Young_readers (reader_id, Last_name,
                                                      First_name, Middle_name,
                                                      birth_id, date_birth_id, parent_id) 

                            VALUES (N'%s', N'%s', N'%s', N'%s', N'%s', N'%s', N'%s')""" % (randint(000000, 999999),
                                                                                           self.ui.lineEdit_13.text(),
                                                                                           self.ui.lineEdit_14.text(),
                                                                                           self.ui.lineEdit_15.text(),
                                                                                           self.ui.lineEdit_16.text(),
                                                                                           self.ui.lineEdit_17.text(),
                                                                                           self.ui.lineEdit_18.text(),
                                                                                           ))

        self.cursor.execute(mySQLQuery)
        self.db_conn.commit()


class ReadersWindow(QtWidgets.QWidget):
    def __init__(self, db_conn, parent=None):
        super().__init__(parent)
        self.ui = ReadersForm()
        self.ui.setupUi(self)

        self.db_conn = db_conn

        cursor = self.db_conn.cursor()
        mySQLQuery = ("""
                        SELECT *
                        FROM Library.Readers
                        """)
        cursor.execute(mySQLQuery)
        data_list = cursor.fetchall()
        header = ['Reader ID', 'Last name', 'First name', 'Middle name', 'Address', 'Phone number', 'Passport ID']

        table_model = MyTableModel(self, data_list, header)
        self.ui.tableView.setModel(table_model)


class YoungReadersWindow(QtWidgets.QWidget):
    def __init__(self, db_conn, parent=None):
        super().__init__(parent)

        self.ui = YoungReadersForm()
        self.ui.setupUi(self)

        self.db_conn = db_conn

        cursor = self.db_conn.cursor()
        mySQLQuery = ("""
                               SELECT *
                               FROM Library.Young_readers
                               """)
        cursor.execute(mySQLQuery)
        data_list = cursor.fetchall()
        header = ['Reader ID', 'Last name', 'First name',
                  'Middle name', 'Birth card ID', 'Date of Birth card ID', 'Parent ID']
        print(data_list)

        table_model = MyTableModel(self, data_list, header)
        self.ui.tableView.setModel(table_model)


class LoginWindow(QtWidgets.QWidget):
    signalConnection = Signal(pypyodbc.Connection)
    signalConnectionError = Signal(pypyodbc.DatabaseError)

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = LoginForm()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.connectDB)

    def connectDB(self):
        username = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()

        try:
            connection = pypyodbc.connect(
                'Driver={SQL Server};'
                'Server=vpngw.avalon.ru;'
                'Database=DevDB2022_IVASHI;'
                'uid=' + username + ';'
                                    'pwd=' + password + ';')

            self.signalConnection.emit(connection)

        except pypyodbc.DatabaseError as err:
            self.signalConnectionError.emit(err)

        self.close()


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
