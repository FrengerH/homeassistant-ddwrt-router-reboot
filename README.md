# Home-assistant dd-wrt router reboot custom component

## About
This custom component allows you to reboot your dd-wrt router using a service call in home-assistant.

## Installation
Place the script in your `/config/custom_components` folder.

## Configuration
Add a ddwrt: in your config.yaml this will show the new service `ddwrt.reboot` in home-assistant.
```yaml
ddwrt:
  host: !secret router_host
  user: !secret router_user
  pass: !secret router_pass
```

## Known issues
No error handling added yet
