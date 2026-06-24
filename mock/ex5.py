from user import User


class VIPUser(User):
    def __int__(
            self, 
            name: str,
            surname: str,
            email: str,
            vip_card_number: int):
        User.__init__(self, name, surname, email)
        self._vip_card_number = vip_card_number if VIPUser._check_card(vip_card_number) else None

    
    @staticmethod
    def _check_card(new_number: int) -> bool:
        return new_number > 999 and new_number % 2 == 0
    
    @staticmethod
    def use_vip_card():
        return None
    
    @property
    def vip_num(self):
        return self._vip_card_number

    @vip_num.setter
    def vip_num(self, new):
        if VIPUser._check_card(new):
            self._vip_card_number = new
