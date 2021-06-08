FROM python:3.7-slim

# Copy local code to the container image.
ENV APP_HOME /app

WORKDIR $APP_HOME

COPY . ./

# Install production dependencies.
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

CMD ["gunicorn", "--timeout", " 600", "--workers", "2", "--threads", "4", "--log-level", "debug", "--bind", "0.0.0.0:8080", "main:app"]