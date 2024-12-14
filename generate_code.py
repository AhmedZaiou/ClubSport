import hashlib
from datetime import datetime, timedelta
import secrets




def generer_hash_md5(message):
    hash_object = hashlib.md5(message.encode())
    return hash_object.hexdigest()
 
def verifier_hash_md5(message, hash_md5): 
    hash_calcule = generer_hash_md5(message)
    return hash_calcule == hash_md5




def create_code():
    message = "RoyalFitness-" 
    new_date = datetime.now() - timedelta(days=1)

    hash_md5_date = generer_hash_md5(new_date.strftime('%Y%m%d')) 
    code = generer_hash_md5(hash_md5_date) 
     
    return f"{message}{code}"


 

if __name__ == "__main__":
    code = create_code() 
    print(code) 
 
        