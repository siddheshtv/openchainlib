class Client:
    def __init__(self) -> None:
        return
    
    def submit_job(self, job, fee, gas):
        return
    
    def calc_fee(self, job):
        return
    
    def calc_gas(self, job):
        return
    
    def pay_job_fee(self):
        return
    
    def validator_interact(self):
        return


class Monitor(Client):
    def __init__(self) -> None:
        super().__init__()
        return
    
    def transaction_status(self):
        return
    

class Wallet(Client, Monitor):
    def __init__(self) -> None:
        super().__init__()