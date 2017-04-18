import pickle
from PyQt5 import QtCore


class Task:

    def __init__(self, name = "", text = "", complete = False):
        self.name = name
        self.text = text
        self.complete = complete


class TaskList(QtCore.QAbstractListModel):

    def __init__(self, parent = None):
        QtCore.QAbstractListModel.__init__(self, parent)
        self._file_name = "Tasks.dat"
        self._load()

    def rowCount(self, parent):
        return len(self._task_list)

    def data(self, index, role):
        if role == QtCore.Qt.DisplayRole | role == QtCore.Qt.EditRole:
            return self._task_list[index].name
        if role == QtCore.Qt.CheckStateRole:
            return self._task_list[index].complete

    def setData(self, index, value, role):
        if role == QtCore.Qt.DisplayRole | role == QtCore.Qt.EditRole:
            self._task_list[index].name = value
        elif role == QtCore.Qt.CheckStateRole:
            self._task_list[index].complete = value

    def removeRow(self, task_index, parent):
        super().beginRemoveRows(parent, task_index, task_index)
        del self._task_list[task_index]
        super().endRemoveRows()

    def insertRow(self, task, parent=QtCore.QModelIndex()):
        task.id = len(self._task_list) + 1
        super().beginInsertRows(parent, len(self._task_list), len(self._task_list))
        self._task_list.append(task)
        super().endInsertRows()

    def _load(self):
        try:
            with open(self._file_name, 'rb') as f:
                self._task_list = pickle.load(f)
        except:
            self._task_list = []

    def save(self):
        with open(self._file_name, 'rb') as f:
            pickle.dump(self._task_list, f)

    def get_task(self, index):
        return self._task_list[index]

