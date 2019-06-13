import telnetlib

# The domain of your component. Should be equal to the name of your component.
DOMAIN = 'ddwrt_router_service'

ATTR_HOST = 'host'
ATTR_USER = 'user'
ATTR_PASS = 'pass'

def setup(hass, config):
    """Set up is called when Home Assistant is loading our component."""
    host = config[DOMAIN].get(ATTR_HOST)
    user = config[DOMAIN].get(ATTR_USER)
    password = config[DOMAIN].get(ATTR_PASS)

    def handle_reboot(call):
        tn = telnetlib.Telnet(host)
        tn.read_until(b"login: ")

        tn.write(user.encode('ascii') + b"\n")
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")

        tn.write(b"reboot\n")
        tn.write(b"exit\n")

        tn.read_all().decode( 'ascii' )

    hass.services.register(DOMAIN, 'reboot', handle_reboot)

    # Return boolean to indicate that initialization was successfully.
    return True