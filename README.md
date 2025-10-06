# Ingesta de Datos - Data Science

Microservicios de ingesta de datos para el proyecto de Cloud Computing.

## 🏗️ Estructura

```
ingesta-datos-ds/
├── contenedor-estudiantes/    # Ingesta MS Estudiantes
├── contenedor-cursos/         # Ingesta MS Cursos  
├── contenedor-inscripciones/  # Ingesta MS Inscripciones
├── docker-compose.yml         # Orquestación
├── .env                       # Configuración
└── .env.example              # Template configuración
```

## 🚀 Despliegue

```bash
# 1. Configurar variables de entorno
cp .env.example .env
# Editar .env con tus valores

# 2. Ejecutar contenedores
docker-compose up --build

# 3. Ejecutar ingesta manual (opcional)
docker-compose run --rm ingesta-estudiantes python ingesta_estudiantes.py
```

## 🔧 Configuración

Variables de entorno en `.env`:
- `MV_INTEGRACION_URL`: URL del load balancer del backend
- `S3_BUCKET`: Bucket S3 de destino  
- `AWS_REGION`: Región de AWS

## 📊 Datos Generados

Los datos se almacenan en S3 en:
- `s3://[bucket]/raw-data/estudiantes/`
- `s3://[bucket]/raw-data/cursos/`
- `s3://[bucket]/raw-data/inscripciones/`

## 🛠️ Tecnologías

- Python 3.9
- Docker
- Docker Compose
- AWS S3
- Requests library

## 📝 Notas

Los contenedores de ingesta se ejecutan una vez y terminan. Para una ingesta continua, se puede configurar un cron job o un proceso repetitivo.
