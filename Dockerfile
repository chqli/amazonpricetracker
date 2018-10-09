FROM jfloff/alpine-python:3.6
RUN pip3 install zmq
RUN pip3 install flask-restful
RUN pip3 install aiohttp
RUN pip3 install asyncio
ADD . /
