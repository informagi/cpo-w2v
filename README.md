# COPD W2V

W2V experiments for COPD lecture on bias in ML

## Initial Steps

### Create Docker container

    docker create -p 8888:8888 \
      -v `pwd`/notebooks:/home/jovyan/work:z \
      --name copd --user `id -u` --group-add users jupyter/minimal-notebook \
      start-notebook.sh --NotebookApp.password=`python pwd.py`
    docker start copd

### Download GoogleNews wordvectors

Pretrained W2V vectors are provided by Google:
https://code.google.com/archive/p/word2vec/

Download the file `GoogleNews-vectors-negative300.bin.gz`.

These pre-trained W2V vectors have also been shared as an 
[Academic Torrent](http://academictorrents.com/details/2aa0d0c6aff92f08719e409db04ecee4721cf21f).

    sudo dnf install transmission-cli
    transmission-cli http://academictorrents.com/download/2aa0d0c6aff92f08719e409db04ecee4721cf21f.torrent

## Etc.

_Etc._
