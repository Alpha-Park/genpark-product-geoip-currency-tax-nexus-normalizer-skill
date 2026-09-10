class ProductGeoipCurrencyTaxNexusNormalizerClient:
    def normalize_currency_and_tax(self, base_price_usd=199.00, destination_country='GB', destination_postal='SW1A 1AA'):
        tax_rate = 0.20 if destination_country == 'GB' else 0.19 if destination_country == 'DE' else 0.0825
        forex_rate = 0.785 if destination_country == 'GB' else 0.920 if destination_country in ['FR', 'DE'] else 1.0
        local_currency = 'GBP' if destination_country == 'GB' else 'EUR' if destination_country in ['FR', 'DE'] else 'USD'
        local_net = round(base_price_usd * forex_rate, 2)
        local_tax = round(local_net * tax_rate, 2)
        local_total = round(local_net + local_tax, 2)
        return {
            'normalization_id': 'tax_geo_5521',
            'destination_country': destination_country,
            'local_currency': local_currency,
            'forex_rate_to_usd': forex_rate,
            'base_price_usd': base_price_usd,
            'local_net_amount': local_net,
            'applicable_tax_rate': tax_rate,
            'local_tax_amount': local_tax,
            'local_total_payable': local_total,
            'nexus_compliance_status': 'VAT_EU_UK_REVERSE_CHARGE_ELIGIBLE',
            'tax_breakdown_url': 'https://tax.nexus.genpark.ai/breakdowns/5521.json'
        }
