"""PyblioManager - MAIN"""

from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QFrame
from PySide6.QtGui import QGuiApplication


class MainWindow(QMainWindow):

    def __init__(self):
        from datas_for_app import TITLE_APP
        super().__init__()
        self.setGeometry(0, 0, *self._screen_size())
        self.setWindowTitle(TITLE_APP)
        self._create_menus()

    @staticmethod
    def _screen_size() -> tuple:
        """
        Obtain the width and height of the screen size, excluding the reserved areas of the window manager.
        Obtenir la largeur et la hauteur de la taille de l'écran en excluant les zones réservées du gestionnaire de
        fenêtre.

        Returns:
            tuple: Width and height. Largeur et hauteur.
        """
        screen_geometry = QGuiApplication.primaryScreen().availableGeometry()
        return screen_geometry.width(), screen_geometry.height()

    def _create_menus(self) -> None:
        """
        Create the menus for the main window menu bar using the data in the 'datas_for_app.py' file, and connect the
        sub-menus to the corresponding methods.
        Créer les menus de la barre de menus de la fenêtre principale en utilisant les données du fichier
        'datas_for_app.py', et connexion des sous-menus aux méthodes correspondantes.
        """
        from datas_for_app import MENUS
        for first_entry_menu, sub_menus in MENUS.items():
            menu = self.menuBar().addMenu(first_entry_menu)
            for sub_menu_str in sub_menus:
                menu.addSeparator() if not sub_menus[sub_menu_str] else (
                    menu.addAction(sub_menu_str).triggered.connect(sub_menus[sub_menu_str]))

    def _init_central_widget(self) -> None:
        """
        Configures the structure of the central widget with layouts (QVBoxLayout and QHBoxLayout) and frames (QFrame)
        to contain user actions and the display.
        Configure la structure du widget central avec des layouts (QVBoxLayout et QHBoxLayout) et des frames (QFrame)
        pour contenir les actions de l'utilisateur et l'affichage.

        Returns:
            None
        """
        central_widget = QWidget()
        # Create layouts :
        central_layout = QVBoxLayout()  # 'central_widget'
        top_frame_layout = QHBoxLayout()  # For frames 'actions' and 'inputs'
        # Create frames :
        frame_action_buttons = QFrame()
        frame_inputs = QFrame()
        frame_display = QFrame()
        # Add widget, layouts and frames :
        # PRÉVOIR D'AJUSTER LES MARGES #
        central_widget.setLayout(central_layout)  # Apply layouts
        central_layout.addLayout(top_frame_layout)
        self.setCentralWidget(central_widget)  # Add widgets
        central_layout.addWidget(frame_display)
        top_frame_layout.addWidget(frame_action_buttons)
        top_frame_layout.addWidget(frame_inputs)


class BookMethods(MainWindow):

    def __init__(self):
        super().__init__()
        self._init_central_widget()

    @staticmethod
    def create_new_entry():
        print("Connect nouvelle entrée")

    @staticmethod
    def edit_entry():
        print("Connect OK")

    @staticmethod
    def view_entry():
        print("Connect OK")

    @staticmethod
    def delete_entry():
        print("Connect OK")

    @staticmethod
    def quit_application():
        print("Quitter")


class BibliograhyMethods(MainWindow):

    def __init__(self):
        super().__init__()
        self._init_central_widget()

    @staticmethod
    def generate_bibliography():
        print("Connect OK")

    @staticmethod
    def open_bibliography():
        print("Connect OK")


class HelpMethods(MainWindow):

    def __init__(self):
        super().__init__()

    def _init_central_widget(self) -> None:
        """Prévoir ouverture nouvelle fenêtre - Méthode surchargée."""
        pass

    @staticmethod
    def show_documentation():
        print("Voir documentation")

    @staticmethod
    def show_directories():
        print("Voir répértoires")

    @staticmethod
    def show_about_dialog():
        print("A propos...")


if __name__ == "__main__":
    app = QApplication([])

    window = MainWindow()
    window.show()

    app.exec()
