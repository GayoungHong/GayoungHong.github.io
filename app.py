
# app.py
import numpy as np

import matplotlib.pyplot as plt

import control

import streamlit as st

from scipy import signal

# 메인 제목
st.title("경기과기대 202021061 홍가영")

# 페이지 제목
st.subheader("폐루프 전달함수")

# 전달함수
st.text("Gs=100/(s+2)(s+3)")



def main():
    
    # 전달함수 계수
    num = np.array([100])
    den = np.array([1, 5, 6])
    
    tf = control.tf(num,den)
    
    closed_tf = control.feedback(tf ,1)
    
    # 전달함수 출력
    print(closed_tf)
    
    
    closed_num, closed_den = control.tfdata(closed_tf)
    print(closed_num)
    print(closed_den)
    
    closed_num = np.array(closed_num)[0,0,:]
    closed_den = np.array(closed_den)[0,0,:]
    
    print(closed_num)
    print(closed_den)
    
    
    
    
    # 시스템 응답
    t, y = signal.step(signal.TransferFunction(closed_num, closed_den))
    
    # Bode plot 그리기
    
     # 응답곡선 그리기
    fig1 = plt.figure()
    plt.plot(t, y)
    plt.xlabel('Time')
    plt.ylabel('Output')
    plt.title('Step Response')
    plt.grid(True)
    st.pyplot(fig1)
    
    # 주파수 응답
    w, mag, phase = signal.bode(signal.TransferFunction(closed_num, closed_den))

    # Bode plot 그리기
    fig2 = plt.figure()
    plt.semilogx(w, mag)
    plt.ylabel('Gain (dB)')
    plt.title('Bode Plot (Gain)')
    plt.grid(True)
    st.pyplot(fig2)
    
    fig3 = plt.figure()
    plt.semilogx(w, phase)
    plt.xlabel('Frequency (rad/s)')
    plt.ylabel('Phase (degrees)')
    plt.title('Bode Plot (Phase)')
    plt.grid(True)
    st.pyplot(fig3)

if __name__ == '__main__':
    main()