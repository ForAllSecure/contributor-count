FROM python:3.9
LABEL maintainer="ForAllSecure, Inc"
LABEL description="Counts SCM contributors for the purpose of licensing"

WORKDIR /app

COPY ./requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . .

ENTRYPOINT ["python", "contrib-count.py"]