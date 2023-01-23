# BY: Xylem Inc.(ITC-M/C-Vadodara)
# PROJECT MADE WITH: Qt Designer and PySide2
# V: 1.0.0
import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence,
                           QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
import pyodbc
import datetime
import time
import os
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import platform
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as Navi
from matplotlib.figure import Figure
from pretty_html_table import build_table
# GUI FILE
from app_modules import *

# define some global variables - Start
ServerName = ''
DataBaseName = ''
SQL_Driver = 'Driver={ODBC Driver 17 for SQL Server};'
conn = ''
cursor = ''
from_date = ''
to_date = ''
find_date = ''
from_time = ''
to_time = ''
sql_query = ''
csv_data = ''
Data_col = []
calender_out = ''
Final_query = ''
map_path = ''
Map_not_found = ''
user_sts = 0
connection_sts = 0
html_data = ''


# define some global variables - End


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self, parent=None)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # REMOVE ==> STANDARD TITLE BAR
        UIFunctions.removeTitleBar(True)
        # ==> END ##

        # SET ==> WINDOW TITLE
        self.setWindowTitle('Main - Reporting Tool')
        UIFunctions.labelTitle(self, 'Main - Reporting Tool')
        UIFunctions.labelDescription(self, 'Set text')
        # ==> END ##

        # WINDOW SIZE ==> DEFAULT SIZE
        startSize = QSize(1000, 720)
        self.resize(startSize)
        self.setMinimumSize(startSize)
        # UIFunctions.enableMaximumSize(self, 500, 720)
        # ==> END ##

        # ==> CREATE MENUS
        ########################################################################

        # ==> TOGGLE MENU SIZE
        self.ui.btn_toggle_menu.clicked.connect(lambda: UIFunctions.toggleMenu(self, 220, True))
        # ==> END ##

        # ==> ADD CUSTOM MENUS
        self.ui.stackedWidget.setMinimumWidth(20)
        UIFunctions.addNewMenu(self, "Home", "btn_home", "url(:/16x16/icons/16x16/cil-home.png)", True)
        UIFunctions.addNewMenu(self, "User Login", "btn_new_user", "url(:/16x16/icons/16x16/cil-user.png)", True)
        UIFunctions.addNewMenu(self, "Connection", "btn_conn", "url(:/16x16/icons/16x16/cil-link-alt.png)", True)
        UIFunctions.addNewMenu(self, "Data Table", "btn_table", "url(:/16x16/icons/16x16/cil-view-module.png)", True)
        UIFunctions.addNewMenu(self, "Data Chart", "btn_graph", "url(:/16x16/icons/16x16/cil-chart-line.png)", True)
        UIFunctions.addNewMenu(self, "Send Email", "btn_email", "url(:/16x16/icons/16x16/cil-cursor.png)", True)
        UIFunctions.addNewMenu(self, "Setting", "btn_widgets", "url(:/16x16/icons/16x16/cil-equalizer.png)",
                               False)
        # ==> END ##

        # START MENU => SELECTION
        UIFunctions.selectStandardMenu(self, "btn_home")
        # ==> END ##

        # ==> START PAGE
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
        # ==> END ##

        # USER ICON ==> SHOW HIDE
        UIFunctions.userIcon(self, "AT", "", True)

        # ==> END ##

        # ==> SET TODAY'S DATE IN TO DATE SELECTION AT INITIAL STAGE##
        today_date = datetime.datetime.today()
        self.ui.To_Date.setDate(today_date)
        self.ui.To_Date_G.setDate(today_date)

        # ==> MOVE WINDOW / MAXIMIZE / RESTORE
        ########################################################################
        def moveWindow(event):
            # IF MAXIMIZED CHANGE TO NORMAL
            if UIFunctions.returStatus(self) == 1:
                UIFunctions.maximize_restore(self)

            # MOVE WINDOW
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        # WIDGET TO MOVE
        self.ui.frame_label_top_btns.mouseMoveEvent = moveWindow
        # ==> END ##

        # ==> LOAD DEFINITIONS
        ########################################################################
        UIFunctions.uiDefinitions(self)
        # ==> END ##

        ########################################################################
        # END - WINDOW ATTRIBUTES
        # ############################# ---/--/--- ############################ #

        ########################################################################
        #                                                                      #
        # START -------------- WIDGETS FUNCTIONS/PARAMETERS ---------------- ##
        #                                                                      #
        # ==> USER CODES BELLOW                                              ##
        ########################################################################

        # ==> QTableWidget PARAMETERS
        ########################################################################
        # self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        # ==> END ##

        ########################################################################
        #                                                                      #
        # END --------------- WIDGETS FUNCTIONS/PARAMETERS ----------------- ##
        #                                                                      #
        # ############################# ---/--/--- ############################ #

        # SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        # ==> END ##

        # ASSIGN FUNCTION TO log in BUTTON
        self.ui.login.clicked.connect(self.loginfunction)
        self.ui.From_Date_PB.clicked.connect(self.F_Date_Pick)
        self.ui.To_Date_PB.clicked.connect(self.T_Date_Pick)
        self.ui.LoadAll_PB.clicked.connect(self.Load_Data)
        self.ui.Filter_PB.clicked.connect(self.Load_panda)
        self.ui.Export_PB.clicked.connect(self.Export_CSV)
        self.ui.btn_browse.clicked.connect(self.browse_file)
        self.ui.btn_save.clicked.connect(self.save_data)
        self.ui.Connect_PB.clicked.connect(self.Connection)
        self.ui.clear_PB.clicked.connect(self.Remove_file)

        # Setting Page Function ###########################
        global map_path
        if os.path.exists("Mapping_path.txt"):
            f = open("Mapping_path.txt", "r+")
            Dsp = f.readlines()
            Dp = [x.strip() for x in Dsp]
            f.close()
            map_path = Dp[0]
            self.ui.browsefile.setText(Dp[0])

        # Connection Page Function ###########################
        # set initial data in connection window if connection file is already there
        if os.path.exists("DataBase.txt"):
            f = open("DataBase.txt", "r+")
            Dsp = f.readlines()
            Dp = [x.strip() for x in Dsp]
            self.ui.ServerName.setText(Dp[0])
            self.ui.DataBase.setText(Dp[1])

        # SETUP GRAPHS  ###########################

        # Assign Function To Buttons On Graph Page
        self.canv = MatplotlibCanvas(self)
        self.df = []
        self.toolbar = Navi(self.canv, self)
        # self.ui.graph_tool.addWidget(self.toolbar)
        self.themes = ['bmh', 'classic', 'dark_background', 'fast',
                       'fivethirtyeight', 'ggplot', 'grayscale', 'seaborn-bright',
                       'seaborn-colorblind', 'seaborn-dark-palette', 'seaborn-dark',
                       'seaborn-darkgrid', 'seaborn-deep', 'seaborn-muted', 'seaborn-notebook',
                       'seaborn-paper', 'seaborn-pastel', 'seaborn-poster', 'seaborn-talk',
                       'seaborn-ticks', 'seaborn-white', 'seaborn-whitegrid', 'seaborn',
                       'Solarize_Light2', 'tableau-colorblind10']

        self.ui.From_Date_PB_G.clicked.connect(self.F_Date_Pick_chart)
        self.ui.To_Date_PB_G.clicked.connect(self.T_Date_Pick_chart)
        self.ui.LoadAll_PB_G.clicked.connect(self.Load_Chart)
        self.ui.Filter_PB_G.clicked.connect(self.Filter_chart)
        self.ui.email_send_pb.clicked.connect(self.email_report)

    ########################################################################
    # MENUS ==> DYNAMIC MENUS FUNCTIONS
    ########################################################################

    def Button(self):
        global user_sts
        # GET BT CLICKED
        btnWidget = self.sender()

        # PAGE HOME
        if btnWidget.objectName() == "btn_home":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
            UIFunctions.resetStyle(self, "btn_home")
            UIFunctions.labelPage(self, "Home")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))

        # PAGE NEW USER
        if btnWidget.objectName() == "btn_new_user":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_login)
            UIFunctions.resetStyle(self, "btn_new_user")
            UIFunctions.labelPage(self, "User Login")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))

        # PAGE WIDGETS
        if btnWidget.objectName() == "btn_widgets":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_setup)
            UIFunctions.resetStyle(self, "btn_widgets")
            UIFunctions.labelPage(self, "Settings")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))

        # PAGE DATA VIEW
        if btnWidget.objectName() == "btn_table":
            global user_sts
            if user_sts == 1:
                self.ui.stackedWidget.setCurrentWidget(self.ui.page_data)
                UIFunctions.resetStyle(self, "btn_table")
                UIFunctions.labelPage(self, "Data Table")
                btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))
            else:
                text = "Please Login."
                UIFunctions.msg_box(self, text)

        # PAGE CONNECTION
        if btnWidget.objectName() == "btn_conn":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_conn)
            UIFunctions.resetStyle(self, "btn_conn")
            UIFunctions.labelPage(self, "Connection")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))

        # PAGE GRAPH
        if btnWidget.objectName() == "btn_graph":

            if user_sts == 1:
                self.ui.stackedWidget.setCurrentWidget(self.ui.page_graph)
                UIFunctions.resetStyle(self, "btn_graph")
                UIFunctions.labelPage(self, "Data Chart")
                btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))
            else:
                text = "Please Login."
                UIFunctions.msg_box(self, text)

        # PAGE CONNECTION
        if btnWidget.objectName() == "btn_email":
            self.ui.stackedWidget.setCurrentWidget(self.ui.Email_setup)
            UIFunctions.resetStyle(self, "btn_email")
            UIFunctions.labelPage(self, "Send Email")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))

    # ==> END ##

    def Connection(self):
        global conn, cursor, sql_query, Final_query, Map_not_found, connection_sts
        serverName = self.ui.ServerName.text()
        dataBaseName = self.ui.DataBase.text()

        if not os.path.exists("DataBase.txt"):
            f = open("DataBase.txt", "w+")
            f.write(f"{serverName}\n")
            f.write(f"{dataBaseName}\n")
            f.close()
            try:

                read_map()
                if Map_not_found == 1:
                    text = "Mapping File Not Found."
                    UIFunctions.msg_box(self, text)
                # sql_query = pd.read_sql_query(Final_query, conn)
                text = "Data Base Connected Successfully."
                UIFunctions.msg_box(self, text)
                connection_sts = 1

            except (Exception,):
                text = "Connection Failed."
                UIFunctions.msg_box(self, text)
                connection_sts = 0
        else:
            try:
                conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                                      f'Server={serverName};'
                                      'Port=1433;'
                                      f'Database={dataBaseName};'
                                      'Trusted_Connection=yes;')
                cursor = conn.cursor()
                read_map()

                text = "Data Base Connected Successfully."
                UIFunctions.msg_box(self, text)
                connection_sts = 1

            except (Exception,):
                text = "Connection Failed."
                UIFunctions.msg_box(self, text)
                connection_sts = 0

    def Remove_file(self):
        if os.path.exists("DataBase.txt"):
            os.remove("DataBase.txt")
            self.ui.ServerName.clear()
            self.ui.DataBase.clear()
        else:
            pass

    # ==> LOG IN FUNCTION - START
    def loginfunction(self):
        global user_sts, conn
        user = self.ui.emailfield.text()
        password = self.ui.passwordfield.text()
        # host = os.environ['COMPUTERNAME']

        if len(user) == 0 or len(password) == 0:
            self.ui.error.setText("Please input all fields.")

        else:
            conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                                  'Server=localhost;'
                                  'Port=1433;'
                                  'Database=Users;'
                                  'Trusted_Connection=yes;')
            cur = conn.cursor()
            query1 = '''SELECT (CASE WHEN EXISTS(SELECT 1 FROM dbo.login_info WITH(NOLOCK) 
            WHERE Username = ?) THEN 1 ELSE 0 END) as result'''
            cur.execute(query1, user)
            result_user = cur.fetchone()[0]
            if result_user == 1:
                query = 'SELECT Password FROM login_info WHERE Username =\'' + user + "\'"
                cur.execute(query)
                result_pass = cur.fetchone()[0]
                if result_pass == password and int(result_user) == 1:
                    # Display Message
                    text = "Login Successful."
                    UIFunctions.msg_box(self, text)
                    user_sts = 1
                    self.ui.error.setText("")
                else:
                    self.ui.error.setText("Invalid username or password")
            else:
                self.ui.error.setText("Invalid username or password")

    # ==> LOG IN FUNCTION - END

    # ==> From Date selection - Start # For Table View
    def F_Date_Pick(self):
        modal_dialog = calender(self)
        modal_dialog.calender_out.connect(self.From_date_pick)  # connect signal and slot
        modal_dialog.setModal(True)
        modal_dialog.show()

    def From_date_pick(self, F):
        self.ui.From_Date.setDate(F)

    # ==> From Date selection - End

    # ==> To Date selection - Start
    def T_Date_Pick(self):
        modal_dialog = calender(self)
        modal_dialog.calender_out.connect(self.To_date_pick)  # connect signal and slot
        modal_dialog.setModal(True)
        modal_dialog.show()

    def To_date_pick(self, T):
        self.ui.To_Date.setDate(T)

    # ==> To Date selection - End # For Table View

    # ==> From Date selection - Start # For Chart View
    def F_Date_Pick_chart(self):
        modal_dialog = calender(self)
        modal_dialog.calender_out.connect(self.From_date_pick_chart)  # connect signal and slot
        modal_dialog.setModal(True)
        modal_dialog.show()

    def From_date_pick_chart(self, F):
        self.ui.From_Date_G.setDate(F)

    # ==> From Date selection - End

    # ==> To Date selection - Start
    def T_Date_Pick_chart(self):
        modal_dialog = calender(self)
        modal_dialog.calender_out.connect(self.To_date_pick_chart)  # connect signal and slot
        modal_dialog.setModal(True)
        modal_dialog.show()

    def To_date_pick_chart(self, T):
        self.ui.To_Date_G.setDate(T)

    # ==> To Date selection - End # For Chart View

    # ==> Export to CSV - Start
    def Export_CSV(self):
        # df = pd.DataFrame(sql_query)
        global csv_data
        time_now = datetime.datetime.now()
        path = os.path.join(os.path.expanduser("~"), 'C:', 'Desktop')
        # place 'r' before the path name to avoid any errors in the path
        csv_data.to_csv(fr'{path}\export_data_{time_now.strftime("%Y-%m-%d")}.csv', index=False)
        # Message
        text = "Data Exported To CSV File Successfully."
        UIFunctions.msg_box(self, text)

    # ==> Export to CSV - END

    # ==> Load all Data - Start
    def Load_Data(self):
        global csv_data, Data_col, sql_query, Map_not_found, Final_query, connection_sts, html_data
        if connection_sts == 1:
            if Map_not_found != 1:
                sql_query = pd.read_sql_query(Final_query, conn)
                Data = pd.DataFrame(sql_query)
                conn.commit()
                Data['DateTime'] = pd.to_datetime(Data['DateTime'])
                # Change Datetime Format
                Data['DateTime'] = Data['DateTime'].dt.strftime('%d-%m-%Y %H:%M:%S')
                csv_data = Data
                # convert data into html Format for sending email
                html_data = build_table(csv_data, 'blue_light')
                Data_col = list(Data.columns)
                # Add item to combo box
                self.ui.colom_name.clear()
                self.ui.colom_name.addItem("All Fields")
                self.ui.colom_name.addItems(Data_col[1:])

                numrows = len(Data)
                self.ui.Data_Table.setColumnCount(len(Data.columns))
                self.ui.Data_Table.setRowCount(numrows)
                self.ui.Data_Table.setHorizontalHeaderLabels(Data.columns)

                for i in range(numrows):
                    for j in range(len(Data.columns)):
                        self.ui.Data_Table.setItem(i, j, QtWidgets.QTableWidgetItem(str(Data.iat[i, j])))
                self.ui.Data_Table.resizeColumnsToContents()

                # print message for no data
                if len(Data) == 0:
                    text = "No Data Found."
                    UIFunctions.msg_box(self, text)
            else:
                text = "Mapping File Not Found."
                UIFunctions.msg_box(self, text)
        else:
            text = "Please Connect The DataBase."
            UIFunctions.msg_box(self, text)

    # ==> Load all Data - End

    # ==> Load filter Data - Start
    def Load_panda(self):

        global from_date, to_date, find_date, to_time, from_time, csv_data, Map_not_found, connection_sts, conn, \
            html_data
        # select from and to date for filter from UI
        select_from_date = self.ui.From_Date.date()
        select_to_date = self.ui.To_Date.date()
        from_date = select_from_date.toPython()
        to_date = select_to_date.toPython()

        # select from and to Time for filter from UI
        select_from_time = self.ui.From_Time.time()
        select_to_time = self.ui.To_Time.time()
        from_time = select_from_time.toPython()
        to_time = select_to_time.toPython()
        find_date1 = datetime.datetime.combine(from_date, from_time)
        find_date2 = datetime.datetime.combine(to_date, to_time)

        # Pass The SQL Query and read data from SQL Database
        if connection_sts == 1:
            if Map_not_found != 1:
                query = pd.read_sql_query(Final_query, conn)
                Data = pd.DataFrame(query)
                conn.commit()
                Data['DateTime'] = pd.to_datetime(Data['DateTime'])

                # Filter Data based on datetime and column
                mask = (Data['DateTime'] > find_date1) & (Data['DateTime'] <= find_date2)
                Data = Data.loc[mask]
                # Change Date Time Format
                Data['DateTime'] = Data['DateTime'].dt.strftime('%d-%m-%Y %H:%M:%S')
                filt = self.ui.colom_name.currentText()
                filt_index = self.ui.colom_name.currentIndex()
                if filt_index != 0:
                    Data = Data.filter(['DateTime', filt])
                    Data = Data.dropna()  # Drop NAN Values from Table
                csv_data = Data
                # convert data into html Format for sending email
                html_data = build_table(csv_data, 'blue_light')
                # Plot data in Table
                num_rows = len(Data)
                self.ui.Data_Table.setColumnCount(len(Data.columns))
                self.ui.Data_Table.setRowCount(num_rows)
                self.ui.Data_Table.setHorizontalHeaderLabels(Data.columns)

                for i in range(num_rows):
                    for j in range(len(Data.columns)):
                        self.ui.Data_Table.setItem(i, j, QtWidgets.QTableWidgetItem(str(Data.iat[i, j])))
                self.ui.Data_Table.resizeColumnsToContents()

                # print message for no data
                if len(Data) == 0:
                    text = "No Data Found."
                    UIFunctions.msg_box(self, text)
            else:
                text = "Mapping File Not Found."
                UIFunctions.msg_box(self, text)
        else:
            text = "Please Connect The DataBase."
            UIFunctions.msg_box(self, text)

    # ==> Load filter Data - End

    # ==> Browse Excel file function - Start

    def browse_file(self):
        global map_path
        path = os.path.curdir
        filter_file = 'Excel File(*.xls, *.xlsx)'
        file = QFileDialog.getOpenFileName(self, 'open file', path, filter_file)
        self.ui.browsefile.setText(file[0])
        map_path = file[0]

    # ==> Browse Excel file function - End

    # ==> save mapping file function - Start

    def save_data(self):
        path = self.ui.browsefile.text()
        if not os.path.exists("Mapping_path.txt"):
            f = open("Mapping_path.txt", "w+")
            f.write(f"{path}\n")
            f.close()
            read_map()
            text = "Mapping Saved Successfully."
            UIFunctions.msg_box(self, text)
        else:
            os.remove("Mapping_path.txt")
            f = open("Mapping_path.txt", "w+")
            f.write(f"{path}\n")
            f.close()
            read_map()
            text = "Mapping Saved Successfully."
            UIFunctions.msg_box(self, text)

    # ==> save mapping file function - End

    # ==> Load all Data - Start
    def Load_Chart(self):
        global csv_data, Data_col, sql_query, Map_not_found, Final_query, connection_sts, conn
        if connection_sts == 1:
            if Map_not_found != 1:
                sql_query = pd.read_sql_query(Final_query, conn)
                self.df = pd.DataFrame(sql_query)
                self.df['DateTime'] = pd.to_datetime(self.df['DateTime'])

                # Change Datetime Format
                self.df['DateTime'] = self.df['DateTime'].dt.strftime('%d-%m-%Y %H:%M:%S')
                Data_col = list(self.df.columns)

                # Add item to combo box
                self.ui.colom_name_G.clear()
                self.ui.colom_name_G.addItem("All Fields")
                self.ui.colom_name_G.addItems(Data_col[1:])

                # Add Data into Chart
                plt.clf()  # Clear the Plot #

                try:
                    self.ui.graph_tool.removeWidget(self.toolbar)
                    self.ui.graph.removeWidget(self.canv)

                    QObject.deleteLater(self.toolbar)
                    QObject.deleteLater(self.canv)
                    self.toolbar = None
                    self.canv = None

                except Exception as e:
                    UIFunctions.msg_box(self, str(e))

                self.canv = MatplotlibCanvas(self)
                self.toolbar = Navi(self.canv, self)

                self.ui.graph_tool.addWidget(self.toolbar)
                self.ui.graph.addWidget(self.canv)

                self.canv.axes.cla()
                ax = self.canv.axes

                self.df.sort_values('DateTime', inplace=True)
                self.df.set_index('DateTime').plot(ax=self.canv.axes)
                ax.grid()
                # cur = matplotlib.widgets.Cursor(ax, horizon=True, verton=True, useblit=True, color='red', linewidth=1)

                legend = ax.legend()
                legend.set_draggable(True)

                ax.set_xlabel('Date')
                ax.set_ylabel('Value')
                ax.set_title("Data Visualization")

                self.canv.draw()
                conn.commit()

                # print message for no data
                if len(self.df) == 0:
                    text = "No Data Found."
                    UIFunctions.msg_box(self, text)
            else:
                text = "Mapping File Not Found."
                UIFunctions.msg_box(self, text)
        else:
            text = "Please Connect The DataBase."
            UIFunctions.msg_box(self, text)

    # ==> Load all Data - End

    # ==> Load filter Data - Start
    def Filter_chart(self):
        global find_date, Map_not_found, connection_sts

        # select from and to date for filter from UI
        select_from_date = self.ui.From_Date_G.date()
        select_to_date = self.ui.To_Date_G.date()
        from_date_G = datetime.datetime.combine(select_from_date.toPython(), datetime.datetime.min.time())
        to_date_G = datetime.datetime.combine(select_to_date.toPython(), datetime.datetime.min.time())

        # Pass The SQL Query and read data from SQL Database
        if connection_sts == 1:
            if Map_not_found != 1:
                query = pd.read_sql_query(Final_query, conn)
                self.df = pd.DataFrame(query)
                self.df['DateTime'] = pd.to_datetime(self.df['DateTime'])

                # Filter Data based on datetime and column
                mask = (self.df['DateTime'] > from_date_G) & (self.df['DateTime'] <= to_date_G)
                self.df = self.df.loc[mask]
                # Change Date Time Format
                self.df['DateTime'] = self.df['DateTime'].dt.strftime('%d-%m-%Y %H:%M:%S')
                filt = self.ui.colom_name_G.currentText()
                filt_index = self.ui.colom_name_G.currentIndex()
                if filt_index != 0:
                    self.df = self.df.filter(['DateTime', filt])
                    self.df = self.df.dropna()  # Drop NAN Values from Table

                # Plot data in Chart
                plt.clf()
                try:
                    self.ui.graph_tool.removeWidget(self.toolbar)
                    self.ui.graph.removeWidget(self.canv)

                    QObject.deleteLater(self.toolbar)
                    QObject.deleteLater(self.canv)
                    self.toolbar = None
                    self.canv = None

                except Exception as e:
                    UIFunctions.msg_box(self, str(e))

                self.canv = MatplotlibCanvas(self)
                self.toolbar = Navi(self.canv, self)

                self.ui.graph_tool.addWidget(self.toolbar)
                self.ui.graph.addWidget(self.canv)

                self.canv.axes.cla()
                ax = self.canv.axes
                self.df.sort_values('DateTime', inplace=True)
                self.df.set_index('DateTime').plot(ax=self.canv.axes)

                legend = ax.legend()
                legend.set_draggable(True)

                ax.set_xlabel('Date')
                ax.set_ylabel('Value')
                ax.set_title("Data Visualization")

                self.canv.draw()

                # print message for no data
                if len(self.df) == 0:
                    text = "No Data Found."
                    UIFunctions.msg_box(self, text)
            else:
                text = "Mapping File Not Found."
                UIFunctions.msg_box(self, text)
        else:
            text = "Please Connect The DataBase."
            UIFunctions.msg_box(self, text)

    # ==> Load filter Data - End

    def email_report(self):
        import Email_module as email

        to = self.ui.sendors_email.text()
        fromm = self.ui.recivers_email.text()

        # msg = "Hello This Message is Generated By Reporting Tool"
        mail = email.send_email(html_data, to, fromm)
        if mail == 0:
            text = "Email Send Successfully."
            UIFunctions.msg_box(self, text)
        else:
            UIFunctions.msg_box(self, str(mail))


    # EVENT ==> MOUSE CLICK
    ########################################################################
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()


########################################################################
# READ MAPPING FILE ==> READ MAPPING FUNCTIONS (EXCEL FILE)
########################################################################


def read_map():
    global Final_query, map_path, Map_not_found
    import openpyexcel

    # read Mapping file
    if os.path.exists("Mapping_path.txt"):
        f = open("Mapping_path.txt", "r+")
        Dsp = f.readlines()
        Dp = [x.strip() for x in Dsp]
        f.close()
        map_path = Dp[0]
    else:
        pass
    file = map_path

    if os.path.exists(file):
        workbook = openpyexcel.load_workbook(file)
        worksheet = workbook.active
        num_rows = worksheet.max_row
        Data = []
        for i in range(1, num_rows + 1):
            cell_obj = worksheet.cell(row=i, column=1)
            Data.append(cell_obj.value)
        # create raw query using for loop
        list_query = []
        num_tag = int(num_rows)

        for i in range(0, num_tag):
            list_query.append(f"max(case when TagIndex = {i} then Val end) as {Data[i]}")
        # create final query
        query = 'DateAndTime as DateTime'
        for i in range(0, len(list_query)):
            query = query + ',' + list_query[i]
        select_str = query
        from_str = '(select *,ROW_NUMBER() over(partition by Tagindex order by DateAndTime) as op from ' \
                   'FloatTable)ft '
        Final_query = f'select {select_str} from {from_str} group by op,ft.DateAndTime;'
        Map_not_found = 0

    else:
        Map_not_found = 1


########################################################################
# ==> Create Calender Ppo-up - Start #
########################################################################


class calender(QDialog):
    calender_out = QtCore.Signal(QtCore.QDate)

    def __init__(self, parent):
        global calender_out
        super(calender, self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.calendar.clicked.connect(self.pick_date)
        self.setWindowTitle("Calendar")
        self.setWindowIcon(QtGui.QIcon("Image/calendar_icon.svg"))

    def pick_date(self):
        self.close()
        out = self.ui.calendar.selectedDate()
        self.calender_out.emit(out)
    ########################################################################
    # ==> Create Calender Ppo-up - End
    ########################################################################


matplotlib.use('Qt5Agg')


class MatplotlibCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, dpi=100):
        fig = Figure(dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MatplotlibCanvas, self).__init__(fig)
        fig.tight_layout()
        plt.style.use('classic')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    QtGui.QFontDatabase.addApplicationFont('fonts/segoeui.ttf')
    QtGui.QFontDatabase.addApplicationFont('fonts/segoeuib.ttf')
    window = MainWindow()
    sys.exit(app.exec_())
