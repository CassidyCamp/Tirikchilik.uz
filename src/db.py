import json


from src.config import Settings


class User:
    
    def check_ds(self, chat_id: int, full_name: str, username: str) -> None:
        
        if self.save_ds(chat_id, full_name, username):
            return True
        else:
            pass
    
    
    def save_ds(self, chat_id: int, full_name: str, username: str) -> None:
        status_user = None
        try:
            with open(Settings.DataUser, "r") as f:
                users = json.load(f)       
        except:
            users = {}
            
        if str(chat_id) not in users:
            status_user = True
            users[str(chat_id)] = {
                'full_name': full_name,
                'username': username
            }
        
        with open(Settings.DataUser, "w") as add_f:
            json.dump(users, add_f, indent=4)
                
        return status_user
            
    
    def check_dsp(self, phone: int) -> None:
        pass
    
    
    def save_dsp(self, phone: int, full_name: str, username: str) -> None:
        pass