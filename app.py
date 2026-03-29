import streamlit as st
import google.generativeai as genai

# 1. Cấu hình (Dán mã của bạn vào)
GOOGLE_API_KEY = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=GOOGLE_API_KEY)

st.title("♊ Gemini Assistant - Final Fix")

# 2. Kiểm tra danh sách model khả dụng (Để sửa lỗi 404)
available_models = []
try:
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            available_models.append(m.name.replace('models/', ''))
except Exception as e:
    st.error(f"Không thể lấy danh sách model: {e}")

# 3. Giao diện chọn model (Nếu có lỗi 404, bạn có thể chọn cái khác ở đây)
if available_models:
    selected_model = st.selectbox("Chọn Model khả dụng trên tài khoản của bạn:", available_models)
    
    user_input = st.text_input("Nhập câu hỏi:", placeholder="Ví dụ: Xin chào...")

    if st.button("Gửi"):
        try:
            with st.spinner("Đang xử lý..."):
                model = genai.GenerativeModel(selected_model)
                response = model.generate_content(user_input)
                st.success("AI trả lời:")
                st.write(response.text)
        except Exception as e:
            st.error(f"Lỗi thực thi: {e}")
else:
    st.warning("Tài khoản của bạn hiện chưa có model nào khả dụng. Hãy kiểm tra lại API Key hoặc vùng lãnh thổ (Tắt VPN).")

st.divider()
st.info("Lưu ý: Nếu danh sách Model trống, hãy thử tạo lại API Key mới tại Google AI Studio.")