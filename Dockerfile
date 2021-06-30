FROM python:3.9.5
COPY . /user_management_system
WORKDIR /user_management_system
RUN pip install --upgrade pip
RUN pip3 install -r requirements.txt
EXPOSE 5000
ENTRYPOINT [ "python" ]
CMD [ "main.py" ]