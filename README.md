# Cocounut

## Usage

1. Clone the repository.
2. Install the required dependencies using Poetry (as defined in pyproject.toml):

```
poetry install
```

If you don’t have Poetry installed, you can install it by running:

```
pip install poetry
```

3. Create and activate a virtual environment:

```
python -m venv venv
```

Windows:

```
.\venv\Scripts\activate
```

macOS/Linux:

```
source venv/bin/activate
```

4. Run the application:

```
uvicorn src.main:app --reload
```

5. Open Swagger for API documentation
   [Coconut Swagger](http://127.0.0.1:8000/docs)
