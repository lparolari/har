# HAR

## Usage

Start jupyter notebook with docker

```
docker pull jupyter/tensorflow-notebook
docker run -p 8888:8888 -v "`pwd`:/home/jovyan/work" jupyter/tensorflow-notebook
```

The conncet the jupyter server with the notebook.

If you use colab, click on _Connect_ button and enter the url given from the `docker run` command.\
If you use vscode, click on _Connect_, select _Existing server_ and enter the url given from the `docker run` command.
