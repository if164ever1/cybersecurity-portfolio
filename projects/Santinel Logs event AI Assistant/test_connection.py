import time
import win32evtlog as win
import pywintypes
import event_types
import create_frame


SERVER = 'localhost'
LOG_TYPE = 'System'

def set_connection():
    handle = win.OpenEventLog(SERVER,LOG_TYPE)
    flags = win.EVENTLOG_BACKWARDS_READ|win.EVENTLOG_SEQUENTIAL_READ
    print(f"Successfully opened '{LOG_TYPE}' event log on {SERVER}.")
    return handle, flags
    

def read_event(handle, flags, last_event):
    all_events = []
    current_last = last_event
    for event in win.ReadEventLog(handle, flags, 0):
        if event.RecordNumber > last_event:
            extracted_data = {
                "id": event.EventID,
                "time": str(event.TimeGenerated),
                "source": event.SourceName,
                "type": event_types.event_types_mapping.get(str(event.EventType), "Unknown")
            }
            all_events.append(extracted_data)
            if event.RecordNumber > current_last:
                current_last = event.RecordNumber
    return all_events, current_last

HADLE, FLAGS = set_connection()

last_record_number = 0

while 1:
    try:
        time.sleep(2)
        event_list, last_record_number = read_event(HADLE, FLAGS, last_record_number)
        if event_list: 
            create_frame.create_frame(event_list)
            # print(event_list)
            # print("\n")
    except pywintypes.error as e:
        print(f"Win32 error opening event log: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

win.CloseEventLog(HADLE)