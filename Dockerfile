FROM python:3.9-alpine
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
RUN chmod +x start-server.sh
ENTRYPOINT ["./start-server.sh"]