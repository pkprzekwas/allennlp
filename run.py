import subprocess

bash_cd ="python3 -m allennlp.run train tutorials/getting_started/simple_tagger.json --serialization-dir /tmp/tutorials/getting_started --recover"

subprocess.call(bash_cd, shell=True)
