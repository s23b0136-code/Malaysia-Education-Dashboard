import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="School Completion Trends", page_icon="📈", layout="wide")

st.title("📈 Objective 1: District-Level School Completion Trends & Retention Drop-Offs")
st.markdown("Evaluating completion rates and pinpointing retention drop-off points as students transition from primary to upper secondary education.")

@st.cache_data
def load_data():
    df = pd.read_excel("completion_school_district_cleaned_final_2.xls", sheet_name=0)
    return df

try:
    df = load_data()
    
    st.sidebar.header("🔍 Filter Parameters")
    states = sorted(df['state'].dropna().unique())
    selected_state = st.sidebar.selectbox("Select State", states)
    
    filtered_df = df[(df['state'] == selected_state) & (df['is_state_total'] == 0)]
    
    if filtered_df.empty:
        st.warning("No district-level data available for the selected state.")
    else:
        st.subheader(f"Educational Stage Completion Breakdown: {selected_state}")
        
        agg_df = filtered_df.groupby(['district', 'stage'])['completion'].mean().reset_index()
        pivot_display = agg_df.pivot(index='district', columns='stage', values='completion').reset_index()
        pivot_display.columns.name = None
        
        st.dataframe(pivot_display.style.format(precision=2), use_container_width=True)
        
        # Visualisation: BAR GRAPH
        fig = px.bar(
            agg_df,
            x='district',
            y='completion',
            color='stage',
            barmode='group',
            title=f"District Completion Rates Across Educational Stages ({selected_state})",
            labels={'district': 'District', 'completion': 'Completion Rate (%)', 'stage': 'Educational Stage'},
            template='plotly_dark',
            height=520
        )
        fig.update_layout(xaxis={'categoryorder':'total descending'}, xaxis_tickangle=-45)
        st.plotly_chart(fig, use_container_width=True)
        
        st.markdown("### 💡 Retention Drop-Off Analysis")
        st.write(
            "Comparing primary completion rates against upper secondary completion across municipal districts "
            "highlights vulnerable drop-off points requiring targeted educational intervention."
        )

except Exception as e:
    st.error(f"Error loading dataset: {e}")
