''' Graphical user interface for screening images

@todo - cross index based on spider id - settings!

@todo - save

@todo - fix advanced settings load

.. Created on Jul 19, 2013
.. codeauthor:: Robert Langlois <rl2528@columbia.edu>
'''

from ImageViewer import MainWindow as ImageViewerWindow
from util.qt4_loader import QtGui,QtCore,qtSlot
import os, numpy

class MainWindow(ImageViewerWindow):
    ''' Main window display for the plotting tool
    '''
    
    def __init__(self, parent=None):
        "Initialize screener window"
        
        ImageViewerWindow.__init__(self, parent)
        self.inifile = 'ara_screen.ini'
        self.selectfile = 'ara_view_select.csv'
        self.selectfout = open(self.selectfile, 'a')
        self.selectedCount = 0
        self.loadSelections()
    
    def advancedSettings(self):
        ''' Get a list of advanced settings
        '''
        
        
        return [ 
               dict(show_images=('All', 'Selected', 'Unselected'), help="Show images of specified type"),
               ]+ImageViewerWindow.sharedAdvancedSettings(self)
        
    def setup(self):
        ''' Display specific setup
        '''
        
        self.connect(self.ui.imageListView.selectionModel(), QtCore.SIGNAL("selectionChanged(const QItemSelection &, const QItemSelection &)"), self.onSelectionChanged)
        self.ui.imageListView.setStyleSheet('QListView::item:selected{ color: #008000; border: 3px solid #6FFF00; }')
    
    def closeEvent(self, evt):
        '''Window close event triggered - save project and global settings 
        
        :Parameters:
            
        evt : QCloseEvent
              Event for to close the main window
        '''
        
        self.selectfout.close()
        ImageViewerWindow.closeEvent(self, evt)
        
    def getSettings(self):
        ''' Get the settings object
        '''
        
        '''
        return QtCore.QSettings(QtCore.QSettings.IniFormat, QtCore.QSettings.UserScope, "Arachnid", "ImageScreen")
        '''
        
        if self.inifile == "": return None
        return QtCore.QSettings(self.inifile, QtCore.QSettings.IniFormat)
        
    # Loading
    def loadSelections(self):
        ''' Load the selections from the default selection file
        '''
        
        if not os.path.exists(self.selectfile): return
        
        self.files = []
        self.file_index = []
        self.selectedCount=0
        fin = open(self.selectfile, 'r')
        for line in fin:
            if line =="": continue
            if line[0] == '@':
                f = line[1:].strip()
                self.updateFileIndex([f])
                self.files.append(f)
            else:
                vals = [int(v) for v in line.strip().split(',')]
                if self.file_index[vals[0]][0] != vals[1]: raise ValueError, "Failed to load internal selection file - file id %d != %d"%(self.file_index[vals[0]][0], vals[1])
                if self.file_index[vals[0]][1] != vals[2]: raise ValueError, "Failed to load internal selection file - stack id %d != %d"%(self.file_index[vals[0]][1], vals[2])
                self.file_index[vals[0]][2]=vals[3]
                self.selectedCount += vals[3]
        fin.close()
        if len(self.files) > 0:
            self.on_loadImagesPushButton_clicked()
    
    # Overriden methods
    def notify_added_item(self, item):
        ''' Called when an image is added to the view
        '''
        
        if self.file_index[item.data(QtCore.Qt.UserRole), 2] > 0:
            self.ui.imageListView.selectionModel().select(self.imageListModel.indexFromItem(item), QtGui.QItemSelectionModel.Select)
    
    def notify_added_files(self, newfiles):
        ''' Called when new files are loaded
        '''
        
        for f in newfiles:
            self.selectfout.write("@%s\n"%f)
    
    def imageSubset(self, index, count):
        '''
        '''
        
        if self.advanced_settings.show_images == 'Selected':
            idx = numpy.argwhere(self.file_index[:, 2]>0)
            return self.file_index[idx[index*count:(index+1)*count].squeeze()],idx[index*count:]
        elif self.advanced_settings.show_images == 'Unselected':
            idx = numpy.argwhere(self.file_index[:, 2]==0)
            return self.file_index[idx[index*count:(index+1)*count].squeeze()],idx[index*count:]
        return ImageViewerWindow.imageSubset(self, index, count)
    
    def imageTotal(self):
        '''
        '''
        
        if self.advanced_settings.show_images == 'Selected':
            return numpy.sum(self.file_index[:, 2]>0)
        elif self.advanced_settings.show_images == 'Unselected':
            return numpy.sum(self.file_index[:, 2]==0)
        return ImageViewerWindow.imageTotal(self)
    
    @qtSlot()
    def on_loadImagesPushButton_clicked(self):
        ''' Load the current batch of images into the list
        '''
        
        self.disconnect(self.ui.imageListView.selectionModel(), QtCore.SIGNAL("selectionChanged(const QItemSelection &, const QItemSelection &)"), self.onSelectionChanged)
        ImageViewerWindow.on_loadImagesPushButton_clicked(self)
        self.connect(self.ui.imageListView.selectionModel(), QtCore.SIGNAL("selectionChanged(const QItemSelection &, const QItemSelection &)"), self.onSelectionChanged)
    
    # Custom Slots
    def onSelectionChanged(self, selected, deselected):
        ''' Called when the list selection has changed
        
        :Parameters:
        
        selection : QItemSelection
                    List of selection items in the list
        deselected : QItemSelection
                     List of deselected items in the list
        '''
        
        
        for index in selected.indexes():
            idx = index.data(QtCore.Qt.UserRole)
            self.file_index[idx][2] = 1
            self.selectedCount+=1
            self.selectfout.write('%d,'%idx)
            self.selectfout.write("%d,%d,%d\n"%tuple(self.file_index[idx]))
        for index in deselected.indexes():
            idx = index.data(QtCore.Qt.UserRole)
            self.file_index[idx][2] = 0
            self.selectedCount-=1
            self.selectfout.write('%d,'%idx)
            self.selectfout.write("%d,%d,%d\n"%tuple(self.file_index[idx]))
        self.selectfout.flush()
        self.setWindowTitle("Selected: %d of %d"%(self.selectedCount, len(self.file_index)))
        