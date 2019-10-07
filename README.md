# Ansible Named Role

Small role for fast deploying named service

## Configuration:

Define your zones:

```
- hosts: DNS
  vars:
    named_config_master_zones:
      - name: test
        ttl: '4h'
        serial: '2019100701'
        cache_time: '2d'
        ns_rows:
          - name: 'www'
            class: 'IN'
            type: 'A'
            ip: '127.0.0.1'
          - name: 'ns1'
            class: 'IN'
            type: 'A'
            ip: '127.0.0.1'
    named_config_master_forwarders:
      - '10.66.0.6'
      - '10.6.0.6'
  roles:
    - ansible-role-named
```
