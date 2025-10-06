#!/bin/bash

echo "🚀 Ejecutando ingesta de datos..."

# Construir contenedores
docker compose build

# Ejecutar ingesta una vez
echo "📥 Ingestionando datos de estudiantes..."
docker compose run --rm ingesta-estudiantes python ingesta_estudiantes.py

echo "📥 Ingestionando datos de cursos..."
docker compose run --rm ingesta-cursos python ingesta_cursos.py

echo "📥 Ingestionando datos de inscripciones..."
docker compose run --rm ingesta-inscripciones python ingesta_inscripciones.py

echo "✅ Ingesta completada!"
echo "📊 Verifica en S3: s3://inscripciones-data-2025-camila/raw-data/"
