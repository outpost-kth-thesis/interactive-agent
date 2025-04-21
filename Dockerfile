FROM python:3.12-slim

RUN apt-get update && apt-get install -y \
    wget gnupg unzip xvfb x11-utils \
    libnss3 libxss1 libasound2 libx11-xcb1 libxcomposite1 libxcursor1 \
    libxdamage1 libxi6 libxtst6 libxrandr2 libgbm1 libgtk-3-0 \
    fonts-liberation libappindicator3-1 lsb-release \
    && apt-get clean

COPY ./.garbage/chrome.deb ./
RUN apt install -y ./chrome.deb

COPY ./.garbage/mitmproxy/* /usr/bin/
COPY scripts scripts

RUN pip install selenium
RUN pip install mitmproxy

COPY src ./src

RUN chmod +x ./src/entrypoint.sh
ENTRYPOINT [ "./src/entrypoint.sh" ]