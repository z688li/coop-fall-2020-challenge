class EventSourcer():
    # Do not change the signature of any functions

    def __init__(self):
        self.value = 0
        self.undo_stack = []
        self.redo_stack = []

    def add(self, num: int):
        self.undo_stack.append(num)
        self.value += num

    def subtract(self, num: int):
        self.undo_stack.append(0-num)
        self.value -= num

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
        for i in range(steps):
            self.undo()

    def bulk_redo(self, steps: int):
        for i in range(steps):
            self.redo()
