from client import ProductGeoipCurrencyTaxNexusNormalizerClient

def main():
    client = ProductGeoipCurrencyTaxNexusNormalizerClient()
    res = client.normalize_currency_and_tax(199.00, 'GB', 'SW1A 1AA')
    print('Tax & Currency Normalizer: ' + res['normalization_id'] + ' (' + res['destination_country'] + ')')
    print('Payable: ' + res['local_currency'] + ' ' + str(res['local_total_payable']) + ' (Tax: ' + str(int(res['applicable_tax_rate']*100)) + '%)')
    print('Compliance: ' + res['nexus_compliance_status'])
    print('Tax Breakdown: ' + res['tax_breakdown_url'])

if __name__ == '__main__':
    main()
