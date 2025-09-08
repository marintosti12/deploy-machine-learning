FROM python:3.12-slim

#  Runtime/env de base
ENV PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PORT=7860

# Crée un user non-root (id 1000 requis par Spaces)
RUN useradd -m -u 1000 user
USER user
ENV PATH="/home/user/.local/bin:$PATH"
WORKDIR /app

RUN pip install --no-cache-dir "poetry==1.8.3" \
 && poetry --version

COPY --chown=user pyproject.toml poetry.lock* /app/

# Désactive le venv interne de Poetry (on installe dans le site-packages global de l’image)
RUN poetry config virtualenvs.create false \
 && poetry install --no-interaction --no-ansi --only main

# Copie du code
COPY --chown=user src /app/src

# Ports
EXPOSE 7860

# Lancement FastAPI
CMD ["bash", "-lc", "uvicorn main:app --app-dir src --host 0.0.0.0 --port $PORT"]
