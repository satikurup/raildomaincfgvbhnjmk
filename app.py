import streamlit as st
import cv2
import webbrowser
st.title("seat Occupancy")
if(st.button('Output')):
  cap=cv2.VideoCapture("Seat Occupancy.mp4")
  st.video("Seat Occupancy.mp4")
  cap.release()
