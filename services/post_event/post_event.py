import requests 


def main():
    api_key = 'ies_b5FJQA10ectkLDsAyXRko1l4QJkLyxtRU1R7uLMyH2s'

    def post_event(event):
        headers = {
            "X-API-Key": api_key
        }

        response = requests.post(
            "http://localhost:5000/api/seismic_events/", 
            json=event,
            headers=headers
        )

        result = response.json()
        
        return result['event']['id']


    event = {
        "iesdata_id": "IES-2026-9631",
        "seiscomp_oid": "Origin/20260928.9631.05",
        "origin_time": "2026-09-28T16:30:00",
        "latitude": 42.2451,
        "longitude": 43.7612,
        "depth": 12.4
    }

    event_id = post_event(event)

    print("Created event ID:", event_id)


    def post_magnitude(event_id, value, magnitude_code):
        headers = {
            "X-API-Key": api_key
        }

        response = requests.post(
            f"http://localhost:5000/api/seismic_events/{event_id}/magnitudes",
            params={
                "value": value,
                "magnitude_code": magnitude_code
            },
            headers=headers
        )


    post_magnitude(event_id, 5.1, "ML")


main()