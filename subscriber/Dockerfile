FROM python:3.8

RUN pip install yosun

# Actually install the application
WORKDIR /usr/src/app

# It's only a single file.  It has to be in the same directory as the
# Dockerfile, or a subdirectory, but not a parent or sibling.
COPY subscriber.py .

# When you just 'docker run publisher' with no command afterwards,
# default to this:
CMD ["python", "-u", "/usr/src/app/subscriber.py"]