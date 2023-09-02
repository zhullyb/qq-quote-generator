FROM python:3.11-alpine
EXPOSE 5000
RUN mkdir /root/templates \
    && mkdir -p /usr/share/fonts/misans \
    && apk add --no-cache \
    firefox font-noto-cjk \
    font-noto-cjk-extra \
    font-noto-emoji \
    && pip install selenium requests flask
COPY main.py screenshot.py utils.py assets/geckodriver /root/
COPY templates/ /root/templates
COPY assets/MiSans-Regular.ttf /usr/share/fonts/misans/
CMD env GECKODRIVER_PATH=/root/geckodriver python3 /root/main.py
