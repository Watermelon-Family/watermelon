# 🍉

🍉 is a command line tool, inspired by tomato.

🍉 has the simplest UI design on par with MySQL🐶 and the most primitive data storage method

At the same time, 🍉 is also a very useful tool. Python beginners can use this project to practice your skills.

## Installation

- use pypi
```shell
$ python3 -m pip install watermelon-todo-list==0.0.1
```

- use source code
```shell
# clone the source code
$ git clone git@github.com:Watermelon-Family/watermelon.git

# run the build.sh, you will get the watermelon-0.0.X.tar.gz
$ sh build.sh

# use pip install 🍉
$ python3 -m pip install dist/watermelon-0.0.1.tar.gz 
```


- use release
```shell
# download the release, then
$ python3 -m pip install dist/watermelon-0.0.1.tar.gz 
```

## How to use 🍉

you can use `watermelon -h` to get help

the command line args👇
```text
watermelon
-f <complete a event>
-r <remove a event>
-a <display self-discipline results [today|month|year]>
-l <show event list>
-g <start self-discipline [work_time:rest_time:event]>
```

## Display

```shell
# create a task
$ watermelon -n codeing:5 

# show the task list, you can also use week, month or year.
$ watermelon -l day      
+---------+------------+----------+----------------------------+
|   name  |  priority  | use time |        create time         |
+---------+------------+----------+----------------------------+
| codeing | ⭐️⭐️⭐️⭐️⭐️ |          | 2022-10-21 19:29:52.355550 |
+---------+------------+----------+----------------------------+

# start watermelon timer
$ watermelon -g 1:0:codeing
It is a time to work! 🍉
 🍉 [100%] 1:0 / 1:00 🕑
 
# finish the task by name
$ watermelon -f codeing

# show the finish list🎉🎉🎉
$ watermelon -a week   
+---------+------------+----------+----------------------------+
|   name  |  priority  | use time |        finish time         |
+---------+------------+----------+----------------------------+
| codeing | ⭐️⭐️⭐️⭐️⭐️ |    🍉    | 2022-10-21 19:32:29.411117 |
+---------+------------+----------+----------------------------+

```