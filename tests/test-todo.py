# test_todo.py
import todo

def test_add_task():
    todo.tasks.clear()
    result = todo.add_task("Learn DevOps")
    assert "Learn DevOps" in todo.tasks
    assert result == "Task 'Learn DevOps' added!"

def test_list_tasks():
    todo.tasks.clear()
    todo.add_task("Task A")
    todo.add_task("Task B")
    output = todo.list_tasks()
    assert "1. Task A" in output
    assert "2. Task B" in output

def test_remove_task():
    todo.tasks.clear()
    todo.add_task("Temp Task")
    result = todo.remove_task(1)
    assert result == "Task 'Temp Task' removed!"
    assert todo.tasks == []

def test_greet():
    assert todo.greet() == "Welcome to the To-Do CLI!"
