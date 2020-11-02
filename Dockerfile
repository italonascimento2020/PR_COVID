FROM python:3.9

RUN mkdir /app
WORKDIR /app
ADD . /app/

RUN pip install --upgrade --trusted-host pypi.org --trusted-host files.pythonhosted.org pip
RUN pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org /app/

# Set up and activate virtual environment
#ENV VIRTUAL_ENV "/venv"
#RUN python -m venv $VIRTUAL_ENV
#ENV PATH "$VIRTUAL_ENV/bin:$PATH"

# Python commands run inside the virtual environment
#RUN python -m pip install \
#        requests 

COPY main.py .
CMD ["python", "main.py"]
