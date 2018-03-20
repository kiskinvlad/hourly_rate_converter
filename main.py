import sys
import json
from PyQt5.Qt import pyqtSlot
from PyQt5.QtGui import QDoubleValidator
from PyQt5.QtWidgets import QWidget, QMainWindow, QLineEdit, QDesktopWidget, QComboBox, QApplication, QHBoxLayout, \
    QVBoxLayout, QFormLayout, QLabel, QPushButton, QMenuBar, QToolBar, QStatusBar
from PyQt5.QtCore import Qt, QRect, QMetaObject, QCoreApplication, QLocale
from GetCurrency import GetCurrency
from Currency import *

CONST_CCY = 'ccy'
CONST_BASECCY = 'base_ccy'
CONST_BUY = 'buy'
CONST_SALE = 'sale'
CONST_WIDTH = 250
CONST_HEIGHT = 300


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        currency_obj = GetCurrency("https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5")
        currency_arr = json.loads(currency_obj.get_currency_data())

        curr_usd = currency_arr[0]
        curr_eur = currency_arr[1]
        curr_rub = currency_arr[2]
        curr_btc = currency_arr[3]

        self.currency_usd_obj = Currency(
            curr_usd[CONST_CCY],
            curr_usd[CONST_BASECCY],
            curr_usd[CONST_BUY],
            curr_usd[CONST_SALE]
        )
        self.currency_eur_obj = Currency(
            curr_eur[CONST_CCY],
            curr_eur[CONST_BASECCY],
            curr_eur[CONST_BUY],
            curr_eur[CONST_SALE]
        )
        self.currency_rub_obj = Currency(
            curr_rub[CONST_CCY],
            curr_rub[CONST_BASECCY],
            curr_rub[CONST_BUY],
            curr_rub[CONST_SALE]
        )
        self.currency_btc_obj = Currency(
            curr_btc[CONST_CCY],
            curr_btc[CONST_BASECCY],
            curr_btc[CONST_BUY],
            curr_btc[CONST_SALE]
        )

        '''### Window base
                components initialization 
        '''
        self.centralWidget = QWidget(self)
        self.horizontalLayout = QHBoxLayout(self.centralWidget)
        self.verticalLayout = QVBoxLayout()
        self.form_wrapper = QVBoxLayout()
        self.formLayout = QFormLayout()
        self.hourly_rate_label = QLabel(self.centralWidget)
        self.hourly_rate_value = QLineEdit(self.centralWidget)
        self.time_track_label = QLabel(self.centralWidget)
        self.time_track_value = QLineEdit(self.centralWidget)
        self.verticalLayout_4 = QVBoxLayout()
        self.comboBox = QComboBox(self.centralWidget)
        self.pushButton = QPushButton(self.centralWidget)
        self.info_wrapper = QVBoxLayout()
        self.result_wrapper = QVBoxLayout()
        self.result_text = QLabel(self.centralWidget)
        self.result_text.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self.usd_currency_wrapper = QVBoxLayout()
        self.usd_currency_output = QLabel(self.centralWidget)
        self.eur_currency_wrapper = QVBoxLayout()
        self.eur_currency_output = QLabel(self.centralWidget)
        self.rub_currency_wrapper = QVBoxLayout()
        self.rub_currency_output = QLabel(self.centralWidget)
        self.btc_currency_wrapper = QVBoxLayout()
        self.btc_currency_output = QLabel(self.centralWidget)

        self.menuBar = QMenuBar(self)
        self.mainToolBar = QToolBar(self)
        self.statusBar = QStatusBar(self)

        self.onlyDouble = QDoubleValidator()

        self.init_ui()

    def init_ui(self):
        self.setObjectName("Hourly Rate Helper")
        self.resize(CONST_WIDTH, CONST_HEIGHT)

        self.centralWidget.setObjectName("centralWidget")
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.form_wrapper.setSpacing(6)
        self.form_wrapper.setObjectName("form_wrapper")
        self.formLayout.setSpacing(6)
        self.formLayout.setObjectName("formLayout")
        self.hourly_rate_label.setObjectName("hourly_rate_label")
        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.hourly_rate_label)
        self.hourly_rate_value.setObjectName("hourly_rate_value")
        self.hourly_rate_value.setValidator(self.onlyDouble)
        self.hourly_rate_value.setStyleSheet("padding: 0 5px")
        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.hourly_rate_value)
        self.time_track_label.setObjectName("time_track_label")
        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.time_track_label)
        self.time_track_value.setObjectName("time_track_value")
        self.time_track_value.setValidator(self.onlyDouble)
        self.time_track_value.setStyleSheet("padding: 0 5px")
        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.time_track_value)
        self.form_wrapper.addLayout(self.formLayout)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.comboBox.setObjectName("comboBox")
        self.verticalLayout_4.addWidget(self.comboBox)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_4.addWidget(self.pushButton)
        self.form_wrapper.addLayout(self.verticalLayout_4)
        self.verticalLayout.addLayout(self.form_wrapper)
        self.info_wrapper.setSpacing(6)
        self.info_wrapper.setContentsMargins(0, 10, 0, 10)
        self.info_wrapper.setObjectName("info_wrapper")
        self.result_wrapper.setSpacing(6)
        self.result_wrapper.setContentsMargins(0, 0, 0, 10)
        self.result_wrapper.setObjectName("result_wrapper")
        self.result_text.setStyleSheet("font-weight: bold")
        self.result_text.setAlignment(Qt.AlignCenter)
        self.result_text.setObjectName("result_text")
        self.result_wrapper.addWidget(self.result_text)
        self.info_wrapper.addLayout(self.result_wrapper)
        self.usd_currency_wrapper.setSpacing(6)
        self.usd_currency_wrapper.setObjectName("usd_currency_wrapper")
        self.usd_currency_output.setAlignment(Qt.AlignCenter)
        self.usd_currency_output.setObjectName("usd_currency_output")
        self.usd_currency_wrapper.addWidget(self.usd_currency_output)
        self.info_wrapper.addLayout(self.usd_currency_wrapper)
        self.eur_currency_wrapper.setSpacing(6)
        self.eur_currency_wrapper.setObjectName("eur_currency_wrapper")
        self.eur_currency_output.setStyleSheet("margin: 0")
        self.eur_currency_output.setLineWidth(1)
        self.eur_currency_output.setAlignment(Qt.AlignCenter)
        self.eur_currency_output.setObjectName("eur_currency_output")
        self.eur_currency_wrapper.addWidget(self.eur_currency_output)
        self.info_wrapper.addLayout(self.eur_currency_wrapper)
        self.rub_currency_wrapper.setObjectName("rub_currency_wrapper")
        self.rub_currency_output.setAlignment(Qt.AlignCenter)
        self.rub_currency_output.setObjectName("rub_currency_output")
        self.rub_currency_wrapper.addWidget(self.rub_currency_output)
        self.info_wrapper.addLayout(self.rub_currency_wrapper)
        self.btc_currency_wrapper.setSpacing(6)
        self.btc_currency_wrapper.setObjectName("btc_currency_wrapper")
        self.btc_currency_output.setAlignment(Qt.AlignCenter)
        self.btc_currency_output.setObjectName("btc_currency_output")
        self.btc_currency_wrapper.addWidget(self.btc_currency_output)
        self.info_wrapper.addLayout(self.btc_currency_wrapper)
        self.verticalLayout.addLayout(self.info_wrapper)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.setCentralWidget(self.centralWidget)
        self.menuBar.setGeometry(QRect(0, 0, 259, 22))
        self.menuBar.setObjectName("menuBar")
        self.setMenuBar(self.menuBar)
        self.mainToolBar.setObjectName("mainToolBar")
        self.addToolBar(Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar.setObjectName("statusBar")
        self.setStatusBar(self.statusBar)
        self.statusBar.showMessage("Created by Kiskin Vlad")
        self.comboBox.addItem("Show in USD")
        self.comboBox.addItem("Show in UAH")
        self.comboBox.addItem("Show in EUR")
        self.comboBox.addItem("Show in BTC")
        self.comboBox.addItem("Show in RUR")

        self.pushButton.clicked.connect(lambda:  self.button_click(
            self.hourly_rate_value.text(),
            self.time_track_value.text(),
            self.comboBox.currentText())
        )

        self.retranslate_ui()
        QMetaObject.connectSlotsByName(self)
        ww = QDesktopWidget()
        wh = QDesktopWidget()
        screen_width = ww.screen().width()
        screen_height = wh.screen().height()

        self.setGeometry(
            (screen_width / 2) - (CONST_WIDTH / 2),
            (screen_height / 2) - (CONST_HEIGHT / 2),
            CONST_WIDTH,
            CONST_HEIGHT
        )
        self.setWindowTitle("HourlyRateHelper")
        self.show()

    def retranslate_ui(self):
        _translate = QCoreApplication.translate
        self.setWindowTitle(_translate("Hourly Rate Helper", "Hourly Rate Helper"))
        self.hourly_rate_label.setText(_translate("Hourly Rate Helper", "Hourly rate:"))
        self.hourly_rate_value.setPlaceholderText(_translate("Hourly Rate Helper", "$$$"))
        self.time_track_label.setText(_translate("Hourly Rate Helper", "Time tracked:"))
        self.time_track_value.setPlaceholderText(_translate("Hourly Rate Helper", "hours"))
        self.pushButton.setText(_translate("Hourly Rate Helper", "Calculate"))
        self.usd_currency_output.setText(
            _translate("Hourly Rate Helper",
                       self.currency_usd_obj.get_ccy() + ": "
                       + format(float(self.currency_usd_obj.get_buy()), '.2f') + self.currency_usd_obj.get_base() + " / "
                       + format(float(self.currency_usd_obj.get_sale()), '.2f') + self.currency_usd_obj.get_base()
                       )
        )
        self.eur_currency_output.setText(
            _translate("Hourly Rate Helper",
                       self.currency_eur_obj.get_ccy() + ": "
                       + format(float(self.currency_eur_obj.get_buy()), '.2f') + self.currency_eur_obj.get_base() + " / "
                       + format(float(self.currency_eur_obj.get_sale()), '.2f') + self.currency_eur_obj.get_base()
                       )
        )
        self.rub_currency_output.setText(
            _translate("Hourly Rate Helper",
                       self.currency_rub_obj.get_ccy() + ": "
                       + format(float(self.currency_rub_obj.get_buy()), '.2f') + self.currency_rub_obj.get_base() + " / "
                       + format(float(self.currency_rub_obj.get_sale()), '.2f') + self.currency_rub_obj.get_base()
                       )
        )
        self.btc_currency_output.setText(
            _translate("Hourly Rate Helper",
                       self.currency_btc_obj.get_ccy() + ": "
                       + self.currency_btc_obj.get_buy() + self.currency_btc_obj.get_base() + " / "
                       + self.currency_btc_obj.get_sale() + self.currency_btc_obj.get_base()
                       )
        )

    @pyqtSlot(int, int, str)
    def button_click(self, rate, hours, out_type):
        _translate = QCoreApplication.translate
        money = 0
        currency_prefix = '$'
        if rate and hours:
            rate = float(rate.replace(",", "."))
            hours = float(hours.replace(",", "."))
            hours = int(hours) + (hours - int(hours)) / 0.60
            self.statusBar.showMessage("Created by Kiskin Vlad")
            if out_type == "Show in UAH":
                money = rate * hours
                money = money * float(self.currency_usd_obj.get_buy())
                currency_prefix = "UAH"
            elif out_type == "Show in EUR":
                money = rate * hours
                money = money * float(self.currency_usd_obj.get_buy())
                money = money / float(self.currency_eur_obj.get_buy())
                currency_prefix = "EUR"
            elif out_type == "Show in RUR":
                money = rate * hours
                money = money * float(self.currency_usd_obj.get_buy())
                money = money / float(self.currency_rub_obj.get_buy())
                currency_prefix = "RUB"
            elif out_type == "Show in BTC":
                money = rate * hours
                money = money / float(self.currency_btc_obj.get_buy())
                currency_prefix = "BTC"
            else:
                money = rate * hours
            money = float(format(money, '.2f'))
            self.result_text.setText(
                _translate("Hourly Rate Helper", "You will be receive: {} {}".format(money, currency_prefix))
            )
        else:
            self.statusBar.showMessage("Please fill all inputs")
            self.result_text.setText(
                _translate("Hourly Rate Helper", ""))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())
