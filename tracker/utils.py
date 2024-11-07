from .models import BlackRedEntry, OddEvenEntry, HighLowEntry
from .enums import Color, Parity, Range
from .configs import logger
import psutil
import random
import string
import uuid



# ********************************* Generate Password *************************************************

# Function to generate a random password
def generate_password():
    characters = get_machine_id() + string.ascii_letters + string.punctuation
    logger.info(f"Characters: {characters}")
    password = ''.join(random.choice(characters) for i in range(15))  # 10-character password
    return password

# Function to get machine's unique identifier (e.g., MAC address)
def get_machine_id():
    
    # Use machine-specific identifier
    machine_uuid = str(uuid.getnode())
    return machine_uuid

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
    