FROM python:3.11-alpine
EXPOSE 5000
RUN mkdir /root/templates \
    && mkdir -p /usr/share/fonts/misans \
    && apk add --no-cache \
    firefox font-noto-cjk \
    font-noto-cjk-extra \
    font-noto-emoji \
    && pip install selenium requests flask
COPY main.py screenshot.py utils.py /root/
COPY templates/ /root/templates
COPY assets/MiSans-Light.ttf /usr/share/fonts/misans/
CMD python3 /root/main.py
