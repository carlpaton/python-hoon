Python scripts pillaged and manipulated for reasons.

### Prime Numbers

This was to demonstrate parallel computing using several Raspberry Pi's. Click here for details on what [prime numbers](/pi-cluster/prime-numbers.md) are.  `./pi-cluster/primenumbers27.py` finds prime numbers using an MPI cluster which I seem to now understand thanks to [Gary Explains](https://www.youtube.com/channel/UCRjSO-juFtngAeJGJRMdIZw) <3

```
time mpiexec python primenumbers27.py
more ~/clusterfile
ip addr show wlan0
time mpiexec -hostfile ~/clusterfile python primenumbers27.py
```

*  https://carlpaton.github.io/2019/10/raspberry-pi-cluster/

### Bubble Sort

Given a list of numbers, `bubblesort27.py` iterates though them one at a time and compare the current `item` with its neighbor to see if it is greater/less than depending on the sort being asc/desc. Based on this you swap them. As a result the number bubble their way up. Not the most efficient way but it works.

```
python bubblesort27.py
```

### Docker

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