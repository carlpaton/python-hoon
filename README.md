Python scripts pillaged and manipulated for reasons.

### Prime Numbers

`./pi-cluster/primenumbers27.py` finds prime numbers using an MPI cluster which I seem to now understand thanks to [Gary Explains](https://www.youtube.com/channel/UCRjSO-juFtngAeJGJRMdIZw) <3

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

