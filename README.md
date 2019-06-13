# Home-assistant dd-wrt router reboot custom component

## About
This custom component allows you to reboot your dd-wrt router using a service call in home-assistant.

## Installation
Place the folder `ddwrt_router_service` in your `/config/custom_components` folder.

## Configuration
Add a ddwrt_router_service: in your config.yaml this will show the new service `ddwrt_router_service.reboot` in home-assistant.
```yaml
ddwrt_router_service:
  host: !secret router_host
  user: !secret router_user
  pass: !secret router_pass
```

## Known issues
No error handling added yet
