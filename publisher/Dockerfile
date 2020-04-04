FROM python:3.8

RUN pip install yosun pydantic

# Actually install the application
WORKDIR /usr/src/app

# When you just 'docker run publisher' with no command afterwards,
# default to this:
CMD ["python", "-u", "/usr/src/app/publisher.py"]