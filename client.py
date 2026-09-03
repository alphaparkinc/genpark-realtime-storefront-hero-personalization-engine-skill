class RealtimeStorefrontHeroPersonalizationEngineClient:
    def personalize_hero_banner(self, user_intent_tag='OUTDOOR_CAMPING_GEAR', referral_channel='GOOGLE_SHOPPING_CAMPAIGN'):
        return {
            'personalization_id': 'prs_hro_7721',
            'headline': 'Gear Up for the Wild: Premium Ultra-Light Tents & Stoves',
            'subheadline': 'Engineered for extreme sub-zero resilience. Complimentary express shipping.',
            'call_to_action': 'EXPLORE_ALPINE_EXPEDITION_COLLECTION',
            'hero_visual_asset_url': 'https://cdn.genpark.ai/heroes/alpine_sunset.webp',
            'predicted_ctr_lift_pct': 24.8,
            'experiment_payload_url': 'https://dynamicyield.personalization.genpark.ai/heroes/7721.json'
        }
