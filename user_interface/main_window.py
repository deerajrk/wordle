from PyQt5.QtWidgets import QMainWindow, QAction, QWidget, QVBoxLayout, QFrame, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
import user_interface.assets.ui_constants as uic
import sys
from user_interface.components.header import Header
from user_interface.components.play_area.guess_area import GuessArea
from user_interface.components.play_area.keyboard_area import KeyboardArea
from user_interface.components.play_area.result_area import ResultArea
from user_interface.components.howto_play import HowToPlay


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self._init_main_window()
        self._init_window_skeleton()

    def _init_main_window(self):
        self.setWindowTitle(uic.APP_TITLE)
        self.setWindowIcon(QIcon(uic.APP_LOGO))
        self.setGeometry(50, 50, 750, 550)
        self.setWindowFlag(Qt.WindowMaximizeButtonHint, True)
        self.setWindowFlag(Qt.WindowMinimizeButtonHint, True)
        self._set_menu_bar()

    def _set_menu_bar(self):
        self.menu_bar = self.menuBar()
        self.menu_game = self.menu_bar.addMenu("Game")
        self.menu_help = self.menu_bar.addMenu("About")
        self._set_menu_game()
        self._set_menu_help()

    def _set_menu_game(self):
        menu_game_new = QAction("&Start new game", self.menu_game)
        menu_game_new.setIcon(QIcon(uic.NEW_ICON))
        menu_game_new.triggered.connect(self._start_new_game)
        menu_game_exit = QAction("&Exit", self.menu_game)
        self.menu_game.addAction(menu_game_new)
        menu_game_exit.setIcon(QIcon(uic.EXIT_ICON))
        menu_game_exit.triggered.connect(sys.exit)
        self.menu_game.addAction(menu_game_exit)

    def _set_menu_help(self):
        menu_help_game = QAction("&How to play", self.menu_help)
        menu_help_game.setIcon(QIcon(uic.HELP_ICON))
        menu_help_game.triggered.connect(self._show_howto_play)
        self.menu_help.addAction(menu_help_game)
        menu_help_about = QAction("&About", self.menu_help)
        menu_help_about.setIcon(QIcon(uic.INFO_ICON))
        menu_help_about.triggered.connect(self._show_about_message)
        self.menu_help.addAction(menu_help_about)

    def _start_new_game(self):
        print("Start new game clicked")

    def _show_howto_play(self):
        howto_play = HowToPlay()
        howto_play.display()

    def _show_about_message(self):
        QMessageBox.information(self, "About Wordle | A recreation", """
        A recreation of the online Wordle game:
        https://www.nytimes.com/games/wordle/index.html \n
        Version: 1.0.0
        2022.02.20
        Created by: Deeraj Rajkarnikar (deeraj.rk@gmail.com)
        """)

    def _init_window_skeleton(self):
        central_widget = QWidget()
        central_layout = QVBoxLayout()
        central_layout.addWidget(Header())
        central_layout.addWidget(self._get_hline())
        self.guess_area = GuessArea()
        self.result_area = ResultArea()
        self.keyboard_area = KeyboardArea()
        central_layout.addWidget(self.guess_area)
        central_layout.addWidget(self.result_area)
        central_layout.addWidget(self.keyboard_area)
        central_layout.addStretch(1)
        central_widget.setLayout(central_layout)
        self.setCentralWidget(central_widget)

    @staticmethod
    def _get_hline():
        h_line = QFrame()
        h_line.setFixedHeight(3)
        h_line.setFrameShape(QFrame.HLine)
        h_line.setFrameShadow(QFrame.Sunken)
        return h_line
        