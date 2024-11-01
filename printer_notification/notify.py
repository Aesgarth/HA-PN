import logging
from escpos.printer import Network
from homeassistant.components.notify import BaseNotificationService

_LOGGER = logging.getLogger(__name__)

def get_service(hass, config, discovery_info=None):
    """Get the notification service."""
    return PrinterNotificationService()

class PrinterNotificationService(BaseNotificationService):
    """Implementation of a notification service for the printer."""

    def __init__(self, ip_address, port=9100):
        # Connect to the network printer with user-defined IP and port
        self.printer = Network(ip_address, port)

    def send_message(self, message="", **kwargs):
        """Send a message to the printer."""
        try:
            self.printer.text(message + '\n')
            self.printer.cut()
        except Exception as e:
            _LOGGER.error("Error sending message to printer: %s", e)
