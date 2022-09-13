# Generate EPC QR code for SEPA transaction

A simple helper script to generate QR Codes for my bills
using https://pypi.org/project/segno/ and https://pypi.org/project/docopt/

It just generates and saves an SVG **locally** which you can use for your
banking app to initiate a payment.

Feel free to change the "default:" values in lines number 8,9,10
or use this to donate for all my projects :-D

Example for this:  
<img src="Example_QR_code_to_donate.svg" alt="Example image to sponsor this project" title="Example image to sponsor this project" width="20%" />

## Installation

Install python (not described here) and the needed python libraries:

```
pip install -r requirements.txt
```

## Usage
Python 3 only!

Either just call the script for an interactive mode

```
python3 generate_epc_qr.py
```

checkout the help:
```
python3 generate_epc_qr.py ---help
```

or generate without questions
```
python3 generate_epc_qr.py "My Bill #1" 10.25
```
