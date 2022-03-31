FROM amd64/python:3.9.7-slim

WORKDIR /app

ENV MODULE_NAME axel

COPY requirements.txt *.whl /app/

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./ /app

ENV JETPACK_ENTRYPOINT ./image.py

CMD ["uvicorn", "image:app", "--host", "0.0.0.0", "--port", "8080"]
