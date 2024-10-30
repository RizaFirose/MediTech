import streamlit as st
import qrcode
from io import BytesIO
from PIL import Image

logo = Image.open("LOGO.png")
with st.sidebar:
    col1, col2 = st.columns([1, 3])
    with col1:
        st.image(logo, width=50)  # Display the logo with specified width

    with col2:
        st.markdown("""<div style="line-height: 1; margin: 0;"><h3 style="margin: 0; padding: 0;">MediTech</h3>
                       <p style="margin: 0; padding: 0; font-size: 12px; color: #777;">Save Lives. Cherish Moments.</p>
                    </div>""", unsafe_allow_html=True)

st.sidebar.subheader("Welcome to MediTech's portal!")
ch = st.sidebar.radio('', ['Personal', 'Contact', 'Medical', 'MediTech SafeScan'])
st.title('Hello Dear User \U0001F642')

# Initialize session state variables
if 'name' not in st.session_state:
    st.session_state.name = ""
if 'age' not in st.session_state:
    st.session_state.age = 1
if 'DOB' not in st.session_state:
    st.session_state.DOB = ""
if 'blood' not in st.session_state:
    st.session_state.blood = ""
if 'gender' not in st.session_state:
    st.session_state.gender = ""
if 'insurance' not in st.session_state:
    st.session_state.insurance = ""
if 'cn' not in st.session_state:
    st.session_state.cn = ""
if 'address' not in st.session_state:
    st.session_state.address = ""
if 'en1' not in st.session_state:
    st.session_state.en1 = ""
if 'enn1' not in st.session_state:
    st.session_state.enn1 = ""
if 'enr1' not in st.session_state:
    st.session_state.enr1 = ""
if 'en2' not in st.session_state:
    st.session_state.en2 = ""
if 'enn2' not in st.session_state:
    st.session_state.enn2 = ""
if 'enr2' not in st.session_state:
    st.session_state.enr2 = ""
if 'medical' not in st.session_state:
    st.session_state.medical = ""
if 'medicine' not in st.session_state:
    st.session_state.medicine = ""
if 'famhis' not in st.session_state:
    st.session_state.famhis = ""
if 'allergies' not in st.session_state:
    st.session_state.allergies = ""
if 'consent' not in st.session_state:
    st.session_state.consent = False

# Define sections
if ch == 'Personal':
    st.session_state.name = st.text_input('Full name', value=st.session_state.name)
    st.session_state.age = st.number_input('Age', min_value=1, step=1, value=st.session_state.age)
    st.session_state.DOB = st.text_input("DOB (DD-MM-YYYY)", value=st.session_state.DOB)
    st.session_state.blood = st.text_input('Blood Group', value=st.session_state.blood)
    default_gender = "Female" if st.session_state.gender == "" else st.session_state.gender
    st.session_state.gender = st.selectbox("Gender", ("Male", "Female"),
        index=("Male", "Female").index(default_gender) if default_gender in ("Male", "Female") else 0)
    st.session_state.insurance = st.text_input('Insurance number', value=st.session_state.insurance)

elif ch == 'Contact':
    st.session_state.cn = st.text_input('Your contact number', value=st.session_state.cn)
    st.session_state.address = st.text_area('Address', value=st.session_state.address)
    st.session_state.en1 = st.text_input('Family contact number 1', value=st.session_state.en1)
    st.session_state.enn1 = st.text_input('Name of the contact person', value=st.session_state.enn1)
    st.session_state.enr1 = st.text_input('Relation to the person', value=st.session_state.enr1)
    st.session_state.en2 = st.text_input('Family contact number 2', value=st.session_state.en2)
    st.session_state.enn2 = st.text_input('Name of the second contact person', value=st.session_state.enn2)
    st.session_state.enr2 = st.text_input('Relation to the second person', value=st.session_state.enr2)

elif ch == 'Medical':
    st.session_state.allergies = st.text_area('Any allergies', value=st.session_state.allergies)
    st.session_state.medical = st.text_area("Past medical history", value=st.session_state.medical)
    st.session_state.medicine = st.text_area('Current medications', value=st.session_state.medicine)
    st.session_state.famhis = st.text_area('Family medical history', value=st.session_state.famhis)
    st.session_state.consent = st.checkbox('*Consent to release your medical information to relevant healthcare providers',
        value=st.session_state.consent)

# Health risk assessment conditions
condition_risks_and_prevention = {
    "hypertension": {
        "risk": "You are prone to heart disease, stroke, and kidney problems.",
        "prevention": "Control blood pressure with regular check-ups, exercise, reduce salt intake, and take prescribed medications."
    },
    "diabetes": {
        "risk": "You may face risks such as cardiovascular disease, neuropathy, and kidney damage.",
        "prevention": "Monitor blood sugar, maintain a healthy diet, exercise regularly, and follow medication guidelines."
    },
    "asthma": {
        "risk": "You are at risk of respiratory complications, especially in polluted areas.",
        "prevention": "Avoid allergens, use prescribed inhalers, and manage stress to reduce asthma attacks."
    },
    "heart disease": {
        "risk": "You are prone to heart attacks, heart failure, and stroke.",
        "prevention": "Maintain a heart-healthy diet, stay active, avoid smoking, and take prescribed medications."
    },
    "arthritis": {
        "risk": "You could suffer from joint pain and mobility loss over time.",
        "prevention": "Stay active, manage weight, and take anti-inflammatory medications as prescribed."
    },
    "obesity": {
        "risk": "You are at higher risk for diabetes, hypertension, and heart disease.",
        "prevention": "Engage in regular physical activity, adopt a balanced diet, and consult a healthcare provider for weight management."
    }}

def assess_specific_health_risks(medical_history, medications, family_history):
    detected_risks = []

    for condition, details in condition_risks_and_prevention.items():
        if condition.lower() in medical_history.lower() or condition.lower() in medications.lower():
            risk_message = f"{condition.capitalize()}: {details['risk']}"
            prevention_message = f"Prevention: {details['prevention']}"
            detected_risks.append(f"{risk_message}\n{prevention_message}")
        elif condition.lower() in family_history.lower():
            risk_message = f"Genetic Predisposition to {condition.capitalize()}: You have a family history of {condition}. You might be at risk."
            prevention_message = f"Prevention: {details['prevention']} Regular check-ups are recommended due to family history."
            detected_risks.append(f"{risk_message}\n{prevention_message}")

    if not detected_risks:
        return "No significant risks detected from your medical or family history at this time. Keep maintaining a healthy lifestyle!"
    else:
        return '\n\n'.join(detected_risks)

# Button 1: Show AI-based health risk based on the inputs
if ch == 'Medical':
    st.markdown("""<style>div.stButton > button:first-child {background-color: #FF6347;
                color: white;border-radius: 8px;font-weight: bold;font-size: 16px;
                padding: 10px 24px;width: 100%;}</style>""", unsafe_allow_html=True)

    if st.button('Show AI-Based Health Risk '):
        with st.expander("Health Risk Assessment Results", expanded=True):
            health_risk = assess_specific_health_risks(st.session_state.medical, st.session_state.medicine, st.session_state.famhis)
            # Add structured and formatted text output
            st.markdown("<div style='background-color:#FFF5F5; padding:15px; border-radius:10px;'>", unsafe_allow_html=True)
            st.subheader('AI-Based Health Risk Assessment:')
            st.markdown(f"<p style='font-size:16px;'>{health_risk.replace('\n', '<br>')}</p>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)

elif ch == 'MediTech SafeScan':
    pw = st.text_input('Enter The Password Given', type='password')
    if st.button('Generate QR Code'):
        if not st.session_state.consent:
            st.error("You must consent to release your medical information.")
        else:
            combined_input = (
                f"Name: {st.session_state.name}\n"
                f"Age: {st.session_state.age}\n"
                f"DOB: {st.session_state.DOB}\n"
                f"Blood Group: {st.session_state.blood}\n"
                f"Gender: {st.session_state.gender}\n"
                f"Insurance Number: {st.session_state.insurance}\n"
                f"Contact Number: {st.session_state.cn}\n"
                f"Address: {st.session_state.address}\n"
                f"Emergency Contact 1: {st.session_state.en1}, Name: {st.session_state.enn1}, Relation: {st.session_state.enr1}\n"
                f"Emergency Contact 2: {st.session_state.en2}, Name: {st.session_state.enn2}, Relation: {st.session_state.enr2}\n"
                f"Allergies: {st.session_state.allergies}\n"
                f"Past Medical History: {st.session_state.medical}\n"
                f"Current Medications: {st.session_state.medicine}\n"
                f"Family Medical History: {st.session_state.famhis}\n")

            gw = 'tech2024'
            if pw == gw:
                qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10,
                                   border=4, )
                qr.add_data(combined_input)
                qr.make(fit=True)

                img = qr.make_image(fill='black', back_color='white')
                img_byte_arr = BytesIO()
                img.save(img_byte_arr, format='PNG')
                img_byte_arr = img_byte_arr.getvalue()

                st.image(img_byte_arr)

                st.download_button(label="Download QR Code", data=img_byte_arr, file_name="qrcode.png",
                                   mime="image/png")