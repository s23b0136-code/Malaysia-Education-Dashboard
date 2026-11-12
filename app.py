import streamlit as st

st.set_page_config(
    page_title="Malaysia Educational Analytics Portal",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown(
    """
    <div style='background-color: #0e1117; padding: 2.5rem; border-radius: 12px; border: 1px solid #303545;'>
        <h1 style='color: #ffffff; text-align: center; margin-bottom: 0.5ynth;'>🇲🇾 Malaysian Educational Analytics & GIS Portal</h1>
        <p style='text-align: center; color: #a3a8b8; font-size: 1.15rem;'>
            An enterprise-grade intelligence platform evaluating school completion trends, institutional density, 
            and psychological attributes impacting student academic test performance.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

st.write("")
st.write("")

col_m1, col_m2, col_m3 = st.columns(3)
with col_m1:
    st.metric(label="📊 Objective 1", value="School Completion", delta="Bar Graph Analysis")
with col_m2:
    st.metric(label="🏫 Objective 2", value="Institutional Density", delta="Donut Hierarchy")
with col_m3:
    st.metric(label="🧠 Objective 3", value="Psychology & Marks", delta="Scatter Correlation")

st.markdown("---")
st.markdown("### 🧭 Core Analytical Objectives")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("#### 📈 1. Completion & Drop-offs")
    st.write("Evaluate district-level school completion trends across Malaysia and pinpoint retention drop-off points from primary to upper secondary education.")

with col2:
    st.markdown("#### 🏫 2. Spatial Density & Hierarchy")
    st.write("Map institutional spatial density and evaluate public versus private sector reliance across municipal areas and school levels.")

with col3:
    st.markdown("#### 🧠 3. Psychology vs. Performance")
    st.write("Determine statistical correlations between psychological attributes (Mindset, Positive view) and individual student test marks.")

st.markdown("---")
st.info("👈 **Getting Started:** Use the sidebar navigation menu on the left to explore each objective page.")
