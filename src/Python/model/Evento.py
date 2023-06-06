from __future__ import print_function
import datetime


import datetime
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
        
# If modifying these scopes, delete the file token.json.

class controllerCalendar():
    def __init__(self):

        self.SCOPES = ['https://www.googleapis.com/auth/calendar.readonly', 'https://www.googleapis.com/auth/calendar']

        self.creds = None
        # The file token.json stores the user's access and refresh tokens, and is
        '''ELIMINAR TOKEN ANTES DE HACER EL EXE PORFA'''
        # created automatically when the authorization flow completes for the first
        # time.
        token_path = 'src/resources/token.json'
        if os.path.exists(token_path):
            self.creds = Credentials.from_authorized_user_file(token_path, self.SCOPES)
        # If there are no (valid) credentials available, let the user log in.
        if not self.creds or not self.creds.valid:
            if self.creds and self.creds.expired and self.creds.refresh_token:
                self.creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'src/resources/credentials.json', self.SCOPES)
                self.creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open(token_path, 'w') as token:
                token.write(self.creds.to_json())

        


    def crearCalendar(self):

        request_body = {
            'summary': 'Calendario MyUn'
        }

        try:
            service = build('calendar', 'v3', credentials=self.creds)

            lista_calendars = service.calendarList().list().execute()
            lista_usuario = lista_calendars.get('items')

            flag = False
            for calendar in lista_usuario:
                if calendar['summary'] == 'Calendario MyUn':
                    flag = True

            if flag == False:
                calendar_creation = service.calendars().insert(body = request_body).execute()
                print(calendar_creation['summary'])
            else:
                print('Calendar already exists')

        except HttpError as error:
            print('An error occurred: %s' % error) 

    def getId(self):
        try: 
            service = build('calendar', 'v3', credentials=self.creds)
            lista_calendars = service.calendarList().list().execute()
            lista_usuario = lista_calendars.get('items')
            for i in range(len(lista_usuario)):
                if lista_usuario[i]['summary'] == 'Calendario MyUn':
                    temp = lista_usuario[i]['id']
            print(temp)
            
            return temp
        except HttpError as error:
            print('An error occurred: %s' % error)
    


class event(controllerCalendar):
    def __init__(self, calendarioId):
        self.calendarioId = calendarioId
        super().__init__()

    def convert_to_RFC_datetime(self, year=1900, month=1, day=1, hour=0, minute=0):
        dt = datetime.datetime(year, month, day, hour, minute, 0).isoformat() + 'Z'
        return dt


    def crearEvent(self, titulo, desc, attendes, fecha):
        # fecha = [año, mes, dia, hora, minutos]
        service = build('calendar', 'v3', credentials=self.creds)

        hour_adjustment = 5
        list_of_attendes = []

        for email in attendes:
            dict_attende = {}
            dict_attende['email'], dict_attende['responseStatus'] = email,'tentative'

            list_of_attendes.append(dict_attende)

        event_request_body = {
            'start': {
                'dateTime': self.convert_to_RFC_datetime(fecha[0], fecha[1], fecha[2], fecha[3] + hour_adjustment, fecha[4]),
                'timeZone': 'America/Bogota'
            },
            'end' : {
                'dateTime': self.convert_to_RFC_datetime(fecha[0], fecha[1], fecha[2], fecha[3] + 2 +hour_adjustment, fecha[4]),
                'timeZone': 'America/Bogota'
            },
            'summary': titulo,
            'description' : desc,
            'colorId': 2,
            'status': 'confirmed',
            'transparency': 'transparent',
            'visibility': 'private',
            'location': 'Bogotá, CO',
            'attendes': [{'email': 'santi4g0303@gmail.com', 'responseStatus': 'accepted'}]
        }
        response = service.events().insert(
            calendarId= self.calendarioId,
            body= event_request_body
        ).execute()




        




    def getEvent(self):
        try:
            service = build('calendar', 'v3', credentials=self.creds)

            # Call the Calendar API
            now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
            print('Getting the upcoming event')
            events_result = service.events().list(calendarId=self.calendarioId, timeMin=now,
                                                maxResults=1, singleEvents=True,
                                                orderBy='startTime').execute()
            events = events_result.get('items', [])

            if not events:
                print('No upcoming events found.')
                return

            # Prints the start and name of the next event
            for event in events:
                start = event['start'].get('dateTime', event['start'].get('date'))
                print(start, ' ', event['summary'], ' ', event['description'])
                return (start, event['summary'], event['description'])

        except HttpError as error:
            print('An error occurred: %s' % error)    

        

if __name__ == '__main__':
    calendario = controllerCalendar()
    calendario.crearCalendar()
    id = calendario.getId()
    eventoCalendario = event(id)
    attendes = ['santi4g0303@gmail.com']
    fecha = [2023, 6, 6, 12, 30]
    eventoCalendario.crearEvent('Reunion de Los Rodriguez', 'Un gran y hermoso evento', [], fecha)
    eventoCalendario.getEvent()


        