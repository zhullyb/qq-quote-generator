FROM python:3.11-alpine
EXPOSE 5000
WORKDIR /root
COPY requirements.txt /root/
RUN pip install -r /root/requirements.txt
RUN mkdir /root/templates \
    && mkdir -p /usr/share/fonts/misans \
    && apk add --no-cache \
    firefox \
    font-freefont \
    font-noto \
    font-noto-cjk \
    font-noto-cjk-extra \
    font-noto-emoji
COPY templates/ /root/templates
COPY MiSans-Regular.ttf /usr/share/fonts/misans/
COPY main.py screenshot.py utils.py geckodriver /root/
CMD env GECKODRIVER_PATH=/root/geckodriver gunicorn --threads 4 -b 0.0.0.0:5000 main:app
