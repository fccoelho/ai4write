"""
Módulo para carregar a imagem logo.webp usando PIL.
A imagem é primeiro codificada em base64, depois decodificada e mostrada.
"""

from PIL import Image
import os
import base64
import io

# Caminho para a imagem
LOGO_PATH = os.path.join(os.path.dirname(__file__), 'logo.webp')

# Variável para armazenar a imagem codificada em base64
logo_base64 = None
logo_image = None

# Carrega a imagem e codifica em base64
try:
    # Lê o arquivo da imagem
    with open(LOGO_PATH, 'rb') as image_file:
        image_data = image_file.read()
    
    # Codifica em base64
    logo_base64 = base64.b64encode(image_data).decode('utf-8')
    print(f"Imagem codificada em base64 com sucesso ({len(logo_base64)} caracteres)")
    
    # Decodifica de volta e carrega com PIL
    decoded_data = base64.b64decode(logo_base64)
    logo_image = Image.open(io.BytesIO(decoded_data))
    print(f"Logo decodificado e carregado: {logo_image.size} pixels, modo {logo_image.mode}")
    
except FileNotFoundError:
    print(f"Erro: Arquivo {LOGO_PATH} não encontrado")
except Exception as e:
    print(f"Erro ao processar a imagem: {e}")

def get_logo():
    """Retorna a imagem do logo carregada."""
    return logo_image

def get_logo_base64():
    """Retorna a string base64 da imagem."""
    return logo_base64

def get_logo_info():
    """Retorna informações sobre a imagem do logo."""
    if logo_image:
        return {
            'size': logo_image.size,
            'mode': logo_image.mode,
            'format': logo_image.format,
            'path': LOGO_PATH,
            'base64_length': len(logo_base64) if logo_base64 else 0
        }
    return None

def show_logo():
    """Mostra a imagem do logo."""
    if logo_image:
        logo_image.show()
    else:
        print("Imagem não carregada")
