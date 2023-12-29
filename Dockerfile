# Use an official Python runtime as a base image
FROM python:3.9

# ARG BLD_USERNAME
# ARG BLD_PASSWORD
# ARG BLD_HOST
# ARG BLD_PORT
# ARG BLD_SERVICE_NAME
# ARG API_USERNAME
# ARG API_PASSWORD
ENV PIP_ROOT_USER_ACTION=ignore

# Set the working directory in the container
WORKDIR /app
# Install Oracle Instant Client and basic dependencies
RUN apt-get update && apt-get install -y \
    libaio1 \
    unzip \
    && rm -rf /var/lib/apt/lists/*

# Download Oracle Instant Client from Oracle's website
ADD https://download.oracle.com/otn_software/linux/instantclient/1921000/instantclient-basic-linux.x64-19.21.0.0.0dbru.zip /tmp/

# Unzip Oracle Instant Client and set up environment variables
RUN unzip /tmp/instantclient-basic-linux.x64-19.21.0.0.0dbru.zip -d /opt \
    && rm /tmp/instantclient-basic-linux.x64-19.21.0.0.0dbru.zip \
    && echo /opt/instantclient* > /etc/ld.so.conf.d/oracle-instantclient.conf \
    && ldconfig

# Set environment variables required for cx_Oracle
ENV ORACLE_HOME=/opt/instantclient_19_21
ENV LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$ORACLE_HOME
ENV PATH=$ORACLE_HOME:$PATH

# Install any needed dependencies specified in requirements.txt
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Flask application code into the container
COPY . /app/

# Expose the port that the Flask app runs on
EXPOSE 5000

# Define the command to run your application
CMD ["python", "main.py"]
