import streamlit as st

st.set_page_config(page_title=  "هژمارکنا کەلوپەلان" , page_icon="📦",
                   layout="centered" )
st.title("هژمارکرنا تێجویا گەهاندنێ")

method=st.selectbox("رێکا گەهاندنێ دیار بکە",
["دەریا (باخیرە)","ئاسمان (فروکە)"])

st.divider()

st.subheader("دياركرنا رەهەندان")
length= st.number_input("درێژی")
width= st.number_input("پانی")
height= st.number_input("بلندی")

if length and width and height :

    cbm=(length*width*height)/1000000

    st.success(f"CBM (cubic meter ) = {cbm:.4f}")

    quantity=st.number_input("چەند دانە تە دڤێن" , min_value=1)

    subtotal= cbm*quantity

    st.write(f"total CBM = {subtotal:.4f}")

    price_per_cbm = 150

    total= price_per_cbm*subtotal

    st.divider()

    st.subheader("کوی گشتی")

    st.success("کوی گشتی")


    st.success(f"کوی گشتی=${total}")