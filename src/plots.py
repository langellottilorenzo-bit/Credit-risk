import matplotlib.pyplot as plt
import seaborn as sns

def plot_pd_distribution(df):
    fig, ax = plt.subplots()
    sns.histplot(df["PD"], bins=20, ax=ax)
    ax.set_title("PD Distribution")
    return fig

def plot_el_by_segment(df):
    fig, ax = plt.subplots()
    el = df.groupby("Segment")["EL"].sum()
    el.plot(kind='bar', ax=ax)
    ax.set_title("Expected Loss by Segment")
    return fig

def plot_ead_lgd(df):
    fig, ax = plt.subplots()
    sns.scatterplot(x="EAD", y="LGD", hue="Segment", data=df, ax=ax)
    ax.set_title("EAD vs LGD")
    return fig
