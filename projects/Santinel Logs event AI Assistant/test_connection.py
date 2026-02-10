import win32evtlog as win
import pywintypes

server = 'localhost'
logtype = 'System'

try:
    handle = win.OpenEventLog(server,logtype)
    flags = win.EVENTLOG_BACKWARDS_READ|win.EVENTLOG_SEQUENTIAL_READ
    print(f"Successfully opened '{logtype}' event log on {server}.")
    total_records = win.GetNumberOfEventLogRecords(handle)
    print(f"Total number of records: {total_records}")
    print(win.OpenEventLog(server, "Security"))        
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
