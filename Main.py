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
from Forms.Search_books import Ui_Form as SearchBooksForm
from Forms.Lending import Ui_Form as LendForm
from Forms.Booking import Ui_Form as BookingForm

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
        self.loginwin.signalConnection.connect(self.set_connection)
        self.loginwin.signalConnectionError.connect(self.errorConnection)

        self.timer = QTimer(self)
        self.connect(self.timer, SIGNAL('timeout()'), self.showtime)
        self.timer.start(1000)
        self.showtime()

        self.ui.pushButton.clicked.connect(self.open_readers)
        self.ui.pushButton_3.clicked.connect(self.open_register)
        self.ui.pushButton_2.clicked.connect(self.open_yng_readers)
        self.ui.pushButton_4.clicked.connect(self.open_search_books)
        self.ui.pushButton_5.clicked.connect(self.open_lending_books)
        self.ui.pushButton_6.clicked.connect(self.open_booking)

        self.connect(self.ui.actionLog_in, SIGNAL('triggered()'), self.open_login)
        self.connect(self.ui.actionLog_out, SIGNAL('triggered()'), self.disable_connection)

    def set_connection(self, emit_conn):
        self.db_conn = emit_conn
        QtWidgets.QMessageBox.about(self, "OK", "Connected")

    def disable_connection(self):
        if self.db_conn is not None:
            self.db_conn = None
            QtWidgets.QMessageBox.about(self, "OK", "disconnected")
        else:
            QtWidgets.QMessageBox.warning(self, "Error", "Already disconnected")

    def errorConnection(self):
        QtWidgets.QMessageBox.warning(self, "Error", "Incorrect username or password")

    def showtime(self):
        time = QTime.currentTime()
        text = time.toString('hh:mm')
        if (time.second() % 2) == 0:
            text = text[:2] + ' ' + text[3:]
        self.ui.lcdNumber.display(text)

    def open_register(self):
        if self.db_conn is None:
            QtWidgets.QMessageBox.warning(self, "Error", "Please login")

        else:
            self.regwin = RegisterWindow(self.db_conn)
            self.regwin.show()

    def open_readers(self):

        if self.db_conn is None:
            QtWidgets.QMessageBox.warning(self, "Error", "Please login")

        else:
            self.readerswin = ReadersWindow(self.db_conn)
            self.readerswin.show()

    def open_yng_readers(self):
        if self.db_conn is None:
            QtWidgets.QMessageBox.warning(self, "Error", "Please login")

        else:
            self.youngreaderswin = YoungReadersWindow(self.db_conn)
            self.youngreaderswin.show()

    def open_login(self):
        self.loginwin.show()

    def open_search_books(self):
        if self.db_conn is None:
            QtWidgets.QMessageBox.warning(self, "Error", "Please login")

        else:
            self.searchwin = SearchBooksWindow(self.db_conn)
            self.searchwin.show()

    def open_lending_books(self):
        if self.db_conn is None:
            QtWidgets.QMessageBox.warning(self, "Error", "Please login")

        else:
            self.lendwin = LendingWindow(self.db_conn)
            self.lendwin.show()

    def open_booking(self):
        if self.db_conn is None:
            QtWidgets.QMessageBox.warning(self, "Error", "Please login")

        else:
            self.bookingwin = BookingWindow(self.db_conn)
            self.bookingwin.show()


class LendingWindow(QtWidgets.QWidget):
    def __init__(self, db_conn, parent=None):
        super().__init__(parent)

        self.ui = LendForm()
        self.ui.setupUi(self)
        self.ui.tabWidget.setCurrentIndex(0)

        self.db_conn = db_conn
        self.cursor = self.db_conn.cursor()

        self.ui.pushButton.clicked.connect(self.lending)

    def lending(self):
        try:
            mySQLQuery = ("""INSERT INTO Library.Lending_of_Books (Book_id, Reader_id, young_reader_id, 
            Date_of_issue, Expected_return_date) 
    
                                VALUES (N'%s', N'%s', NULL, N'%s', N'%s')""" % (self.ui.lineEdit_3.text(),
                                                                                self.ui.lineEdit_2.text(),
                                                                                self.ui.lineEdit.text(),
                                                                                self.ui.lineEdit_4.text(),
                                                                                ))

            issued_change = ("""UPDATE Library.Book_copy SET Issued_not_issued = N'Выдан'
                                
                                WHERE Book_copy_id ='%s' """ % (self.ui.lineEdit_3.text()))

            self.cursor.execute(mySQLQuery)
            self.cursor.execute(issued_change)
            self.db_conn.commit()
            QtWidgets.QMessageBox.about(self, 'OK', 'Note has been added')
            self.close()

        except pypyodbc.IntegrityError:
            QtWidgets.QMessageBox.warning(self, 'Error', 'Incorrect data')


class BookingWindow(QtWidgets.QWidget):
    def __init__(self, db_conn, parent=None):
        super().__init__(parent)

        self.ui = BookingForm()
        self.ui.setupUi(self)
        self.db_conn = db_conn
        self.cursor = self.db_conn.cursor()
        self.ui.pushButton.clicked.connect(self.booking)

    def booking(self):
        try:
            mySQLQuery = ("""INSERT INTO Library.Booking (Book_id, Reader_id, young_reader_id, People_in_queue) 
    
                                VALUES (N'%s', N'%s', NULL, N'%s')""" % (self.ui.lineEdit_2.text(),
                                                                         self.ui.lineEdit.text(),
                                                                         '1'
                                                                         ))

            self.cursor.execute(mySQLQuery)
            self.db_conn.commit()
            QtWidgets.QMessageBox.about(self, 'OK', 'Note has been added')
            self.close()

        except pypyodbc.IntegrityError:
            QtWidgets.QMessageBox.warning(self, 'Error', 'Incorrect data')


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
        try:
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
            QtWidgets.QMessageBox.about(self, 'OK', 'New reader has been added')
            self.close()

        except pypyodbc.IntegrityError:
            QtWidgets.QMessageBox.warning(self, 'Error', 'Incorrect data')

    def yng_reg(self):
        try:
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
            QtWidgets.QMessageBox.about(self, 'OK', 'New reader has been added')
            self.close()

        except pypyodbc.IntegrityError:
            QtWidgets.QMessageBox.warning(self, 'Error', 'Incorrect data')


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


class SearchBooksWindow(QtWidgets.QWidget):
    def __init__(self, db_conn, parent=None):
        super().__init__(parent)
        self.ui = SearchBooksForm()
        self.ui.setupUi(self)

        self.db_conn = db_conn

        cursor = self.db_conn.cursor()
        mySQLQuery = ("""
                        SELECT 
                            Library.Book_copy.Book_copy_id, 
                            Library.Book.Book_title, 
                            Library.Book_copy.ISBN, 
                            Library.Book.Author_id, 
                            Library.Author.First_name, 
                            Library.Author.Last_name, 
                            Library.Author.Country,
                            Library.Book_copy.Issued_not_issued
                        FROM Library.Author 
                        INNER JOIN Library.Book ON Library.Author.Author_id = Library.Book.Author_id CROSS JOIN
                         Library.Book_copy
                        """)
        cursor.execute(mySQLQuery)
        data_list = cursor.fetchall()
        header = ['Book ID', 'Book title', 'ISBN', 'Author ID',
                  'Author first name', 'Author last name', 'Country', 'issued_not_issued']

        table_model = MyTableModel(self, data_list, header)
        self.ui.tableView.setModel(table_model)


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
