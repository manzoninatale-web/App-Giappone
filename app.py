import streamlit as st

# Configurazione della pagina stile iPhone
st.set_page_config(
    page_title="Giappone On-The-Road",
    page_icon="🇯🇵",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# CSS personalizzato per rendere l'interfaccia identica a un'app iOS nativa
st.markdown("""
    <style>
    .main { background-color: #f2f2f7; }
    h1 { color: #1c1c1e; font-family: -apple-system, BlinkMacSystemFont, sans-serif; font-weight: 700; text-align: center; }
    .stTabs [data-baseweb="tab-list"] { gap: 8px; justify-content: center; }
    .stTabs [data-baseweb="tab"] {
        background-color: #ffffff; border-radius: 12px; padding: 10px 16px;
        box-shadow: 0px 1px 3px rgba(0,0,0,0.1); font-weight: 600; color: #007aff;
    }
    .stTabs [aria-selected="true"] { background-color: #007aff !important; color: white !important; }
    div.浪漫 card {
        background-color: white; padding: 16px; border-radius: 16px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05); margin-bottom: 12px;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🇯🇵 Il Mio Viaggio in Giappone")
st.write("### 🚗 Itinerario Dinamico Modificabile")

# Inizializzazione del database interno dell'app (se vuoto, carica il tuo itinerario)
if "itinerario" not in st.session_state:
    st.session_state.itinerario = {
        "Giorno 1-2: Izu & Mt. Omuro": [
            "Ritiro auto a Tokyo e guida panoramica sulla Izu Skyline.",
            "Salita in seggiovia sul cratere del Monte Omuro (Ike, Ito).",
            "Visita alle scogliere della Costa di Jogasaki.",
            "Notte in Ryokan tradizionale con Onsen."
        ],
        "Giorno 3: Dogashima Trail": [
            "Guida verso la costa ovest attraverso le cascate di Kawazu.",
            "Passeggiata sul Dogashima Yuhodo Hiking Trail.",
            "Esplorazione dall'alto della grotta marina Tensodo Cave.",
            "Tramonto d'oro sul mare di Suruga."
        ],
        "Giorno 4: Cape Ose & Fuji": [
            "Guida lungo la Prefectural Road 17 con vista sul Monte Fuji.",
            "Esplorazione di Cape Ose (Santuario e foresta di ginepri).",
            "Osservazione del misterioso laghetto di acqua dolce Kami-ike."
        ],
        "Giorno 5: Tsumago-juku (Alpi)": [
            "Road trip verso la Valle del Kiso (Prefettura di Nagano).",
            "Pranzo a base di Soba noodles e Gohei Mochi nel villaggio.",
            "Passeggiata nel tempo lungo la via pedonale dell'era Edo.",
            "Notte in una Minshuku illuminata dalle lanterne."
        ],
        "Giorno 6: Seki Katana Museum": [
            "Guida verso Seki (Gifu), la capitale delle lame dei samurai.",
            "Visita al Seki Swordsmith Museum (9-1 Minamikase).",
            "Acquisti di coltelli artigianali alla Gifu Cutlery Hall.",
            "Sosta fotografica al suggestivo 'Laghetto di Monet'."
        ],
        "Giorno 7-8: Kyoto": [
            "Auto parcheggiata in hotel. Spostamenti in metro e a piedi.",
            "Giorno 7: Ginkaku-ji, Sentiero Filosofia, Kiyomizu-dera e Gion.",
            "Giorno 8: Fushimi Inari (torii rossi), Kinkaku-ji (Tempio d'Oro), Arashiyama."
        ],
        "Giorno 9-10: Adachi & Motonosumi": [
            "Giorno 9: Guida verso ovest fino all'Adachi Museum of Art (Giardini Zen).",
            "Giorno 10: Arrivo a Motonosumi Shrine (123 Torii rossi sulla scogliera).",
            "Lancio della monetina nella scatola delle offerte a 5 metri d'altezza."
        ],
        "Giorno 11-12: Hiroshima & Rientro": [
            "Traghetto per l'isola sacra di Miyajima e il torii galleggiante.",
            "Cena con Okonomiyaki e riconsegna dell'auto a Hiroshima Station.",
            "Visita al Museo della Pace e Shinkansen super-veloce per Tokyo."
        ],
        "Giorno 13-16: Tokyo Finale": [
            "G13: Arte digitale al teamLab, isola di Odaiba e lusso a Ginza.",
            "G14: Santuario Meiji, Harajuku, incrocio di Shibuya e Shibuya Sky.",
            "G15: Tempio Senso-ji ad Asakusa, quartiere nerd Akihabara e mercato Ueno.",
            "G16: Colazione street food a Tsukiji e shopping souvenir dell'ultimo minuto."
        ]
    }

# INTERFACCIA APP: Navigazione a Tab (stile iOS)
tabs = st.tabs(list(st.session_state.itinerario.keys()))

for i, (giorno, tappe) in enumerate(st.session_state.itinerario.items()):
    with tabs[i]:
        st.write(f"### 📍 {giorno}")
        
        # Mostra le tappe attuali con checkbox per segnarle come fatte durante il viaggio
        tappe_aggiornate = []
        for index, tappa in enumerate(tappe):
            fatto = st.checkbox(tappa, key=f"check_{giorno}_{index}")
            tappe_aggiornate.append(tappa)
            
        st.markdown("---")
        
        # FUNZIONE AGGIUNTIVA: Pannello per modificare o espandere le tappe direttamente dall'iPhone
        with st.expander("⚙️ Gestisci tappe di questa giornata"):
            nuova_tappa = st.text_input("Aggiungi una nuova attrazione:", key=f"add_{giorno}")
            if st.button("Inserisci", key=f"btn_add_{giorno}"):
                if nuova_tappa:
                    st.session_state.itinerario[giorno].append(nuova_tappa)
                    st.rerun()
            
            tappa_da_rimuovere = st.selectbox("Elimina una tappa:", ["---"] + tappe, key=f"del_{giorno}")
            if st.button("Rimuovi Selezionata", key=f"btn_del_{giorno}"):
                if tappa_da_rimuovere != "---":
                    st.session_state.itinerario[giorno].remove(tappa_da_rimuovere)
                    st.rerun()
