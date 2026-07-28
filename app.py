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
    </style>
""", unsafe_allow_html=True)

st.title("🇯🇵 Giappone On-The-Road")
st.write("### 🚗 Espandi le tappe per descrizioni e link foto")

# Database con link testuali alle foto e dettagli per il viaggio
if "database_viaggio" not in st.session_state:
    st.session_state.database_viaggio = {
        "Izu & Mt. Omuro": [
            {
                "titolo": "🌋 Salita al Monte Omuro",
                "link_foto": "https://google.com",
                "descrizione": "L'iconico vulcano spento a forma di ciotola rovesciata. Prendi la seggiovia panoramica e goditi la camminata di 20 minuti lungo il bordo del cratere con vista sul Monte Fuji e sull'oceano."
            },
            {
                "titolo": "🌉 Scogliere di Jogasaki",
                "link_foto": "https://google.com",
                "descrizione": "Una frastagliata costa vulcanica formata da antica lava del Monte Omuro. Attraversa il famoso ponte sospeso Kawayama, lungo 48 metri e sospeso a ben 23 metri sopra le onde impetuose."
            }
        ],
        "Dogashima Trail": [
            {
                "titolo": "🌊 Dogashima Yuhodo Trail & Tensodo",
                "link_foto": "https://google.com",
                "descrizione": "Un breve e meraviglioso sentiero costiero. Arriverai sopra la spettacolare Grotta Tensodo, dove un foro circolare nel soffitto roccioso fa filtrare la luce creando un'acqua azzurro brillante."
            }
        ],
        "Cape Ose": [
            {
                "titolo": "⛩️ Cape Ose (Osezaki)",
                "link_foto": "https://google.com",
                "descrizione": "La punta nord-occidentale di Izu. Offre una vista cartolina del Monte Fuji sopra il mare. Visita l'antico santuario dei pescatori e il laghetto misterioso di acqua dolce circondato dal mare salato."
            }
        ],
        "Tsumago-juku": [
            {
                "titolo": "🏮 Antica Tsumago-juku",
                "link_foto": "https://google.com",
                "descrizione": "Un vero e proprio salto nel tempo nell'era Edo dei samurai. Le auto sono vietate, i fili elettrici interrati e le locande in legno tradizionali si illuminano la sera solo con lanterne di carta."
            }
        ],
        "Seki Museum": [
            {
                "titolo": "⚔️ Seki Swordsmith Museum",
                "link_foto": "https://google.com",
                "descrizione": "La capitale mondiale delle lame. Esplora la storia della forgia delle Katane dei samurai e fai acquisti di coltelli da cucina professionali nella adiacente Cutlery Hall."
            }
        ],
        "Kyoto": [
            {
                "titolo": "⛩️ Fushimi Inari-taisha",
                "link_foto": "https://google.com",
                "descrizione": "Il celeberrimo sentiero montano protetto da oltre 10.000 torii rosso scarlatto dedicati al dio del riso e dell'agricoltura. Consiglio: cammina presto al mattino per evitare la folla."
            },
            {
                "titolo": "🏯 Kinkaku-ji (Il Tempio d'Oro)",
                "link_foto": "https://google.com",
                "descrizione": "Uno dei monumenti più famosi al mondo: un padiglione zen interamente ricoperto di foglie d'oro splendenti che si riflette in modo simmetrico sul laghetto dello specchio d'acqua circostante."
            }
        ],
        "Adachi & Motonosumi": [
            {
                "titolo": "🖼️ Adachi Museum of Art",
                "link_foto": "https://google.com",
                "descrizione": "Votato per vent'anni consecutivi come il giardino più bello del Giappone. Le ampie vetrate del museo incorniciano la natura esterna trasformandola in quadri viventi in continuo mutamento."
            },
            {
                "titolo": "🦊 Motonosumi Shrine",
                "link_foto": "https://google.com",
                "descrizione": "Spettacolare tunnel di 123 torii rossi che serpeggia su una scogliera nera di fronte all'oceano blu. Sfida te stesso a lanciare una moneta nella scatola delle offerte montata a 5 metri d'altezza!"
            }
        ],
        "Hiroshima": [
            {
                "titolo": "⛩️ Isola Sacra di Miyajima",
                "link_foto": "https://google.com",
                "descrizione": "Prendi il traghetto per vedere il maestoso ed enorme Torii di legno che sembra fluttuare sulle acque dell'oceano durante l'alta marea. Attento ai cervi liberi che girano sull'isola!"
            }
        ],
        "Tokyo Finale": [
            {
                "titolo": "🔮 teamLab & Odaiba",
                "link_foto": "https://google.com",
                "descrizione": "Il volto iper-tecnologico di Tokyo. Esplora le stanze d'arte digitale immersiva prima di spostarti sull'isola di Odaiba per vedere la statua del robot Gundam gigante."
            },
            {
                "titolo": "🚦 Incrocio di Shibuya & Shibuya Sky",
                "link_foto": "https://google.com",
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
                # Descrizione testuale
                st.write(tappa["descrizione"])
                
                # Link cliccabile in perfetto stile Markdown per aprire le foto su internet
                st.markdown(f"🔗 **[Clicca qui per vedere le foto su internet]({tappa['link_foto']})**")
                
                # Checkbox per lo stato della visita
                st.checkbox("Segna come visitato", key=f"fatto_{macro_zona}_{index}")

st.markdown("<br><p style='text-align: center; color: gray; font-size: 11px;'>Tocca i titoli per aprire i dettagli</p>", unsafe_allow_html=True)
