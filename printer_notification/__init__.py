from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from .const import DOMAIN

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up Printer Notification from a config entry."""
    ip_address = entry.data["ip_address"]
    port = entry.data.get("port", 9100)

    # Register notification service or other functionality here
    hass.services.async_register("notify", f"{DOMAIN}_notification", PrinterNotificationService(ip_address, port))

    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Handle unloading of a config entry."""
    # Unregister the service if needed
    hass.services.async_remove("notify", f"{DOMAIN}_notification")
    return True
