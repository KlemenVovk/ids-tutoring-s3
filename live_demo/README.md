# IDS tutoring session 3: Docker and docker compose

This is the repository containing everything from the live demo.

The goal is to motivate and introduce containerization (and Docker) through a [practical story](https://klemenvovk.github.io/ids-tutoring/session3). The story is about a data scientist deploying a model in various ways, failing, and adjusting. Each folder in here is a part of the story that introduces a new concept.

A general outline of the structure and concepts introduced:
- `0_preparation` - we introduce a synthetically generated dataset. It can be generated with `gen_dataset.py` and will be used throughout the story. The company is producing metal parts of various dimensions (given by x, y and z) from different materials (steel, aluminum, copper) through different processes (turning, drilling, milling). The parts can be of varying complexities (an integer between 1 and 10), and for each we have the time it took to produce it in minutes. This is also our target variable. The hope is that the model will be able to predict how long a certain part will take to produce, which will help with scheduling different parts and increase efficiency (therefore increasing profits as more parts can be produced).
- `1_traditional` - the data scientist creates the model and tries "deploying" the model just by preparing a runnable Python script and passing it around.
- `2_api` - passing around the script soon becomes troublesome as the usage of the model scales. This is why the data scientist decides to centralize and creates an API for the model that everyone can access. The API is deployed directly on the company server. The deployment on the server is fragile, as other people, updates, and generally just a changing environment disturb it often, so the data scientist asks for a VM and deploys the API in that.
- `3_containers_basic` -  as company needs grow and more and more VMs are created on the server, everything grinds to a halt due to the server not being able to handle all VMs and overprovisioning. This time around, the data scientist decides to switch from VMs to containers. We introduce the concept of Dockerfiles and how to create containers.
- `4_containers_compose` - docker compose is introduced to simplify deployment of the containers
- `5_containers_redis` - redis is added to cache model results and show how multiple containers can be deployed with docker compose and how they can interact, as well as how to use premade containers when possible.
- `6_containers_persistence` - data persistence is introduced to save the redis database and to enable model swapping when the container is live. This is done to introduce volume mapping.
- `7_containers_env` - environment variables (and .env files) are introduced to showcase how we can use them for configuration, as well as safely accessing sensitive data. *Note: .env files should never be in git, I explicitly put them in here for demo purposes*.
  
