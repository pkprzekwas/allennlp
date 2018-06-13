This repository contains a very shallow wrapping script around allen nlp, to make testing of (PyTorch, Python 3.6) support easy on Clusterone. It should run bioth locally and on Clusterone.

For the original `allennlp` README, see (here)[https://github.com/allenai/allennlp/blob/master/README.md]

# Overview

The `allennlp` package mostly functions as a command line utility. As passing bash scripts to start jobs is not yet supported by Clusterone, the command line is wrapped in a python script in this repo (`run.py`).
This is far from ideal, and will be dropped as soon as Clusterone's interfaces become more flexible (`Project POLYMORPH`).

Allen NLP is started by starting the `run` module, and passing:
- a`mode` argument that defines if a training or evaluation task will be performed, and whether it should expect a GPU. It accepts:
    - `train` (default): execute a training task on a one GPU
    - `train_CPU` (default): execute a training task on CPU
    - `evaluate`: execute an evaluation task on CPU

- a `logs_path` argument, that defines where the script should write outputs. It defaults to `/logs/outputs`, meaning the path is by default the correct path to successfully run on Clusterone. Locally, a valid output path needs to be provided.

# Testing Instructions

After setting up a project based on this repository, create the following jobs. No datasets is required as the code will download it itself.

1. Run (Pytorch, Python 3.6, CPU) jobs
`just create job single ... --mode train_cpu --python-version 3.6 --instance-type <CPU-instances> --framework pytorch-1.0.0 --requirements requirements.txt`

2. Run (Pytorch, Python 3.6, GPU) jobs
`just create job single ... --mode train --python-version 3.6 --instance-type <GPU-instances> --framework pytorch-1.0.0 --requirements requirements.txt`


## Playing with the test locally
After cloning the repository, run `pip install requirements.txt`. The original allen nlp repository gives instructions on how to adjust this depending on your system.



## Acceptance Criteria
Tests pass if you see an output that indicates the job is successfully training (see line outlined by >>>). Note the loss, and the "1%" which indicates how far the training has progressed and would eventually reach 100% (8 hours on a GPU).
If in doubt, run the test locally first to build intuition on how the results should look like.

```
... stdout was cut ...

2018-06-13 15:28:25,496 - INFO - allennlp.training.trainer - Beginning training.
2018-06-13 15:28:25,496 - INFO - allennlp.training.trainer - Epoch 0/19
2018-06-13 15:28:25,496 - INFO - allennlp.training.trainer - Peak CPU memory usage MB: 3849.433088
  0%|          | 0/2190 [00:00<?, ?it/s]2018-06-13 15:28:25,556 - INFO - allennlp.training.trainer - Training
/Users/malomarrec/code/allennlp/allennlp/modules/encoder_base.py:93: UserWarning: invalid index of a 0-dim tensor. This will be an error in PyTorch 0.5. Use tensor.item() to convert a 0-dim tensor to a Python number
  num_valid = torch.sum(mask[:, 0]).int().data[0]
>>> start_acc: 0.0250, end_acc: 0.0387, span_acc: 0.0138, em: 0.0150, f1: 0.0699, loss: 9.5805 ||:   1%|          | 20/2190 [39:50<72:03:05
```
