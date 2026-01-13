FROM apache/spark:4.0.1

USER root

ENV DEBIAN_FRONTEND=noninteractive

# ---- System packages (ONLY what is missing) ----
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        ca-certificates \
        build-essential \
        vim \
        nano \
        bash-completion && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# ---- Python packages (Spark already has pyspark) ----
RUN pip install --no-cache-dir \
        jupyterlab \
        numpy \
        pandas \
        ipython

# ---- Jupyter + permissions ----
RUN mkdir -p /home/spark/.local/share/jupyter/runtime \
             /opt/spark-notebooks && \
    chown -R spark:spark /home/spark /opt/spark-notebooks

RUN echo ". /usr/share/bash-completion/bash_completion" >> /etc/bash.bashrc

USER spark
ENV SHELL=/bin/bash

WORKDIR /opt/spark-notebooks

EXPOSE 8888 4040

CMD ["python3", "-m", "jupyterlab", \
     "--ip=0.0.0.0", \
     "--port=8888", \
     "--no-browser", \
     "--NotebookApp.token=''"]