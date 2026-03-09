
# app.py
import pandas as pd
import numpy as np
import uuid
import random
from datetime import datetime
from faker import Faker
from sklearn.ensemble import IsolationForest

from dash import Dash, html, dcc, dash_table, Input, Output, State, callback_context
import plotly.express as px
import plotly.graph_objects as go

fake = Faker()

BANK_LOCATIONS = {
    "RTR Exchange": {"city": "Ottawa", "lat": 45.4215, "lon": -75.6972, "type": "exchange"},
    "RBC": {"city": "Toronto", "lat": 43.6532, "lon": -79.3832, "type": "bank"},
    "TD": {"city": "Toronto", "lat": 43.6532, "lon": -79.3832, "type": "bank"},
    "Scotiabank": {"city": "Halifax", "lat": 44.6488, "lon": -63.5752, "type": "bank"},
    "BMO": {"city": "Montreal", "lat": 45.5017, "lon": -73.5673, "type": "bank"},
    "CIBC": {"city": "Toronto", "lat": 43.6532, "lon": -79.3832, "type": "bank"},
    "Desjardins": {"city": "Levis", "lat": 46.8033, "lon": -71.1779, "type": "bank"},
    "National Bank": {"city": "Montreal", "lat": 45.5017, "lon": -73.5673, "type": "bank"},
    "HSBC": {"city": "Vancouver", "lat": 49.2827, "lon": -123.1207, "type": "bank"},
    "NeoBank": {"city": "Toronto", "lat": 43.6532, "lon": -79.3832, "type": "bank"}
}

BANKS = list(BANK_LOCATIONS.keys())
BANK_IDS = {bank: f"{i:03d}" for i, bank in enumerate(BANKS) if bank != "RTR Exchange"}

STATUS_CODES = {
    "ACSC": "Settled",
    "ACSP": "Finality",
    "ACWP": "Accepted",
    "RJCT": "Rejected"
}

REJECT_REASONS = {
    "AM04": "Insufficient funds",
    "AC01": "Incorrect account number",
    "DUPL": "Duplicate payment detected",
    "FF07": "Invalid amount format",
    "MD07": "Customer account deceased",
    "AB04": "Settlement process aborted",
    "SL01": "Daily limit exceeded",
    "SL02": "Monthly threshold reached",
    "RF01": "Risk scoring triggered",
    "ML01": "ML anomaly detection",
    "CB01": "Cross-border restriction",
    "NB01": "NeoBank risk policy"
}

transactions_df = pd.DataFrame(columns=[
    "timestamp","uetr","debtor","creditor","amount",
    "status","reason_code","reason_description",
    "risk_score","risk_label","risk_factors"
])

liquidity = {bank: random.randint(200000,500000) for bank in BANKS if bank!="RTR Exchange"}
model = IsolationForest(contamination=0.02, random_state=42)

def calculate_risk_factors(amount, debtor, creditor, is_cross_border=False):
    risk_factors=[]
    if amount>10000:
        risk_factors.append({"factor":"EXTREME_HIGH_AMOUNT","description":f"Extremely high amount ${amount:,.2f}","score":70})
    elif amount>5000:
        risk_factors.append({"factor":"VERY_HIGH_AMOUNT","description":f"Very high amount ${amount:,.2f}","score":50})
    elif amount>1000:
        risk_factors.append({"factor":"HIGH_AMOUNT","description":f"High amount ${amount:,.2f}","score":20})

    if debtor=="NeoBank":
        risk_factors.append({"factor":"NEOBANK_RISK","description":"NeoBank higher risk profile","score":10})

    if is_cross_border:
        risk_factors.append({"factor":"CROSS_BORDER","description":"Cross border transaction","score":15})

    risk_score=sum(f["score"] for f in risk_factors)

    if risk_score>70:
        label="CRITICAL RISK"
    elif risk_score>50:
        label="HIGH RISK"
    elif risk_score>20:
        label="MEDIUM RISK"
    else:
        label="LOW RISK"

    return risk_factors,risk_score,label

def generate_payment():
    available=[b for b in BANKS if b!="RTR Exchange"]
    debtor=random.choice(available)
    creditor=random.choice([b for b in available if b!=debtor])

    amount=round(abs(np.random.normal(120,60)),2)

    factors,score,label=calculate_risk_factors(amount,debtor,creditor)

    if liquidity[debtor]<amount:
        status="RJCT"
        reason="Insufficient funds"
    else:
        if random.random()<0.9:
            status="ACSC"
            reason="Transaction completed"
            liquidity[debtor]-=amount
            liquidity[creditor]+=amount
        else:
            status="RJCT"
            reason="Random rejection"

    return {
        "timestamp":datetime.now(),
        "uetr":str(uuid.uuid4()),
        "debtor":debtor,
        "creditor":creditor,
        "amount":amount,
        "status":status,
        "reason_code":"",
        "reason_description":reason,
        "risk_score":score,
        "risk_label":label,
        "risk_factors":"; ".join([f["factor"] for f in factors])
    }

def process_cycle():
    global transactions_df,model
    new=[generate_payment() for _ in range(random.randint(3,6))]
    df=pd.DataFrame(new)
    transactions_df=pd.concat([transactions_df,df],ignore_index=True)

app=Dash(__name__)

app.layout=html.Div([
    html.H1("RTR AI Payment Monitoring Dashboard",style={"textAlign":"center"}),
    html.Button("Start",id="start",n_clicks=0),
    html.Button("Stop",id="stop",n_clicks=0),
    dcc.Interval(id="interval",interval=2000,disabled=True),
    dcc.Graph(id="amount-chart"),
    dash_table.DataTable(id="table",page_size=10)
])

@app.callback(
    Output("interval","disabled"),
    [Input("start","n_clicks"),Input("stop","n_clicks")]
)
def control(start,stop):
    ctx=callback_context
    if not ctx.triggered:
        return True
    btn=ctx.triggered[0]["prop_id"].split(".")[0]
    if btn=="start":
        return False
    return True

@app.callback(
    [Output("amount-chart","figure"),
     Output("table","data"),
     Output("table","columns")],
    Input("interval","n_intervals")
)
def update(n):
    process_cycle()
    df=transactions_df.tail(200)
    fig=px.scatter(df,x=df.index,y="amount",color="risk_label",
                   title="Transaction Amounts")
    cols=[{"name":i,"id":i} for i in df.columns]
    return fig,df.to_dict("records"),cols

if __name__=="__main__":
    app.run(debug=True,port=8050)
