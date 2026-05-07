from datetime import datetime

class Task:

    def __init__(self, task_id: int, description: str):

        self.id = task_id
        self.description = description
        self.completed = False
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M")

    def mark_complete(self):
        self.completed = True

    def to_dict(self) -> dict :
        return{
            "id": self.id,
            "description": self.description,
            "completed": self.completed,
            "created_at": self.created_at

        }
   
    def from_dict(cls, data: dict ) -> "Task":

        task  = cls(data["id"], data["description"])
        task.completed = data["completed"]
        task.created_at = data["created_at"]
        return task_id

    def __str__(self) -> str:

        status = "✓" if self.completed else "○"
        return f"[{status}] #{self.id:03d} {self.description} ({self.created_at})"
