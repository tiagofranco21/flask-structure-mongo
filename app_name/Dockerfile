FROM python:3.8
RUN mkdir -p /home/project/app_name
WORKDIR /home/project/app_name
COPY . .
EXPOSE 5000
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python3","index.py"]
