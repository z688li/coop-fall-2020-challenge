class EventSourcer():
    # Do not change the signature of any functions

    def __init__(self):
        self.value = 0
        self.undo_stack = []
        self.redo_stack = []

    def add(self, num: int):
        self.undo_stack.append(num)
        self.value += num
        # self.redo_stack = []

    def subtract(self, num: int):
        self.undo_stack.append(0-num)
        self.value -= num
        # self.redo_stack = []

    def undo(self):
        if len(self.undo_stack) != 0:
            undo_value = self.undo_stack.pop()
            self.redo_stack.append(undo_value)
            self.value -= undo_value

    def redo(self):
        if len(self.redo_stack) != 0:
            redo_value = self.redo_stack.pop()
            self.undo_stack.append(redo_value)
            self.value += redo_value

    def bulk_undo(self, steps: int):
        max_undo = len(self.undo_stack)
        index = min(max_undo,steps)
        for i in range(index):
            undo_value = self.undo_stack.pop()
            self.redo_stack.append(undo_value)
            self.value -= undo_value

    def bulk_redo(self, steps: int):
        max_redo = len(self.redo_stack)
        index = min(max_redo,steps)
        for i in range(index):
            redo_value = self.redo_stack.pop()
            self.undo_stack.append(redo_value)
            self.value += redo_value