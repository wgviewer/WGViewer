import logging
import os
import sys

from PyQt5.QtCore import QTimer, pyqtSlot
from PyQt5.QtWidgets import QWidget, QTabWidget, QLabel, QPushButton
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QGridLayout

from .tabs.advance_functions import TabAdvanceFunctions
from .tabs.tab_ship import TabShips
from .tabs.tab_expedition import TabExpedition


def get_data_path(relative_path):
    # This needs to be in current file
    bundle_dir = getattr(sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__)))
    res = os.path.join(bundle_dir, relative_path)
    return relative_path if not os.path.exists(res) else res


class MainInterfaceTabs(QWidget):
    def __init__(self, parent, api, threadpool, is_realrun):
        super().__init__()
        logging.info("Creating Main Interface Tabs...")
        self.api = api
        self.is_realrun = is_realrun

        # do NOT change the order of creation
        self.layout = QGridLayout()
        self.tab_ships = TabShips(self.api, self.is_realrun)
        # TODO TODO fix the data problem
        self.tab_exp = TabExpedition()
        tabwidget = QTabWidget()

        tabwidget.addTab(self.tab_exp, "  Expedition  ")
        tabwidget.addTab(self.tab_ships, "  Dock  ")

        self.layout.addWidget(tabwidget, 0, 0)
        self.setLayout(self.layout)

        if self.is_realrun:
            pass
        else:
            self._testrun()

    def _testrun(self):
        pass
        # import json
        # p = get_data_path('api_getShipList.json')
        # with open(p) as f:
        #     d = json.load(f)
        # self.on_received_shiplist(d)

    def init_tab_bar(self):
        # Initialize tab screen
        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab_ships = TabShips(self, self.is_realrun)
        self.tab4 = QWidget()
        self.tab5 = QWidget()
        self.tab_advance = TabAdvanceFunctions(self)

        # Add tabs
        self.tabs.addTab(self.tab_ships,"  Ships  ")
        self.tabs.addTab(self.tab1,"  Sortie  ")
        self.tabs.addTab(self.tab2,"  Fleets  ")
        self.tabs.addTab(self.tab4,"  Equipment  ")
        self.tabs.addTab(self.tab5,"  Tactics  ")
        self.tabs.addTab(self.tab_advance,"  Advance Functions  ")

    # def recurring_timer(self):
    #     self.counter +=1
    #     print("I'm in " + os.path.basename(__file__))
    #     print("active thread = " + str(self.threadpool.activeThreadCount()))
    #     self.l.setText("Counter: %d" % self.counter)


# End of File