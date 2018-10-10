
#### Please follow these steps to run docker containers of the services
- If docker is not available, Dockerfile can be used as a reference to setup the environment for the apps
- `docker build . -t pywithzmq`
- Run **DataManager** with ` docker run --net host -it -p 6000:6000 --entrypoint python3 pywithzmq zmq_data_manager.py`
- Run **Scheduler** with `docker run --net host -it -p 7000:7000 --entrypoint python3 pywithzmq scheduler.py`
- Run **APIServer** with `docker run --net host -it -p 5000:5000 --entrypoint python3 pywithzmq api_server.py`
- Run the **Algorithm** with `docker run --net host -it  --entrypoint python3 pywithzmq algo.py`

#### Notes
- For communication among the processes, I've used TCP ports because, on my windows laptop, the IPC protocol from zeromq is not supported
and for communication among docker containers, IPC won't work.But, if we can deploy these apps on a machine natively then we can leverage fast IPC communication. This would be a one line change in the code. Given the 5 seconds delay that we have with the scheduler, I think moving to IPC will be an overkill.
- To prove the correctness and ease of running, I've suggested docker and TCP based sockets in zeromq
- Given the limited time, I haven't handled scenarios where APIServer or DataManager are not responding
- The webserver used for APIServer is a minimalist development server. For real application I would use a WSGI container like gunicorn
- Since all the four services are independent services, it makes sense to have separate project for each, but since we don't have lot in each module, I'm using all services in same package.
- Also we're not seeing any substantial benefit of asyncio given the nature of the use case which is
`Every 5 seconds contact DataManager and APIServer parallely and then decide the price` We could've accomplished that using threads.
- The requirement says, the Algorithm contacts the APIServer again **After x seconds**, I've chosen **x as 3** which is completely arbitrary
- I've chosen the buffer size for DataManager as 1KB, but in real application, we can easily have much larger buffer