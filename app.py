
import streamlit as st
import datetime
import urllib.parse

# Page Config
st.set_page_config(
    page_title="รายงาน ปะฉะดะ",
    page_icon="👮‍♂️",
    layout="centered"
)

# Custom CSS for "Cyber" UI
st.markdown("""
<style>
    /* Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Sarabun:wght@300;400;700&family=Orbitron:wght@500;700&display=swap');
    
    /* Global Styles */
    .stApp {
        background-color: #050510;
        background-image: 
            radial-gradient(circle at 10% 20%, rgba(0, 242, 255, 0.1) 0%, transparent 20%),
            radial-gradient(circle at 90% 80%, rgba(255, 0, 255, 0.1) 0%, transparent 20%);
        font-family: 'Sarabun', sans-serif;
    }
    
    h1, h2, h3, h4, h5, h6 {
        color: #e0e0e0 !important;
        font-family: 'Orbitron', sans-serif; /* Cyber font for headers */
        letter-spacing: 1px;
    }
    
    p, label, .stMarkdown, .stRadio label {
        color: #b0b0b0 !important;
    }
    
    /* Header Box - Cyber Style */
    .header-box {
        background: linear-gradient(90deg, rgba(0,20,40,0.95) 0%, rgba(0,0,0,0.95) 100%);
        border: 1px solid #00f2ff;
        box-shadow: 0 0 20px rgba(0, 242, 255, 0.2);
        padding: 30px;
        border-radius: 10px;
        text-align: center;
        margin-bottom: 25px;
        position: relative;
        overflow: hidden;
    }
    
    .header-box::before {
        content: "";
        position: absolute;
        top: 0; left: 0; width: 100%; height: 2px;
        background: linear-gradient(90deg, transparent, #00f2ff, transparent);
        animation: scanline 3s infinite linear;
    }
    
    @keyframes scanline {
        0% { transform: translateX(-100%); }
        100% { transform: translateX(100%); }
    }
    
    .header-box h1 {
        text-shadow: 0 0 10px rgba(0, 242, 255, 0.8);
    }
    
    /* Containers */
    div[data-testid="stVerticalBlock"] > div[style*="flex-direction: column;"] > div[data-testid="stStack"] {
        background: rgba(20, 25, 40, 0.7); # Dark blue tint
        border: 1px solid rgba(0, 242, 255, 0.3); # Cyan border
        border-radius: 10px;
        padding: 20px;
        backdrop-filter: blur(10px);
        box-shadow: 0 4px 6px rgba(0,0,0,0.3);
    }
    
    /* Inputs */
    .stSelectbox div[data-baseweb="select"] > div, .stTextInput input, .stDateInput input, .stNumberInput input, .stTimeInput input {
        background-color: #1a1f2e !important;
        color: #00f2ff !important; /* Cyan text */
        border: 1px solid #334155 !important;
        border-radius: 5px;
    }
    
    /* Buttons */
    .stButton>button {
        background: linear-gradient(45deg, #00dbde 0%, #fc00ff 100%); /* Cyan-Pink Gradient */
        color: white !important;
        border: none;
        border-radius: 5px;
        font-family: 'Orbitron', sans-serif;
        text-transform: uppercase;
        letter-spacing: 1px;
        transition: all 0.3s;
        box-shadow: 0 0 10px rgba(0, 219, 222, 0.5);
    }
    
    .stButton>button:hover {
        transform: scale(1.02);
        box-shadow: 0 0 20px rgba(252, 0, 255, 0.7);
    }
    
    /* Text Area */
    .stTextArea textarea {
        background-color: #0a0e17 !important;
        color: #00ff00 !important; /* Matrix Green text */
        border: 1px solid #333 !important;
        font-family: monospace;
    }
    
    /* Footer */
    .footer-text {
        text-align: center;
        color: #555;
        font-size: 0.8rem;
        margin-top: 30px;
        font-family: 'Orbitron', sans-serif;
    }

    /* Radio Button as Cards */
    div[role="radiogroup"] {
        display: flex;
        flex-direction: column; /* Vertical Stack */
        gap: 10px;
        justify-content: center;
        margin-bottom: 20px;
    }
    div[role="radiogroup"] label > div:first-child {
        display: none; /* Hide radio circle */
    }
    div[role="radiogroup"] label {
        background-color: #1a1f2e;
        border: 2px solid #00f2ff; /* Cyan Border */
        border-radius: 10px;
        padding: 15px 10px;
        text-align: center;
        cursor: pointer;
        transition: all 0.3s ease;
        width: 100%; /* Full Width */
        display: flex;
        justify-content: center;
        align-items: center;
    }
    div[role="radiogroup"] label:hover {
        border-color: #fc00ff; /* Pink Hover */
        box-shadow: 0 0 10px rgba(252, 0, 255, 0.3);
    }
    div[role="radiogroup"] label[data-checked="true"] {
        background: linear-gradient(135deg, #00dbde 0%, #fc00ff 100%); /* Cyan-Pink Gradient */
        border-color: #ffffff;
        color: white !important;
        font-weight: bold;
        box-shadow: 0 0 20px rgba(0, 219, 222, 0.6);
        transform: scale(1.02);
    }
    div[role="radiogroup"] label[data-checked="true"] p {
        color: white !important;
        font-size: 1.1rem;
        text-shadow: 0 0 8px rgba(255, 255, 255, 0.8);
    }
    div[role="radiogroup"] label p {
        font-size: 1rem;
        font-family: 'Orbitron', sans-serif;
        letter-spacing: 1px;
        margin: 0;
        text-shadow: 0 0 5px rgba(0, 242, 255, 0.6);
    }

</style>
""", unsafe_allow_html=True)

# --- Header ---
st.markdown("""
    <div class="header-box">
        <h1>👮‍♂️ รายงาน ปะฉะดะ</h1>
        <p>สภ.หนองหญ้าไซ ภ.จว.สุพรรณบุรี</p>
    </div>
""", unsafe_allow_html=True)

# Report Type Toggle
report_type = st.radio("เลือกประเภทรายงาน", ["🚀 1. ปล่อยแถว (ก่อนปฏิบัติ)", "📊 2. ผลการปฏิบัติ (หลังภารกิจ)"], horizontal=False)

# --- Common Inputs ---
with st.container(border=True):
    st.markdown("### 👮‍♂️ ข้อมูลเจ้าหน้าที่")
    
    commanders_list = [
        {"label": "พ.ต.ท.สมชาย ธัญญเจริญ (รอง ผกก.ป.)", "value": "พ.ต.ท.สมชาย ธัญญเจริญ\nรอง ผกก.ป.สภ.หนองหญ้าไซ"},
        {"label": "พ.ต.ท.พุทธิชาติ บรรสุทธิ (รอง ผกก.สส.)", "value": "พ.ต.ท.พุทธิชาติ บรรสุทธิ\nรอง ผกก.สส.สภ.หนองหญ้าไซ"},
        {"label": "พ.ต.ท.พงษ์ศธร กิ่มเพ็ชร (รอง ผกก.สอบสวน)", "value": "พ.ต.ท.พงษ์ศธร กิ่มเพ็ชร\nรอง ผกก.(สอบสวน)"},
        {"label": "พ.ต.ท.บุญถิ่น พุ่มอ่ำ (สวป.)", "value": "พ.ต.ท.บุญถิ่น พุ่มอ่ำ\nสวป.สภ.หนองหญ้าไซ"},
        {"label": "พ.ต.ท.เฉลิมศักดิ์ ประเมนาโพธิ์ (สว.สส.)", "value": "พ.ต.ท.เฉลิมศักดิ์ ประเมนาโพธิ์\nสว.สส.สภ.หนองหญ้าไซ"}
    ]
    
    selected_commanders = st.multiselect(
        "ผู้บังคับบัญชา (เลือก 1-2 ท่าน)",
        options=commanders_list,
        default=[commanders_list[0], commanders_list[3]],
        format_func=lambda x: x['label']
    )
    
    # Duty Officer 20 Options
    officer_20_options = [
        {"label": "ร.ต.ต.อำนาจ ขันทสิกรรม (รอง สว(จร.)สภ.หนองหญ้าไซ)", "value": "ร.ต.ต.อำนาจ ขันทสิกรรม\nรอง สว(จร.)สภ.หนองหญ้าไซ"},
        {"label": "ร.ต.ต.ไกรวุฒิ นามวาท (รอง สว(ป.)สภ.หนองหญ้าไซ)", "value": "ร.ต.ต.ไกรวุฒิ นามวาท\nรอง สว(ป.)สภ.หนองหญ้าไซ"},
        {"label": "ร.ต.ต.ทองหล่อ ทองมาก (รอง สว(ป.)สภ.หนองหญ้าไซ)", "value": "ร.ต.ต.ทองหล่อ ทองมาก\nรอง สว(ป.)สภ.หนองหญ้าไซ"}
    ]
    
    selected_leader_opt = st.selectbox(
        "ร้อยเวร 20",
        options=officer_20_options + [{"label": "✏️ ระบุเอง...", "value": "custom"}],
        format_func=lambda x: x['label'],
        index=2
    )
    
    if selected_leader_opt['value'] == "custom":
        c_custom1, c_custom2 = st.columns(2)
        custom_name = c_custom1.text_input("ระบุชื่อ ร้อยเวร 20", "")
        custom_pos = c_custom2.text_input("ระบุตำแหน่ง", "รอง สว(ป.)สภ.หนองหญ้าไซ")
        leader = f"{custom_name}\n{custom_pos}"
    else:
        leader = selected_leader_opt['value']

# --- Specific Inputs ---
if "ปล่อยแถว" in report_type:
    with st.container(border=True):
        st.markdown("### 🕒 เวลาและสถานที่ (ปล่อยแถว)")
        c1, c2 = st.columns(2)
        r_date = c1.date_input("วันที่", datetime.date.today())
        r_time = c2.time_input("เวลา", datetime.time(19, 0))
        
        location_options = [
            "บริเวณ แยกหอนาฬิกา",
            "ปั้ม ปตท.",
            "แยกไทรแก้ว",
            "หน้า ธกส"
        ]
        
        selected_loc_opt = st.selectbox(
            "สถานที่ปล่อยแถว",
            options=location_options + ["✏️ ระบุเอง..."]
        )
        
        if selected_loc_opt == "✏️ ระบุเอง...":
            location = st.text_input("ระบุสถานที่ปล่อยแถว", "")
        else:
            location = selected_loc_opt
        
        # Generate Release Message
        thai_months = ["ม.ค.", "ก.พ.", "มี.ค.", "เม.ย.", "พ.ค.", "มิ.ย.", "ก.ค.", "ส.ค.", "ก.ย.", "ต.ค.", "พ.ย.", "ธ.ค."]
        date_str = f"{r_date.day} {thai_months[r_date.month-1]} {str(r_date.year+543)[2:]}"
        time_str = f"{r_time.strftime('%H.%M')} น."
        
        # Build Commanders String
        commander_txt = ""
        for cmd in selected_commanders:
            commander_txt += f"👮🏻‍♂️{cmd['value']}\n"
        
        message_content = f"""สภ.หนองหญ้าไซ ภ.จว.สุพรรณบุรี
วันนี้( {date_str} ) เวลา {time_str}
{commander_txt.strip()}
👮🏽‍♂️{leader}
ปล่อยแถวชุดปฏิการพิเศษ (ปะฉะดะ)
{location} ออกป้องกันเหตุในเขตพื้นที่รับผิดชอบ แต่เวลานี้
จึงเรียนมาเพื่อโปรดทราบ"""

else:
    with st.container(border=True):
        st.markdown("### 📈 ผลการปฏิบัติงาน")
        
        c_d1, c_d2 = st.columns(2)
        res_date = c_d1.date_input("วันที่", datetime.date.today())
        
        c_t1, c_t2 = st.columns(2)
        start_time = c_t1.time_input("เวลาเริ่ม", datetime.time(19, 0))
        end_time = c_t2.time_input("เวลาสิ้นสุด", datetime.time(19, 30))
        
        team_count = st.number_input("กำลังรวม (นาย)", value=11)
        
        st.write("---")
        st.markdown("**สถิติผลการปฏิบัติ**")
        c1, c2 = st.columns(2)
        with c1:
            stat_release = st.number_input("1. ปล่อยแถว (ครั้ง)", value=2)
            stat_checkpoint = st.number_input("2. ตั้งจุดตรวจ/จุดสกัด (ครั้ง)", value=1)
            stat_moto = st.number_input("3. ตรวจค้น จยย. (คัน)", value=3)
        with c2:
            stat_car = st.number_input("4. ตรวจค้นรถยนต์ (คัน)", value=6)
            stat_person = st.number_input("5. ตรวจค้นบุคคล (ราย)", value=5)
            stat_risk = st.number_input("6. ตรวจจุดเสี่ยง (แห่ง)", value=3)

        # Generate Result Message
        thai_months = ["ม.ค.", "ก.พ.", "มี.ค.", "เม.ย.", "พ.ค.", "มิ.ย.", "ก.ค.", "ส.ค.", "ก.ย.", "ต.ค.", "พ.ย.", "ธ.ค."]
        date_str = f"{res_date.day} {thai_months[res_date.month-1]} {str(res_date.year+543)[2:]}"
        time_range = f"{start_time.strftime('%H.%M')}-{end_time.strftime('%H.%M')} น."
        
        # Build Stats Text
        stats_txt = ""
        if stat_release > 0: stats_txt += f"1. ปล่อยแถว  {stat_release}  ครั้ง\n"
        if stat_checkpoint > 0: stats_txt += f"2. ตั้งจุดตรวจ/ จุดสกัด  {stat_checkpoint}  ครั้ง\n"
        if stat_moto > 0: stats_txt += f"3. ตรวจค้น จยย.  {stat_moto} คัน\n"
        if stat_car > 0: stats_txt += f"4. ตรวจค้นรถยนต์ {stat_car} คัน\n"
        if stat_person > 0: stats_txt += f"5. ตรวจค้นบุคคล  {stat_person} ราย\n"
        if stat_risk > 0: stats_txt += f"6. ตรวจจุดเสี่ยง  {stat_risk} แห่ง"
        
        # Build Commanders String
        commander_txt = ""
        for cmd in selected_commanders:
            commander_txt += f"👮🏻‍♂️{cmd['value']}\n"
            
        message_content = f"""สภ.หนองหญ้าไซ ภ.จว.สุพรรณบุรี
{date_str} {time_range}
{commander_txt.strip()}
 👮🏻‍♀️{leader}
พร้อมชุดปฏิบัติการ "ปะ ฉะ ดะ" 
กำลังรวม {team_count} นาย 
ออกปฏิบัติการในพื้นที่รับผิดชอบ 

ผลการปฏิบัติ มีดังนี้
{stats_txt}

จึงเรียนมาเพื่อโปรดทราบ"""

# Preview Section
# Preview Section
with st.container(border=True):
    st.markdown("### 📱 ตัวอย่างข้อความ (Preview)")
    st.text_area("ตรวจสอบและแก้ไขข้อความได้ที่นี่", message_content, height=400)
    
    st.markdown("---")
    
    c_btn1, c_btn2 = st.columns(2)
    with c_btn1:
        if st.button("📋 คัดลอกข้อความ", use_container_width=True):
            st.code(message_content, language="text")
            st.toast("คัดลอกเรียบร้อย!")

    with c_btn2:
        encoded_msg = urllib.parse.quote(message_content)
        line_link = f"https://line.me/R/msg/text/?{encoded_msg}"
        st.link_button("🚀 เปิดแอป LINE เพื่อส่ง", line_link, type="primary", use_container_width=True)

st.markdown("""
<div class="footer-text">Developed for Police Station Usage</div>
""", unsafe_allow_html=True)
