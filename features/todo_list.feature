Feature: To-Do List Manager
  The user should be able to manage tasks effectively using the command-line system.

  # 1) Add task
  Scenario: Add a new task
    Given the to-do list is empty
    When the user adds a task "Buy groceries"
    Then the to-do list should contain "Buy groceries"

  # 2) List all tasks
  Scenario: List all existing tasks
    Given the to-do list contains tasks:
      | Task         |
      | Buy groceries|
      | Pay bills    |
    When the user lists all tasks
    Then the output should contain:
      """
      Buy groceries
      Pay bills
      """

  # 3) Mark task completed
  Scenario: Mark a task as completed
    Given the to-do list contains tasks with status:
      | Task         | Status  |
      | Buy groceries| Pending |
    When the user marks task "Buy groceries" as completed
    Then the task "Buy groceries" should appear as completed

  # 4) Clear all tasks
  Scenario: Clear the entire list
    Given the to-do list contains tasks:
      | Task         |
      | Buy groceries|
      | Pay bills    |
    When the user clears the task list
    Then the to-do list should be empty

  # 5) NEW FEATURE: Delete a task
  Scenario: Delete a specific task
    Given the to-do list contains tasks:
      | Task         |
      | Homework     |
      | Pay bills    |
    When the user deletes the task "Homework"
    Then the to-do list should not contain "Homework"
