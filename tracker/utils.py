from .models import BlackRedEntry, OddEvenEntry, HighLowEntry
from .enums import Color, Parity, Range
import platform
import hashlib
from .configs import logger
import psutil
import random
import string
import uuid
import subprocess



# ********************************* Generate Password *************************************************

# Function to generate a random password
def generate_password():
    characters = get_machine_id() + string.ascii_letters + string.punctuation
    logger.info(f"Characters: {characters}")
    password = ''.join(random.choice(characters) for i in range(15))  # 10-character password
    return password



def get_windows_uuid():
    try:
        # Use WMIC to get the system's UUID
        result = subprocess.check_output("wmic csproduct get UUID", shell=True)
        return result.decode().split("\n")[1].strip()
    except subprocess.CalledProcessError as e:
        return f"Error fetching machine UUID: {e}"
    
def get_linux_uuid():
    try:
        # Use dmidecode to fetch the UUID from the system
        result = subprocess.check_output("sudo dmidecode -s system-uuid", shell=True)
        return result.decode().strip()
    except subprocess.CalledProcessError as e:
        return f"Error fetching machine UUID: {e}"
    
def get_macos_uuid():
    try:
        # Use ioreg to fetch the system UUID
        result = subprocess.check_output("ioreg -rd1 -c IOPlatformExpertDevice | grep IOPlatformUUID", shell=True)
        return result.decode().split("= ")[1].strip().strip('"')
    except subprocess.CalledProcessError as e:
        return f"Error fetching machine UUID: {e}"
    


# Function to get machine's unique identifier (e.g., MAC address)
def get_machine_id():
    
    
    system_info = platform.uname()
    unique_string = f"{system_info.system}-{system_info.node}-{system_info.machine}-{system_info.processor}"
    print(f'Machine: {unique_string}')
    print(f"{platform.system()}")
    machine_id = hashlib.sha256(unique_string.encode()).hexdigest()
    # Hash the combined string
    return machine_id

# Use machine-specific identifier
# machine_uuid = str(uuid.getnode())
# logger.info(f'Machine ID: {machine_uuid}')
# return machine_uuid

# os_platform = platform.system()
# if os_platform == "Windows":
#     return get_windows_uuid()
# elif os_platform == "Linux":
#     return get_linux_uuid()
# elif os_platform == "Darwin":  # macOS
#     return get_macos_uuid()
# else:
#     return f"Unsupported platform: {os_platform}"


# ********************************* Log Number ********************************************************
 

def log_request(number):
    
    try:
        color = get_color(number)
        parity = get_parity(number)
        _range = get_range(number)
        BlackRedEntry.objects.create(color=color)
        OddEvenEntry.objects.create(parity=parity)
        HighLowEntry.objects.create(range_value=_range)
        
        return {'color': color, 'parity': parity, 'range': _range, 'number': number, "status":"logged"}
    
    except Exception as e:
        
        logger.error(f"Error saving value: {type(e).__name__} - {str(e)}")
        
        return {"message":f"Error saving {number} value: {type(e).__name__} - {str(e)}", "status":"error"}
    
        
        
        


def get_color(number):
    
    if number in [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]:
        
        return Color.BLACK.value
    
    elif number == 0:
        
        return Color.GREEN.value
    
    else:
        
        return Color.RED.value
    
    
def get_parity(number):
    
    if number % 2 == 0:
        
        return Parity.EVEN.value
    
    else:
        
        return Parity.ODD.value

def get_range(number):
    
    if number in range(19):
        
        return Range.LOW.value
    
    else:
        
        return Range.HIGH.value
    

#******************************* Reset Table ******************************************************

def reset_table(request, table_name):
    
    try:
        if table_name == "color":
            BlackRedEntry.objects.all().delete()
        elif table_name == "parity":
            OddEvenEntry.objects.all().delete()
        elif table_name == "range":
            HighLowEntry.objects.all().delete()
        elif table_name == "all": # Delete all entries
            BlackRedEntry.objects.all().delete()
            OddEvenEntry.objects.all().delete()
            HighLowEntry.objects.all().delete()
            
        return {"message": f"All records in the {table_name} table(s) have been deleted successfully"}
    
    except Exception as e:
        
        logger.error(f"Error saving value: {type(e).__name__} - {str(e)}")
        
        return {"message":f"Error clearing records from {table_name} table(s): {type(e).__name__} - {str(e)}", "status":"error"}
    