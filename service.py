#controller
from database import Task
from database import Family


class TaskService:
    def __init__(self):
        self.model = Task()

    def create(self, params):
        return self.model.create_task(params)

    def update(self, item_id, params):
        return self.model.update_task(item_id, params)

    def delete(self, item_id):
        return self.model.delete_task(item_id)

    def list(self):
        response = self.model.list_tasks()
        return response

class FamilyService:
    def __init__(self):
        self.model = Family()

    def create(self, tile, name):
        return self.model.create_member(tile, name)

    def update(self, params):
        return self.model.update_member(params)

    def delete(self, item_id):
        return self.model.delete_member(item_id)

    def list(self):
        return self.model.list_members()













