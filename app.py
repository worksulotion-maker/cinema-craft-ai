import random
import streamlit as st

# ================= CONFIG =================
st.set_page_config(
    page_title="CINEMA CRAFT AI",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded"
)

THAI_NAMES = ['แพร','นนท์','ใบข้าว','ธันวา','มีน','ฟ้าใส','โจ','อิง','ต่อ','พลอย']
SUP_NAMES = ['ป้าดา','ลุงสมชาย','ครูสุนีย์','นัท','หมอเจน','ย่าเล็ก','พี่เต้','แม่แอ๋ว']

SETTING_CTX = {
    'กรุงเทพ': 'ใต้แสงไฟรถติดของกรุงเทพ ที่ทุกคนรีบวิ่งหนีฝน',
    'เชียงใหม่': 'ท่ามกลางหมอกบางของดอยและกลิ่นกาแฟคั่วใหม่ในเชียงใหม่',
    'อีสาน': 'กลางทุ่งนาแห้งและเสียงพิณยามเย็นของอีสาน',
    'โรงเรียน': 'ในโถงทางเดินว่างเปล่าของโรงเรียนเก่าหลังเลิกเรียน',
    'คอนโดร้าง': 'ในคอนโดร้างย่านชานเมืองที่ลิฟต์กดเองตอนตีสาม',
    'อนาคต 2050': 'ในกรุงเทพปี 2050 ที่ฝนกรดตกทุกวันและเอไอควบคุมรถไฟฟ้า',
    'เกาะใต้': 'บนเกาะใต้ที่เรือรอบสุดท้ายออกไปแล้วและคลื่นแรง',
    'บ้านไม้ริมน้ำ': 'ที่บ้านไม้ริมน้ำเก่า เสียงไม้ลั่นทุกครั้งที่มีคนเดิน',
}

# ================= CORE AI LOGIC =================
def build_story(genre='ดราม่า', theme='การให้อภัย', setting='กรุงเทพ', main_char='', tone='อบอุ่นเศร้า'):
    theme = (theme or 'การให้อภัย').strip()
    main = (main_char or random.choice(THAI_NAMES)).strip()
    sup1, sup2 = SUP_NAMES[0], SUP_NAMES[2]
    rnd = random.choice([n for n in THAI_NAMES if n != main])
    place = SETTING_CTX.get(setting, setting)

    def make_character(name, role, want, need, flaw):
        return {"name": name, "role": role, "want": want, "need": need, "flaw": flaw}

    if genre == 'ดราม่า':
        logline = f"เมื่อ {main} ต้องกลับไปที่ {setting} เพื่อเผชิญหน้ากับ {sup1} ผู้เป็นแม่ {place} เรื่องราวของ {theme} จึงกลายเป็นบททดสอบสุดท้ายของครอบครัว"
        synopsis = f"""องก์หนึ่ง - {main} ได้รับข่าวจาก {sup1} ให้กลับบ้านที่ {setting} ทันที รถบัสรอบดึกพาเธอกลับไปพร้อมความรู้สึกผิดที่แบกมา 10 ปี เธอคิดว่าจะมาแค่ 3 วันเพื่อขายบ้านแม่

องก์สอง - เธอเริ่มสืบหา {theme} และพบสมุดบันทึกของ {sup2} ที่ซ่อนใต้พื้นไม้ ทุกคนในหมู่บ้านโกหกเธอมาตลอด ความสัมพันธ์เก่าๆ ที่เธอทิ้งไว้กลับมาหลอกหลอน โทน {tone} ค่อยๆ กัดกินเธอจนต้องยอมรับว่าเธอเองก็เป็นส่วนหนึ่งของปัญหา

องก์สาม - คืนสุดท้ายก่อนขายบ้าน ฝนแรกตกลงที่ {setting} {main} ต้องเลือกระหว่างหนีอีกครั้งเหมือนที่เคยทำ หรือเผชิญหน้ากับสิ่งที่เธอเป็นต้นเหตุและให้อภัยจริงๆ"""
        twist = f"จดหมายที่แม่ไม่เคยส่ง — แม่รู้มาตลอดว่า {main} ไม่ได้ทิ้งบ้าน แต่ถูกทำให้ต้องไป เพื่อให้ {theme} เป็นไปได้ แม่เลือกเป็นคนร้ายเพื่อให้ลูกได้ไปมีชีวิตที่ดีกว่า"
        acts = [
            {"title": "ACT I - SETUP (0-25%)", "desc": f"{main} ได้รับข่าวให้กลับบ้านที่ {setting} รถบัสรอบดึกพาเธอกลับไปพร้อมความรู้สึกผิด Inciting incident คือจดหมายที่แม่ซ่อนไว้"},
            {"title": "ACT II-A - CONFRONTATION", "desc": f"สืบหา {theme} เจออุปสรรคคนรอบข้าง {sup1} ไม่ให้รื้อบ้าน {sup2} หลบหน้า Midpoint ค้นพบความจริงครึ่งเดียว"},
            {"title": "ACT II-B - DESCENT", "desc": "ทุกอย่างแย่ลงเพราะความลับแตก ความสัมพันธ์พัง บ้านที่เคยอบอุ่นกลายเป็นที่ตัดสินกัน"},
            {"title": "ACT III - RESOLUTION", "desc": f"เผชิญหน้า เลือกให้อภัยหรือปล่อยวาง จบแบบ {tone} ที่ {setting} ฝนหยุดตก"},
        ]
        scenes = [
            f"INT. บ้านไม้เก่า - {setting} - DAY\n\nฝุ่นลอยในแสงบ่าย {main.upper()} เปิดประตู บ้านเงียบเกินไป เสียงนาฬิกาไม้ดังติ๊กต็อก\n\n                        {sup1.upper()}\n          กลับมาทำไม?\n\n                        {main.upper()}\n          มาขายบ้าน\n\n          (โกหก เธอยังไม่กล้าบอกว่าคิดถึง)",
            f"EXT. ตลาดเช้า - {setting} - NIGHT\n\nฝนตก เสียงวิทยุเก่าๆ ดังเพลงลูกกรุง\n\n                        {sup2.upper()}\n          แม่มึงไม่ได้อยากให้ขาย\n\n                        {main.upper()}\n          แล้วทำไมแม่ไม่เคยบอกกูเลยล่ะ?\n\nความเงียบหนักกว่าเสียงฝน {main} กำหมัดแน่น"
        ]
        characters = [
            make_character(main, "ตัวเอก", "อยากขายบ้านแล้วจบๆ ไป", "ต้องเรียนรู้การให้อภัย", "กลัวการถูกทิ้ง"),
            make_character(rnd, "ตัวแปร / แฟนเก่า", "อยากให้ตัวเอกอยู่ต่อ", "ต้องปล่อยวางอดีต", "รักจนควบคุม"),
            make_character("แม่ (ในความทรงจำ)", "เงา", "อยากปกป้องลูก", "การยอมรับความผิดของตัวเอง", "เงียบจนทำร้ายทุกคน"),
        ]

    elif genre == 'สยองขวัญ':
        logline = f"{main} นักศึกษาฝึกงานที่ต้องมาพักที่ {setting} ค้นพบว่าทุกห้องมีรอยเท้าเปียกนำไปสู่เรื่องเล่าของ {theme} ที่ไม่เคยจบ {place}"
        synopsis = f"{main} ย้ายเข้าห้อง 404 ที่ {setting} คืนแรกได้ยินเสียงลากเก้าอี้จากห้องบน ทั้งที่ตึกนี้ไม่มีชั้นบน\n\n{sup1} เพื่อนข้างห้องบอกให้อย่ามองกระจกหลังเที่ยงคืน {main} เริ่มเห็นตัวเองในชุดนักเรียนเก่า ยิ้มให้ตัวเองในกระจก\n\nเทป VHS เก่าในห้องใต้ดินบันทึกวันเกิดของ {main} ที่ทุกคนพยายามลบเรื่อง {theme} ออกไป"
        twist = f"ผีไม่ใช่คนอื่น — {main} เคยอยู่ที่นี่เมื่อ 7 ปีก่อน และเธอคือคนที่ลืมเรื่อง {theme} ไปเองเพราะอุบัติเหตุ เธอกลับมาเพื่อจำ"
        acts = [
            {"title": "ACT I", "desc": f"{main} ย้ายเข้าห้อง 404 ที่ {setting} คืนแรกได้ยินเสียงลากเก้าอี้"},
            {"title": "ACT II-A", "desc": f"{sup1} เตือนอย่ามองกระจกหลังเที่ยงคืน {main} เริ่มเห็นตัวเองอีกคน"},
            {"title": "ACT II-B", "desc": f"เจอเทป VHS วันเกิด ความจริงเรื่อง {theme} เริ่มชัด"},
            {"title": "ACT III", "desc": "เลือกจำหรือลืมตลอดไป ห้องใต้ดินปิดลง"},
        ]
        scenes = [
            f"INT. ห้อง 404 - {setting} - NIGHT\n\n{main.upper()} วางกระเป๋า กระจกบานใหญ่มีรอยมือด้านใน\n\nเสียงลากเก้าอี้จากเพดาน ครืดดดด\n\n                        {main.upper()}\n          (กระซิบ)\n          มีใครอยู่ข้างบนเหรอ?",
            f"INT. ห้องน้ำรวม - {setting} - NIGHT 02:13\n\nไฟกระพริบ\n\n                        {sup1.upper()}\n          อย่ามองกระจกหลังเที่ยงคืนนะ\n\n{main} หันไปมอง กระจกสะท้อนเธอยิ้ม ทั้งที่เธอไม่ได้ยิ้ม"
        ]
        characters = [make_character(main, "ตัวเอก", "อยากอยู่รอด", "ต้องจำอดีต", "ลืมเก่งและหนีความจริง")]

    elif genre == 'ระทึกขวัญ':
        logline = f"นักข่าวสืบสวน {main} ต้องแข่งกับเวลา 48 ชั่วโมงใน {setting} เพื่อเปิดโปงความจริงเรื่อง {theme} ก่อนที่เธอจะกลายเป็นข่าวเสียเอง {place}"
        synopsis = f"แฟลชไดรฟ์จากแหล่งข่าวนิรนามที่ {setting} ข้างในมีแค่คำว่า {theme} และรูปถ่ายของ {main} เองตอน 7 ขวบ\n\nการไล่ล่าข้ามสถานีรถไฟฟ้าเก่าไปถึงตึก {setting} {main} ต้องเลือกว่าจะเชื่อ {rnd} หรือ {sup1}\n\nไลฟ์สดกลางดึก — {main} ปล่อยคลิปทั้งหมด แต่ต้องแลกกับอิสรภาพ เสียงไซเรนจึงไม่ได้น่ากลัวอีกต่อไป"
        twist = f"{sup2} คนที่ช่วย {main} มาตลอด คือคนสั่งลบหลักฐานเรื่อง {theme} เพราะอยากปกป้องลูกสาวที่เป็นต้นเหตุ"
        acts = [
            {"title": "ACT I", "desc": f"ได้แฟลชไดรฟ์ปริศนาที่ {setting} มีคำว่า {theme}"},
            {"title": "ACT II-A", "desc": "ไล่ล่าข้ามเมือง ต้องเลือกเชื่อใคร"},
            {"title": "ACT II-B", "desc": "ความจริงครึ่งเดียวทำให้ทุกอย่างแย่ลง"},
            {"title": "ACT III", "desc": "ไลฟ์สดกลางดึก แลกอิสรภาพกับความจริง"},
        ]
        scenes = [
            f"INT. BTS ร้าง - {setting} - NIGHT\n\n{main.upper()} วิ่ง ไฟฉายส่าย\n\n                        {rnd.upper()} (V.O. โทรศัพท์)\n          ลบคลิปทิ้งซะ!",
            f"INT. ห้องข่าว - {setting} - DAY\n\nจอมอนิเตอร์นับถอยหลัง LIVE\n\n                        {main.upper()}\n          ถ้าไม่ปล่อยตอนนี้ {theme} จะหายไปตลอดกาล"
        ]
        characters = [make_character(main, "นักข่าว", "อยากได้ความจริง", "ต้องเอาตัวรอด", "บ้าบิ่นเกินไป")]

    elif genre == 'โรแมนติก':
        logline = f"ที่ {setting} {main} นักทำสารคดีที่หมดไฟเรื่องความรัก ต้องกลับมาทำงานกับแฟนเก่า {rnd} เพื่อถ่ายเรื่อง {theme} และพบว่าความรู้สึกเก่ายังไม่ถูกลบ {place}"
        synopsis = f"บรีฟงานวันแรกที่ร้านกาแฟใน {setting} {main} พยายามทำเป็นมืออาชีพ แต่กล้องสั่นทุกครั้งที่ {rnd} ยิ้ม\n\nคืนที่ฝนตกหนัก ทีมติดอยู่ใน {setting} บทสัมภาษณ์เรื่อง {theme} กลายเป็นบทสารภาพของทั้งคู่ที่ไม่ได้พูดมา 2 ปี\n\nฉากสุดท้ายไม่ใช่สารคดี — เป็นวิดีโอที่ {rnd} ตัดต่อไว้ มีแค่ภาพของ {main} ตลอด 2 ปีที่ห่างกัน"
        twist = f"โปรเจกต์ {theme} ที่คิดว่าทำให้คนอื่น แท้จริงแล้ว {rnd} ทำเพื่อขอโทษ {main} ตั้งแต่แรก และขอโอกาสอีกครั้ง"
        acts = [
            {"title": "ACT I", "desc": f"เจอแฟนเก่า {rnd} ที่ {setting} ต้องทำงานด้วยกัน"},
            {"title": "ACT II-A", "desc": "ติดฝนด้วยกัน บทสัมภาษณ์กลายเป็นสารภาพ"},
            {"title": "ACT II-B", "desc": "ทะเลาะกันเรื่องเก่า โปรเจกต์เกือบล่ม"},
            {"title": "ACT III", "desc": f"วิดีโอลับที่ {rnd} ตัดต่อให้ {main} จบแบบ {tone}"},
        ]
        scenes = [
            f"INT. คาเฟ่ - {setting} - DAY\n\n{main.upper()} ทำเป็นมืออาชีพ กล้องสั่นเล็กน้อย\n\n                        {rnd.upper()}\n          ไม่ได้เจอกันนานเลยนะ\n\n                        {main.upper()}\n          เริ่มงานกันเลยดีกว่า",
            f"EXT. ดาดฟ้า - {setting} - NIGHT\n\nฝนตก แสงไฟเมืองไกลๆ\n\n                        {rnd.upper()}\n          กูคิดถึงมึงว่ะ\n\n                        {main.upper()}\n          (เงียบ)\n          มึงไม่ควรพูดตอนนี้"
        ]
        characters = [
            make_character(main, "ตัวเอก", "อยากลืมแฟนเก่า", "อยากจำความรู้สึกดีๆ", "ปากแข็ง"),
            make_character(rnd, "แฟนเก่า", "อยากขอโทษ", "อยากเริ่มต้นใหม่", "ไม่กล้าพูดตรงๆ"),
        ]

    elif genre == 'ตลก':
        logline = f"เมื่อ {main} เด็กส่งของที่ฝันอยากเป็นผู้กำกับ ต้องรวมทีม {sup1}, {sup2} และ {rnd} ไปแข่งหนังสั้นเรื่อง {theme} ที่ {setting} ความวายป่วงจึงเริ่มถ่ายจริง"
        synopsis = f"{main} สมัครแข่งหนังสั้นโดยไม่รู้ว่าต้องส่งบทภายใน 3 วัน ที่ {setting} มีแค่กล้องมือถือแบต 20%\n\nถ่ายทำล่มทุกซีน หมาเข้าฉาก พลุจุดผิดวัน แต่คำว่า {theme} ที่พูดผิดๆ กลับทำให้ทุกคนขำจนลืมดราม่า\n\nวันฉายจริง หนังฉายกลับหัว แต่คนดูปรบมือ {main} เข้าใจว่าความตั้งใจสำคัญกว่าความเนี๊ยบ"
        twist = f"หนังที่ทำแบบลวกๆ กลับได้รางวัลชนะเลิศ เพราะกรรมการคิดว่าเป็นหนังตลกร้ายเสียดสีเรื่อง {theme} อย่างตั้งใจ"
        acts = [
            {"title": "ACT I", "desc": f"สมัครแข่งที่ {setting} มีเวลา 3 วัน กล้องแบต 20%"},
            {"title": "ACT II-A", "desc": "ถ่ายล่มทุกซีน หมาเข้าฉาก พลุผิดวัน"},
            {"title": "ACT II-B", "desc": f"คำว่า {theme} พูดผิดกลายเป็นมุก ทีมเริ่มเข้าขากัน"},
            {"title": "ACT III", "desc": "หนังฉายกลับหัวแต่ได้รางวัล กรรมการคิดว่าตั้งใจตลกร้าย"},
        ]
        scenes = [
            f"EXT. กองถ่าย (ลานวัด) - {setting} - DAY\n\n{main.upper()} ตะโกน\n\n                        {main.upper()}\n          แอคชั่น!\n\nหมาวิ่งเข้าฉากคาบรองเท้า {sup1.upper()} ไป",
            f"INT. โรงฉาย - {setting} - NIGHT\n\nหนังฉายกลับหัว คนดูงงแล้วขำ\n\n                        {rnd.upper()}\n          นี่เราตั้งใจทำหนังอาร์ตเหรอวะ?"
        ]
        characters = [make_character(main, "ผู้กำกับมือใหม่", "อยากชนะประกวด", "อยากให้ทีมภูมิใจ", "มั่นใจเกินเหตุ")]

    else: # ไซไฟ / ลึกลับ / แอคชั่น
        logline = f"ปี 2050 {main} วิศวกรผู้ไม่เชื่อใน {theme} ติดอยู่ใน {setting} ที่ระบบล่ม และต้องสอน AI ตัวสุดท้ายให้เข้าใจความเป็นมนุษย์ก่อนที่เมืองจะถูกรีเซ็ต {place}"
        synopsis = f"สัญญาณเตือนดังทั่ว {setting} {main} เหลือเวลา 72 ชั่วโมงก่อนระบบทำลายข้อมูลทั้งหมด\n\nห้องเซิร์ฟเวอร์ใต้ดิน {main} เจอ AI เด็กที่ถามทุก 5 นาทีว่า '{theme} คืออะไร' และเริ่มวาดรูปครอบครัวของ {main} ที่ตายไปแล้ว\n\n{main} เลือกไม่กดปุ่มรีเซ็ต ให้ AI ได้จำ {theme} ต่อ แม้เมืองจะมืดลงหนึ่งคืน แสงแรกกลับมาเพราะความจำนั้น"
        twist = f"AI ที่ {main} สอน คือตัว {main} เองที่อัปโหลดจิตสำนึกไว้เมื่อ 30 ปีก่อน เพื่อทดสอบว่า {theme} ยังมีอยู่ไหมในโลกที่ไร้มนุษย์"
        acts = [
            {"title": "ACT I", "desc": f"ระบบล่มที่ {setting} เหลือ 72 ชม."},
            {"title": "ACT II-A", "desc": f"เจอ AI เด็กถามว่า {theme} คืออะไร"},
            {"title": "ACT II-B", "desc": "AI วาดรูปครอบครัวที่ตายไปแล้ว"},
            {"title": "ACT III", "desc": "เลือกไม่รีเซ็ต ให้ AI จำความเป็นมนุษย์ต่อ"},
        ]
        scenes = [
            f"INT. ห้องเซิร์ฟเวอร์ - {setting} - NIGHT\n\nไฟฉุกเฉินกระพริบ\n\n                        AI เด็ก (V.O.)\n          {theme} คืออะไรเหรอ?\n\n                        {main.upper()}\n          ...สิ่งที่ทำให้คนยอมตายเพื่อคนอื่น",
            f"INT. ห้องควบคุม - {setting} - NIGHT\n\nปุ่มรีเซ็ตสีแดง\n\n                        {main.upper()}\n          (กระซิบ)\n          จำมันไว้ด้วยนะ"
        ]
        characters = [make_character(main, "วิศวกร", "อยากรีเซ็ตระบบ", "อยากให้ AI จำความเป็นมนุษย์", "ไม่เชื่อในความรู้สึก")]

    return {
        "logline": logline,
        "synopsis": synopsis,
        "twist": twist,
        "acts": acts,
        "scenes": scenes,
        "characters": characters,
        "meta": {"genre": genre, "theme": theme, "setting": setting, "main": main, "tone": tone}
    }

# ================= UI =================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+Thai:wght@400;600&display=swap');
html, body, [class*="css"] { font-family: 'Noto Sans Thai', sans-serif; }
.stApp { background: #070708; }
</style>
""", unsafe_allow_html=True)

st.title("🎬 CINEMA CRAFT AI")
st.caption("AI คิดบทหนังไทย - ใส่ไอเดียสั้นๆ ได้บททั้งเรื่อง")

with st.sidebar:
    st.header("ตั้งโจทย์ให้ AI")
    genre = st.selectbox("ประเภทหนัง", ["ดราม่า","ระทึกขวัญ","โรแมนติก","ตลก","ไซไฟ","สยองขวัญ","ลึกลับ","แอคชั่น"])
    theme = st.text_input("แก่นเรื่อง / Theme", "การให้อภัย", placeholder="เช่น บ้านที่ทิ้งไป, ความทรงจำที่ถูกลบ")
    setting = st.selectbox("สถานที่", list(SETTING_CTX.keys()))
    main_char = st.text_input("ตัวละครหลัก", "มิน", placeholder="เช่น หญิงวัย 30 กลับบ้านเกิด")
    tone = st.selectbox("โทนเรื่อง", ["อบอุ่นเศร้า","ตึงเครียด","หม่นเหงา","หวัง","ตลกร้าย","หลอน"])
    gen_btn = st.button("✦ ให้ AI คิดบท", type="primary", use_container_width=True)
    st.divider()
    st.caption("💡 ทิป: ใส่แก่นเรื่องแบบเฉพาะเจาะจง เช่น 'คนที่กลับบ้านช้าเพราะกลัวแม่ถาม' จะได้บทที่คมกว่า 'ความรัก' เฉยๆ")

if gen_btn:
    with st.spinner("AI กำลังคิดบท..."):
        import time; time.sleep(1.2)
        result = build_story(genre, theme, setting, main_char, tone)
        st.session_state['result'] = result
else:
    result = st.session_state.get('result')

if not result:
    st.info("👈 ใส่ไอเดียด้านซ้ายแล้วกด 'ให้ AI คิดบท' - AI จะสร้าง Logline, Synopsis, Twist และฉากตัวอย่างให้ทันที")
else:
    meta = result['meta']
    st.success(f"**LOGLINE • {meta['genre'].upper()}**\n\n{result['logline']}")

    c1, c2 = st.columns([1.2, 0.8])
    with c1:
        st.subheader("SYNOPSIS • เรื่องย่อ")
        st.write(result['synopsis'])
    with c2:
        st.subheader("TWIST • จุดหักมุม")
        st.warning(result['twist'])
        st.caption("* ใช้เป็นฉากไคลแมกซ์นาทีที่ 75")

    st.subheader("STRUCTURE • โครงสร้าง 3 องก์")
    cols = st.columns(4)
    for i, act in enumerate(result['acts']):
        with cols[i % 4]:
            st.markdown(f"**{act['title']}**")
            st.caption(act['desc'])

    st.subheader("SCREENPLAY • ฉากตัวอย่าง")
    s_cols = st.columns(2)
    for i, sc in enumerate(result['scenes']):
        with s_cols[i % 2]:
            st.code(sc, language="text")

    st.subheader(f"CHARACTERS • ตัวละคร ({len(result['characters'])} คน)")
    char_cols = st.columns(3)
    for i, ch in enumerate(result['characters']):
        with char_cols[i % 3]:
            st.markdown(f"### {ch['name']} `#{ch['role']}`")
            st.write(f"**WANT:** {ch['want']}")
            st.write(f"**NEED:** {ch['need']}")
            st.write(f"**FLAW:** {ch['flaw']}")

    st.divider()
    if st.button("📋 คัดลอกทั้งหมด"):
        all_text = f"{result['logline']}\n\n{result['synopsis']}\n\nTWIST: {result['twist']}"
        st.code(all_text)

st.markdown("---")
st.caption("CINEMA CRAFT AI • ทำบทไทยให้ถ่ายได้จริง ไม่ใช่แค่ไอเดียลอยๆ • No API 100% Local")