# app.py
import streamlit as st
st.image("cropped_logo.png",use_container_width=True)
st.markdown("<h4 style='text-align: center;'>Cell File Generator</h4>", unsafe_allow_html=True)

# User inputs
lat = st.text_input("Enter Latitude (LAT)")

lon = st.text_input("Enter Longitude (LON)")
azi1 = st.text_input("Enter First Azimuth")
azi2 = st.text_input("Enter Second Azimuth")
azi3 = st.text_input("Enter Third Azimuth")

# Predefined values
system = "2100"
site = "KER32915"
cell_name = "1"
cell_name2 = "2"
cell_name3 = "3"
cell_id = "1"
pci = "1"
tac = "56238"
arfcn = "1357"
mcc = "404"
mnc = "43"
ant_bw = "65"

# Generate TXT file when button is clicked
if st.button("Generate Cell File"):
    header = "SYSTEM\tSITE\tLAT\tLON\tDIR\tCELL_NAME\tCELL_ID\tPCI\tTAC\tARFCN\tMCC\tMNC\tANT_BW"
    row1 = f"{system}\t{site}\t{lat}\t{lon}\t{azi1}\t{cell_name}\t{cell_id}\t{pci}\t{tac}\t{arfcn}\t{mcc}\t{mnc}\t{ant_bw}"
    row2 = f"{system}\t{site}\t{lat}\t{lon}\t{azi2}\t{cell_name2}\t{cell_id}\t{pci}\t{tac}\t{arfcn}\t{mcc}\t{mnc}\t{ant_bw}"
    row3 = f"{system}\t{site}\t{lat}\t{lon}\t{azi3}\t{cell_name3}\t{cell_id}\t{pci}\t{tac}\t{arfcn}\t{mcc}\t{mnc}\t{ant_bw}"

    output_text = header + "\n" + row1 + "\n" + row2 + "\n" + row3

    st.download_button(
        label="Download Cell file",
        data=output_text,
        file_name="SignalEdges_cell_file.txt",
        mime="text/plain"
    )
