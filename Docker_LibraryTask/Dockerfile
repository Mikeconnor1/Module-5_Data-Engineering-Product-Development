FROM python:3.12.3

#Setting a working directory in the container
WORKDIR /app

#Copying the py file and everything else into the app foldert
COPY . /app

#installing depnendancies
RUN pip install -r requirements.txt

# Running the application
ENTRYPOINT ["python", "./UnittestPythonCode.py"]