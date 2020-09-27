#!/usr/bin/env python

from ansible.module_utils.basic import AnsibleModule

def get_uptime():
    with open('/proc/uptime', 'r') as f:
        uptime_seconds = float(f.readline().split()[0])
    return uptime_seconds

def main():
  module = AnsibleModule(
    argument_spec=dict(),
    supports_check_mode=False
  )

  result = dict()
  result["changed"] = True
  result["uptime"] = get_uptime()

  module.exit_json(**result)

if __name__ == '__main__':
    main()

