FROM python:3.8
ENV PYTHONUNBUFFERED 1
RUN mkdir /web_Welltory
WORKDIR /web_Welltory
COPY requirements.txt /web_Welltory/
RUN pip install --upgrade pip && pip install -r requirements.txt
ADD . /web_Welltory/