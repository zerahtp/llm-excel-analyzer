# 📊 LLM Excel Analyzer

**LLM Excel Analyzer**, kullanıcıdan gelen doğal dil komutlarını kullanarak Excel veya CSV dosyaları üzerinde Python analiz kodu üretip çalıştıran bir veri analiz aracıdır.  
RAG (Retrieval-Augmented Generation) yapısı ve GPT-3.5-turbo (OpenAI) modeli sayesinde, teknik bilgiye sahip olmayan kullanıcılar bile kolayca veri analizi gerçekleştirebilir.

---

## 🚀 Özellikler

- 💬 Doğal dil ile analiz komutu girin (örneğin: "A ve B sütunlarının ortalamasını hesapla")
- 📁 Excel veya CSV dosyası yükleyin
- ⚙️ LLM, Python kodunu otomatik oluşturur
- 🧠 `LangChain` ile bağlamdan destek alır (average_formula.md üzerinden)
- 📈 Sonuçları anlık olarak hesaplar ve gösterir
- 💻 Streamlit tabanlı kullanıcı arayüzü

---

## 🧠 Proje Akışı

1. Kullanıcı, analiz etmek istediği komutu doğal dilde girer.
2. Sistem, `average_formula.md` dokümanından bağlam alarak bir kod üretim zinciri oluşturur.
3. LLM bu komutu işleyip uygun Python kodunu üretir.
4. Kod `exec()` ile çalıştırılır ve sonuç ekrana yazdırılır.

---

## 📦 Kullanılan Teknolojiler

| Teknoloji | Açıklama |
|----------|----------|
| [Streamlit](https://streamlit.io/) | Web tabanlı arayüz |
| [LangChain](https://www.langchain.com/) | LLM + bellek + retrieval zincirleme |
| [OpenAI GPT-3.5 Turbo](https://platform.openai.com/docs/models/gpt-3-5) | Doğal dilden Python kod üretimi |
| [Chroma](https://docs.trychroma.com/) | Vektör veri tabanı |
| [Pandas](https://pandas.pydata.org/) | Veri işlemleri |
| `.md` + `TextLoader` | Domain bilgisi (kurallar) bağlam olarak verilir |

---

## 🛠️ Kurulum

1. Repoyu klonlayın:
```bash
git clone https://github.com/zerahtp/llm-excel-analyzer.git
cd llm-excel-analyzer
