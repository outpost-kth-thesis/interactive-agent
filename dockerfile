FROM python:3.13-slim

RUN apt-get update && apt-get install -y \
    wget gnupg unzip xvfb x11-utils \
    libnss3 libxss1 libasound2 libx11-xcb1 libxcomposite1 libxcursor1 \
    libxdamage1 libxi6 libxtst6 libxrandr2 libgbm1 libgtk-3-0 \
    fonts-liberation libappindicator3-1 lsb-release \
    && apt-get clean

RUN apt-get install -y dbus dbus-x11
RUN dbus-uuidgen > /etc/machine-id && \
    service dbus start

COPY ./.garbage/chrome.deb ./
RUN apt install -y ./chrome.deb

RUN pip install selenium
RUN pip install chromedriver-autoinstaller

COPY src ./src

RUN Xvfb :99 -screen 0 1280x1024x24 & export DISPLAY=:99

RUN xvfb-run python src/main.py

