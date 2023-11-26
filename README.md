show how 8000 when running without -p isn't accessible.
explain we are using pip instead of conda as conda isnt in the default python image
cattle vs pets
introduce ENV
README inside each folder
ssh into container just to show that it really is an OS
tip that you need --build in docker compose to rebuild
pinning versions docker
note async/await is not used here just for simplicity, you should absolutely use it.
you have to be careful with caching in practice - it can cause all sorts of issues.
image vs build
COPY vs ADD
next steps: multistage or ADD for new model, frontend by just adding a new container...
depends on