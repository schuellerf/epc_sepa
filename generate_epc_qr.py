#!/usr/bin/env python3
"""Generate Sepa/EPC QR code

Usage:
    generate.py [--name=<name>] [--iban=<iban>] [--bic=<bic>] REASON_FOR_PAYMENT AMOUNT

Options:
    --name=<name>  Name of the Bank Account Owner [default: Schüller Florian DI]
    --iban=<iban>  International Bank Account Number [default: AT27 1500 0040 7107 1486]
    --bic=<bic>    Business Identifier Code [default: OBKLAT2L]

"""

from segno import helpers
from docopt import docopt

import sys

if len(sys.argv) == 1:
    print("Interactive mode")
    try:
        reason = input("Text/Reason of the transaction: ")
        amount = input("Amount of the transaction: ")
        sys.argv.extend([reason, amount])
    except: #ignore errors to continue to docopt, for help
        print("  ...canceled interactive mode")

args = docopt(__doc__)

print(f"{args}")

reason = args["REASON_FOR_PAYMENT"]
amount = args["AMOUNT"].replace(",",".")
account_name = args["--name"]
iban = args["--iban"]
bic = args["--bic"]

qrcode = helpers.make_epc_qr(name=account_name,
                              iban=iban,
                              bic=bic,
                              amount=amount,
                              text=reason)
filename = f'{reason}.svg'.replace("/","_")
qrcode.save(filename)

print(f"{filename} saved")
