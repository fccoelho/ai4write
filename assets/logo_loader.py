"""
Módulo para carregar a imagem logo.webp usando PIL.
"""

from PIL import Image
import os

# Caminho para a imagem
LOGO_PATH = os.path.join(os.path.dirname(__file__), 'logo.webp')

# Carrega a imagem usando PIL
try:
    logo_image = Image.open(LOGO_PATH)
    print(f"Logo carregado com sucesso: {logo_image.size} pixels, modo {logo_image.mode}")
except FileNotFoundError:
    print(f"Erro: Arquivo {LOGO_PATH} não encontrado")
    logo_image = None
except Exception as e:
    print(f"Erro ao carregar a imagem: {e}")
    logo_image = None

def get_logo():
    """Retorna a imagem do logo carregada."""
    return logo_image

def get_logo_info():
    """Retorna informações sobre a imagem do logo."""
    if logo_image:
        return {
            'size': logo_image.size,
            'mode': logo_image.mode,
            'format': logo_image.format,
            'path': LOGO_PATH
        }
    return None
