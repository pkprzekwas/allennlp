import subprocess

bash_cd ="python3 -m allennlp.run train tutorials/getting_started/simple_tagger.json --serialization-dir /tmp/tutorials/getting_started -s '/logs/outputs'"

subprocess.call(bash_cd, shell=True)
