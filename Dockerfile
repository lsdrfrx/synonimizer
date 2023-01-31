# Указывает Docker использовать официальный образ python 3 с dockerhub в качестве базового образа
FROM python:3.8.3-alpine
# Устанавливает переменную окружения, которая гарантирует, что вывод из python будет отправлен прямо в терминал без предварительной буферизации
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# Устанавливает рабочий каталог контейнера — "app"
WORKDIR /usr/src/app
# Копирует все файлы из нашего локального проекта в контейнер
# Запускает команду pip install для всех библиотек, перечисленных в requirements.txt

RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

RUN pip install --upgrade pip
COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY ./scripts/entrypoint.sh .
# copy project
COPY . .
# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/scripts/entrypoint.sh"]