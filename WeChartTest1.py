import win32clipboard as w
import win32con
import win32api
import win32gui
import time


#把文字放入剪贴板
def setText(aString):
    w.OpenClipboard()
    w.EmptyClipboard()
    w.SetClipboardData(win32con.CF_UNICODETEXT,aString)
    w.CloseClipboard()

#模拟ctrl+V
def ctrlV():
    win32api.keybd_event(17,0,0,0) #ctrl
    win32api.keybd_event(86,0,0,0) #V
    win32api.keybd_event(86,0,win32con.KEYEVENTF_KEYUP,0)#释放按键
    win32api.keybd_event(17,0,win32con.KEYEVENTF_KEYUP,0)

#模拟alt+s
def altS():
    win32api.keybd_event(18,0,0,0)
    win32api.keybd_event(83,0,0,0)
    win32api.keybd_event(83,0,win32con.KEYEVENTF_KEYUP,0)
    win32api.keybd_event(18,0,win32con.KEYEVENTF_KEYUP,0)
# 模拟enter
def enter():
    win32api.keybd_event(13,0,0,0)
    win32api.keybd_event(13,0,win32con.KEYEVENTF_KEYUP,0)
#模拟单击
def click():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
#移动鼠标的位置
def movePos(x,y):
    win32api.SetCursorPos((x,y))

if __name__=="__main__":

    #获取鼠标当前位置
    #hwnd=win32gui.FindWindow("MozillaWindowClass",None)
    hwnd = win32gui.FindWindow("WeChatMainWndForPC", None)
    win32gui.ShowWindow(hwnd,win32con.SW_SHOW)
    win32gui.MoveWindow(hwnd,0,0,1000,700,True)
    time.sleep(0.01)
    #1.移动鼠标到通讯录位置，单击打开通讯录
    movePos(28,147)
    click()
    #2.移动鼠标到搜索框，单击，输入要搜索的名字
    movePos(148,35)
    click()
    setText('胡歌') #假设我的好友里有胡歌
    ctrlV()
    time.sleep(1) #别问我为什么要停1秒，问就是给微信一个反应的时间，他反应慢反应不过来，其他位置暂停的原因同样
    enter()
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

    time.sleep(1)
    #3.复制要发送的消息，发送
    setText('你好啊')
    ctrlV()
    altS()
