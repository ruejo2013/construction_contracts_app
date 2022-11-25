import os

from deta import Deta

import pandas as pd
from dotenv import load_dotenv
from constants import Constants

# load_dotenv(".env")


deta = Deta(Constants.DETA_KEY)
db = deta.Base("contract_db")
db_inv = deta.Base("invoice_db")
fh = deta.Drive("files")    

def insert_milestone(contractId, InvoiceId, Amount, milestone, date):
    return db.put(
        {
            "key": InvoiceId, "contractId": contractId,
            "expense": Amount, "milestone": milestone,
            "date": date
            }
        )

def fetch_all_invoice(accNumber, contractId):
    if (
        accNumber in Constants.ACCOUNT_NUMBER
        and contractId in Constants.CONTRACTORS_ID
    ):
        result = db.fetch()
        return result.items
    else:
        return None


def pay_milestone(InvoiceId, contractId, account_number, Amount, date):
    return db_inv.put(
        {
            "key": InvoiceId, "accountNumber": account_number,
            "contractId": contractId, "paymentAmount": Amount, "date": date
            }
        )


def get_invoivces():
    items = db.fetch()
    invoices = [item['key'] for item in items.items]
    return invoices


def fetch_all_payments(accNumber, contractId):
    if (
        accNumber in Constants.ACCOUNT_NUMBER
        and contractId in Constants.CONTRACTORS_ID
    ):
        result = db_inv.fetch()
        return result.items
    else:
        return None


def process_df(contractID: str, fit: list, fh: list):
    df1 = pd.DataFrame(fit)
    df2 = pd.DataFrame(fh)
    df1 = df1[['expense', 'key', 'milestone']]
    # merge both dfs
    df = pd.merge(df1, df2, how='inner', on = 'key')
    # convert to date
    df["date"] = pd.to_datetime(df["date"]).dt.strftime('%Y-%m-%d')
    df = df[df['contractId'] == contractID]
    df['paymentAmount'] = '$' + df['paymentAmount'].astype(str)
    df = df.rename(
        columns={'expense': 'invoiceAmount', 'date': 'paymenDate'}
        )
    df = df[
        [
            'contractId', 'accountNumber', 'milestone', 'invoiceAmount',
            'paymenDate', 'paymentAmount'
            ]
        ]
    df = df.sort_values(by='paymentAmount')
    return df 





