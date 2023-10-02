# python
微信自动发消息，微信机器人（简易），可以给一个特定的人发送一句特定的消息，后续会继续完善的
<!DOCTYPE html>
<html>
<head>
    <title>To-Do List</title>
</head>
<body>
    <h1>To-Do List</h1>
    
    <!-- Form to add a new task -->
    <form id="task-form">
        <label for="task">Add Task:</label>
        <input type="text" id="task" required>
        <button type="button" onclick="addTask()">Add</button>
    </form>

    <!-- Display the task list -->
    <ul id="task-list"></ul>

    <script>
        // Function to add a new task
        function addTask() {
            var taskInput = document.getElementById("task");
            var taskText = taskInput.value.trim();
            if (taskText === "") return; // Ignore empty tasks

            var taskList = document.getElementById("task-list");
            var taskItem = document.createElement("li");

            var checkBox = document.createElement("input");
            checkBox.type = "checkbox";
            checkBox.addEventListener("change", function() {
                if (this.checked) {
                    taskItem.style.textDecoration = "line-through";
                } else {
                    taskItem.style.textDecoration = "none";
                }
            });

            var taskTextElement = document.createElement("span");
            taskTextElement.textContent = taskText;

            var deleteButton = document.createElement("button");
            deleteButton.textContent = "Delete";
            deleteButton.addEventListener("click", function() {
                taskList.removeChild(taskItem);
            });

            taskItem.appendChild(checkBox);
            taskItem.appendChild(taskTextElement);
            taskItem.appendChild(deleteButton);

            taskList.appendChild(taskItem);
            taskInput.value = "";
        }
    </script>
</body>
</html>
