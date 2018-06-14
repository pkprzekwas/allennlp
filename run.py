import subprocess

TRAIN_CPU ="python3 -m allennlp.run train training_config/bidaf_cpu.json -s '/logs/outputs'"
subprocess.call(TRAIN_CPU, shell=True)
