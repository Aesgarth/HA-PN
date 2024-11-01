def setup(hass, config):
    """Set up the printer notification component."""
    hass.services.register_notification_service("printer_notification", PrinterNotificationService)
    return True
