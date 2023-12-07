# Copyright (c) 2016 Shotgun Software Inc.
#
# CONFIDENTIAL AND PROPRIETARY
#
# This work is provided "AS IS" and subject to the Shotgun Pipeline Toolkit
# Source Code License included in this distribution package. See LICENSE.
# By accessing, using, copying or modifying this work you indicate your
# agreement to the Shotgun Pipeline Toolkit Source Code License. All rights
# not expressly granted therein are reserved by Shotgun Software Inc.

import locale

from sgtk.platform.qt import QtGui, QtCore
from tank_vendor import six
from .label_base_widget import LabelBaseWidget
from .shotgun_field_meta import ShotgunFieldMeta


@six.add_metaclass(ShotgunFieldMeta)
class PercentWidget(LabelBaseWidget):
    """
    Display a ``percent`` field value as returned by the Shotgun API.
    """

    _DISPLAY_TYPE = "percent"

    def _string_value(self, value):
        """
        Convert the Shotgun value for this field into a string

        :param value: The value to convert into a string
        :type value: :obj:`int` or :obj:`float`
        """
        return locale.format("%d", value, grouping=True) + "%"


@six.add_metaclass(ShotgunFieldMeta)
class PercentEditorWidget(QtGui.QSpinBox):
    """
    Allows editing of a ``percent`` field value as returned by the Shotgun API.

    Pressing ``Enter`` or ``Return`` when the widget has focus will cause the
    value to be applied and the ``value_changed`` signal to be emitted.
    """

    _EDITOR_TYPE = "percent"

    def get_value(self):
        """
        :return: The internal value being displayed by the widget.
        """
        return self.value()

    def keyPressEvent(self, event):
        """
        Provides shortcuts for applying modified values.

        :param event: The key press event object
        :type event: :class:`~PySide.QtGui.QKeyEvent`
        """
        if event.key() in [QtCore.Qt.Key_Enter, QtCore.Qt.Key_Return]:
            self.value_changed.emit()
        else:
            super(PercentEditorWidget, self).keyPressEvent(event)

    def setup_widget(self):
        """
        Prepare the widget for display.

        Called by the metaclass during initialization.
        """
        # SG min/max values for percentages
        self.setMaximum(999)
        self.setMinimum(-999)
        self.setSuffix("%")
        self.setMinimumWidth(100)

    def _display_default(self):
        """
        Display the default value of the widget.
        """
        self.clear()

    def _display_value(self, value):
        """
        Set the value displayed by the widget.

        :param value: The value returned by the Shotgun API to be displayed
        """
        self.setValue(value)
