# TBD

## Hints

- install requirements:
    ```
    python -m venv .venv
    source .venv/bin/activate
    python -m pip install -r requirements.txt
    ```

- run in dev mode and execute example calculation
    ```
    uvicorn main:app --reload
    ```

- Invoke example calculation http://localhost:8000/add?v1=1&v2=2
- See OpenApi spec http://localhost:8000/docs

- Build image with Dockerfile
  ```
  docker build -t fastapi .
  ```

- Run image (for some reason it does not work as promised)
  ```
  docker run --rm --env PORT=8080 -p 8080:8080 fastapi:latest
  ```
  
## Useful links
- https://fastapi.tiangolo.com/tutorial/