# HAR

## Usage

Start jupyter notebook with docker

```
docker pull jupyter/tensorflow-notebook
docker run -p 8888:8888 -v "`pwd`:/home/jovyan/work" jupyter/tensorflow-notebook start-notebook.sh --NotebookApp.notebook_dir="/home/jovyan/work"
```

Docker with GPU

```
docker run --device /dev/nvidia0:/dev/nvidia0 --device /dev/nvidiactl:/dev/nvidiactl --device /dev/nvidia-uvm:/dev/nvidia-uvm -p 8888:8888 -v "`pwd`:/home/jovyan/work" jupyter/tensorflow-notebook start-notebook.sh --NotebookApp.notebook_dir="/home/jovyan/work" --NotebookApp.token=""
```

Then connect the jupyter server with the notebook.

If you use colab, click on _Connect_ button and enter the url given from the `docker run` command.\
If you use vscode, click on _Connect_, select _Existing server_ and enter the url given from the `docker run` command.
