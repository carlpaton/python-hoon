### Prime Numbers

This was to demonstrate parallel computing using several Raspberry Pi's. Click here for details on what [prime numbers](/pi-cluster/prime-numbers.md) are.  `./pi-cluster/primenumbers27.py` finds prime numbers using an MPI cluster which I seem to now understand thanks to [Gary Explains](https://www.youtube.com/channel/UCRjSO-juFtngAeJGJRMdIZw) <3

*  https://carlpaton.github.io/2019/10/raspberry-pi-cluster/

MPI lib - message passing interface, this is a standard way of sending blocks of data into a cluster from one node to another.

Scatter - the MPI program will see each core in your cluster as something it can ask to do work. It will scatter the numbers accross the nodes to check if they are prime.

Gather - the MPI program will then gather the results. This is done on the master node that you started the command from.

### What Are Prime Numbers?

* Greater than 1
* Whole number with exactly two factors, itself and 1.

Some examples of prime numbers: 2,3,5,7,11,13,17,19

The number 4 is not a prime number because it can be divided evenly by 4, 2, and 1. 
The number 5 is a prime number because it cannot be divided evenly by any other numbers except for 5 and 1.

```
2 / 1 = 2
2 / 2 = 1

3 / 1 = 3
3 / 2 = 1.x
3 / 3 = 1

4 / 1 = 4
4 / 2 = 2
4 / 3 = 1.x
4 / 4 = 1

5 / 1 = 5
5 / 2 = 2.x
5 / 3 = 1.x
5 / 4 = 1.x
5 / 5 = 1

6 / 1 = 6
6 / 2 = 3
6 / 3 = 2
6 / 4 = 1.x
6 / 5 = 1.x
6 / 6 = 1

7 / 1 = 7
7 / 2 = 3.x
7 / 3 = 2.x
7 / 4 = 1.x
7 / 5 = 1.x
7 / 6 = 1.x
7 / 7 = 1
```

### All the runs!

Yeah sweet you copied the code but where can you run this?

#### Docker

A quick way to play with command line scripts is to bring up a Ubuntu docker container. The scripts will then need `--allow-run-as-root` when executing. (for reasons)

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

#### Bare Metal - Ubuntu-18.04

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

```
pip3 install mpi4py
pip install mpi4py 
```

#### Raspberry PI Cluster

1. Install `2019-09-26-raspbian-buster-full.zip` using `balenaEtcher-1.5.70-x64.AppImage` and complete the setup on each PI.
2. Change the hostnames to `node1` and `node2` (would be sweet to have more!)

* https://www.raspberrypi.org/documentation/installation/installing-images/README.md

3. Install the message passing interface `mpi4py`

```
sudo apt-get install python-mpi4py
```

* https://mpi4py.readthedocs.io/en/stable/

4. CD to `pi-cluster` and run the python script using the MPI library but with no cluster information: 

```
time mpiexec python primenumbers27.py
```

5. Allow each node to authenticate using SSH (Secure Shell) using public & private keys.

```
MAGIC HERE!!
```

6. Update `clusterfile` to include the IP of each node and run again using additional params

```
more ~/clusterfile
ip addr show wlan0
time mpiexec -hostfile ~/clusterfile python primenumbers27.py
```
