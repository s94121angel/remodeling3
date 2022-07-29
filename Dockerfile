FROM jupyter/scipy-notebook:2022-06-02

RUN mkdir my-model train-code script
ENV MODEL_DIR=/home/jovyan/my-model
ENV MODEL_FILE_LDA=clf_lda.joblib
ENV MODEL_FILE_NN=clf_nn.joblib


RUN pip install --no-cache-dir joblib==1.1.0

COPY train.py /home/jovyan/train-code/train.py
EXPOSE 8080


COPY run.sh /home/jovyan/script/run.sh
ENTRYPOINT ["/bin/bash", "/home/jovyan/script/run.sh"]

