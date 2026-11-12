import streamlit as st
import pandas as pd
import plotly.express as px
import scipy.stats as stats

st.set_page_config(page_title="Psychology & Academic Performance", page_icon="🧠", layout="wide")

st.title("🧠 Objective 3: Psychological Attributes vs. Student Academic Test Scores")
st.markdown("Determining statistical correlations between psychological attributes (Mindset, Positive view) and individual student test marks.")

@st.cache_data
def load_data():
    df = pd.read_excel("pilot_questionnaire_cleaned (1)_2.xlsx", sheet_name="Cleaned_Data")
    return df

try:
    df = load_data()
    df.columns = [c.strip() for c in df.columns]
    
    st.sidebar.header("🔍 Analysis Controls")
    attr = st.sidebar.selectbox("Select Psychological Attribute", ["Positive view", "Mindset"])
    
    st.subheader(f"Statistical Correlation: {attr} vs. Test Mark")
    
    valid_data = df[['TEST MARK', attr]].dropna()
    corr, p_value = stats.pearsonr(valid_data[attr], valid_data['TEST MARK'])
    
    col_m1, col_m2 = st.columns(2)
    with col_m1:
        st.metric(label="Pearson Correlation Coefficient (r)", value=f"{corr:.3f}")
    with col_m2:
        st.metric(label="Statistical Significance (p-value)", value=f"{p_value:.4f}")
        
    # Visualisation: Scatter Plot with Regression Trendline
    fig_scatter = px.scatter(
        df,
        x=attr,
        y='TEST MARK',
        trendline="ols",
        template='plotly_dark',
        title=f"Scatter Plot & Regression Trend: {attr} vs. Test Mark",
        labels={attr: attr, 'TEST MARK': 'Test Mark'},
        hover_data=['Respondent_ID'] if 'Respondent_ID' in df.columns else None,
        height=550
    )
    st.plotly_chart(fig_scatter, use_container_width=True)
    
    st.markdown("### 📋 Sample Respondent Data Preview")
    st.dataframe(df[['Respondent_ID', 'Positive view', 'Mindset', 'TEST MARK']].head(10), use_container_width=True)

except Exception as e:
    st.error(f"Error loading dataset: {e}")
