# Learning & Magic

Python scripts (some magical) which are pillaged and manipulated for reasons of understanding the power of Python.

### Bubble Sort

* https://github.com/carlpaton/python-hoon/tree/master/bubble-sort

### Complete Python Developer Zero to Mastery

* https://github.com/carlpaton/python-hoon/tree/master/complete-python-developer-zero-to-mastery

### Machine Learning Fundamentals

* https://github.com/carlpaton/python-hoon/tree/master/machine-learning-fundamentals

### Prime Numbers

Warm them `Raspberry PI` CPUs!

* https://github.com/carlpaton/python-hoon/tree/master/prime-numbers

# All the runs!

Yeah sweet you copied the code but where can you run this?

### Docker

A quick way to play with command line scripts is to bring up a Ubuntu docker container. The scripts will then need `--allow-run-as-root` when executing. (for reasons?)

```
docker run -ti --name ubuntu-c ubuntu
docker start -i ubuntu-c
```

Then install git & python, clone this repository and run the commands shown above per example.

Example:

```
time mpiexec --allow-run-as-root python primenumbers27.py
```

*  https://carlpaton.github.io/2018/04/linux-commands/ 

### Bare Metal - Ubuntu-18.04

https://linuxize.com/post/how-to-install-pip-on-ubuntu-18.04/

```
--- 3x
sudo apt update
sudo apt install python3-pip
pip3 --version

--- 2.7
sudo apt update
sudo apt install python-pip
```

https://mpi4py.readthedocs.io/en/stable/install.html#using-pip-or-easy-install

**pip** is a de facto standard package-management system used to install and manage software packages written in **Python**.

```
pip3 install mpi4py ??
pip install mpi4py 
```

### Windows 10

IDLE is Python’s Integrated Development and Learning Environment.

* https://docs.python.org/3/library/idle.html

### Cloud Based

* https://colab.research.google.com/
* https://repl.it/