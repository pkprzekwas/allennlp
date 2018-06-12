import subprocess
import os, argparse

EVALUATE ="python3 -m allennlp.run evaluate https://s3-us-west-2.amazonaws.com/allennlp/models/bidaf-model-2017.09.15-charpad.tar.gz --evaluation-data-file https://s3-us-west-2.amazonaws.com/allennlp/datasets/squad/squad-dev-v1.1.json"

TRAIN ="python3 -m allennlp.run train training_config/bidaf.json -s '/logs/outputs'"

parser = argparse.ArgumentParser()
parser.add_argument("--mode", default="train", help="train or evaluate")
args = parser.parse_args()

if args.mode == "train":
    print("Running %s" % args.mode)
    subprocess.call(TRAIN, shell=True)
elif args.mode =="evaluate":
    print("Running %s" % args.mode)
    subprocess.call(EVALUATE, shell=True)
else:
    raise(NotImplementedError)
