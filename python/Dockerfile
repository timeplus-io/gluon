# generate clean, final image for end users
FROM jupyter/base-notebook:python-3.9.10

ARG VERSION

WORKDIR /timeplus
ADD ./requirements.txt /timeplus
ADD ./dist/ /timeplus/
RUN pip3 install -r requirements.txt
RUN pip3 install /timeplus/timeplus-$VERSION.tar.gz

RUN rm /timeplus/requirements.txt
RUN rm /timeplus/timeplus-$VERSION*

EXPOSE 8888