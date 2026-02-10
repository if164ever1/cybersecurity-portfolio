import time
import win32evtlog as win
import pywintypes
import event_types

SERVER = 'localhost'
LOG_TYPE = 'System'

def set_connection():
    handle = win.OpenEventLog(SERVER,LOG_TYPE)
    flags = win.EVENTLOG_BACKWARDS_READ|win.EVENTLOG_SEQUENTIAL_READ
    print(f"Successfully opened '{LOG_TYPE}' event log on {SERVER}.")
    return handle, flags
    

def read_event(handle, flags):
    all_events = []
    for event in win.ReadEventLog(handle, flags, 0):
        extracted_data = {
            "id": event_types.event_types_mapping.get(str(event.EventID), "Unknown"),
            "time": event_types.event_types_mapping.get(str(event.TimeGenerated), "Unknown"),
            "source": event_types.event_types_mapping.get(str(event.SourceName), "Unknown"),
            "type": event_types.event_types_mapping.get(str(event.EventType), "Unknown")
        }
        all_events.append(extracted_data)
    return all_events

HADLE, FLAGS = set_connection()

while 1:
    try:
        time.sleep(2)
        event_list = read_event(HADLE, FLAGS)
        if event_list: 
            print(event_list)
    except pywintypes.error as e:
        print(f"Win32 error opening event log: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

win.CloseEventLog(HADLE)