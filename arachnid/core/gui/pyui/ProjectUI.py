# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/robertlanglois/workspace/arachnida/src/arachnid/core/gui/pyui/ProjectUI.ui'
#
# Created: Fri Jan  3 10:26:26 2014
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from ..util.qt4_loader import QtCore, QtGui

class Ui_ProjectWizard(object):
    def setupUi(self, ProjectWizard):
        ProjectWizard.setObjectName("ProjectWizard")
        ProjectWizard.resize(719, 500)
        ProjectWizard.setWizardStyle(QtGui.QWizard.MacStyle)
        ProjectWizard.setOptions(QtGui.QWizard.IndependentPages|QtGui.QWizard.NoCancelButton|QtGui.QWizard.NoDefaultButton)
        self.introductionPage = QtGui.QWizardPage()
        self.introductionPage.setObjectName("introductionPage")
        self.gridLayout_2 = QtGui.QGridLayout(self.introductionPage)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 0, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.introductionPage)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/icons/icons/FrankLab_logo081511.png"))
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_5 = QtGui.QLabel(self.introductionPage)
        self.label_5.setMinimumSize(QtCore.QSize(200, 0))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap(":/icons/icons/HHMIlogo.png"))
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 1, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.introductionPage)
        self.label_4.setMinimumSize(QtCore.QSize(281, 0))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(":/icons/icons/ColumbiaLogo.png"))
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 2, 0, 1, 2)
        self.label_7 = QtGui.QLabel(self.introductionPage)
        self.label_7.setMaximumSize(QtCore.QSize(120, 110))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap(":/icons/icons/220px-NIH_Master_Logo_Vertical_2Color.png"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 3, 1, 1, 1)
        ProjectWizard.addPage(self.introductionPage)
        self.settingsQuestionPage = QtGui.QWizardPage()
        self.settingsQuestionPage.setObjectName("settingsQuestionPage")
        self.verticalLayout = QtGui.QVBoxLayout(self.settingsQuestionPage)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_2 = QtGui.QWidget(self.settingsQuestionPage)
        self.widget_2.setObjectName("widget_2")
        self.formLayout_3 = QtGui.QFormLayout(self.widget_2)
        self.formLayout_3.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.formLayout_3.setObjectName("formLayout_3")
        self.yesLeginonPushButton = QtGui.QPushButton(self.widget_2)
        self.yesLeginonPushButton.setMinimumSize(QtCore.QSize(250, 50))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/mini/mini/accept.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.yesLeginonPushButton.setIcon(icon)
        self.yesLeginonPushButton.setCheckable(True)
        self.yesLeginonPushButton.setFlat(False)
        self.yesLeginonPushButton.setObjectName("yesLeginonPushButton")
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.LabelRole, self.yesLeginonPushButton)
        self.noLeginonPushButton = QtGui.QPushButton(self.widget_2)
        self.noLeginonPushButton.setMinimumSize(QtCore.QSize(250, 50))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/mini/mini/cancel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.noLeginonPushButton.setIcon(icon1)
        self.noLeginonPushButton.setCheckable(True)
        self.noLeginonPushButton.setFlat(False)
        self.noLeginonPushButton.setObjectName("noLeginonPushButton")
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.LabelRole, self.noLeginonPushButton)
        self.verticalLayout.addWidget(self.widget_2)
        ProjectWizard.addPage(self.settingsQuestionPage)
        self.leginonDBPage = QtGui.QWizardPage()
        self.leginonDBPage.setObjectName("leginonDBPage")
        self.leginonDBLayout = QtGui.QVBoxLayout(self.leginonDBPage)
        self.leginonDBLayout.setObjectName("leginonDBLayout")
        ProjectWizard.addPage(self.leginonDBPage)
        self.manualSettingsPage = QtGui.QWizardPage()
        self.manualSettingsPage.setObjectName("manualSettingsPage")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.manualSettingsPage)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox_2 = QtGui.QGroupBox(self.manualSettingsPage)
        self.groupBox_2.setObjectName("groupBox_2")
        self.formLayout_4 = QtGui.QFormLayout(self.groupBox_2)
        self.formLayout_4.setFieldGrowthPolicy(QtGui.QFormLayout.FieldsStayAtSizeHint)
        self.formLayout_4.setContentsMargins(0, 3, 0, 3)
        self.formLayout_4.setObjectName("formLayout_4")
        self.label_3 = QtGui.QLabel(self.groupBox_2)
        self.label_3.setObjectName("label_3")
        self.formLayout_4.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_3)
        self.widget = QtGui.QWidget(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.micrographComboBox = QtGui.QComboBox(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.micrographComboBox.sizePolicy().hasHeightForWidth())
        self.micrographComboBox.setSizePolicy(sizePolicy)
        self.micrographComboBox.setMinimumSize(QtCore.QSize(200, 0))
        self.micrographComboBox.setEditable(True)
        self.micrographComboBox.setObjectName("micrographComboBox")
        self.horizontalLayout.addWidget(self.micrographComboBox)
        self.micrographFileToolButton = QtGui.QToolButton(self.widget)
        self.micrographFileToolButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/mini/mini/folder.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.micrographFileToolButton.setIcon(icon2)
        self.micrographFileToolButton.setObjectName("micrographFileToolButton")
        self.horizontalLayout.addWidget(self.micrographFileToolButton)
        self.openMoreFilesToolButton = QtGui.QToolButton(self.widget)
        self.openMoreFilesToolButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/mini/mini/folder_add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.openMoreFilesToolButton.setIcon(icon3)
        self.openMoreFilesToolButton.setObjectName("openMoreFilesToolButton")
        self.horizontalLayout.addWidget(self.openMoreFilesToolButton)
        self.displayImagesToolButton = QtGui.QToolButton(self.widget)
        self.displayImagesToolButton.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/mini/mini/images.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.displayImagesToolButton.setIcon(icon4)
        self.displayImagesToolButton.setObjectName("displayImagesToolButton")
        self.horizontalLayout.addWidget(self.displayImagesToolButton)
        self.formLayout_4.setWidget(0, QtGui.QFormLayout.FieldRole, self.widget)
        self.label_6 = QtGui.QLabel(self.groupBox_2)
        self.label_6.setObjectName("label_6")
        self.formLayout_4.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_6)
        self.widget_3 = QtGui.QWidget(self.groupBox_2)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.gainFileComboBox = QtGui.QComboBox(self.widget_3)
        self.gainFileComboBox.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gainFileComboBox.sizePolicy().hasHeightForWidth())
        self.gainFileComboBox.setSizePolicy(sizePolicy)
        self.gainFileComboBox.setEditable(True)
        self.gainFileComboBox.setObjectName("gainFileComboBox")
        self.horizontalLayout_3.addWidget(self.gainFileComboBox)
        self.gainFilePushButton = QtGui.QPushButton(self.widget_3)
        self.gainFilePushButton.setEnabled(False)
        self.gainFilePushButton.setText("")
        self.gainFilePushButton.setIcon(icon2)
        self.gainFilePushButton.setAutoDefault(False)
        self.gainFilePushButton.setFlat(True)
        self.gainFilePushButton.setObjectName("gainFilePushButton")
        self.horizontalLayout_3.addWidget(self.gainFilePushButton)
        self.formLayout_4.setWidget(2, QtGui.QFormLayout.FieldRole, self.widget_3)
        self.invertCheckBox = QtGui.QCheckBox(self.groupBox_2)
        self.invertCheckBox.setChecked(True)
        self.invertCheckBox.setObjectName("invertCheckBox")
        self.formLayout_4.setWidget(3, QtGui.QFormLayout.FieldRole, self.invertCheckBox)
        self.verticalLayout_2.addWidget(self.groupBox_2)
        self.groupBox = QtGui.QGroupBox(self.manualSettingsPage)
        self.groupBox.setObjectName("groupBox")
        self.formLayout = QtGui.QFormLayout(self.groupBox)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.FieldsStayAtSizeHint)
        self.formLayout.setContentsMargins(0, 3, 0, 3)
        self.formLayout.setObjectName("formLayout")
        self.label_8 = QtGui.QLabel(self.groupBox)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_8)
        self.pixelSizeDoubleSpinBox = QtGui.QDoubleSpinBox(self.groupBox)
        self.pixelSizeDoubleSpinBox.setObjectName("pixelSizeDoubleSpinBox")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.pixelSizeDoubleSpinBox)
        self.label_10 = QtGui.QLabel(self.groupBox)
        self.label_10.setObjectName("label_10")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_10)
        self.voltageDoubleSpinBox = QtGui.QDoubleSpinBox(self.groupBox)
        self.voltageDoubleSpinBox.setMaximum(5000.0)
        self.voltageDoubleSpinBox.setObjectName("voltageDoubleSpinBox")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.voltageDoubleSpinBox)
        self.label_11 = QtGui.QLabel(self.groupBox)
        self.label_11.setObjectName("label_11")
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_11)
        self.csDoubleSpinBox = QtGui.QDoubleSpinBox(self.groupBox)
        self.csDoubleSpinBox.setObjectName("csDoubleSpinBox")
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.csDoubleSpinBox)
        self.verticalLayout_2.addWidget(self.groupBox)
        ProjectWizard.addPage(self.manualSettingsPage)
        self.referenceQuestionPage = QtGui.QWizardPage()
        self.referenceQuestionPage.setObjectName("referenceQuestionPage")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.referenceQuestionPage)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget_4 = QtGui.QWidget(self.referenceQuestionPage)
        self.widget_4.setObjectName("widget_4")
        self.formLayout_5 = QtGui.QFormLayout(self.widget_4)
        self.formLayout_5.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.formLayout_5.setContentsMargins(0, 0, 0, 0)
        self.formLayout_5.setObjectName("formLayout_5")
        self.yesReferencePushButton = QtGui.QPushButton(self.widget_4)
        self.yesReferencePushButton.setMinimumSize(QtCore.QSize(250, 50))
        self.yesReferencePushButton.setIcon(icon)
        self.yesReferencePushButton.setCheckable(True)
        self.yesReferencePushButton.setFlat(False)
        self.yesReferencePushButton.setObjectName("yesReferencePushButton")
        self.formLayout_5.setWidget(0, QtGui.QFormLayout.LabelRole, self.yesReferencePushButton)
        self.noReferencePushButton = QtGui.QPushButton(self.widget_4)
        self.noReferencePushButton.setMinimumSize(QtCore.QSize(250, 50))
        self.noReferencePushButton.setIcon(icon1)
        self.noReferencePushButton.setCheckable(True)
        self.noReferencePushButton.setFlat(False)
        self.noReferencePushButton.setObjectName("noReferencePushButton")
        self.formLayout_5.setWidget(1, QtGui.QFormLayout.LabelRole, self.noReferencePushButton)
        self.verticalLayout_3.addWidget(self.widget_4)
        ProjectWizard.addPage(self.referenceQuestionPage)
        self.referencePage = QtGui.QWizardPage()
        self.referencePage.setObjectName("referencePage")
        self.referenceLayout = QtGui.QHBoxLayout(self.referencePage)
        self.referenceLayout.setObjectName("referenceLayout")
        ProjectWizard.addPage(self.referencePage)
        self.additionalSettingsPage = QtGui.QWizardPage()
        self.additionalSettingsPage.setObjectName("additionalSettingsPage")
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.additionalSettingsPage)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.groupBox_4 = QtGui.QGroupBox(self.additionalSettingsPage)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout = QtGui.QGridLayout(self.groupBox_4)
        self.gridLayout.setObjectName("gridLayout")
        self.label_9 = QtGui.QLabel(self.groupBox_4)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 0, 0, 1, 1)
        self.particleDiameterStackedWidget = QtGui.QStackedWidget(self.groupBox_4)
        self.particleDiameterStackedWidget.setObjectName("particleDiameterStackedWidget")
        self.page = QtGui.QWidget()
        self.page.setObjectName("page")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.page)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.particleSizeDoubleSpinBox = QtGui.QDoubleSpinBox(self.page)
        self.particleSizeDoubleSpinBox.setMaximum(10000.0)
        self.particleSizeDoubleSpinBox.setObjectName("particleSizeDoubleSpinBox")
        self.horizontalLayout_2.addWidget(self.particleSizeDoubleSpinBox)
        self.particleDiameterStackedWidget.addWidget(self.page)
        self.page_2 = QtGui.QWidget()
        self.page_2.setObjectName("page_2")
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.page_2)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.particleSizeSpinBox = QtGui.QSpinBox(self.page_2)
        self.particleSizeSpinBox.setMaximum(10000)
        self.particleSizeSpinBox.setObjectName("particleSizeSpinBox")
        self.horizontalLayout_4.addWidget(self.particleSizeSpinBox)
        self.particleDiameterStackedWidget.addWidget(self.page_2)
        self.gridLayout.addWidget(self.particleDiameterStackedWidget, 0, 1, 1, 1)
        self.particleSizeUnitComboBox = QtGui.QComboBox(self.groupBox_4)
        self.particleSizeUnitComboBox.setObjectName("particleSizeUnitComboBox")
        self.particleSizeUnitComboBox.addItem("")
        self.particleSizeUnitComboBox.addItem("")
        self.gridLayout.addWidget(self.particleSizeUnitComboBox, 0, 2, 1, 1)
        self.windowSizeUnitComboBox = QtGui.QComboBox(self.groupBox_4)
        self.windowSizeUnitComboBox.setObjectName("windowSizeUnitComboBox")
        self.windowSizeUnitComboBox.addItem("")
        self.windowSizeUnitComboBox.addItem("")
        self.gridLayout.addWidget(self.windowSizeUnitComboBox, 1, 2, 1, 1)
        self.windowSizeStackedWidget = QtGui.QStackedWidget(self.groupBox_4)
        self.windowSizeStackedWidget.setObjectName("windowSizeStackedWidget")
        self.page_3 = QtGui.QWidget()
        self.page_3.setObjectName("page_3")
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.page_3)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.windowSizeDoubleSpinBox = QtGui.QDoubleSpinBox(self.page_3)
        self.windowSizeDoubleSpinBox.setMaximum(10000.0)
        self.windowSizeDoubleSpinBox.setObjectName("windowSizeDoubleSpinBox")
        self.horizontalLayout_5.addWidget(self.windowSizeDoubleSpinBox)
        self.windowSizeStackedWidget.addWidget(self.page_3)
        self.page_4 = QtGui.QWidget()
        self.page_4.setObjectName("page_4")
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.page_4)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.windowSizeSpinBox = QtGui.QSpinBox(self.page_4)
        self.windowSizeSpinBox.setMaximum(10000)
        self.windowSizeSpinBox.setObjectName("windowSizeSpinBox")
        self.horizontalLayout_6.addWidget(self.windowSizeSpinBox)
        self.windowSizeStackedWidget.addWidget(self.page_4)
        self.gridLayout.addWidget(self.windowSizeStackedWidget, 1, 1, 1, 1)
        self.label_21 = QtGui.QLabel(self.groupBox_4)
        self.label_21.setObjectName("label_21")
        self.gridLayout.addWidget(self.label_21, 1, 0, 1, 1)
        self.label = QtGui.QLabel(self.groupBox_4)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.maskDiameterStackedWidget = QtGui.QStackedWidget(self.groupBox_4)
        self.maskDiameterStackedWidget.setObjectName("maskDiameterStackedWidget")
        self.page_5 = QtGui.QWidget()
        self.page_5.setObjectName("page_5")
        self.horizontalLayout_7 = QtGui.QHBoxLayout(self.page_5)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.maskDiameterDoubleSpinBox = QtGui.QDoubleSpinBox(self.page_5)
        self.maskDiameterDoubleSpinBox.setMaximum(10000.0)
        self.maskDiameterDoubleSpinBox.setObjectName("maskDiameterDoubleSpinBox")
        self.horizontalLayout_7.addWidget(self.maskDiameterDoubleSpinBox)
        self.maskDiameterStackedWidget.addWidget(self.page_5)
        self.page_6 = QtGui.QWidget()
        self.page_6.setObjectName("page_6")
        self.horizontalLayout_8 = QtGui.QHBoxLayout(self.page_6)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.maskDiameterSpinBox = QtGui.QSpinBox(self.page_6)
        self.maskDiameterSpinBox.setMaximum(10000)
        self.maskDiameterSpinBox.setObjectName("maskDiameterSpinBox")
        self.horizontalLayout_8.addWidget(self.maskDiameterSpinBox)
        self.maskDiameterStackedWidget.addWidget(self.page_6)
        self.gridLayout.addWidget(self.maskDiameterStackedWidget, 2, 1, 1, 1)
        self.maskDiameterUnitComboBox = QtGui.QComboBox(self.groupBox_4)
        self.maskDiameterUnitComboBox.setObjectName("maskDiameterUnitComboBox")
        self.maskDiameterUnitComboBox.addItem("")
        self.maskDiameterUnitComboBox.addItem("")
        self.gridLayout.addWidget(self.maskDiameterUnitComboBox, 2, 2, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 3, 1, 1, 1)
        self.verticalLayout_6.addWidget(self.groupBox_4)
        self.groupBox_3 = QtGui.QGroupBox(self.additionalSettingsPage)
        self.groupBox_3.setObjectName("groupBox_3")
        self.formLayout_2 = QtGui.QFormLayout(self.groupBox_3)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_19 = QtGui.QLabel(self.groupBox_3)
        self.label_19.setObjectName("label_19")
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_19)
        self.workerCountSpinBox = QtGui.QSpinBox(self.groupBox_3)
        self.workerCountSpinBox.setMaximum(10000)
        self.workerCountSpinBox.setProperty("value", 1)
        self.workerCountSpinBox.setObjectName("workerCountSpinBox")
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.workerCountSpinBox)
        self.label_20 = QtGui.QLabel(self.groupBox_3)
        self.label_20.setObjectName("label_20")
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_20)
        self.threadCountSpinBox = QtGui.QSpinBox(self.groupBox_3)
        self.threadCountSpinBox.setMaximum(10000)
        self.threadCountSpinBox.setProperty("value", 1)
        self.threadCountSpinBox.setObjectName("threadCountSpinBox")
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.threadCountSpinBox)
        self.enableStderrCheckBox = QtGui.QCheckBox(self.groupBox_3)
        self.enableStderrCheckBox.setText("")
        self.enableStderrCheckBox.setObjectName("enableStderrCheckBox")
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.FieldRole, self.enableStderrCheckBox)
        self.label_12 = QtGui.QLabel(self.groupBox_3)
        self.label_12.setObjectName("label_12")
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_12)
        self.verticalLayout_6.addWidget(self.groupBox_3)
        ProjectWizard.addPage(self.additionalSettingsPage)
        self.fineTunePage = QtGui.QWizardPage()
        self.fineTunePage.setSubTitle("")
        self.fineTunePage.setObjectName("fineTunePage")
        self.settingsHorizontalLayout = QtGui.QHBoxLayout(self.fineTunePage)
        self.settingsHorizontalLayout.setContentsMargins(3, 3, 3, 3)
        self.settingsHorizontalLayout.setObjectName("settingsHorizontalLayout")
        self.workflowListView = QtGui.QListView(self.fineTunePage)
        self.workflowListView.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.workflowListView.setObjectName("workflowListView")
        self.settingsHorizontalLayout.addWidget(self.workflowListView)
        ProjectWizard.addPage(self.fineTunePage)
        self.monitorPage = QtGui.QWizardPage()
        self.monitorPage.setObjectName("monitorPage")
        self.monitorLayout = QtGui.QVBoxLayout(self.monitorPage)
        self.monitorLayout.setContentsMargins(0, 0, 0, 0)
        self.monitorLayout.setObjectName("monitorLayout")
        ProjectWizard.addPage(self.monitorPage)

        self.retranslateUi(ProjectWizard)
        self.particleDiameterStackedWidget.setCurrentIndex(0)
        self.windowSizeStackedWidget.setCurrentIndex(0)
        self.maskDiameterStackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(ProjectWizard)

    def retranslateUi(self, ProjectWizard):
        ProjectWizard.setWindowTitle(QtGui.QApplication.translate("ProjectWizard", "Wizard", None, QtGui.QApplication.UnicodeUTF8))
        self.introductionPage.setTitle(QtGui.QApplication.translate("ProjectWizard", "Welcome to Arachnid", None, QtGui.QApplication.UnicodeUTF8))
        self.introductionPage.setSubTitle(QtGui.QApplication.translate("ProjectWizard", "<font color=\"#663300\" size=5>Workflow manager for processing data collected by electron microscopy</font>", None, QtGui.QApplication.UnicodeUTF8))
        self.settingsQuestionPage.setTitle(QtGui.QApplication.translate("ProjectWizard", "Leginon Settings Import", None, QtGui.QApplication.UnicodeUTF8))
        self.settingsQuestionPage.setSubTitle(QtGui.QApplication.translate("ProjectWizard", "Would you like to import your experimental settings from a Leginon database?", None, QtGui.QApplication.UnicodeUTF8))
        self.yesLeginonPushButton.setText(QtGui.QApplication.translate("ProjectWizard", "Yes", None, QtGui.QApplication.UnicodeUTF8))
        self.noLeginonPushButton.setText(QtGui.QApplication.translate("ProjectWizard", "No", None, QtGui.QApplication.UnicodeUTF8))
        self.leginonDBPage.setTitle(QtGui.QApplication.translate("ProjectWizard", "Leginon Import", None, QtGui.QApplication.UnicodeUTF8))
        self.manualSettingsPage.setTitle(QtGui.QApplication.translate("ProjectWizard", "Manual Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("ProjectWizard", "Images", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("ProjectWizard", "Micrographs", None, QtGui.QApplication.UnicodeUTF8))
        self.micrographFileToolButton.setToolTip(QtGui.QApplication.translate("ProjectWizard", "Open list of files", None, QtGui.QApplication.UnicodeUTF8))
        self.openMoreFilesToolButton.setToolTip(QtGui.QApplication.translate("ProjectWizard", "Add more files to list", None, QtGui.QApplication.UnicodeUTF8))
        self.displayImagesToolButton.setToolTip(QtGui.QApplication.translate("ProjectWizard", "Display images", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("ProjectWizard", "Gain reference", None, QtGui.QApplication.UnicodeUTF8))
        self.invertCheckBox.setToolTip(QtGui.QApplication.translate("ProjectWizard", "Do the micrographs require contrast inversion", None, QtGui.QApplication.UnicodeUTF8))
        self.invertCheckBox.setText(QtGui.QApplication.translate("ProjectWizard", "Invert Contrast", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("ProjectWizard", "Microscope Parameters", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("ProjectWizard", "Pixel Size (1/A)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("ProjectWizard", "Voltage (kV)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("ProjectWizard", "CS (mm)", None, QtGui.QApplication.UnicodeUTF8))
        self.referenceQuestionPage.setTitle(QtGui.QApplication.translate("ProjectWizard", "Reference Preprocessing", None, QtGui.QApplication.UnicodeUTF8))
        self.referenceQuestionPage.setSubTitle(QtGui.QApplication.translate("ProjectWizard", "Would you like to select a raw map to be transformed into a reference?", None, QtGui.QApplication.UnicodeUTF8))
        self.yesReferencePushButton.setText(QtGui.QApplication.translate("ProjectWizard", "Yes", None, QtGui.QApplication.UnicodeUTF8))
        self.noReferencePushButton.setText(QtGui.QApplication.translate("ProjectWizard", "No", None, QtGui.QApplication.UnicodeUTF8))
        self.referencePage.setTitle(QtGui.QApplication.translate("ProjectWizard", "Reference Map", None, QtGui.QApplication.UnicodeUTF8))
        self.additionalSettingsPage.setTitle(QtGui.QApplication.translate("ProjectWizard", "Additional Parameters", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_4.setTitle(QtGui.QApplication.translate("ProjectWizard", "Data dimensions", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("ProjectWizard", "Particle Diameter", None, QtGui.QApplication.UnicodeUTF8))
        self.particleSizeDoubleSpinBox.setToolTip(QtGui.QApplication.translate("ProjectWizard", "Diameter of particle in angstroms", None, QtGui.QApplication.UnicodeUTF8))
        self.particleSizeUnitComboBox.setItemText(0, QtGui.QApplication.translate("ProjectWizard", "Å", None, QtGui.QApplication.UnicodeUTF8))
        self.particleSizeUnitComboBox.setItemText(1, QtGui.QApplication.translate("ProjectWizard", "Px", None, QtGui.QApplication.UnicodeUTF8))
        self.windowSizeUnitComboBox.setItemText(0, QtGui.QApplication.translate("ProjectWizard", "Å", None, QtGui.QApplication.UnicodeUTF8))
        self.windowSizeUnitComboBox.setItemText(1, QtGui.QApplication.translate("ProjectWizard", "Px", None, QtGui.QApplication.UnicodeUTF8))
        self.windowSizeDoubleSpinBox.setToolTip(QtGui.QApplication.translate("ProjectWizard", "Diameter of particle in angstroms", None, QtGui.QApplication.UnicodeUTF8))
        self.label_21.setToolTip(QtGui.QApplication.translate("ProjectWizard", "Window width in pixels", None, QtGui.QApplication.UnicodeUTF8))
        self.label_21.setText(QtGui.QApplication.translate("ProjectWizard", "Window Width", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ProjectWizard", "Mask Diameter", None, QtGui.QApplication.UnicodeUTF8))
        self.maskDiameterDoubleSpinBox.setToolTip(QtGui.QApplication.translate("ProjectWizard", "Diameter of particle in angstroms", None, QtGui.QApplication.UnicodeUTF8))
        self.maskDiameterUnitComboBox.setItemText(0, QtGui.QApplication.translate("ProjectWizard", "Å", None, QtGui.QApplication.UnicodeUTF8))
        self.maskDiameterUnitComboBox.setItemText(1, QtGui.QApplication.translate("ProjectWizard", "Px", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("ProjectWizard", "Parallel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_19.setText(QtGui.QApplication.translate("ProjectWizard", "Process Count", None, QtGui.QApplication.UnicodeUTF8))
        self.label_20.setText(QtGui.QApplication.translate("ProjectWizard", "Thread Count", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("ProjectWizard", "Log to Console", None, QtGui.QApplication.UnicodeUTF8))
        self.fineTunePage.setTitle(QtGui.QApplication.translate("ProjectWizard", "Fine Tune Options", None, QtGui.QApplication.UnicodeUTF8))

from ..icons import icons_rc;icons_rc;
