import streamlit as st
import pickle

# -----------------------------
# Page Styling
# -----------------------------
st.markdown("""
    <style>
        /* Background color */
        .stApp {
            background-color: #E3F2FD; /* light blue background */
        }

        /* Center and style title */
        .center-title {
            text-align: center;
            font-size: 36px;
            color: #0D47A1; /* deep blue */
            font-weight: bold;
        }

        /* Subheaders and prediction text */
        .prediction {
            text-align: center;
            font-size: 22px;
            color: #1B5E20; /* green for success */
        }
    </style>
""", unsafe_allow_html=True)

# -----------------------------
# Input functions
# -----------------------------
def get_pelvic_tilt():
    return st.text_input("Pelvic Tilt (numeric)")

def get_sacral_slope():
    return st.text_input("Sacral Slope (numeric)")

def get_degree_spondylolisthesis():
    return st.text_input("Degree of Spondylolisthesis (numeric)")


# -----------------------------
# Prediction function
# -----------------------------
def predict_species(PT, SS, DS):
    try:
        loaded_model = pickle.load(open(r"C:\Users\KAILAASH\Downloads\logistic_model_Orthopedic (1).pkl", 'rb'))
        new_data = [[float(PT), float(SS), float(DS)]]
        prediction = loaded_model.predict(new_data)[0]

        # Class labels
        class_labels = {
            1: "Normal",
            0: "Disc Hernia",
            2: "Spondylolisthesis"
        }

        predicted_label = class_labels.get(prediction, "Unknown")

        st.markdown(f"<h3 class='prediction'>🧠 Predicted Class: {predicted_label}</h3>", unsafe_allow_html=True)
        st.write(f"Model raw output: {prediction}")

    except Exception as e:
        st.error(f"Error during prediction: {e}")


# -----------------------------
# Main App
# -----------------------------
if __name__ == "__main__":
    st.markdown("<h1 class='center-title'>🩺 Orthopedic Spinal Disease Classification</h1>", unsafe_allow_html=True)

    st.image(
        r"C:\Users\KAILAASH\Desktop\M.S1ST SEM\BSS\12 Orthopedic patients - Biomechanical Analysis\disc herination.jpeg",
        caption="Spinal Posture Analysis",use_container_width=True)

    st.write("""
    ### About
    This app predicts whether a patient's spinal condition is **Normal**, **Disc Hernia**, or **Spondylolisthesis**
    based on biomechanical parameters using a **Logistic Regression** model.
    """)

    pelvic_tilt = get_pelvic_tilt()
    sacral_slope = get_sacral_slope()
    degree_spondylolisthesis = get_degree_spondylolisthesis()

    if st.button("Predict"):
        predict_species(pelvic_tilt, sacral_slope, degree_spondylolisthesis)
