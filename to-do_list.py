class ToDoList:
    def __init__(self) -> None:
        self.serial = 0
        self.todo = {}

    def add_task(self, task: str) -> None:
        self.serial += 1
        self.todo[self.serial] = task

    def edit_task(self, task_id: int, new_task: str) -> None:
        try:
            self.todo[task_id] = new_task
        except KeyError:
            print(f'Task with ID {task_id} does not exist.')

    def delete_task(self, task_id: int) -> None:
        try:
            del self.todo[task_id]
        except KeyError:
            print(f'Task with ID {task_id} does not exist.')

    def view_task(self, task_id: int) -> None:
        try:
            print(self.todo[task_id])
        except KeyError:
            print(f'Task with ID {task_id} does not exist.')

    def view_todo(self) -> None:
        print()
        for task_id, task in self.todo.items():
            print(f'{task_id}. {task}')
        print()

school = ToDoList()

school.add_task('Go to market.')
school.add_task('Study for test.')
school.add_task('Do assignment.')

school.view_todo()
school.view_task(2)

school.edit_task(2, 'Study for exams')
school.view_todo()
school.view_task(2)

school.delete_task(1)
school.view_todo()
school.view_task(1)