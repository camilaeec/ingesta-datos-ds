import boto3
import requests
import json
import os
from datetime import datetime

# Configuración
API_URL = os.getenv('API_URL')
S3_BUCKET_NAME = os.getenv('S3_BUCKET')
AWS_REGION = os.getenv('AWS_REGION', 'us-east-1')

def obtener_datos_inscripciones():
    """Obtiene datos REALES de inscripciones"""
    try:
        print(f"📡 Conectando a: {API_URL}")
        response = requests.get(f"{API_URL}", timeout=30)
        
        if response.status_code == 200:
            datos = response.json()
            print(f"✅ Obtenidos {len(datos)} inscripciones REALES")
            return datos
        else:
            print(f"❌ Error API: {response.status_code}")
            return []
            
    except Exception as e:
        print(f"❌ Error de conexión: {e}")
        return []

def main():
    print("🚀 Iniciando ingesta de Inscripciones - CONEXIÓN REAL")
    
    # 1. Obtener datos REALES
    datos = obtener_datos_inscripciones()
    if not datos:
        print("💥 No se pudieron obtener datos")
        return
    
    # 2. Formatear datos
    datos_formateados = {
        "metadata": {
            "timestamp": datetime.now().isoformat(),
            "source": "ms-inscripciones",
            "total_records": len(datos)
        },
        "data": datos
    }
    
    # 3. Subir a S3
    try:
        s3 = boto3.client('s3', region_name=AWS_REGION)
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        s3_key = f"raw-data/inscripciones/inscripciones-{timestamp}.json"
        
        s3.put_object(
            Bucket=S3_BUCKET_NAME,
            Key=s3_key,
            Body=json.dumps(datos_formateados, indent=2),
            ContentType='application/json'
        )
        
        print(f"📤 Datos subidos a S3: {s3_key}")
        print("🎉 Ingesta de inscripciones COMPLETADA!")
        
    except Exception as e:
        print(f"❌ Error subiendo a S3: {e}")

if __name__ == "__main__":
    main()