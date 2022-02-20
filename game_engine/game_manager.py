from PyQt5.QtCore import pyqtSlot, QThread, pyqtSignal
from pynput import keyboard
import user_interface.assets.ui_constants as uic

class GameManager(QThread):
    update_user_input = pyqtSignal(str)

    def __init__(self, am):
        super().__init__()
        self.am = am
        self.current_word = None

    def start_new_game(self):
        self._start_listen()

    @pyqtSlot(str)
    def register_single_key(self, key):
        print("here")
        print("Single key: " + key)

    @pyqtSlot()
    def run(self):
        self._start_listen()

    def _start_listen(self):
        listener = keyboard.Listener(on_press = self._on_press)
        listener.start()
        listener.join()

    def _on_press(self, key):
        try:
            k = key.char
        except:
            k = key.name
        if k.upper() in uic.KEYS_OF_INTEREST:
            print("Key pressed: " + k)
            return False

    def verify_word(self, word):
        pass
