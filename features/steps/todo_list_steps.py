from behave import given, when, then


@given("the to-do list is empty")
def step_impl(context):
    context.todo_list = []


@given("the to-do list contains tasks")
def step_impl(context):
    context.todo_list = []
    for row in context.table:
        context.todo_list.append({"task": row["Task"], "status": "Pending"})


@given("the to-do list contains tasks with status")
def step_impl(context):
    context.todo_list = []
    for row in context.table:
        context.todo_list.append({"task": row["Task"], "status": row["Status"]})


@when('the user adds a task "{task}"')
def step_impl(context, task):
    context.todo_list.append({"task": task, "status": "Pending"})


@when("the user lists all tasks")
def step_impl(context):
    lines = [item["task"] for item in context.todo_list]
    context.output = "\n".join(lines)


@when('the user marks task "{task}" as completed')
def step_impl(context, task):
    for item in context.todo_list:
        if item["task"] == task:
            item["status"] = "Completed"


@when("the user clears the task list")
def step_impl(context):
    context.todo_list = []


@when('the user deletes the task "{task}"')
def step_impl(context, task):
    context.todo_list = [item for item in context.todo_list if item["task"] != task]


@then('the to-do list should contain "{task}"')
def step_impl(context, task):
    tasks = [item["task"] for item in context.todo_list]
    assert task in tasks, f"Task '{task}' not found in list"


@then("the to-do list should be empty")
def step_impl(context):
    assert len(context.todo_list) == 0, "List is not empty"


@then('the to-do list should not contain "{task}"')
def step_impl(context, task):
    tasks = [item["task"] for item in context.todo_list]
    assert task not in tasks, f"Task '{task}' is still in the list"


@then("the output should contain")
def step_impl(context):
    expected_output = "\n".join(
        line.rstrip()
        for line in context.text.strip().splitlines()
    ).strip()

    actual_output = "\n".join(
        line.rstrip()
        for line in context.output.strip().splitlines()
    ).strip()

    assert expected_output == actual_output, (
        f"Expected output:\n{expected_output}\n\nActual output:\n{actual_output}"
    )



@then('the task "{task}" should appear as completed')
def step_impl(context, task):
    for item in context.todo_list:
        if item["task"] == task:
            assert item["status"] == "Completed", f"Task '{task}' is not marked completed"
            return
    assert False, f"Task '{task}' not found"
