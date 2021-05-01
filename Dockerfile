FROM gcr.io/google-appengine/python

# Flask App
ADD ./main.py main.py
ADD requirements.txt requirements.txt
ADD winner_prediction.p winner_prediction.p

# Install dependencides
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

EXPOSE 8080

CMD ["python3", "main.py"]