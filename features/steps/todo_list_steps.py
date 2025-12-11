from behave import given, when, then
from todo_list import ToDoList

@given("the to-do list is empty")
def step_empty_list(context):
    context.todo = ToDoList()

@when('the user adds a task "{title}"')
def step_add_task(context, title):
    context.todo.add_task(title)

@then('the to-do list should contain "{title}"')
def step_check_contains(context, title):
    titles = [task.title for task in context.todo.list_tasks()]
    assert title in titles


# LIST TASKS
@given("the to-do list contains tasks:")
def step_given_tasks(context):
    context.todo = ToDoList()
    for row in context.table:
        context.todo.add_task(row["Task"])

@when("the user lists all tasks")
def step_list_tasks(context):
    context.list_output = [task.title for task in context.todo.list_tasks()]

@then("the output should contain:")
def step_check_output(context):
    expected_lines = context.text.strip().split("\n")
    for line in expected_lines:
        assert line.strip() in context.list_output


# MARK COMPLETED
@given("the to-do list contains tasks with status:")
def step_given_tasks_status(context):
    context.todo = ToDoList()
    for row in context.table:
        context.todo.add_task(row["Task"])
        if row["Status"] == "Completed":
            context.todo.mark_task_completed(row["Task"])

@when('the user marks task "{title}" as completed')
def step_mark_completed(context, title):
    context.todo.mark_task_completed(title)

@then('the task "{title}" should appear as completed')
def step_check_completed(context, title):
    for task in context.todo.list_tasks():
        if task.title == title:
            assert task.status == "Completed"


# CLEAR LIST
@when("the user clears the task list")
def step_clear_list(context):
    context.todo.clear_tasks()

@then("the to-do list should be empty")
def step_check_empty(context):
    assert len(context.todo.list_tasks()) == 0


# DELETE TASK
@when('the user deletes the task "{title}"')
def step_delete_task(context, title):
    context.todo.delete_task(title)

@then('the to-do list should not contain "{title}"')
def step_not_contain(context, title):
    titles = [task.title for task in context.todo.list_tasks()]
    assert title not in titles
