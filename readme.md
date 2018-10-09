
#### Please follow these steps
- `docker build . -t pywithzmq`
- Run **DataManager** with ` docker run --net host -it -p 6000:6000 --entrypoint python3 pywithzmq zmq_data_manager.py`
- Run **Scheduler** with `docker run --net host -it -p 7000:7000 --entrypoint python3 pywithzmq scheduler.py`
- Run **APIServer** with `docker run --net host -it -p 5000:5000 --entrypoint python3 pywithzmq api_server.py`
- Run the **Algorithm** with `docker run --net host -it  --entrypoint python3 pywithzmq algo.py`

#### Notes
- If docker is not available, Dockerfile can be used as a reference to setup the environment for the apps
-