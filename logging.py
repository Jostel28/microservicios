import logging
import win32evtlogutil

def setup_logging():
    # Configura el logger
    logger = logging.getLogger('MyMicroservice')
    logger.setLevel(logging.INFO)
    
    # Crea un manejador para enviar los logs al Windows Event Viewer
    def log_to_event_viewer(message, event_id=1):
        try:
            win32evtlogutil.ReportEvent("MyMicroservice", event_id, eventType=logging.INFO, strings=[message])
            logger.info(f"Evento registrado: {message}")
        except Exception as e:
            logger.error(f"No se pudo registrar el evento: {e}")

    return logger, log_to_event_viewer

# Uso del logger
logger, log_event = setup_logging()
logger.info("El servicio ha iniciado correctamente.")
log_event("El servicio de autenticación ha iniciado.")
