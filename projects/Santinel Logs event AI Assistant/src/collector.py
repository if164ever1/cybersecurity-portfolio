import time
import win32evtlog as win
import pywintypes
import config
import formatter as formatter
import engine as engine


def set_connection():
    handle = win.OpenEventLog(config.SERVER, config.TARGET_LOG)
    flags = win.EVENTLOG_BACKWARDS_READ|win.EVENTLOG_SEQUENTIAL_READ
    print(f"Successfully opened '{config.TARGET_LOG}' event log on {config.SERVER}.")
    return handle, flags
    

def read_event(handle, flags, last_event):
    all_events = []
    current_last = last_event
    
    while True:
        events = win.ReadEventLog(handle, flags, 0)
        if len(events) == 0:
            break    
        for event in events:
            if event.RecordNumber > last_event:
                extracted_data = {
                    "id": event.EventID,
                    "time": str(event.TimeGenerated),
                    "source": event.SourceName,
                    "type": config.EVENT_TYPES_MAPPING.get(str(event.EventType), "Unknown"),
                    "record_no": event.RecordNumber
                }
                all_events.append(extracted_data)
                if event.RecordNumber > current_last:
                    current_last = event.RecordNumber
    return all_events, current_last

HADLE, FLAGS = set_connection()

last_record_number = formatter.get_last_record()
engine.prepare_for_ml()

while 1:
    try:
        time.sleep(2)
        event_list, last_record_number = read_event(HADLE, FLAGS, last_record_number)
        if event_list: 
            formatter.create_frame(event_list)
            # print(event_list)
            # print("\n")
    except pywintypes.error as e:
        print(f"Win32 error opening event log: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

win.CloseEventLog(HADLE)