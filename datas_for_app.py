from main import BookMethods, BibliograhyMethods, HelpMethods

TITLE_APP = "Gestionnaire bibliographique"

# TO MANAGE THE MENU BAR (Pour la gestion de la barre des menus) :
MENUS = {  # For menu display (Pour l'affichage des menus).
    "Livre": {
        "Saisir nouvelle référence": BookMethods.create_new_entry,
        "SEP1": False,
        "Modifier référence": BookMethods.edit_entry,
        "Visualiser référence": BookMethods.view_entry,
        "Suppression référence": BookMethods.delete_entry,
        "SEP2": False,
        "Quitter": BookMethods.quit_application
    },
    "Bibliographie": {
        "Générer une bibliographie": BibliograhyMethods.generate_bibliography,
        "Ouvrir une bibliographie": BibliograhyMethods.open_bibliography
    },
    "Aide": {
        "Documentation": HelpMethods.show_documentation,
        "Affichage des répertoires et fichiers créés": HelpMethods.show_directories,
        "SEP": False,
        "A propos...": HelpMethods.show_about_dialog
    }
}
