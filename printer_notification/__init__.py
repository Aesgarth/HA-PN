async def async_setup_entry(hass, config_entry):
    """Set up Printer Notification from a config entry."""
    ip_address = config_entry.data.get("ip_address")
    port = config_entry.data.get("port", 9100)

    # Pass the config data to the PrinterNotificationService
    hass.services.register_notification_service("printer_notification", PrinterNotificationService(ip_address, port))

    return True
