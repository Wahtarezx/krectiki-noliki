class TaskManager:
    tasks_dict = {}

    def new_task(self, task, index):
        if index not in self.tasks_dict.keys():
            self.tasks_dict[index] = task
        elif task in self.tasks_dict[index]:
            raise ValueError('Такой пункт уже есть')
        else:
            self.tasks_dict[index] += f'; {task}'

    def sort_dict(self):
        new_dict = {}
        for i_key in sorted(self.tasks_dict.keys()):
            new_dict[i_key] = self.tasks_dict[i_key]
        return new_dict

    def total_string(self):
        string = ''
        answer = self.sort_dict()
        for elem in answer:
            string += f'{elem} - {answer[elem]}\n'
        return string

    def __str__(self):
        return self.total_string()

    def delete(self, task, index):
        self.tasks_dict[index] = self.tasks_dict[index].replace(task, '')
        if '; ' in self.tasks_dict[index]:
            self.tasks_dict[index] = self.tasks_dict[index].replace('; ', '')
        if self.tasks_dict[index] == '':
            self.tasks_dict.pop(index)


manager = TaskManager()
manager.new_task("сделать уборку", 4)
manager.new_task("помыть посуду", 4)
manager.new_task("отдохнуть", 1)
manager.new_task("поесть", 2)
manager.new_task("сдать ДЗ", 2)
print(manager)
manager.new_task("поесть", 2)


