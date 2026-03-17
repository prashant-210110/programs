import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# --- Configuration ---
st.set_page_config(
    page_title="DataPulse | Analysis & Calc", 
    page_icon="📊", 
    layout="wide"
)

# Custom CSS
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stButton>button { width: 100%; border-radius: 5px; height: 3em; background-color: #ff4b4b; color: white; }
    .stSelectbox label, .stNumberInput label { font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# --- Sidebar ---
st.sidebar.title("🚀 Navigation")
menu = st.sidebar.radio(
    "Select a module:",
    ["🧮 Smart Calculator", "📈 Data Explorer & Plotter"]
)

# -------------------------
# Module 1: Calculator
# -------------------------
if menu == "🧮 Smart Calculator":
    st.title("🧮 Smart Calculator")
    st.info("Perform quick arithmetic operations below.")
    
    col1, col2 = st.columns(2)
    with col1:
        num1 = st.number_input("First Value", value=0.0, step=0.1, format="%.2f")
    with col2:
        num2 = st.number_input("Second Value", value=0.0, step=0.1, format="%.2f")

    operation = st.selectbox(
        "Operation",
        ["Add (+)", "Subtract (-)", "Multiply (×)", "Divide (÷)", "Modulus (%)", "Power (^)" ]
    )

    if st.button("Calculate Result"):
        try:
            if "Add" in operation:
                result = num1 + num2
            elif "Subtract" in operation:
                result = num1 - num2
            elif "Multiply" in operation:
                result = num1 * num2
            elif "Divide" in operation:
                if num2 == 0:
                    st.error("Division by zero is undefined.")
                    result = None
                else:
                    result = num1 / num2
            elif "Modulus" in operation:
                result = num1 % num2
            elif "Power" in operation:
                result = num1 ** num2

            if result is not None:
                st.metric(label="Result", value=f"{result:,.2f}")
        except Exception as e:
            st.error(f"An error occurred: {e}")

# -------------------------
# Module 2: File Upload & Plot
# -------------------------
elif menu == "📈 Data Explorer & Plotter":
    st.title("📂 Data Analysis Tool")
    
    uploaded_file = st.file_uploader(
        "Upload your dataset (CSV or Excel)", 
        type=["csv", "xlsx"]
    )

    if uploaded_file:
        @st.cache_data
        def load_data(file):
            if file.name.endswith(".csv"):
                return pd.read_csv(file)
            return pd.read_excel(file)

        df = load_data(uploaded_file)
        
        # --- Layout: Tabs ---
        tab1, tab2, tab3, tab4 = st.tabs(["📋 Data Preview", "📊 Visualizer", "🧮 Statistics", "🔥 Correlation Heatmap"])

        with tab1:
            st.dataframe(df, use_container_width=True)
            st.write(f"**Shape:** {df.shape[0]} rows × {df.shape[1]} columns")

        with tab3:
            st.write("### Numerical Summary")
            st.table(df.describe())

        with tab2:
            st.subheader("Configure Visualization")
            c1, c2, c3 = st.columns(3)
            
            with c1:
                x_col = st.selectbox("X-Axis", df.columns)
            with c2:
                y_col = st.selectbox("Y-Axis (Optional)", [None] + list(df.columns))
            with c3:
                plot_type = st.selectbox(
                    "Chart Type",
                    ["Line", "Scatter", "Bar", "Histogram", "Boxplot"]
                )

            with st.form("plot_form"):
                submit_plot = st.form_submit_button("Update Chart")

            if submit_plot:
                fig, ax = plt.subplots(figsize=(10, 5))
                sns.set_style("whitegrid")
                
                try:
                    if plot_type == "Line":
                        sns.lineplot(data=df, x=x_col, y=y_col, ax=ax)
                    elif plot_type == "Scatter":
                        sns.scatterplot(data=df, x=x_col, y=y_col, ax=ax)
                    elif plot_type == "Bar":
                        sns.barplot(data=df, x=x_col, y=y_col, ax=ax)
                    elif plot_type == "Histogram":
                        sns.histplot(df[x_col], kde=True, ax=ax)
                    elif plot_type == "Boxplot":
                        sns.boxplot(data=df, x=x_col, y=y_col, ax=ax)

                    plt.xticks(rotation=45)
                    st.pyplot(fig)
                except Exception as e:
                    st.error(f"Could not generate plot: {e}. Ensure selected columns are appropriate.")

        with tab4:
            st.write("### Correlation Heatmap (Numerical Features)")
            try:
                corr = df.select_dtypes(include="number").corr()
                fig, ax = plt.subplots(figsize=(8, 6))
                sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax)
                st.pyplot(fig)
            except Exception as e:
                st.error(f"Could not generate heatmap: {e}")

    else:
        st.info("👆 Please upload a file to begin your analysis.")
