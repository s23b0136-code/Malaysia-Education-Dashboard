import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Institutional Density & Hierarchy", page_icon="🏫", layout="wide")

st.title("🏫 Objective 2: Spatial Density & Sector Reliance Hierarchy")
st.markdown("Mapping the spatial density of educational institutions and evaluating public versus private sector reliance across municipal areas and school levels.")

@st.cache_data
def load_data():
    df = pd.read_excel("dataset_schools_cleaned (1)_2.xlsx", sheet_name="Sheet1")
    return df

try:
    df = load_data()
    
    st.sidebar.header("🔍 Filter Parameters")
    areas = sorted(df['Area'].dropna().unique())
    selected_area = st.sidebar.selectbox("Select Municipality / Area", ["All Areas"] + list(areas))
    
    sub_df = df if selected_area == "All Areas" else df[df['Area'] == selected_area]
    
    st.subheader(f"Institutional Overview: {selected_area}")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### Public vs. Private Sector Reliance")
        status_counts = sub_df['Status'].value_counts().reset_index()
        status_counts.columns = ['Status', 'Count']
        
        # Visualisation: Donut Chart
        fig_status = px.pie(
            status_counts,
            names='Status',
            values='Count',
            hole=0.5,
            template='plotly_dark',
            title="Sector Breakdown (Public vs. Private)"
        )
        st.plotly_chart(fig_status, use_container_width=True)
        
    with col2:
        st.markdown("#### School Level Distribution")
        level_counts = sub_df['Level'].value_counts().reset_index()
        level_counts.columns = ['Level', 'Count']
        
        # Visualisation: Donut Chart
        fig_level = px.pie(
            level_counts,
            names='Level',
            values='Count',
            hole=0.5,
            template='plotly_dark',
            title="Educational Levels Breakdown"
        )
        st.plotly_chart(fig_level, use_container_width=True)
        
    st.markdown("---")
    st.markdown("### 🌐 Donut Chart Hierarchy (Sunburst Mapping)")
    
    # Visualisation: Donut Chart Hierarchy
    fig_sunburst = px.sunburst(
        sub_df,
        path=['Level', 'Status', 'Area'],
        template='plotly_dark',
        title="Hierarchical Sector & Level Density (Level ➔ Sector ➔ Area)"
    )
    st.plotly_chart(fig_sunburst, use_container_width=True)

except Exception as e:
    st.error(f"Error loading dataset: {e}")
