class IMEI:
    def __init__(self, number):
        self.number = number
        self.check(number)
    
    def check(self, number):
        if self.validate(number):
            print(f"THIS IS A VALID {'IMEI' if len(str(self.number)) == 15 else 'IMEISV'}.")

    def validate(self, number):
        number_str = str(self.number)
        length = len(number_str)

        if not number_str.isdigit():
            raise ValueError("ERR --> VALID IMEI/IMEISV HAS NO NON-DIGIT NUMBER.")
        
        if length == 15:
            self.IMEI_validator()
            return True

        if length == 16:
            self.IMEISV_validator()
            return True
        
        raise ValueError("LENGTH ERR --> THIS IS NOT A VALID IMEI.")

    def IMEI_validator(self):
        last_digit = int(str(self.number)[-1])
        check_sum = IMEI.luhn_algorithm(int(str(self.number)[:14]))

        if last_digit != check_sum:
            raise ValueError("CHECKSUM ERR --> THIS IS NOT A VALID IMEI.")
            
    def IMEISV_validator(self):
        rbi = str(self.number)[:2]
        serial = int(str(self.number)[10:16])
        valid_rbis = ['01', '10', '30', '33', '35', '44', '45', '49', '50', '51', '52', '86', '91', '98']
        
        if rbi not in valid_rbis or serial == 0:
            raise ValueError("IMEISV ERR --> THIS IS NOT A VALID IMEISV.")

    @staticmethod    
    def summed_digit(number):
        return sum(int(i) for i in str(number))

    @staticmethod
    def luhn_algorithm(number):
        length = len(str(number))
        number = number if length == 14 else number[:14]
        digits = [int(i) for i in str(number)]

        # Double every other digits
        doulbed_digits = [digit * 2 if i % 2 == 1 else digit 
                            for i, digit in enumerate(digits)]
        
        sum = 0
        for i in doulbed_digits:
            if i < 10:
                sum += i
            else:
                sum += IMEI.summed_digit(i)
        
        check_sum = 10 - (sum % 10)

        return check_sum
        

if __name__ == "__main__":
    imei = 864025057375935
    imeisv = 3520991000000010
    IMEI = IMEI(imeisv)