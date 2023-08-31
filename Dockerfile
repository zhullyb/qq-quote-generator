FROM python:3.11-alpine
COPY main.py screenshot.py utils.py /root/
RUN mkdir /root/templates
COPY templates/ /root/templates/
EXPOSE 5000
RUN apk add --no-cache firefox font-noto-cjk font-noto-cjk-extra font-noto-emoji && pip install selenium requests flask
CMD python3 /root/main.py