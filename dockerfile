# FROM ubuntu

# RUN apt-get update
# RUN apt-get install unzip
# RUN apt-get install -y xvfb


# COPY ./.garbage/chrome.deb ./

# RUN apt install -y ./chrome.deb
# RUN wget https://chromedriver.storage.googleapis.com/114.0.5735.90/chromedriver_linux64.zip
# RUN unzip chromedriver_linux64.zip

# RUN mv chromedriver /usr/bin

# RUN google-chrome --version

# WORKDIR /app 

# COPY requirements.txt ./


# # Install python
# RUN apt-get install python3
# # RUN apt-get install python3-pip -y
# RUN apt-get install python3-selenium -y

# COPY ./src ./src

# RUN xvfb-run python3 ./src/main.py

# # Declare a volume at the specified path for persistent data storage
# # VOLUME <Your working directory path>
# # (eg:-VOLUME /media/projects/Test)

# # Specify the default command to execute when the container starts
# # ENTRYPOINT [ "python", "app.py"]

FROM python:3.12-slim

# Install dependencies
RUN apt-get update && apt-get install -y \
    wget gnupg unzip xvfb x11-utils \
    libnss3 libxss1 libasound2 libx11-xcb1 libxcomposite1 libxcursor1 \
    libxdamage1 libxi6 libxtst6 libxrandr2 libgbm1 libgtk-3-0 \
    fonts-liberation libappindicator3-1 lsb-release \
    && apt-get clean

RUN apt-get install -y dbus dbus-x11
RUN dbus-uuidgen > /etc/machine-id && \
    service dbus start


# Install Chrome
# RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add - \
#     && echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list \
#     && apt-get update && apt-get install -y google-chrome-stable


COPY ./.garbage/chrome.deb ./
RUN apt install -y ./chrome.deb

# Install ChromeDriver
# RUN CHROME_VERSION=$(google-chrome --version | grep -oP '\d+\.\d+\.\d+') && \
#     wget -q "https://chromedriver.storage.googleapis.com/$CHROME_VERSION/chromedriver_linux64.zip" -O /tmp/chromedriver.zip && \
#     unzip /tmp/chromedriver.zip -d /usr/local/bin && \
#     chmod +x /usr/local/bin/chromedriver

# RUN wget https://storage.googleapis.com/chrome-for-testing-public/135.0.7049.95/linux64/chromedriver-linux64.zip
# RUN unzip chromedriver-linux64.zip
# RUN mv chromedriver-linux64/chromedriver /usr/bin


# Install Selenium
RUN pip install selenium
RUN pip install chromedriver-autoinstaller

# Copy your script
COPY src ./src

# Run with xvfb
# ENTRYPOINT ["xvfb-run", "python", "./src/main.py"]
RUN Xvfb :99 -screen 0 1280x1024x24 & export DISPLAY=:99

RUN xvfb-run python src/main.py
# RUN xvfb-run google-chrome https://www.example.com --disable-features=IdentityConsistency,SignInProfile,Signin --no-first-run --no-sandbox --disable-gpu
