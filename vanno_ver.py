from libs.mainwindow import *

__appname__ = 'vanno_ver' if sys.argv[0].split('/')[-1] == 'vanno_ver.py' else 'vanno'

class MainWindow_ver(MainWindow):
    def diritemChanged(self, item=None):
        with self.lmdb.begin(write=True) as txn:
            flag = txn.put(item.text().encode('ascii'), '1'.encode('ascii'), overwrite=False)
            if flag:
                self.checknum += 1
            else:
                txn.delete(item.text().encode('ascii'))
                self.checknum -= 1
            self.savebtncnt_label.setText('{0}/{1}'.format(self.checknum, self.job_list_total_no))


    def importDirs(self):
        if self.curSessLineEdit.text() == '':
            return

        if self.savebtn_label.text() == 'Not saved':
            return QMessageBox.warning(self, 'Warning', 'Please press "Save finished folders" button.')

        if not self.mayContinue():
            return

        self.checkList = []
        with self.lmdb.begin() as txn:
            cursor = txn.cursor()
            for key, value in cursor:
                insort(self.checkList, key.decode('ascii'))
            self.checknum = len(self.checkList)

        if int(self.curSessLineEdit.text()) > self.sess_no or int(self.curSessLineEdit.text()) <= 0:
            return QMessageBox.warning(self, 'Error', '<p><b>IndexError:</b></p>list index out of range')

        ###
        self.lastOpenDir = os.path.join(self.imageDirPath, str(self.curSession))
        self.curSession = int(self.curSessLineEdit.text())
        self.folderListWidget.clear()
        self.job_list_per_sess = self.job_list[self.curSession - 1]
        for folder_path in self.job_list_per_sess:
            item = QListWidgetItem(folder_path)
            item.setFlags(item.flags() | Qt.ItemIsUserCheckable)
            if item.text() in self.checkList:
                item.setCheckState(Qt.Checked)
            else:
                item.setCheckState(Qt.Unchecked)
            self.folderListWidget.addItem(item)

        self.savebtncnt_label.setText('{0}/{1}'.format(len(self.checkList), self.job_list_total_no))
        self.edit_label.setText('Image DIR: ' + self.imageDirPath)


    def openDirDialog(self, _value=False, dirpath=None):
        if not self.mayContinue():
            return

        defaultOpenDirPath = dirpath if dirpath else '..'

        if self.imageDirPath and os.path.exists(self.imageDirPath):
            defaultOpenDirPath = self.imageDirPath + '/..'
        elif self.lastOpenDir and os.path.exists(self.lastOpenDir):
            defaultOpenDirPath = self.lastOpenDir + '/../..'
        elif self.filePath and os.path.exists(os.path.dirname(self.filePath)):
            defaultOpenDirPath = os.path.dirname(self.filePath) + '/../..'
        else:
            defaultOpenDirPath = '..'

        self.imageDirPath = ustr(QFileDialog.getExistingDirectory(self, '%s - Open Directory' % __appname__, defaultOpenDirPath,
                                                 QFileDialog.ShowDirsOnly | QFileDialog.DontResolveSymlinks))
        if self.imageDirPath == '':
            self.folderListWidget.clear()
        else:
            self.lastOpenDir = self.imageDirPath
            self.job_list_dict = self.importJobs()
            self.curSessLineEdit.setText(str(self.curSession))

            self.sess_no = len(self.job_list_dict[self.ids[0]])
            self.job_list = [[] for i in range(self.sess_no)]

            for i in range(self.sess_no):
                for id in self.ids:
                    self.job_list[i] += self.job_list_dict[id][i]
                self.job_list_total += self.job_list[i]
            self.job_list_total_no = len(self.job_list_total)

            self.importDirs()


    def verifyImg(self, _value=False):
        # Proceding next image without dialog if having any label
         if self.filePath is not None:
            try:
                self.labelFile.toggleVerify()
            except AttributeError:
                # If the labelling file does not exist yet, create if and
                # re-save it with the verified attribute.
                self.saveFile()
                self.labelFile.toggleVerify()

            self.canvas.verified = self.labelFile.verified
            self.paintCanvas()
            self.saveFile()


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

        win = MainWindow_ver(login.logged_id, defaultPrefdefClassFile=os.path.join(env_path, 'predefined_classes.txt'))
        # print(win.defaultSaveDir)
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
