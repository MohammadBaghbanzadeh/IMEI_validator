# IMEI Validator
The IMEI class is a Python script that validates International Mobile Equipment Identity (IMEI) and International Mobile Station Equipment Identity Number (IMEISV).

## Usage
Clone the repo or download the script 'imei_validator.py'
Import the class IMEI from the script.
Create an instance of IMEI by passing the 15- or 16-digit number as argument.
The check() method will validate the number and print whether it's a valid IMEI or IMEISV.
python
```
from imei_validator import IMEI

imei = 864025057375935
imeisv = 3520991000000010

IMEI(imei).check() # Output: THIS IS A VALID IMEI.
IMEI(imeisv).check() # Output: THIS IS A VALID IMEISV.
```
## Methodology
* The constructor accepts the number as input and calls the check() method.
* The check() method checks the length of the number and calls either IMEI_validator() or IMEISV_validator() based on the length.
* The IMEI_validator() method checks the validity of the IMEI number using the Luhn algorithm.
* The IMEISV_validator() method checks the validity of the IMEISV number by validating the Reporting Body Identifier (RBI) and Serial Number fields.
* The luhn_algorithm() is used for the Luhn checksum calculation and returns the check digit.
## Limitations
* This script only checks the validity of the given number, it does not determine whether the device with the given number actually exists or is in use.
* The RBI list is limited to those observed in 2021. It's possible that new RBIs have been added since then.
