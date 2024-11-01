
import voluptuous as vol
from homeassistant import config_entries
from homeassistant.core import callback

from .const import DOMAIN  # Import the domain of the integration

@config_entries.HANDLERS.register(DOMAIN)
class PrinterNotificationConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Printer Notification."""

    VERSION = 1
    CONNECTION_CLASS = config_entries.CONN_CLASS_LOCAL_PUSH

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        errors = {}

        if user_input is not None:
            # Validate the input here if necessary
            ip_address = user_input["ip_address"]
            port = user_input["port"]

            # Try to connect or validate the printer here if possible, then proceed
            return self.async_create_entry(title="Printer Notification", data=user_input)

        # Show the form if no valid input received yet
        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema(
                {
                    vol.Required("ip_address", default="192.168.0.100"): str,
                    vol.Optional("port", default=9100): int,
                }
            ),
            errors=errors,
        )

    @staticmethod
    @callback
    def async_get_options_flow(config_entry):
        return PrinterNotificationOptionsFlow(config_entry)


class PrinterNotificationOptionsFlow(config_entries.OptionsFlow):
    """Handle options for Printer Notification."""

    def __init__(self, config_entry):
        """Initialize Printer Notification options flow."""
        self.config_entry = config_entry

    async def async_step_init(self, user_input=None):
        """Manage the options."""
        if user_input is not None:
            return self.async_create_entry(title="", data=user_input)

        # Show the options form
        return self.async_show_form(
            step_id="init",
            data_schema=vol.Schema(
                {
                    vol.Required("ip_address", default=self.config_entry.options.get("ip_address", "192.168.0.100")): str,
                    vol.Optional("port", default=self.config_entry.options.get("port", 9100)): int,
                }
            ),
        )
