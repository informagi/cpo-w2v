# CPO W2V

W2V experiments for CPO & iCIS lecture on bias in ML.

## Initial Steps

### Create Docker container

    docker create -p 8888:8888 \
      -v `pwd`/notebooks:/home/jovyan/work:z \
      --name cpo --user `id -u` --group-add users jupyter/minimal-notebook \
      start-notebook.sh --NotebookApp.password=`python pwd.py`
    docker start cpo

### Download GoogleNews wordvectors

Pretrained W2V vectors are provided by Google:
https://code.google.com/archive/p/word2vec/

Download the file `GoogleNews-vectors-negative300.bin.gz`.

These pre-trained W2V vectors have also been shared as an 
[Academic Torrent](http://academictorrents.com/details/2aa0d0c6aff92f08719e409db04ecee4721cf21f).

    sudo dnf install transmission-cli
    transmission-cli http://academictorrents.com/download/2aa0d0c6aff92f08719e409db04ecee4721cf21f.torrent

## Notebooks:
This repository contains three Jupyter notebooks:
- cpo-notebook.ipynb : Notebook used for the CPO & iCIS lecture
- Reproducing_figures_poster_ipynb : Notebook for reproducing all the figures from the poster/paper
- Word2vec_Bias_plots : Experimental notebook, use at own risk. 

## FDIA 2019:
This work resulted into a short paper and poster presented at [FDIA 2019](http://www.ir.disco.unimib.it/essir2019/fdia/). Both the pdf of the paper and poster can be found here. 
