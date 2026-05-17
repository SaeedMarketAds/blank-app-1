import sys
import streamlit as st
from google import genai

# إعداد واجهة التطبيق على Streamlit وتغيير العنوان
st.set_page_config(page_title="Saeed MarketAds - منصة التسويق الذكي", page_icon="🤖")

# عرض الصورة الرسمية للروبوت بالحروف الكبيرة كما اتفقنا
try:
    st.image("ROBOT.jpg", caption="Saeed DataBot 🤖", use_container_width=True)
except Exception:
    # إذا لم تتوفر الصورة بعد، سيعرض عنواناً نصياً بدلاً منها
    st.title("🤖 Saeed MarketAds")

st.subheader("منصة التسويق الذكي - Saeed DataBot")
st.write("أهلاً بك يا أستاذ سعيد. الروبوت جاهز ومستعد لمساعدتك في ابتكار الأفكار الحملات التسويقية اليوم!")
st.write("---")

# جلب مفتاح الـ API بأمان من إعدادات Streamlit Secrets
# (سنقوم بضبط هذا المفتاح في إعدادات المنصة لاحقاً)
if "GOOGLE_API_KEY" in st.secrets:
    GOOGLE_API_KEY = st.secrets["GOOGLE_API_KEY"]
else:
    # حل احتياطي إذا كنت تجرب محلياً
    GOOGLE_API_KEY = st.sidebar.text_input("ضع مفتاح Gemini API هنا:", type="password")

# الاتصال بجوجل
client = None
if GOOGLE_API_KEY:
    try:
        client = genai.Client(api_key=GOOGLE_API_KEY)
        st.success("تم الاتصال بالذكاء الاصطناعي من جوجل بنجاح! ✅")
    except Exception as e:
        st.error(f"خطأ في الاتصال: {e}")
else:
    st.warning("⚠️ يرجى إضافة مفتاح الـ API الخاص بك لتفعيل الروبوت.")

# صندوق المحادثة الذكي (واجهة المستخدم)
user_input = st.text_input("اكتب طلبك التسويقي هنا (مثال: اكتب لي إعلان لمنتج ملابس):", key="user_query")

if st.button("إرسال للروبوت 🚀"):
    if not client:
        st.error("الروبوت غير متصل. تأكد من وضع مفتاح الـ API الحقيقي أولاً.")
    elif not user_input:
        st.info("يرجى كتابة سؤال أو طلب أولاً.")
    else:
        with st.spinner("⏳ الروبوت يفكر الآن ويصنع الأفكار... يرجى الانتظار..."):
            try:
                # استدعاء نموذج جينيريت الرائع
                response = client.models.generate_content(
                    model='gemini-2.5-flash',
                    contents=user_input,
                )
                
                if response.text:
                    st.markdown("### 🤖 إجابة الروبوت:")
                    st.write(response.text)
                else:
                    st.error("لم يتم استلام رد من النموذج.")
                    
            except Exception as ex:
                st.error("Notice: حدث خطأ أثناء معالجة الطلب، يرجى المحاولة مجدداً.")
st.write("---")
st.caption("تطوير أستاذ: سعيد المسوري للتسويق الإلكتروني © 2026")
