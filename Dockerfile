#defining the base image
FROM python:3.12.0

#setting the working directory
WORKDIR /game

#copying the content from the current directory to the working directory
COPY . /game

#installing the required packages
RUN pip install numpy

#command to run the application
CMD ["python", "rps.py"]
