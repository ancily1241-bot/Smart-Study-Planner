TESTING TABLE

Test Case 1
Feature: Add Task
Input: Subject = Python, Topic = Functions
Expected Result: Task should be added successfully.
Actual Result: The task was added successfully and displayed when viewing tasks.
Status: PASS

Test Case 2
Feature: View Tasks
Input: Click View Tasks button
Expected Result: All tasks should be displayed.
Actual Result: All saved tasks were displayed correctly.
Status: PASS

Test Case 3
Feature: Search Tasks
Input: Python
Expected Result: All Python-related tasks should be displayed.
Actual Result: Matching Python tasks were displayed correctly.
Status: PASS

Test Case 4
Feature: Delete Task
Input: Task Number = 1
Expected Result: Selected task should be removed.
Actual Result: The selected task was removed successfully.
Status: PASS

Test Case 5
Feature: Save Tasks
Input: Click Save Tasks button
Expected Result: Task data should be saved to tasks.json.
Actual Result: Data was successfully saved to tasks.json.
Status: PASS

Test Case 6
Feature: Load Tasks
Input: Click Load Tasks button
Expected Result: Previously saved tasks should be loaded.
Actual Result: Tasks were loaded correctly from tasks.json.
Status: PASS