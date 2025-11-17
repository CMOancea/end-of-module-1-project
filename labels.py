
# labels.py — FULL TRANSLATION DICTIONARY + HELPERS

"""labels.py file containing:

All variable labels (translated names of each question)
All value labels (full dictionary, ordered by variable name)
Helper functions robust to floats/ints/strings
translate() function to convert the entire dataframe
Fully sorted ascending by variable name (D01 → D22, GEN, RETA, regione, etc.)

Import it in Jupyter using:
from labels import translated_labels, variable_labels, map_codes, translate

"""

import pandas as pd


# 1. VARIABLE LABELS (question text)

variable_labels = {
    'D01': "Climate change is real",
    'D02': "Climate change is an important problem",
    'D03': "Plastic pollution is a serious problem",
    'D04': "EU SUP directive was necessary",
    'D05': "Attached-cap rule is fair/appropriate",
    'D06_1': "Drinking inconvenience due to attached cap",
    'D07': "Willingness to pay to avoid attached cap",
    'D08': "Frequency of using reusable bottle",
    'D09': "Behavioural change due to attached-cap rule",
    'D13': "Owns a plastic-free / reusable bottle",
    'D14': "Was previously an environmental association member",
    'D15': "Membership in environmental association",
    'D16': "Environmental volunteer activity",
    'D17': "Voluntary tax donation (5‰)",
    'D18': "Environmental donation willingness",
    'D19': "Voting in referendum",
    'D20': "Voting in latest elections",
    'D22': "Education level",
    'GEN': "Sex",
    'RETA': "Age group",
    'regione': "Region of residency"
}


# 2. VALUE LABELS — sorted by variable name

translated_labels = {

    # Likert-type questions: D01–D05
    'D01': {
        1.0: 'Yes',
        2.0: 'No'
    },

    'D02': {
        1.0: "Strongly agree",
        2.0: "Agree",
        3.0: "Neutral",
        4.0: "Disagree",
        5.0: "Strongly disagree"
    },

    'D03': {
        1.0: "Strongly agree",
        2.0: "Agree",
        3.0: "Neutral",
        4.0: "Disagree",
        5.0: "Strongly disagree"
    },

    'D04': {
        1.0: "Strongly agree",
        2.0: "Agree",
        3.0: "Neutral",
        4.0: "Disagree",
        5.0: "Strongly disagree"
    },

    'D05': {
        1.0: "Strongly agree",
        2.0: "Agree",
        3.0: "Neutral",
        4.0: "Disagree",
        5.0: "Strongly disagree"
    },

    'D06_1': {
        1.0: 'Very little',
        2.0: '2',
        3.0: '3',
        4.0: '4',
        5.0: 'A lot'
    },

    'D07': {
        1.0: 'Zero, I would not buy it',
        2.0: '€0.01',
        3.0: '€0.05',
        4.0: '€0.10',
        5.0: 'More than €0.10'
    },

    'D08': {
        1.0: 'Yes, often',
        2.0: 'Yes, but only when necessary',
        3.0: 'No'
    },

    'D09': {
        1.0: 'No',
        2.0: 'Yes, I buy more plastic bottles',
        3.0: 'Yes, I buy fewer plastic bottles',
        4.0: 'Yes, I try to detach the cap',
        5.0: 'Yes, other'
    },

    'D13': {
        1.0: 'Yes, and I always carry it with me',
        2.0: 'Yes, but I often forget it',
        3.0: 'Yes, but I never use it',
        4.0: 'No, but I should buy one',
        5.0: 'No'
    },

    'D14': {
        1.0: 'Yes',
        2.0: 'I was before, not anymore',
        3.0: 'No'
    },

    'D15': {
        1.0: 'Yes',
        2.0: 'I used to be, but not anymore',
        3.0: 'No'
    },

    'D16': {
        1.0: 'Yes',
        2.0: 'I was before, not anymore',
        3.0: 'No'
    },

    'D17': {
        1.0: 'Yes',
        2.0: 'Only the 5‰',
        3.0: 'No'
    },

    'D18': {
        1.0: 'Yes / I would but cannot',
        2.0: 'No'
    },

    'D19': {
        1.0: 'Yes',
        2.0: 'No',
        3.0: 'I don’t remember',
        4.0: 'Prefer not to answer'
    },

    'D20': {
        1.0: 'Yes',
        2.0: 'No',
        3.0: 'I don’t remember',
        4.0: 'Prefer not to answer'
    },

    'D22': {
        1.0: 'None',
        2.0: 'Middle school diploma',
        3.0: 'High school diploma',
        4.0: 'Bachelor’s degree',
        5.0: 'Master’s degree',
        6.0: 'PhD / Master / Doctorate'
    },

    'GEN': {
        1.0: 'Male',
        2.0: 'Female',
        3.0: 'Prefer not to answer'
    },

    'RETA': {
        1.0: '18–24',
        2.0: '25–34',
        3.0: '35–44',
        4.0: '45–54',
        5.0: '55–64',
        6.0: '65–74',
        7.0: '75–99',
        8.0: 'Screenout'
    },

    # Region names are already textual → no mapping needed
    'regione': {
        1.0: 'Piemonte',
        2.0: "Valle D'Aosta",
        3.0: 'Lombardia',
        4.0: 'Trentino Alto Adige',
        5.0: 'Veneto',
        6.0: 'Friuli Venezia Giulia',
        7.0: 'Liguria',
        8.0: 'Emilia Romagna',
        9.0: 'Toscana',
        10.0: 'Umbria',
        11.0: 'Marche',
        12.0: 'Lazio',
        13.0: 'Abruzzo',
        14.0: 'Molise',
        15.0: 'Campania',
        16.0: 'Puglia',
        17.0: 'Basilicata',
        18.0: 'Calabria',
        19.0: 'Sicilia',
        20.0: 'Sardegna'
    }
}



# 3. HELPER FUNCTIONS ROBUST TO FLOAT/INT/STRING

def map_codes(series, varname):
    """
    Safely maps numeric values to text labels,
    handling float (1.0), int (1), and str ("1").
    """
    if varname not in translated_labels:
        return series

    mapping = translated_labels[varname]

    def convert(value):
        if pd.isna(value):
            return pd.NA

        # direct match (float key support)
        if value in mapping:
            return mapping[value]

        # try integer version
        try:
            iv = int(value)
            if iv in mapping:
                return mapping[iv]
        except:
            pass

        # string-based match
        sv = str(value).strip()
        if sv in mapping:
            return mapping[sv]

        return pd.NA

    return series.apply(convert)


def translate(df):
    """
    Returns a NEW dataframe with all coded variables translated.
    """
    df2 = df.copy()
    for col in df2.columns:
        if col in translated_labels:
            df2[col] = map_codes(df2[col], col)
    return df2
