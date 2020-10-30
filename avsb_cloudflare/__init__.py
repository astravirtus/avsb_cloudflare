import os

import CloudFlare

from loguru import logger

from .avsb_zones import DnsRecords


def main():
  """
  Application entrypoint.
  """
  dr = DnsRecords(interface=CloudFlare.CloudFlare(token=os.environ.get('ivnaiap2_PROD_CLOUDFLARE_API_KEY')))
  dr.backup_dns_records()
