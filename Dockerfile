FROM python:3.9-slim
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
ENV GOOGLE_MAPS_API_KEY=$GOOGLE_MAPS_API_KEY
CMD ["python", "app.py"]