import requests

class CatFacts():
    BASE_URL = 'https://cat-fact.herokuapp.com'

    def _get_random_verified_facts(self):
        facts = []

        for attempt in range(10):
            r = requests.get(f'{self.BASE_URL}/facts/random', params={'amount': 10})
            data = r.json()
            for fact in data:
                if fact['status']['verified']:
                    facts.append(fact['text'])
        return facts

    def get_random_facts(self):
        return self._get_random_verified_facts()