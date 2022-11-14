# 🍉

![PyPI](https://img.shields.io/pypi/v/watermelon-todo-list)
![GitHub](https://img.shields.io/github/license/Watermelon-Family/watermelon)
![GitHub Workflow Status (event)](https://img.shields.io/github/workflow/status/Watermelon-Family/watermelon/pytest)


🍉 is a command line tool, inspired by tomato🍅.

🍉 has the simplest UI design on par with MySQL🐶 and the most primitive data storage method

At the same time, 🍉 is also a very useful tool. Python beginners can use this project to practice your skills.

We strongly recommend using 🍉 with tmux on MacOS.

## Installation

- use pypi(recommend)
```shell
$ python3 -m pip install watermelon-todo-list
```

- use source code
```shell
# clone the source code
$ git clone git@github.com:Watermelon-Family/watermelon.git

# run the build.sh, you will get the watermelon-todo-list-0.0.X.tar.gz
$ sh build.sh

# use pip install 🍉
$ python3 -m pip install dist/watermelon-todo-list-0.0.1.tar.gz
```


- use release
```shell
# download the release, then
$ python3 -m pip install dist/watermelon-todo-list-0.0.1.tar.gz
```

## How to use 🍉

you can use `watermelon -h` to get help

the command line args👇
```text
watermelon [options]

Options:
  -h, --help       show this help message and exit
  -n NEW_EVENT     create a event with priority like [name:priority]
  -f FINISH_EVENT  finish a event by name
  -r REMOVE_EVENT  remove a event by name
  -l LIST_EVENT    list event [day|week|month|year]
  -g WORK          start a timer with [work_time:break_time:event_name]
  -a LIST_ACHIVE   list achievement [day|week|month|year]
```

## Display

⭐️: priority

🍉: 25min

```shell
# create a task
$ watermelon -n coding:5 

# show the task list, you can also use week, month or year.
$ watermelon -l day      
+---------+------------+----------+----------------------------+
|   name  |  priority  | use time |        create time         |
+---------+------------+----------+----------------------------+
|  coding | ⭐️⭐️⭐️⭐️⭐️ |          | 2022-10-21 19:29:52.355550 |
+---------+------------+----------+----------------------------+

# start watermelon timer
$ watermelon -g 1:0:coding
It is a time to work! 🍉
 🍉 [100%] 1:0 / 1:00 🕑
 
# finish the task by name
$ watermelon -f coding

# show the finish list🎉🎉🎉
$ watermelon -a week   
+---------+------------+----------+----------------------------+
|   name  |  priority  | use time |        finish time         |
+---------+------------+----------+----------------------------+
|  coding | ⭐️⭐️⭐️⭐️⭐️ |    🍉    | 2022-10-21 19:32:29.411117 |
+---------+------------+----------+----------------------------+

```
