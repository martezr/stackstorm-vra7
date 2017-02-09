# vRealize Automation 7 Integration Pack

Stackstorm VMware vRealize Automation 7 Integration Pack

## Configuration

Copy the example configuration in [vra7.yaml.example](./vra7.yaml.example)
to `/opt/stackstorm/configs/vra7.yaml` and edit as required.

```yaml
---
hostname: cloud.company.local
username: administrator@vsphere.local
password: VMware1!
tenant: vsphere.local
verify_ssl: false
```

## Actions

* `get_all_requests` - Get all requests
* `get_resource_by_name` - Get resource details by name
