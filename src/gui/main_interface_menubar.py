import os

from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QMenuBar, QAction, QMessageBox

from ..data import data as wgr_data


class MainInterfaceMenuBar(QMenuBar):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        self.init_file_menu()
        self.init_view_menu()
        self.init_preferences_menu()
        self.init_help_menu()

    def create_action(self, text, handler, shortcut=None):
        q = QAction(text, self)
        q.triggered.connect(handler)
        if shortcut != None:
            q.setShortcut(shortcut)
        else:
            pass
        return q

    def init_file_menu(self):
        menu = self.addMenu("File")
        menu.addAction(self.create_action("Open Cache Folder", self.open_cache_folder))
        menu.addSeparator()
        menu.addAction(self.create_action("Quit", self.quit_application))

    def init_view_menu(self):
        menu = self.addMenu("View")
        menu.addAction(self.create_action("&Open Navy Base Overview", self.parent.init_side_dock, "Ctrl+O"))

    def init_preferences_menu(self):
        menu = self.addMenu("Preferences")
        scheme = menu.addMenu("Color Scheme")
        # TODO
        scheme.addAction("Bright (Native)")
        scheme.addAction("Dark")

    def init_help_menu(self):
        menu = self.addMenu("Help")
        menu.addAction(self.create_action("&About Warship Girls Viewer", self.open_author_info))


    # ================================
    # QActions
    # ================================


    def quit_application(self):
        # TODO: in the future, inform user and/or save unfinished tasks
        QCoreApplication.exit()

    def open_cache_folder(self):
        path = wgr_data._get_data_dir()
        os.startfile(path)

    # def clear_cache_folder(self):
    #     wgr_data._clear_cache()

    def open_author_info(self):
        def get_hyperlink(link, text):
            return "<a style=\"color:hotpink;text-align: center;\" href='"+link+"'>"+text+"</a>"

        msg_str = '<h1>Warship Girls Viewer</h1>'
        msg_str += "\n"
        msg_str += get_hyperlink('https://github.com/WarshipGirls/WGViewer', 'GitHub - WGViewer')
        QMessageBox.about(self, "About", msg_str)


# End of File