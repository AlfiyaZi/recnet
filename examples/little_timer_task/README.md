
## Little timer task

Based on an example designed by [Herbert Jaeger](http://www.pdx.edu/sites/www.pdx.edu.sysc/files/Jaeger_TrainingRNNsTutorial.2005.pdf).
This task has two input signals, a *start signal* and a *duration signal*. The target output is a signal which starts at
each *start signal* peak and builds a rectangular signal. This signal length is the value of the *duration signal* at starting peak.

<table>
  <tr>
    <td><img src="little_timer_task.png" ></td>
  </tr>
</table>


### How to use it

1. Install:
    - [recnet](https://github.com/joergfranke/recnet/blob/master/README.md).
    - [requirements.txt](https://github.com/joergfranke/recnet/tree/master/examples/little_timer_task/requirements.txt)
1. Generate data set
    - Run `make_data_set.py`
2. Train model
    - Run `train_model.py`
3. Use model
    - Add name of the network parameter file from outcome to `use_model.py`
    - Run `use_model.py`


### Hints

For training its useful to have minimum two output signal. So in this example we use the target output and the inverse
output. Otherwise cross entropy does't work.

