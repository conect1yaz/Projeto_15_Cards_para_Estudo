
import streamlit as st
import json
import html
from random import choice


# ============================================================
# CONFIGURAÇÕES
# ============================================================

st.set_page_config(
    page_title="Meus Cards | Study Cards",
    page_icon="📚",
    layout="wide"
)

st.session_state.setdefault("dados", {})
st.session_state.setdefault("carregado", False)
st.session_state.setdefault("pergunta", None)


# ============================================================
# IDENTIDADE VISUAL
# ============================================================

st.markdown("""
<style>

/* CORES ROXO E CIANO PASTEL */
.card .upper-part-face {
    background: #E9DDFC !important;
    color: #70558F !important;
}

.card .upper-part-back {
    background: #DDF5F7 !important;
    color: #527F87 !important;
}

.card .lower-part-face {
    background: #DCCCF5 !important;
    color: #70558F !important;
}

.card .lower-part-back {
    background: #C9EEF2 !important;
    color: #527F87 !important;
}

/* FUNDO GERAL */
.stApp {
    background: linear-gradient(
        135deg,
        #F8F3FF 0%,
        #FFF5FA 55%,
        #F0FAFF 100%
    );
    color: #55466F;
}

/* ÁREA PRINCIPAL */
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

p {
    color: #786C89;
}

/* CABEÇALHO */
.cards-header {
    background: linear-gradient(
        120deg,
        #E9DDFC,
        #FCE5F0,
        #DDF5F7
    );
    border: 1px solid #E9DDF7;
    border-radius: 27px;
    padding: 32px;
    margin-bottom: 30px;
    box-shadow: 0 8px 24px rgba(128, 99, 164, 0.08);
    position: relative;
    overflow: hidden;
}

.cards-header::after {
    content: "✎";
    position: absolute;
    right: 38px;
    bottom: 5px;
    font-size: 85px;
    color: rgba(255,255,255,0.65);
    transform: rotate(-18deg);
}

.cards-tag {
    display: inline-block;
    background: rgba(255,255,255,0.7);
    color: #8567A6;
    padding: 7px 14px;
    border-radius: 25px;
    font-size: 11px;
    font-weight: bold;
    letter-spacing: 1.2px;
}

/* CENTRALIZAR O CARD NA PÁGINA */
.card {
    margin-left: auto !important;
    margin-right: auto !important;
}

.cards-header h1 {
    color: #70558F !important;
    font-size: 35px;
    margin: 17px 0 10px 0;
}

.cards-header p {
    color: #786C89;
    font-size: 15px;
    line-height: 1.7;
    max-width: 650px;
    margin-bottom: 0;
}

/* ETIQUETAS DAS SEÇÕES */
.section-label {
    color: #A184C4;
    font-size: 11px;
    font-weight: bold;
    letter-spacing: 2px;
    margin-bottom: 8px;
}

/* CARDS DE INFORMAÇÃO */
.info-card {
    background: rgba(255,255,255,0.82);
    border: 1px solid #E9DDF7;
    border-radius: 19px;
    padding: 20px;
    min-height: 115px;
    box-shadow: 0 5px 15px rgba(128,99,164,0.05);
}

.info-icon {
    font-size: 25px;
    margin-bottom: 9px;
}

.info-title {
    color: #80649E;
    font-weight: bold;
    font-size: 14px;
}

.info-description {
    color: #897D98;
    font-size: 12px;
    line-height: 1.6;
    margin-top: 5px;
}

/* DICAS */
.study-tip {
    background: #F0FAFF;
    border-left: 4px solid #A9DDE3;
    padding: 16px 19px;
    border-radius: 12px;
    color: #64858A;
    font-size: 13px;
    line-height: 1.7;
    margin: 18px 0 24px 0;
    box-shadow: 0 4px 14px rgba(128,99,164,0.04);
}

/* ÁREA DE UPLOAD */
div[data-testid="stFileUploader"] {
    background: linear-gradient(
        145deg,
        #FFFFFF,
        #FBF7FF
    );
    border: 2px dashed #CDB5EA;
    border-radius: 21px;
    padding: 20px;
    box-shadow: 0 5px 18px rgba(128,99,164,0.05);
    transition: all 0.3s ease;
}

div[data-testid="stFileUploader"]:hover {
    border-color: #B58BD9;
    background: #FDF9FF;
}

div[data-testid="stFileUploader"] label {
    color: #80649E;
    font-weight: 700;
}

div[data-testid="stFileUploader"] button {
    background: #E9DDFC !important;
    color: #70558F !important;
    border: 1px solid #D5C1EE !important;
    border-radius: 12px !important;
}

/* BOTÕES */
.stButton > button {
    background: linear-gradient(
        120deg,
        #DCC9F7,
        #F5D8E9
    ) !important;
    color: #624B82 !important;
    border: 1px solid #D7C0ED !important;
    border-radius: 14px !important;
    padding: 11px 20px !important;
    font-weight: 700 !important;
    transition: all 0.25s ease !important;
    box-shadow: 0 4px 12px rgba(128,99,164,0.08);
}

.stButton > button:hover {
    transform: translateY(-3px);
    border-color: #C5A8E4 !important;
    box-shadow: 0 8px 17px rgba(128,99,164,0.13);
}

/* INDICADORES */
.stat-card {
    background: rgba(255,255,255,0.85);
    border: 1px solid #E9DDF7;
    border-radius: 17px;
    padding: 17px;
    text-align: center;
    box-shadow: 0 4px 13px rgba(128,99,164,0.05);
}

.stat-number {
    color: #8063A5;
    font-size: 25px;
    font-weight: bold;
}

.stat-label {
    color: #9684A8;
    font-size: 12px;
    margin-top: 4px;
}

/* MENSAGENS */
div[data-testid="stAlert"] {
    border-radius: 15px;
}

/* PAINEL DE APRENDIZADO */
.learning-panel {
    background: linear-gradient(
        120deg,
        #F2EAFE,
        #FFF0F6,
        #EAF9FA
    );
    border: 1px solid #E9DDF7;
    border-radius: 20px;
    padding: 21px;
    text-align: center;
    margin: 22px 0;
}

.learning-title {
    color: #A184C4;
    font-size: 12px;
    font-weight: bold;
    letter-spacing: 2px;
}

.learning-description {
    color: #786C89;
    font-size: 14px;
    margin-top: 8px;
}

/* RODAPÉ */
.footer-cards {
    text-align: center;
    padding: 20px;
    color: #A18CB9;
    font-size: 13px;
    line-height: 1.8;
}

/* SEPARADORES */
hr {
    border: none;
    border-top: 2px dashed #E4D5F2;
    margin: 28px 0;
}

/* RESPONSIVIDADE */
@media (max-width: 700px) {

    .cards-header {
        padding: 23px;
    }

    .cards-header h1 {
        font-size: 27px;
    }

    .cards-header::after {
        font-size: 48px;
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
<div class="cards-header">

    <span class="cards-tag">
        ✦ SEU CANTINHO DE ESTUDOS
    </span>

    <h1>📚 Meus Cards</h1>

    <p>
        Um pouquinho de estudo por vez!
        Organize suas perguntas, descubra novas respostas
        e teste seus conhecimentos de uma maneira leve e divertida.
    </p>

</div>
""")


# ============================================================
# APRESENTAÇÃO DA ÁREA
# ============================================================

st.html("""
<div class="section-label">
    ✧ SEU ESPAÇO DE APRENDIZADO
</div>

<h2 style="margin-top:5px;">
    Vamos preparar seus estudos?
</h2>

<p style="font-size:14px; line-height:1.7;">
    Carregue um arquivo com suas perguntas e respostas
    para começar uma nova sessão de aprendizado.
</p>
""")


# ============================================================
# INFORMAÇÕES
# ============================================================

c1, c2, c3 = st.columns(3, gap="medium")

with c1:
    st.html("""
    <div class="info-card">
        <div class="info-icon">📂</div>
        <div class="info-title">Carregue</div>
        <div class="info-description">
            Escolha seu arquivo JSON com perguntas e respostas.
        </div>
    </div>
    """)

with c2:
    st.html("""
    <div class="info-card">
        <div class="info-icon">🧠</div>
        <div class="info-title">Pratique</div>
        <div class="info-description">
            Tente responder antes de revelar o conteúdo.
        </div>
    </div>
    """)

with c3:
    st.html("""
    <div class="info-card">
        <div class="info-icon">🌷</div>
        <div class="info-title">Evolua</div>
        <div class="info-description">
            Revise seus conhecimentos no seu próprio ritmo.
        </div>
    </div>
    """)


# ============================================================
# ÁREA DE UPLOAD
# ============================================================

st.markdown("---")

st.html("""
<div class="section-label">
    ✦ PRIMEIRO PASSO
</div>

<h3>Escolha seus materiais</h3>
""")

st.markdown("""
<div class="study-tip">
    ✏️ Selecione um arquivo <b>.json</b> com suas perguntas
    e respostas. Você também pode criar seus próprios materiais
    na aba de geração com inteligência artificial.
</div>
""", unsafe_allow_html=True)


arquivo = st.file_uploader(
    "📁 Escolha seu arquivo de cards",
    type=["json"],
    help="Selecione um arquivo JSON gerado pelo Study Cards."
)


if arquivo is not None:

    if st.button("✨ Carregar meus cards", use_container_width=True):

        try:

            cards = json.load(arquivo)

            if not isinstance(cards, dict) or not cards:
                raise ValueError(
                    "O arquivo não possui perguntas e respostas válidas."
                )

            if not all(
                isinstance(p, str) and isinstance(r, str)
                for p, r in cards.items()
            ):
                raise ValueError(
                    "O arquivo precisa conter perguntas e respostas em texto."
                )

            st.session_state["dados"] = cards
            st.session_state["carregado"] = True
            st.session_state["pergunta"] = choice(list(cards.keys()))

            st.rerun()

        except Exception as e:
            st.error(f"Não foi possível carregar o arquivo: {e}")


# ============================================================
# EXIBIÇÃO DOS CARDS
# ============================================================

if st.session_state.get("carregado", False):

    dados = st.session_state["dados"]

    if dados:

        pergunta = st.session_state["pergunta"]
        resposta = dados[pergunta]

        quantidade = len(dados)

        st.markdown("---")

        # MENSAGEM DE SUCESSO

        st.success("Tudo pronto! Seus materiais foram carregados com sucesso. ♡")

        # INDICADORES

        st.html("""
        <div class="section-label">
            ✧ SEU PROGRESSO DE ESTUDO
        </div>
        """)

        col1, col2, col3 = st.columns(3, gap="medium")

        with col1:
            st.html(f"""
            <div class="stat-card">
                <div class="stat-number">{quantidade}</div>
                <div class="stat-label">Cards disponíveis</div>
            </div>
            """)

        with col2:
            st.html("""
            <div class="stat-card">
                <div class="stat-number">♡</div>
                <div class="stat-label">Aprenda no seu ritmo</div>
            </div>
            """)

        with col3:
            st.html("""
            <div class="stat-card">
                <div class="stat-number">✦</div>
                <div class="stat-label">Uma pergunta por vez</div>
            </div>
            """)

        # PAINEL DE APRENDIZADO

        st.html("""
        <div class="learning-panel">

            <div class="learning-title">
                ✦ SEU MOMENTO DE APRENDER ✦
            </div>

            <div class="learning-description">
                Respire, pense na resposta e descubra
                o quanto você já sabe!
            </div>

        </div>
        """)

        # CARREGAR CSS ORIGINAL DOS CARDS
        # NÃO ALTERAR O ARQUIVO style.txt

        with open("style.txt", "r", encoding="utf-8") as f:
            estilo = f.read()

        st.markdown(estilo, unsafe_allow_html=True)

        # CONTEÚDO DO CARD

        pergunta_segura = html.escape(pergunta)
        resposta_segura = html.escape(resposta)

        st.html(f"""
        <div style="
            width: 100%;
            display: flex;
            justify-content: center;
            align-items: center;
        ">
            <div class="card">
                <div class="upper-part">
                    <div class="upper-part-face">{pergunta_segura}</div>
                    <div class="upper-part-back">{resposta_segura}</div>
                </div>
                <div class="lower-part">
                    <div class="lower-part-face">Pergunta</div>
                    <div class="lower-part-back">Resposta</div>
                </div>
            </div>
        </div>
        """)

        # INSTRUÇÃO

        st.markdown("""
        <p style="
            text-align:center;
            color:#9A80B7;
            font-size:13px;
            margin-top:18px;
        ">
            💡 Clique no card para revelar a resposta!
        </p>
        """, unsafe_allow_html=True)

        st.markdown("")

        # PRÓXIMA PERGUNTA

        if st.button(
            "🔄 Escolher outra pergunta",
            use_container_width=True
        ):

            perguntas = list(dados.keys())

            if len(perguntas) > 1:
                perguntas.remove(pergunta)

            st.session_state["pergunta"] = choice(perguntas)

            st.rerun()


# ============================================================
# RODAPÉ
# ============================================================

st.markdown("---")

st.html("""
<div class="footer-cards">

    Feito com carinho ♡ e uma ajudinha do Teteco 🐈

    <br>

    <span style="
        font-size:11px;
        letter-spacing:1px;
    ">
        STUDY CARDS • SEU CANTINHO DE APRENDIZADO
    </span>

</div>
""")
