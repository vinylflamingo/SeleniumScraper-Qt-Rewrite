from twilio.rest import Client

class TextService:
    def __init__(self):
        pass
        
    def sendSms(self, matches, phoneNumber):
        client = Client("REMITTED FOR GITHUB", "REMITTED FOR GITHUB")
        client.messages.create(to=f"+1{phoneNumber}",
                            from_="+12052878153",
                            body=f"Matches found: {matches}")
