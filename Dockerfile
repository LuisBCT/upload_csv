FROM python:3.9

RUN apt-get update && apt-get install -y sudo
RUN sudo apt install -y unixodbc

ENV PIP_DISABLE_PIP_VERSION_CHECK=1
ENV PYTHONNUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .

RUN python -m venv venv

RUN /bin/bash -c "source venv/bin/activate"
RUN pip install -r requirements.txt
RUN sudo apt install unixodbc

COPY . .

EXPOSE 8000

CMD ["uvicorn", "app:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
