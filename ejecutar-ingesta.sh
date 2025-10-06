#!/bin/bash

echo "🚀 Ejecutando ingesta de datos..."

# Detectar qué comando de Docker usar
if command -v docker-compose &> /dev/null; then
    DOCKER_CMD="docker-compose"
    echo "✅ Usando docker-compose"
elif docker compose version &> /dev/null; then
    DOCKER_CMD="docker compose"
    echo "✅ Usando docker compose"
else
    echo "❌ Error: No se encontró docker-compose ni docker compose"
    exit 1
fi

# Construir contenedores
echo "🐳 Construyendo contenedores..."
$DOCKER_CMD build

# Ejecutar ingesta una vez
echo "📥 Ingestionando datos de estudiantes..."
$DOCKER_CMD run --rm ingesta-estudiantes python ingesta_estudiantes.py

echo "📥 Ingestionando datos de cursos..."
$DOCKER_CMD run --rm ingesta-cursos python ingesta_cursos.py

echo "📥 Ingestionando datos de inscripciones..."
$DOCKER_CMD run --rm ingesta-inscripciones python ingesta_inscripciones.py

echo "✅ Ingesta completada!"
echo "📊 Verifica en S3: s3://inscripciones-data-2025-camila/raw-data/"
