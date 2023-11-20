# fastapi_crud
Repository for Transcribing and Customizing Zenn's [FastAPI Introduction](https://zenn.dev/sh0nk/books/537bb028709ab9)


## How to use
### Launch the API
Navigate to the project directory:

```bash
cd path/to/fastapi_crud
```

Launch the API using Docker Compose:
```bash
docker-compose up
```

### Access Swagger UI
Once the API is running, access Swagger UI by visiting `http://localhost:8000/docs` in your web browser.

### Run Unit Tests
Run unit tests using Docker Compose and Poetry:
```bash
docker-compose run --entrypoint "poetry run pytest tests --asyncio-mode=auto" demo-app
```
