from PyQt6.QtWidgets import QPushButton, QWidget, QLabel, QLineEdit, QGridLayout
from datetime import datetime

from model import ParenthesesTasks


class ProtocolGenTab(QWidget):
    correct_text = 'Правильно решенных задач: '
    failed_text = 'Неправильных попыток: '
    skipped_text = 'Пропущено примеров: '

    def __init__(self):
        super(QWidget, self).__init__()

        self.solved_tasks_amount = 0
        self.failed_attempts_amount = 0
        self.skipped_amount = 0

        self.layout = QGridLayout(self)

        self.task_label = QLabel(self)
        self.indicator_label = QLabel(self)
        self.correct_solved_tasks_label = QLabel(self)
        self.failed_attempts_amount_label = QLabel(self)
        self.skipped_amount_label = QLabel(self)
        self.indicator_label.setText('Решается...')
        self.correct_solved_tasks_label.setText(self.correct_text + str(self.solved_tasks_amount))
        self.failed_attempts_amount_label.setText(self.failed_text + str(self.failed_attempts_amount))
        self.skipped_amount_label.setText(self.skipped_text + str(self.skipped_amount))
        self.line = QLineEdit(self)

        self.layout.addWidget(self.task_label, 0, 0)
        self.layout.addWidget(self.line, 0, 1)
        self.layout.addWidget(self.indicator_label, 0, 2)

        self.line.move(80, 20)
        self.line.resize(200, 32)
        self.task_label.move(20, 20)

        self.check_answer_button = QPushButton('Проверить ответ')
        self.next_task_button = QPushButton('Следующая задача')
        self.skip_button = QPushButton('Пропустить')
        self.check_answer_button.clicked.connect(self.check_answer)
        self.next_task_button.clicked.connect(self.next_task)
        self.skip_button.clicked.connect(self.skip_task)

        self.layout.addWidget(self.check_answer_button, 1, 1)
        self.layout.addWidget(self.next_task_button, 2, 1)
        self.layout.addWidget(self.correct_solved_tasks_label, 3, 0)
        self.layout.addWidget(self.failed_attempts_amount_label, 3, 1)
        self.layout.addWidget(self.skipped_amount_label, 3, 3)
        self.layout.addWidget(self.skip_button, 4, 1)
        self.setLayout(self.layout)

        self.filename = 'logs_' + datetime.now().strftime('%H.%M.%S') + '.txt'
        self.parentheses_tasks = ParenthesesTasks(5, 6, 10)
        self.current_task, self.answer = self.parentheses_tasks.get_task(self.filename)
        self.task_label.setText(self.current_task)
        self.solved = False

    def check_answer(self):
        try:
            if not self.solved and int(self.line.text()) == self.answer:
                self.indicator_label.setText('Правильно')
                self.solved = True
                self.solved_tasks_amount += 1
                self.correct_solved_tasks_label.setText(self.correct_text + str(self.solved_tasks_amount))
            else:
                with open(self.filename, 'a') as f:
                    f.write("Roma's answer: " + self.line.text())
                    f.write('\n')
                self.indicator_label.setText('Неправильно') #, ответ: ' + str(self.answer))
                self.failed_attempts_amount += 1
                self.failed_attempts_amount_label.setText(self.failed_text + str(self.failed_attempts_amount))
                self.line.clear()

        except:
            pass

    def next_task(self, skip=False):
        if self.solved or skip:
            self.current_task, self.answer = self.parentheses_tasks.get_task(self.filename)
            self.task_label.setText(self.current_task)
            self.solved = False
            self.indicator_label.setText('Решается...')
        else:
            pass

    def skip_task(self):
        self.next_task(True)
        self.skipped_amount += 1
        self.skipped_amount_label.setText(self.skipped_text + str(self.skipped_amount))
        with open(self.filename, 'a') as f:
            f.write("Roma skipped this one\n")

