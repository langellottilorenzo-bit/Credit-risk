import pandas as pd

def calculate_kpis(df):
    df = df.copy()
    df["EL"] = df["PD"] * df["LGD"] * df["EAD"]

    total_ead = df["EAD"].sum()
    total_el = df["EL"].sum()

    npl_ead = df[df["Default"] == 1]["EAD"].sum()
    provisions = df["Provisions"].sum()

    kpis = {
        "Total EAD": total_ead,
        "Expected Loss": total_el,
        "NPL Ratio": npl_ead / total_ead if total_ead > 0 else 0,
        "Coverage Ratio": provisions / npl_ead if npl_ead > 0 else 0,
        "Cost of Risk": total_el / total_ead if total_ead > 0 else 0
    }

    return kpis, df
