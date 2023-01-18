import streamlit as st
import pandas as pd


st.title("การไฟฟ้าส่วนภูมิภาคอำเภอแกลง 12/12 หมู่ 12 ตำบลทุ่งควายกิน อำเภอแกลง จังหวัดระยอง 21110")
st.write("GECC 2566")


st.markdown("## Technology Sectors")
st.markdown("## GECC 2566 ด้านเทคโนโลยี")

code = '''
แผนกบริการลูกค้า โทร 038-672685
แผนกบัญชีประมวลผล โทร 038-671780
แผนกก่อสร้าง โทร 038-671155
แผนกปฏิบัติการ โทร 038-672682-3
แผนกมิเตอร์ โทร 038-672684
แผนกคลังพัสดุ โทร 038-672437
แผนกบริหาร โทร 038-671155
    '''

show_btn = st.button("เบอร์โทรติดต่อ/Contact!")
if show_btn:
    st.code(code, language = 'python')

cols = st.columns(2)
with cols[0]:
    หมายเลขมิเตอร์_Pea_num = st.number_input("ใส่หมายเลขมิเตอร์")
    st.markdown(f"หมายเลขมิเตอร์ของคุณคือ {หมายเลขมิเตอร์_Pea_num}") 

#st.markdown("# NLP Task")

with cols[1]:
    text_inp = st.text_input("Input your Name")
    word_tokenize = "|".join(text_inp.split()) 
    st.markdown(f"{word_tokenize}")



df = pd.DataFrame({
    'First column' : [1, 2, 3, 4],
    'Second column' : [10, 20, 60, 80]
})
st.dataframe(df)

show_chart_btn = st.button("Show chart!!!")
if show_chart_btn:
    st.line_chart(df, x = 'First column', y = 'Second column')

