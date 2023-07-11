# Bogon lists

## Overview

Run bogons.py to reach out to team-cymru.org's ipv4 and ipv6 bogon list. Two files will be created for ipv4 and ipv6 lists. The files are formatted for use with juniper devices with the format:

```set policy-options prefix-list pl-bogons-ipv6 <prefix>```

## Dependencies

```shell
pip3 install requests
pip3 install Jinja2
```
