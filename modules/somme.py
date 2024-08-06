class SommeData:
    def __init__(self):
        self.sum_EMI = 0
        self.sum_EMI_ANNUL = 0
    
    def set_sum_EMI(self, value):
        self.sum_EMI = value
    
    def set_sum_EMI_ANNUL(self, value):
        self.sum_EMI_ANNUL = value
    
    def get_sum_EMI(self):
        return self.sum_EMI
    
    def get_sum_EMI_ANNUL(self):
        return self.sum_EMI_ANNUL  