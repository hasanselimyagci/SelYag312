FROM python:3.8-slim

WORKDIR /app/
ADD requirements.txt /app/

RUN pip install torch==2.0.0 --index-url https://download.pytorch.org/whl/cpu
RUN pip install -r requirements.txt

ADD . /app/

# Expose the port on which the application will run
EXPOSE 8000

# Run the FastAPI application using uvicorn server
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]