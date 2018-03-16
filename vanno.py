from libs.mainwindow import *

__appname__ = 'vanno_ver' if sys.argv[0].split('/')[-1] == 'vanno_ver.py' else 'vanno'

def get_main_app(argv=[]):
    """
    Standard boilerplate Qt application code.
    Do everything but app.exec_() -- so that we can test the application in one thread
    """
    app = QApplication(argv)
    app.setApplicationName(__appname__)
    app.setWindowIcon(newIcon("app"))

    login = Login()
    # Tzutalin 201705+: Accept extra agruments to change predefined class file
    # Usage : labelImg.py image predefClassFile
    if login.exec_() == QDialog.Accepted:
        # win = MainWindow(login.logged_id,argv[1] if len(argv) >= 2 else None,
        #                  argv[2] if len(argv) >= 3 else os.path.join(
        #                      os.path.dirname(sys.argv[0]),
        #                      'data', 'predefined_classes.txt'))

        win = MainWindow(login.logged_id, defaultPrefdefClassFile=os.path.join(env_path, 'predefined_classes.txt'))
        win.show()


        return app, win
    else:
        sys.exit()


def main(argv=[]):
    '''construct main app and run it'''
    app, _win = get_main_app(argv)
    return app.exec_()


if __name__ == '__main__':
    sys.exit(main(sys.argv))
