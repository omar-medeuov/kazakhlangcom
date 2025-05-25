#Pull base image, <image>[:<tag>]

FROM python:3.12-alpine

ENV PYTHONUNBUFFERED=1 
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1


WORKDIR /kazakhlang


#Install dependencies
COPY ./requirements.txt .
RUN pip install -r requirements.txt

#I wanna know where am i
RUN echo "test"

COPY . . 

#RUN python3 ./manage.py migrate

#shouldnt be running it during build, build would never end! you wont receive your image
CMD python3 ./manage.py runserver 0.0.0.0:8000


