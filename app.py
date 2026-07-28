import streamlit as st

# Configurazione della pagina stile iPhone
st.set_page_config(
    page_title="Giappone On-The-Road",
    page_icon="🇯🇵",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# CSS per rendere l'interfaccia identica a un'app iOS nativa
st.markdown("""
    <style>
    .main { background-color: #f2f2f7; }
    h1 { color: #1c1c1e; font-family: -apple-system, BlinkMacSystemFont, sans-serif; font-weight: 700; text-align: center; }
    .stTabs [data-baseweb="tab-list"] { gap: 6px; justify-content: center; }
    .stTabs [data-baseweb="tab"] {
        background-color: #ffffff; border-radius: 10px; padding: 6px 12px;
        box-shadow: 0px 1px 2px rgba(0,0,0,0.05); font-weight: 600; color: #007aff; font-size: 13px;
    }
    .stTabs [aria-selected="true"] { background-color: #007aff !important; color: white !important; }
    img { border-radius: 12px; width: 100%; height: auto; display: block; margin-bottom: 10px; }
    </style>
""", unsafe_allow_html=True)

st.title("🇯🇵 Giappone On-The-Road")
st.write("### 🚗 Tocca le tappe per vedere foto e dettagli")

# Database con formattazione Markdown nativa per le immagini
if "database_viaggio" not in st.session_state:
    st.session_state.database_viaggio = {
        "Izu & Mt. Omuro": [
            {
                "titolo": "🌋 Salita al Monte Omuro",
                "foto": "https://picsum.photos",
                "descrizione": "L'iconico vulcano spento a forma di ciotola rovesciata. Prendi la seggiovia panoramica e goditi la camminata di 20 minuti lungo il bordo del cratere con vista sul Monte Fuji e sull'oceano."
            },
            {
                "titolo": "🌉 Scogliere di Jogasaki",
                "foto": "https://picsum.photos",
                "descrizione": "Una frastagliata costa vulcanica formata da antica lava del Monte Omuro. Attraversa il famoso ponte sospeso Kawayama, lungo 48 metri e sospeso a ben 23 metri sopra le onde impetuose."
            }
        ],
        "Dogashima Trail": [
            {
                "titolo": "🌊 Dogashima Yuhodo Trail & Tensodo",
                "foto": "https://picsum.photos",
                "descrizione": "Un breve e meraviglioso sentiero costiero. Arriverai sopra la spettacolare Grotta Tensodo, dove un foro circolare nel soffitto roccioso fa filtrare la luce creando un'acqua azzurro brillante."
            }
        ],
        "Cape Ose": [
            {
                "titolo": "⛩️ Cape Ose (Osezaki)",
                "foto": "https://picsum.photos",
                "descrizione": "La punta nord-occidentale di Izu. Offre una vista cartolina del Monte Fuji sopra il mare. Visita l'antico santuario dei pescatori e il laghetto misterioso di acqua dolce circondato dal mare salato."
            }
        ],
        "Tsumago-juku": [
            {
                "titolo": "🏮 Antica Tsumago-juku",
                "foto": "https://picsum.photos",
                "descrizione": "Un vero e proprio salto nel tempo nell'era Edo dei samurai. Le auto sono vietate, i fili elettrici interrati e le locande in legno tradizionali si illuminano la sera solo con lanterne di carta."
            }
        ],
        "Seki Museum": [
            {
                "titolo": "⚔️ Seki Swordsmith Museum",
                "foto": "https://picsum.photos",
                "descrizione": "La capitale mondiale delle lame. Esplora la storia della forgia delle Katane dei samurai e fai acquisti di coltelli da cucina professionali nella adiacente Cutlery Hall."
            }
        ],
        "Kyoto": [
            {
                "titolo": "⛩️ Fushimi Inari-taisha",
                "foto": "https://picsum.photos",
                "descrizione": "Il celeberrimo sentiero montano protetto da oltre 10.000 torii rosso scarlatto dedicati al dio del riso e dell'agricoltura. Consiglio: cammina presto al mattino per evitare la folla."
            },
            {
                "titolo": "🏯 Kinkaku-ji (Il Tempio d'Oro)",
                "foto": "https://picsum.photos",
                "descrizione": "Uno dei monumenti più famosi al mondo: un padiglione zen interamente ricoperto di foglie d'oro splendenti che si riflette in modo simmetrico sul laghetto dello specchio d'acqua circostante."
            }
        ],
        "Adachi & Motonosumi": [
            {
                "titolo": "🖼️ Adachi Museum of Art",
                "foto": "https://picsum.photos",
                "descrizione": "Votato per vent'anni consecutivi come il giardino più bello del Giappone. Le ampie vetrate del museo incorniciano la natura esterna trasformandola in quadri viventi in continuo mutamento."
            },
            {
                "titolo": "🦊 Motonosumi Shrine",
                "foto": "https://picsum.photos",
                "descrizione": "Spettacolare tunnel di 123 torii rossi che serpeggia su una scogliera nera di fronte all'oceano blu. Sfida te stesso a lanciare una moneta nella scatola delle offerte montata a 5 metri d'altezza!"
            }
        ],
        "Hiroshima": [
            {
                "titolo": "⛩️ Isola Sacra di Miyajima",
                "foto": "https://picsum.photos",
                "descrizione": "Prendi il traghetto per vedere il maestoso ed enorme Torii di legno che sembra fluttuare sulle acque dell'oceano durante l'alta marea. Attento ai cervi liberi che girano sull'isola!"
            }
        ],
        "Tokyo Finale": [
            {
                "titolo": "🔮 teamLab & Odaiba",
                "foto": "https://picsum.photos",
                "descrizione": "Il volto iper-tecnologico di Tokyo. Esplora le stanze d'arte digitale immersiva prima di spostarti sull'isola di Odaiba per vedere la statua del robot Gundam gigante."
            },
            {
                "titolo": "🚦 Incrocio di Shibuya & Shibuya Sky",
                "foto": "https://picsum.photos",
                "descrizione": "Attraversa l'incrocio pedonale più pazzo e affollato del mondo, poi sali sulla spettacolare terrazza panoramica all'aperto di Shibuya Sky per ammirare le luci di Tokyo dall'alto."
            }
        ]
    }

# Creazione delle sezioni a scorrimento (Tab)
tabs = st.tabs(list(st.session_state.database_viaggio.keys()))

for i, (macro_zona, tappe) in enumerate(st.session_state.database_viaggio.items()):
    with tabs[i]:
        st.write(f"## 📍 {macro_zona}")
        
        for index, tappa in enumerate(tappe):
            with st.expander(tappa["titolo"]):
                # Forziamo il rendering dell'immagine tramite sintassi HTML nativa per eludere i blocchi di Safari
                st.markdown(f'<img src="{tappa["foto"]}" alt="{tappa["titolo"]}">', unsafe_allow_html=True)
                st.write(tappa["descrizione"])
                st.checkbox("Segna come visitato", key=f"fatto_{macro_zona}_{index}")

st.markdown("<br><p style='text-align: center; color: gray; font-size: 11px;'>Tocca i titoli per aprire i dettagli</p>", unsafe_allow_html=True)
