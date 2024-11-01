import logging
from escpos.printer import Network
from homeassistant.components.notify import BaseNotificationService

_LOGGER = logging.getLogger(__name__)

def get_service(hass, config, discovery_info=None):
    """Get the notification service."""
    return PrinterNotificationService()

class PrinterNotificationService(BaseNotificationService):
    """Implementation of a notification service for the printer."""

    def __init__(self):
        # Set up connection to the printer
        self.printer = Network('<printer_ip>')  # Replace with your printer's IP

    def send_message(self, message="", **kwargs):
        """Send a message to the printer."""
        try:
            self.printer.text(message + '\n')
            self.printer.cut()
        except Exception as e:
            _LOGGER.error("Error sending message to printer: %s", e)
