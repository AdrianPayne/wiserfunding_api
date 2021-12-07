FROM python:3.9
COPY . .
WORKDIR .
ENV PYTHONPATH "${PYTHONPATH}:."

RUN pip install -r requirements.txt

CMD ["python", "v1/app.py"]