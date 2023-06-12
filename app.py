# app.py
import streamlit as st

import matplotlib.pyplot as plt

import numpy as np

from scipy import signal

# 메인 제목
st.title("경기과기대 202021061 홍가영")

# 페이지 제목
st.subheader("폐루프 전달함수")

# 전달함수 계수
num = [100]
den = [1, 5, 6, 100]

# 폐루프 전달함수 계산
closed_loop_tf = signal.TransferFunction(num, den) / (1 + signal.TransferFunction(num, den))

    # 전달함수 출력
st.markdown("Closed-Loop Transfer Function:")
st.latex("T(s) = \\frac{{100}}{{(s+2)(s+3) + 100}}")
    
    # Bode plot 그리기
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6))
    
    # 게인 그래프
w, mag, phase = signal.bode(closed_loop_tf)
ax1.semilogx(w, mag)
ax1.set_ylabel('Gain (dB)')
ax1.grid(True)

    # 위상 그래프
ax2.semilogx(w, phase)
ax2.set_xlabel('Frequency (rad/s)')
ax2.set_ylabel('Phase (degrees)')
ax2.grid(True)

st.pyplot(fig)

if __name__ == '__main__':
    main()