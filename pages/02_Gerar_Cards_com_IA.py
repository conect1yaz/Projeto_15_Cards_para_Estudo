
import streamlit as st
from gerador import Gerador
import json

# ============================================================
# CONFIGURAÇÕES INICIAIS
# ============================================================

st.set_page_config(
    page_title="Gerador de Cards | Study Cards",
    page_icon="🧠",
    layout="wide"
)

gerador = Gerador("openai/gpt-oss-120b")

st.session_state.setdefault("dados", None)

# ============================================================
# IDENTIDADE VISUAL
# ============================================================

st.markdown("""
<style>

/* FUNDO E ÁREA PRINCIPAL */
.stApp {
    background: linear-gradient(
        135deg,
        #F8F3FF 0%,
        #FFF5FA 55%,
        #F0FAFF 100%
    );
    color: #55466F;
}

.block-container {
    max-width: 1050px;
    padding-top: 2rem;
    padding-bottom: 4rem;
}

/* TÍTULOS */
h1, h2, h3 {
    color: #70558F !important;
    font-family: 'Trebuchet MS', sans-serif;
}

p, label {
    color: #786C89;
}

/* CABEÇALHO */
.generator-header {
    background: linear-gradient(
        120deg,
        #E9DDFC,
        #FCE5F0,
        #DDF5F7
    );
    border: 1px solid #E9DDF7;
    border-radius: 26px;
    padding: 30px;
    margin-bottom: 25px;
    box-shadow: 0 8px 24px rgba(128, 99, 164, 0.08);
    position: relative;
    overflow: hidden;
}

.generator-tag {
    display: inline-block;
    background: rgba(255,255,255,0.7);
    color: #8567A6;
    padding: 7px 14px;
    border-radius: 25px;
    font-size: 11px;
    font-weight: bold;
    letter-spacing: 1.2px;
}

.generator-header h1 {
    color: #70558F !important;
    font-size: 34px;
    margin: 17px 0 9px 0;
}

.generator-header p {
    color: #786C89;
    font-size: 15px;
    line-height: 1.7;
    margin-bottom: 0;
    max-width: 650px;
}

.generator-header::after {
    content: "✧";
    position: absolute;
    right: 35px;
    bottom: 5px;
    font-size: 85px;
    color: rgba(255,255,255,0.6);
    transform: rotate(15deg);
}

/* CAMPO DE TEXTO */
.stTextInput input {
    background: #FFFFFF !important;
    border: 1px solid #DCC9F7 !important;
    border-radius: 14px !important;
    color: #624B82 !important;
    padding: 13px !important;
}

.stTextInput input:focus {
    border-color: #B99AD9 !important;
    box-shadow: 0 0 0 2px rgba(185,154,217,0.15);
}

/* BOTÕES */
.stButton > button,
.stDownloadButton > button {
    background: linear-gradient(
        120deg,
        #DCC9F7,
        #F5D8E9
    ) !important;
    color: #624B82 !important;
    border: 1px solid #D7C0ED !important;
    border-radius: 14px !important;
    padding: 10px 20px !important;
    font-weight: 700 !important;
    transition: all 0.25s ease !important;
    box-shadow: 0 4px 12px rgba(128, 99, 164, 0.08);
}

.stButton > button:hover,
.stDownloadButton > button:hover {
    transform: translateY(-3px);
    border-color: #C5A8E4 !important;
    box-shadow: 0 8px 17px rgba(128, 99, 164, 0.13);
}

/* EXEMPLOS */
.example-card {
    background: rgba(255,255,255,0.8);
    border: 1px solid #E9DDF7;
    border-radius: 16px;
    padding: 15px;
    min-height: 90px;
    box-shadow: 0 4px 12px rgba(128,99,164,0.04);
}

.example-card strong {
    color: #80649E;
    font-size: 14px;
}

.example-card p {
    color: #897D98;
    font-size: 12px;
    margin-top: 6px;
    margin-bottom: 0;
}

/* DICA */
.study-tip {
    background: #F0FAFF;
    border-left: 4px solid #A9DDE3;
    padding: 15px 18px;
    border-radius: 12px;
    color: #64858A;
    font-size: 13px;
    line-height: 1.7;
    margin: 20px 0;
}

/* RESULTADOS */
.result-header {
    background: linear-gradient(
        120deg,
        #F0EAFE,
        #FFF0F6,
        #EAF9FA
    );
    border: 1px solid #E9DDF7;
    border-radius: 18px;
    padding: 20px;
    margin: 20px 0;
}

.result-header h2 {
    margin: 0;
    font-size: 23px;
}

.result-header p {
    margin-top: 8px;
    margin-bottom: 0;
    font-size: 13px;
}

/* SEPARADORES */
hr {
    border: none;
    border-top: 2px dashed #E4D5F2;
    margin: 25px 0;
}

/* POPOVER */
div[data-testid="stPopover"] button {
    border-radius: 13px;
}

/* MENSAGENS */
div[data-testid="stAlert"] {
    border-radius: 14px;
}

/* RESPONSIVIDADE */
@media (max-width: 700px) {
    .generator-header {
        padding: 22px;
    }

    .generator-header h1 {
        font-size: 27px;
    }

    .generator-header::after {
        font-size: 45px;
        right: 15px;
    }
}

footer {
    visibility: hidden;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# CABEÇALHO
# ============================================================

st.html("""
<div class="generator-header">

    <span class="generator-tag">
        ✦ INTELIGÊNCIA ARTIFICIAL • STUDY CARDS
    </span>

    <h1>Vamos criar seus cards? 🧠</h1>

    <p>
        Escolha um assunto, deixe a inteligência artificial
        preparar suas perguntas e transforme qualquer conteúdo
        em uma nova oportunidade de aprendizado.
    </p>

</div>
""")


# ============================================================
# EXEMPLOS DE TEMAS
# ============================================================

st.markdown("### ✨ O que você gostaria de estudar?")

st.markdown("""
<p style="font-size:14px;">
    Digite um assunto abaixo para começar a criar seus materiais.
</p>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2, gap="medium")

with col1:
    st.html("""
    <div class="example-card">
        <strong>📜 História</strong>
        <p>Revolução Francesa e seus principais acontecimentos.</p>
    </div>
    """)

with col2:
    st.html("""
    <div class="example-card">
        <strong>💻 Programação</strong>
        <p>Fundamentos de Python e lógica de programação.</p>
    </div>
    """)

col3, col4 = st.columns(2, gap="medium")

with col3:
    st.html("""
    <div class="example-card">
        <strong>🫀 Biologia</strong>
        <p>Anatomia do coração humano.</p>
    </div>
    """)

with col4:
    st.html("""
    <div class="example-card">
        <strong>🌎 Inglês</strong>
        <p>Verbos irregulares e tempos verbais.</p>
    </div>
    """)


# ============================================================
# CAMPO DE TEMA
# ============================================================

st.markdown("")

tema = st.text_input(
    "📌 Qual será o tema dos seus cards?",
    placeholder="Ex.: Causas da Primeira Guerra Mundial..."
)

st.markdown("""
<div class="study-tip">
    💡 <b>Dica do Teteco:</b> quanto mais específico for o tema,
    mais direcionadas serão as perguntas.
    Em vez de escrever apenas "História", experimente
    "Causas da Primeira Guerra Mundial".
</div>
""", unsafe_allow_html=True)


# ============================================================
# BOTÃO DE GERAÇÃO
# ============================================================

if st.button("✨ Gerar meus cards", use_container_width=True):

    if not tema.strip():
        st.warning("Digite um tema antes de gerar seus cards!")

    else:
        st.session_state["dados"] = None

        with st.spinner("🐱 Teteco está preparando seus materiais..."):

            try:
                resultado = gerador.gerar_perguntas(tema.strip())

                if isinstance(resultado, Exception):
                    raise resultado

                if not isinstance(resultado, dict) or not resultado:
                    raise ValueError(
                        "A IA não retornou um conjunto válido de perguntas."
                    )

                st.session_state["dados"] = resultado

            except Exception as e:
                st.error(
                    f"Não foi possível gerar os cards. "
                    f"Verifique sua conexão e tente novamente. Detalhes: {e}"
                )


# ============================================================
# EXIBIR RESULTADOS
# ============================================================

dados = st.session_state.get("dados")

if dados:

    st.markdown("---")

    st.html("""
    <div class="result-header">

        <h2>✦ Seus cards estão prontos!</h2>

        <p>
            Confira as perguntas e respostas abaixo.
            Depois, salve seu arquivo para começar a estudar.
        </p>

    </div>
    """)

    st.success(f"🎉 Foram preparados {len(dados)} cards para seus estudos!")

    # EXIBIÇÃO DAS PERGUNTAS E RESPOSTAS

    for i, (pergunta, resposta) in enumerate(dados.items(), start=1):

        with st.container(border=True):

            st.markdown(
                f"<span style='color:#A184C4; font-size:12px; "
                f"font-weight:bold; letter-spacing:1px;'>"
                f"CARD {i:02d}</span>",
                unsafe_allow_html=True
            )

            st.markdown(f"### 📝 {pergunta}")

            st.markdown("""
            <div style="
                background:#F6F1FC;
                border-left:4px solid #CDB5EA;
                border-radius:12px;
                padding:15px;
                color:#69577E;
                line-height:1.7;
            ">
                <b style="color:#8567A6;">✦ Resposta</b>
            </div>
            """, unsafe_allow_html=True)

            st.markdown(resposta)

    # ========================================================
    # AVISO
    # ========================================================

    st.markdown("""
    <div class="study-tip">
        📚 <b>Não esqueça:</b> confira as informações geradas
        pela IA antes de utilizá-las nos seus estudos.
    </div>
    """, unsafe_allow_html=True)

    # ========================================================
    # DOWNLOAD
    # ========================================================

    st.markdown("### 💾 Salve seus materiais")

    st.markdown("""
    <p style="font-size:14px;">
        Baixe suas perguntas e respostas em JSON.
        Depois, carregue o arquivo na aba Meus Cards!
    </p>
    """, unsafe_allow_html=True)

    with st.popover("📁 Salvar meus cards", use_container_width=True):

        nome_arquivo = st.text_input(
            "Nome do arquivo",
            value="meus_cards"
        ).strip().replace(" ", "_")

        if not nome_arquivo:
            nome_arquivo = "meus_cards"

        st.caption(f"Arquivo: {nome_arquivo}.json")

        st.download_button(
            label="⬇️ Baixar arquivo JSON",
            data=json.dumps(
                dados,
                indent=4,
                ensure_ascii=False
            ),
            file_name=f"{nome_arquivo}.json",
            mime="application/json",
            use_container_width=True
        )


# ============================================================
# RODAPÉ
# ============================================================

st.markdown("---")

st.html("""
<div style="
    text-align:center;
    padding:18px;
    color:#A18CB9;
    font-size:13px;
">
    ✨ Criando novas formas de aprender com Teteco 🐈
    <br>
    <span style="font-size:11px;">
        STUDY CARDS • SEU CANTINHO DE APRENDIZADO
    </span>
</div>
""")
