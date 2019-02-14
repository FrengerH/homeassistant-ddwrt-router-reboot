# Home-assistant dd-wrt router reboot custom component

## About
This custom component allows you to reboot your dd-wrt router using a service call in home-assistant.

## Installation
Place the script in your `/config/custom_components` folder.

## Configuration
Add a ddwrt: in your config.yaml this will show the new service `ddwrt.reboot` in home-assistant. Call this service with the parameters `host`, `user` and `pass`
```yaml
ddwrt:
```

I created a script that calls the new `ddwrt.reboot` service and pass the parameters, so I can use my secrets.yaml file to store the host, user and pass of my router.

example:
```yaml
script:
  reboot_router:
    sequence:
    - service: ddwrt.reboot
      data:
        host: !secret router_host
        user: !secret router_user
        pass: !secret router_pass
```


## Known issues
No error handling added yet