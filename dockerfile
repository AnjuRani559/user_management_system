FROM python:3.9.5
COPY . /user_management_system
WORKDIR /user_management_system
RUN pip install --upgrade pip
RUN pip3 install -r requirements.txt
ENV FLASK_APP=main.py
ENV FLASK_RUN_HOST=127.0.0.1
RUN apk add --no-cache gcc musl-dev linux-headers
EXPOSE 5000
ENTRYPOINT [ "python" ]
CMD ["manage.py seed_db"]
CMD [ "main.py" ]
