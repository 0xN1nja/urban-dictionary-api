FROM python:latest
COPY . /app
WORKDIR /app
RUN ["pip","install","flask","bs4","requests"]
EXPOSE 5000
CMD ["python","main.py"]