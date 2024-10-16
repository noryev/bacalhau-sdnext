FROM python:3.8-slim

WORKDIR /app

COPY sdnext-wrapper.py /app/
RUN pip install flask requests

CMD ["python", "sdnext-wrapper.py"]