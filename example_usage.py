from client import RealtimeStorefrontHeroPersonalizationEngineClient

def main():
    client = RealtimeStorefrontHeroPersonalizationEngineClient()
    res = client.personalize_hero_banner('RUNNING_SHOES')
    print('Storefront Hero Personalizer: ' + res['personalization_id'])
    print('Headline: "' + res['headline'] + '"')
    print('Projected CTR Lift: +' + str(res['predicted_ctr_lift_pct']) + '%')
    print('Payload URL: ' + res['experiment_payload_url'])

if __name__ == '__main__':
    main()
