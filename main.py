import streamlit as st
import pandas as pd
import os
import traceback
from rag_engine import retrieval_chain  # senin LLM zincirin
import re

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

st.title("📊 Excel / CSV Komut Yorumlayıcı (RAG + LLM)")

# 1. Komut girme - EXCEL YÜKLEMESİNDEN ÖNCE
user_command = st.text_input("Lütfen analiz komutunuzu girin (örnek: A ve B sütunlarının ortalamasını hesapla)")

# 2. Komut varsa analize geç
if user_command:
    if "ortalama" in user_command.lower() or "sütun" in user_command.lower() or "hesapla" in user_command.lower():
        st.info("📁 Bu işlem için bir dosya yüklemeniz gerekiyor.")

        uploaded_file = st.file_uploader("CSV veya Excel dosyanızı yükleyin", type=["csv", "xlsx"])

        if uploaded_file:
            file_name = uploaded_file.name
            file_path = os.path.join("uploads", file_name)
            with open(file_path, "wb") as f:
                f.write(uploaded_file.read())

            df = pd.read_excel(file_path) if file_name.endswith(".xlsx") else pd.read_csv(file_path)
            st.success("✅ Dosya yüklendi!")
            st.dataframe(df)

            try:
                from rag_engine import retrieval_chain
                import re

                generated_code = retrieval_chain.invoke(user_command)
                clean_code = re.sub(r"```(?:python)?\n?([\s\S]+?)```", r"\1", generated_code).strip()
                st.code(generated_code, language="python")

                local_vars = {"df": df}
                exec(clean_code, {}, local_vars)

                result = local_vars.get("result") or local_vars.get("sonuc")
                st.success("📈 Sonuç:")
                st.write(result)
            except Exception as e:
                st.error("❌ Hata oluştu:")
                st.text(traceback.format_exc())

        else:
            st.warning("Lütfen bir dosya yükleyin.")

    else:
        st.info("🧠 Komut LLM'e yönlendiriliyor...")
        from rag_engine import ChatOpenAI

        llm = ChatOpenAI(model="gpt-3.5-turbo")
        response = llm.invoke(user_command)
        st.success("🧠 LLM Cevabı:")
        st.write(response.content)

