# python3.7のイメージをダウンロード
FROM python:3.7-alpine
# pythonの出力表示をDocker用に調整
ENV PYTHONUNBUFFERED = 1

WORKDIR /src

# pipを使ってpoetryをインストール
RUN pip install --no-cache-dir fastapi uvicorn

EXPOSE 8000

# uvicornのサーバーを立ち上げる
ENTRYPOINT [ "uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000" ]