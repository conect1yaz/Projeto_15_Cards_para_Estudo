
import streamlit as st
import base64

# ==========================================================
# CONFIGURAÇÕES
# ==========================================================

st.set_page_config(
    page_title="Study Cards | Estude com Teteco",
    page_icon="🐱",
    layout="wide"
)

# ==========================================================
# ESTILO VISUAL
# ==========================================================

st.markdown("""
<style>

/* FUNDO GERAL */
.stApp {
    background: linear-gradient(135deg, #F8F3FF 0%, #FFF5FA 55%, #F0FAFF 100%);
    color: #55466F;
}

.block-container {
    max-width: 1150px;
    padding-top: 2.5rem;
    padding-bottom: 4rem;
}

/* SIDEBAR */
[data-testid="stSidebar"] {
    background: #EDE4FA;
    border-right: 1px solid #E3D5F4;
}

[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] p {
    color: #66517F;
}

/* TÍTULOS */
h1, h2, h3 {
    color: #70558F !important;
    font-family: 'Trebuchet MS', sans-serif;
}

p {
    color: #786C89;
}

/* BOTÕES */
.stButton > button,
.stPageLink > a {
    background: #DCC9F7;
    color: #624B82;
    border: 1px solid #CFB9F0;
    border-radius: 15px;
    padding: 0.65rem 1rem;
    font-weight: 600;
    transition: all 0.25s ease;
}

.stButton > button:hover,
.stPageLink > a:hover {
    background: #F4D6E8;
    color: #74517D;
    border-color: #E8BBD7;
    transform: translateY(-3px);
}

/* CARDS DA PÁGINA INICIAL */
.study-card {
    background: rgba(255, 255, 255, 0.78);
    border: 1px solid #E9DDF7;
    border-radius: 22px;
    padding: 25px;
    min-height: 190px;
    box-shadow: 0 5px 18px rgba(128, 99, 164, 0.07);
    transition: all 0.3s ease;
}

.study-card:hover {
    transform: translateY(-6px);
    box-shadow: 0 12px 25px rgba(128, 99, 164, 0.13);
    border-color: #D7BDF1;
}

.study-icon {
    font-size: 35px;
    margin-bottom: 12px;
}

.study-card h3 {
    font-size: 19px;
    margin-bottom: 8px;
}

.study-card p {
    font-size: 14px;
    line-height: 1.6;
}

/* BOAS-VINDAS */
.hero {
    background: linear-gradient(120deg, #E9DDFC, #FCE5F0, #DDF5F7);
    border-radius: 28px;
    padding: 35px;
    margin: 20px 0 30px 0;
    border: 1px solid rgba(255,255,255,0.8);
    box-shadow: 0 8px 25px rgba(128, 99, 164, 0.08);
}

.hero-label {
    background: rgba(255,255,255,0.65);
    color: #8567A6;
    border-radius: 30px;
    padding: 7px 14px;
    font-size: 12px;
    font-weight: bold;
    letter-spacing: 1px;
}

.hero h1 {
    font-size: 37px;
    margin-top: 20px;
    margin-bottom: 10px;
}

.hero p {
    font-size: 16px;
    line-height: 1.7;
    max-width: 600px;
}

/* TETECO */
.teteco {
    background: rgba(255,255,255,0.72);
    border: 2px dashed #CDB5EA;
    border-radius: 25px;
    padding: 22px;
    text-align: center;
    box-shadow: 0 8px 22px rgba(128, 99, 164, 0.08);
}

.teteco-face {
    display: flex;
    justify-content: center;
    align-items: center;
}

.teteco-face img {
    width: 180px;
    height: 180px;
    object-fit: contain;
    animation: flutuar 3s ease-in-out infinite;
    filter: drop-shadow(0 8px 8px rgba(110, 80, 140, 0.12));
}

.teteco p {
    font-size: 14px;
    color: #80649E;
    font-weight: 600;
}

@keyframes flutuar {
    0%, 100% { transform: translateY(0); }
    50% { transform: translateY(-8px); }
}

/* DECORAÇÕES DE PAPELARIA */

/* Cards com aparência de papel */
.study-card {
    position: relative;
    overflow: hidden;
}

.study-card::after {
    content: "✦";
    position: absolute;
    right: 17px;
    top: 12px;
    color: #E5C9F0;
    font-size: 23px;
    transition: transform 0.3s ease;
}

.study-card:hover::after {
    transform: rotate(25deg) scale(1.3);
}

/* Pequeno efeito nos ícones */
.study-icon {
    display: inline-block;
    transition: transform 0.3s ease;
}

.study-card:hover .study-icon {
    transform: rotate(-8deg) scale(1.12);
}

/* Botões com movimento suave */
.stButton > button,
.stPageLink > a {
    box-shadow: 0 4px 10px rgba(128, 99, 164, 0.08);
}

.stButton > button:active,
.stPageLink > a:active {
    transform: scale(0.97);
}

/* Seletores com cantos arredondados */
div[data-baseweb="select"] > div {
    border-radius: 12px;
    border-color: #DCC9F7;
}

/* Campos de texto */
.stTextInput input,
.stTextArea textarea {
    border-radius: 12px;
    border-color: #DCC9F7;
}

/* DETALHES */
.section-label {
    color: #A184C4;
    font-size: 12px;
    font-weight: bold;
    letter-spacing: 2px;
}

hr {
    border-color: #E9DDF7;
}

footer {
    visibility: hidden;
}

/* RESPONSIVIDADE */
@media (max-width: 700px) {
    .hero {
        padding: 22px;
    }

    .hero h1 {
        font-size: 27px;
    }

    .teteco-face {
        font-size: 55px;
    }
}

</style>
""", unsafe_allow_html=True)


# ==========================================================
# CABEÇALHO
# ==========================================================

st.html("""
<div style="
    display:flex;
    justify-content:space-between;
    align-items:center;
    flex-wrap:wrap;
    gap:10px;
">
    <div style="font-size:25px; font-weight:800; color:#8063A5;">
        ✿ Study Cards
    </div>

    <div style="
        background:#FFFFFF;
        padding:9px 17px;
        border-radius:30px;
        color:#967DB1;
        font-size:13px;
        border:1px solid #E9DDF7;
    ">
        ♡ Seu cantinho de estudos
    </div>
</div>
""")


# ==========================================================
# HERO / BOAS-VINDAS
# ==========================================================

st.html("""
<div class="hero">
    <span class="hero-label">✦ SEU ESPAÇO DE APRENDIZADO ✦</span>

    <h1>Aprender pode ser divertido! ♡</h1>

    <p>
        Organize seus estudos, crie seus próprios cards e descubra
        uma maneira mais leve e interativa de aprender.
        Seu próximo aprendizado começa aqui!
    </p>
</div>
""")

# Carregar imagem do Teteco
with open("assets/teteco.png", "rb") as arquivo:
    teteco_base64 = base64.b64encode(arquivo.read()).decode()

# ==========================================================
# MASCOTE TETECO
# ==========================================================

col1, col2 = st.columns([1.7, 1], gap="large")

with col1:
    st.html("""
    <div style="padding:15px 5px;">
        <div class="section-label">✧ OLÁ, ESTUDANTE!</div>

        <h2 style="font-size:30px;">
            Que bom ter você por aqui!
        </h2>

        <p style="font-size:16px; line-height:1.8;">
            Está preparado para aprender alguma coisa nova?
            Escolha seus cards, teste sua memória e avance
            no seu próprio ritmo.
        </p>

        <div style="
            color:#A184C4;
            font-size:14px;
            margin-top:20px;
        ">
            ✎ Aprenda • Revise • Evolua
        </div>
    </div>
    """)

with col2:
    st.html(f"""
    <div class="teteco">
        <div class="teteco-face">
            <img
                src="data:image/png;base64,{teteco_base64}"
                style="width:180px; height:180px; object-fit:contain;"
            >
        </div>

        <h3 style="margin:5px 0;color:#8063A5;">
            Oi! Eu sou o Teteco!
        </h3>

        <p>
            Separei meus caderninhos.
            Vamos estudar juntos? ♡
        </p>

        <div style="font-size:22px;">✏️ 📚 ✨</div>
    </div>
    """)


# ==========================================================
# ÁREA DE NAVEGAÇÃO
# ==========================================================

st.markdown("---")

st.html("""
<div class="section-label">✦ POR ONDE COMEÇAMOS?</div>
<h2>Escolha sua próxima atividade</h2>
""")

c1, c2 = st.columns(2, gap="large")

with c1:
    st.html("""
    <div class="study-card">
        <div class="study-icon">📚</div>
        <h3>Meus Cards</h3>
        <p>
            Abra seus arquivos de perguntas e respostas
            e comece uma nova sessão de estudos.
        </p>
    </div>
    """)

    st.page_link(
        "pages/01_Cards.py",
        label="Abrir meus cards →",
        icon="📖",
    )

with c2:
    st.html("""
    <div class="study-card">
        <div class="study-icon">✨</div>
        <h3>Crie seus materiais</h3>
        <p>
            Transforme temas e conteúdos em materiais
            de estudo com a ajuda da inteligência artificial.
        </p>
    </div>
    """)

    st.info(
        "Encontre as opções de geração de cards no menu lateral."
    )


# ==========================================================
# COMO FUNCIONA
# ==========================================================

st.markdown("---")

st.html("""
<div class="section-label">✧ SEU GUIA DE ESTUDOS</div>
<h2>Como funciona?</h2>
""")

a, b, c = st.columns(3, gap="medium")

with a:
    st.markdown("""
    <div class="study-card">
        <div class="study-icon">📝</div>
        <h3>01. Prepare</h3>
        <p>Escolha um tema ou carregue seus próprios cards.</p>
    </div>
    """, unsafe_allow_html=True)

with b:
    st.markdown("""
    <div class="study-card">
        <div class="study-icon">🧠</div>
        <h3>02. Aprenda</h3>
        <p>Responda às perguntas e teste o que você sabe.</p>
    </div>
    """, unsafe_allow_html=True)

with c:
    st.markdown("""
    <div class="study-card">
        <div class="study-icon">🌟</div>
        <h3>03. Evolua</h3>
        <p>Revise os conteúdos e fortaleça sua memória.</p>
    </div>
    """, unsafe_allow_html=True)


# ==========================================================
# RODAPÉ
# ==========================================================

st.markdown("---")

st.html("""
<div style="
    text-align:center;
    padding:20px;
    color:#A18CB9;
    font-size:13px;
">
    Feito com carinho ♡ e uma ajudinha do Teteco 🐈
    <br>
    <span style="font-size:11px;">
        STUDY CARDS • SEU CANTINHO DE APRENDIZADO
    </span>
</div>
""")
