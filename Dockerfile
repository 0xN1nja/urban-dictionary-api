FROM python:latest
COPY . /app
WORKDIR /app
RUN ["pip","install","flask","bs4","requests"]
EXPOSE 8000
CMD ["python","src/main.py"]