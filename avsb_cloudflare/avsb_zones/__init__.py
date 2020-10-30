import os

from datetime import datetime

from loguru import logger


class DnsRecords(object):
  def __init__(self, *args, **kwargs):
    self.interface = kwargs['interface']

  def backup_dns_records(self):
    timestamp = datetime.utcnow().strftime('%Y-%m-%d_%H%M%S')

    zones = self.interface.zones.get()

    for zone in zones:
      logger.info(f'''Backing DNS records for zone: {zone['name']}''')

      try:
        os.mkdir('backups')
      except FileExistsError as error:
        pass

      filename = os.path.join('backups', f'''{zone['name']}_{timestamp}.txt''')

      with open(file=filename, mode='w') as file:
        file.write(self.interface.zones.dns_records.export.get(zone['id']))
