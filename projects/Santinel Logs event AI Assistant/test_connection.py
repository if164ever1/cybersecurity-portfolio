import win32evtlog as win
import pywintypes

server = 'localhost'
logtype = 'System'

def read_event(handle, flags): 
    for event in win.ReadEventLog(handle, flags, 0):
        event_id = event.EventID
        time_generated = event.TimeGenerated
        source_name = event.SourceName
        # 1 - Error | 2 - Warning | 4 - Information | 8 - Audit Success | 16 - Audit Failure
        event_type = event.EventType
        print(f"Event ID: {event_id} - Time generated: {time_generated} - Source Name: {source_name}\n Event Type: {event_type}")

try:
    handle = win.OpenEventLog(server,logtype)
    flags = win.EVENTLOG_BACKWARDS_READ|win.EVENTLOG_SEQUENTIAL_READ
    print(f"Successfully opened '{logtype}' event log on {server}.")
    total_records = win.GetNumberOfEventLogRecords(handle)
    print(f"Total number of records: {total_records}")
    
    read_event(handle, flags)
    
except pywintypes.error as e:
    print(f"Win32 error opening event log: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
finally:
    try:
        if 'handle' in locals() and handle:
            win.CloseEventLog(handle)
    except Exception:
        pass