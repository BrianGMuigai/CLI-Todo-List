import json
import os
from task import Task 

class TaskManager:

    DEFAULT_FILE = "tasks.json"

    def__init__(self, filepath: str = DEFAULT_FILE):

        self.filepath = filepath
        self.tasks =[]
        self._next_id = 1

        self._load()

    def _load(self):
        """Load tasks from the JSON file into self.tasks."""

        if not os.path.exists(self.filepath):
            return


       with open(self.filepath, "r") as f:

        data = json.load(f)


        self.tasks = [ Task.from_dict(item) for item in data]

       if self.tasks:

       self._next_id = max(self.tasks, key= lambda t: t.id).id + 1 

    def _save(self):
        """Saves all tasks to the JSON file."""


        with open(self.filepath, "w" ) as f :

            json.dump([task.to_dict() for task in self.tasks], f, indent=2)

    def add_task(self, description: str) -> Task:
         """Create a new task, add it to the list, save, return it."""

    if not description.strip():

        raise ValueError("Task description cannot be empty.")

        new_task = Task(self._next_id, description.strip())

        self.tasks.append(new_task)

        self._next_id +=1
        self.save()
        return new_task

    def complete_task(self, task_id: int) -> Task:
        """Mark a task as complete by its id."""

        task = self._find_by_id(task_id)

        if task is None:
            raise ValueError(f"No task found with id {task_id}.")

        if task.completed:
            raise ValueError(f"Task #{task_id:03d} is already completed")

        task.mark_complete()
        self._save()
        return task


   def delete_task(self, task_id: int ) -> Task:
        """Remove a task permanetly."""

        task = self ._find_by_id(task_id)
        if task is None:
            raise ValueError(f"No task found with id {task_id}.")

        self.tasks.remove(task)
        self._save()
        return task

  def list_tasks(self, show_completed: bool =True ) -> list:
        """Return tasks, optionally filtering out completed ones. """

       if show_completed:
          return self.tasks
       return [t for t in self.tasks if not t.completed]

    def pending _count(self) -> int:
        """How many tasks are not yet completed."""

       return sum(1 for t in self.tasks if not t.completed)

   def _find_by_id(self, task_id: int):
        """Return the Task with id, or None if not found."""

        return next((t for t in self.tasks if t.id == task_id), None)















