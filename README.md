# Telegram File Repeater Bot

Este proyecto es un bot de Telegram desarrollado en Python utilizando la librería `pyTelegramBotAPI` (Telebot). El bot permite reenviar archivos a los usuarios mediante enlaces personalizados.

## ¿Cómo funciona?

1. El usuario debe crear un bot con [@BotFather](https://t.me/BotFather) y obtener el `BOT_TOKEN`.
2. El bot debe ser añadido a un grupo de Telegram (preferiblemente privado). Allí recibirá todos los archivos que se quieran compartir.
3. Al recibir un archivo en el grupo, el bot:
   - Guarda el `file_id` del archivo.
   - Genera un enlace personalizado que contiene la URL del bot y un parámetro `start` con el ID del archivo.
   - Devuelve este enlace al grupo.

4. Comparte este enlace con los usuarios, al hacer clic en el enlace, cualquier usuario será redirigido al bot, este último le enviará automáticamente el archivo correspondiente.

## Variables de entorno necesarias

Para ejecutar el bot correctamente, debes proporcionar las siguientes variables de entorno:

- `BOT_TOKEN`: Token del bot generado por [@BotFather](https://t.me/BotFather).
- `STORAGE_ID`: ID del grupo donde el bot recibirá los archivos.
- `BOT_LINK`: Enlace al bot (por ejemplo, `https://t.me/NombreDeTuBot`).

## Requisitos

- Python 3.7 o superior
- Librería `pyTelegramBotAPI`

## Ejecución

1. Clona este repositorio.
2. Ejecuta el siguiente comando para instalar las dependencias necesarias:

```bash
pip install -r requirements.txt
```

3. Crea un archivo `.env` o configura las variables de entorno necesarias.
4. Ejecuta el script principal:

```bash
python bot.py
```

## Ejemplo de archivo `.env`

```env
BOT_TOKEN=123456789:ABCdefGHIjklMNOpqrSTUvwxYZ
STORAGE_ID=-1001234567890
BOT_LINK=https://t.me/NombreDeTuBot
```
