import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# Page config
# -----------------------------
st.set_page_config(
    page_title="Neuro AI Experiments",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 Neuro AI Experiments")
st.subheader("Interactive Cognitive Load Signal Explorer")

st.markdown("""
This mini dashboard explores simulated EEG-like signals across different cognitive load levels.

**Labels**
- 0 = Low cognitive load
- 1 = Medium cognitive load
- 2 = High cognitive load
""")

# -----------------------------
# Generate synthetic dataset
# -----------------------------
np.random.seed(42)

samples_per_class = 100
features = 10

low_load = np.random.normal(loc=0.2, scale=0.1, size=(samples_per_class, features))
medium_load = np.random.normal(loc=0.5, scale=0.1, size=(samples_per_class, features))
high_load = np.random.normal(loc=0.8, scale=0.1, size=(samples_per_class, features))

X = np.vstack([low_load, medium_load, high_load])
y = np.array([0] * samples_per_class + [1] * samples_per_class + [2] * samples_per_class)

feature_names = [f"signal_{i+1}" for i in range(features)]

df = pd.DataFrame(X, columns=feature_names)
df["cognitive_load"] = y

# -----------------------------
# Sidebar controls
# -----------------------------
st.sidebar.header("Controls")

selected_label = st.sidebar.selectbox(
    "Select cognitive load level",
    options=[0, 1, 2],
    format_func=lambda x: {
        0: "Low Load",
        1: "Medium Load",
        2: "High Load"
    }[x]
)

filtered_df = df[df["cognitive_load"] == selected_label].reset_index(drop=True)

sample_index = st.sidebar.slider(
    "Select sample index",
    min_value=0,
    max_value=len(filtered_df) - 1,
    value=0
)

sample = filtered_df.loc[sample_index, feature_names]

# -----------------------------
# Layout
# -----------------------------
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("## Signal Visualization")

    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(feature_names, sample.values, marker="o")
    ax.set_title("Simulated EEG-like Signal")
    ax.set_xlabel("Signal Feature")
    ax.set_ylabel("Signal Value")
    ax.grid(True, alpha=0.3)
    plt.xticks(rotation=45)

    st.pyplot(fig)

with col2:
    st.markdown("## Sample Details")
    st.write("**Selected class:**", selected_label)
    st.write("**Sample index:**", sample_index)

    st.markdown("### Signal Values")
    st.dataframe(sample.to_frame(name="value"))

# -----------------------------
# Mean pattern by class
# -----------------------------
st.markdown("## Average Signal Pattern by Cognitive Load")

fig2, ax2 = plt.subplots(figsize=(10, 5))

for label, name in zip([0, 1, 2], ["Low Load", "Medium Load", "High Load"]):
    class_mean = df[df["cognitive_load"] == label][feature_names].mean()
    ax2.plot(feature_names, class_mean.values, marker="o", label=name)

ax2.set_title("Average Signal Pattern by Cognitive Load")
ax2.set_xlabel("Signal Feature")
ax2.set_ylabel("Average Signal Value")
ax2.legend()
ax2.grid(True, alpha=0.3)
plt.xticks(rotation=45)

st.pyplot(fig2)

# -----------------------------
# Dataset preview
# -----------------------------
st.markdown("## Dataset Preview")
st.dataframe(df.head(10))
