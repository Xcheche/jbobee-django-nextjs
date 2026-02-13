# -------------------------
# Stage 0: Base Python Image
# -------------------------
FROM python:3.12.2-slim-bookworm AS python

# -------------------------
# Stage 1: Build Wheels
# -------------------------
FROM python AS python-build-stage

ARG BUILD_ENVIRONMENT=local

# Install build dependencies (for compiling wheels)
RUN apt-get update && apt-get install --no-install-recommends -y \
    build-essential \
    libpq-dev \
    gdal-bin libgdal-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements files
COPY ./requirements .

# Build wheels for offline installation
RUN pip wheel --wheel-dir /usr/src/app/wheels -r ${BUILD_ENVIRONMENT}.txt

# -------------------------
# Stage 2: Run Stage
# -------------------------
FROM python AS python-run-stage

ARG BUILD_ENVIRONMENT=local
ARG APP_HOME=/app

# Environment variables (GDAL included)
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    BUILD_ENVIRONMENT=${BUILD_ENVIRONMENT} \
    GDAL_CONFIG=/usr/bin/gdal-config \
    CPLUS_INCLUDE_PATH=/usr/include/gdal \
    C_INCLUDE_PATH=/usr/include/gdal

# Set working directory
WORKDIR ${APP_HOME}

# Install runtime dependencies only
RUN apt-get update && apt-get install --no-install-recommends -y \
    libpq-dev gettext gdal-bin libgdal-dev \
    && rm -rf /var/lib/apt/lists/*

# Create django user and static directory
RUN addgroup --system django && \
    adduser --system --ingroup django django && \
    mkdir -p ${APP_HOME}/staticfiles && \
    chown -R django:django ${APP_HOME}/staticfiles && \
    chmod 775 ${APP_HOME}/staticfiles

# Copy pre-built wheels
COPY --from=python-build-stage /usr/src/app/wheels /wheels/

# Install Python packages from wheels (no build tools needed)
RUN pip install --no-cache-dir --no-index --find-links=/wheels/ /wheels/* \
    && rm -rf /wheels/

# Copy entrypoint and start scripts
COPY --chown=django:django ./docker/local/django/entrypoint.sh /entrypoint.sh  
COPY --chown=django:django ./docker/local/django/start.sh /start.sh  

# Fix line endings & make executable
RUN sed -i 's/\r$//g' /entrypoint.sh /start.sh && \
    chmod +x /entrypoint.sh /start.sh

# Copy project files
COPY --chown=django:django . ${APP_HOME}

# Switch to django user
USER django

# Set entrypoint
ENTRYPOINT ["/entrypoint.sh"]
