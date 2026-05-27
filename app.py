import streamlit as st

# ── 페이지 설정 ──────────────────────────────────────────────
st.set_page_config(
    page_title="자기소개 | My Portfolio",
    page_icon="👨‍💻",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── CSS 스타일 ────────────────────────────────────────────────
st.markdown("""
<style>
    /* 전체 배경 */
    .stApp {
        background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
    }

    /* 헤더 카드 */
    .profile-card {
        background: rgba(255,255,255,0.07);
        border: 1px solid rgba(255,255,255,0.15);
        backdrop-filter: blur(12px);
        border-radius: 20px;
        padding: 40px;
        text-align: center;
        margin-bottom: 24px;
        box-shadow: 0 8px 32px rgba(0,0,0,0.3);
    }
    .profile-avatar {
        font-size: 90px;
        line-height: 1;
        margin-bottom: 12px;
    }
    .profile-name {
        font-size: 2.4rem;
        font-weight: 800;
        color: #ffffff;
        margin: 0;
    }
    .profile-title {
        font-size: 1.1rem;
        color: #a78bfa;
        margin-top: 6px;
        letter-spacing: 2px;
        text-transform: uppercase;
    }
    .profile-bio {
        color: #cbd5e1;
        font-size: 1rem;
        margin-top: 16px;
        line-height: 1.8;
    }

    /* 섹션 카드 */
    .section-card {
        background: rgba(255,255,255,0.06);
        border: 1px solid rgba(255,255,255,0.1);
        border-radius: 16px;
        padding: 28px 32px;
        margin-bottom: 20px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.2);
    }
    .section-title {
        font-size: 1.3rem;
        font-weight: 700;
        color: #a78bfa;
        margin-bottom: 18px;
        border-bottom: 2px solid rgba(167,139,250,0.3);
        padding-bottom: 10px;
    }

    /* 스킬 배지 */
    .skill-badge {
        display: inline-block;
        background: linear-gradient(135deg, #6d28d9, #4f46e5);
        color: #fff;
        padding: 6px 14px;
        border-radius: 20px;
        font-size: 0.82rem;
        font-weight: 600;
        margin: 4px;
    }
    .skill-badge-secondary {
        background: linear-gradient(135deg, #0891b2, #0e7490);
    }
    .skill-badge-tertiary {
        background: linear-gradient(135deg, #059669, #047857);
    }

    /* 연락처 아이콘 */
    .contact-item {
        color: #cbd5e1;
        font-size: 0.95rem;
        margin: 10px 0;
        display: flex;
        align-items: center;
        gap: 10px;
    }

    /* 타임라인 */
    .timeline-item {
        border-left: 3px solid #6d28d9;
        padding-left: 20px;
        margin-bottom: 22px;
        position: relative;
    }
    .timeline-item::before {
        content: "●";
        color: #a78bfa;
        position: absolute;
        left: -11px;
        top: 0;
        font-size: 0.9rem;
    }
    .timeline-date {
        color: #a78bfa;
        font-size: 0.82rem;
        font-weight: 600;
        letter-spacing: 1px;
    }
    .timeline-title {
        color: #f1f5f9;
        font-size: 1.05rem;
        font-weight: 700;
        margin: 4px 0;
    }
    .timeline-sub {
        color: #94a3b8;
        font-size: 0.9rem;
    }

    /* 취미 카드 */
    .hobby-card {
        background: rgba(255,255,255,0.05);
        border-radius: 12px;
        padding: 16px;
        text-align: center;
        border: 1px solid rgba(255,255,255,0.08);
    }
    .hobby-icon { font-size: 2rem; }
    .hobby-label { color: #e2e8f0; font-size: 0.9rem; margin-top: 6px; }

    /* 진행 바 레이블 */
    .skill-label {
        color: #cbd5e1;
        font-size: 0.88rem;
        margin-bottom: 2px;
    }
    div[data-testid="stProgress"] > div > div {
        background: linear-gradient(90deg, #6d28d9, #a78bfa) !important;
        border-radius: 10px !important;
    }
    div[data-testid="stProgress"] > div {
        background: rgba(255,255,255,0.1) !important;
        border-radius: 10px !important;
    }

    /* 사이드바 */
    [data-testid="stSidebar"] {
        background: rgba(15,12,41,0.95);
        border-right: 1px solid rgba(255,255,255,0.1);
    }
    [data-testid="stSidebar"] .stMarkdown { color: #cbd5e1; }

    /* 메트릭 */
    [data-testid="stMetric"] {
        background: rgba(255,255,255,0.06);
        border-radius: 12px;
        padding: 16px;
        border: 1px solid rgba(255,255,255,0.1);
    }
    [data-testid="stMetricValue"] { color: #a78bfa !important; font-weight: 800; }
    [data-testid="stMetricLabel"] { color: #94a3b8 !important; }
</style>
""", unsafe_allow_html=True)

# ── 사이드바 ──────────────────────────────────────────────────
with st.sidebar:
    st.markdown("## 🧭 Navigation")
    menu = st.radio(
        "",
        ["🏠 홈", "💼 경력", "🛠 기술스택", "🎯 프로젝트", "📬 연락처"],
        label_visibility="collapsed",
    )
    st.markdown("---")
    st.markdown("### 📎 빠른 링크")
    st.markdown("[![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white)](https://github.com/sky940819-alt)")
    st.markdown("[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=flat&logo=linkedin&logoColor=white)](#)")
    st.markdown("---")
    st.caption("Made with ❤️ using Streamlit")


# ═══════════════════════════════════════════════════════════════
# 🏠 홈
# ═══════════════════════════════════════════════════════════════
if menu == "🏠 홈":
    # 프로필 헤더
    st.markdown("""
    <div class="profile-card">
        <div class="profile-avatar">👨‍💻</div>
        <p class="profile-name">홍길동</p>
        <p class="profile-title">Full-Stack Developer &amp; Data Engineer</p>
        <p class="profile-bio">
            안녕하세요! 데이터와 웹을 연결하는 개발자 <strong>홍길동</strong>입니다.<br>
            Python과 클라우드 기반 데이터 파이프라인, 그리고 사용자 중심의 웹 서비스를 개발합니다.<br>
            새로운 기술을 탐구하고 팀과 함께 성장하는 것을 즐깁니다. 🚀
        </p>
    </div>
    """, unsafe_allow_html=True)

    # 요약 지표
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.metric("경력", "5년+")
    with c2:
        st.metric("프로젝트", "30+")
    with c3:
        st.metric("기술 스택", "20+")
    with c4:
        st.metric("GitHub Stars", "120+")

    st.markdown("<br>", unsafe_allow_html=True)

    # 소개 + 관심 분야
    left, right = st.columns([3, 2])
    with left:
        st.markdown("""
        <div class="section-card">
            <div class="section-title">👤 About Me</div>
            <p style="color:#cbd5e1; line-height:1.9; font-size:0.95rem;">
                현재 <strong style="color:#a78bfa">KDN(한국전력데이터네트웍스)</strong>에서 데이터 엔지니어링 및
                내부 시스템 개발 업무를 담당하고 있습니다.<br><br>
                복잡한 데이터를 쉽게 시각화하고, 누구나 편리하게 사용할 수 있는
                직관적인 UI/UX를 만드는 것에 큰 보람을 느낍니다.<br><br>
                끊임없이 배우고, 코드로 세상을 더 편리하게 만드는 것이 목표입니다. 💡
            </p>
        </div>
        """, unsafe_allow_html=True)

    with right:
        st.markdown("""
        <div class="section-card">
            <div class="section-title">🎯 관심 분야</div>
            <p style="color:#cbd5e1; font-size:0.93rem; line-height:2;">
                📊 데이터 시각화 & 분석<br>
                ☁️ 클라우드 인프라 (AWS / Azure)<br>
                🤖 AI / 머신러닝 응용<br>
                🌐 웹 풀스택 개발<br>
                🔄 DevOps & CI/CD 자동화
            </p>
        </div>
        """, unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════
# 💼 경력
# ═══════════════════════════════════════════════════════════════
elif menu == "💼 경력":
    st.markdown("## 💼 경력 & 학력")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class="section-card">
            <div class="section-title">🏢 경력 사항</div>

            <div class="timeline-item">
                <div class="timeline-date">2022.03 — 현재</div>
                <div class="timeline-title">KDN 한국전력데이터네트웍스</div>
                <div class="timeline-sub">데이터엔지니어 · 정규직</div>
                <p style="color:#94a3b8; font-size:0.88rem; margin-top:8px;">
                  데이터 파이프라인 설계 및 운영<br>
                  내부 포털 시스템 풀스택 개발<br>
                  Streamlit 기반 데이터 대시보드 구축
                </p>
            </div>

            <div class="timeline-item">
                <div class="timeline-date">2020.07 — 2022.02</div>
                <div class="timeline-title">스타트업 A</div>
                <div class="timeline-sub">백엔드 개발자 · 정규직</div>
                <p style="color:#94a3b8; font-size:0.88rem; margin-top:8px;">
                  FastAPI 기반 REST API 서버 개발<br>
                  PostgreSQL / Redis 운영<br>
                  AWS EC2, RDS 인프라 관리
                </p>
            </div>

            <div class="timeline-item">
                <div class="timeline-date">2019.01 — 2020.06</div>
                <div class="timeline-title">IT 컨설팅 B사</div>
                <div class="timeline-sub">주니어 개발자 · 정규직</div>
                <p style="color:#94a3b8; font-size:0.88rem; margin-top:8px;">
                  Java Spring 기반 웹 시스템 개발<br>
                  데이터 마이그레이션 스크립트 작성<br>
                  고객사 요구사항 분석 및 구현
                </p>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="section-card">
            <div class="section-title">🎓 학력</div>

            <div class="timeline-item">
                <div class="timeline-date">2015 — 2019</div>
                <div class="timeline-title">○○대학교</div>
                <div class="timeline-sub">컴퓨터공학과 · 학사 졸업</div>
                <p style="color:#94a3b8; font-size:0.88rem; margin-top:8px;">
                  졸업논문: 딥러닝 기반 이미지 분류<br>
                  학점: 4.1 / 4.5
                </p>
            </div>

            <div class="timeline-item">
                <div class="timeline-date">2012 — 2015</div>
                <div class="timeline-title">○○고등학교</div>
                <div class="timeline-sub">이과 계열 졸업</div>
            </div>
        </div>

        <div class="section-card" style="margin-top:0;">
            <div class="section-title">🏆 자격증 & 수상</div>
            <div class="timeline-item">
                <div class="timeline-date">2023.08</div>
                <div class="timeline-title">AWS Solutions Architect Associate</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2022.05</div>
                <div class="timeline-title">정보처리기사</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2021.11</div>
                <div class="timeline-title">SQLD (SQL 개발자)</div>
            </div>
        </div>
        """, unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════
# 🛠 기술스택
# ═══════════════════════════════════════════════════════════════
elif menu == "🛠 기술스택":
    st.markdown("## 🛠 기술 스택")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class="section-card">
            <div class="section-title">🐍 언어 & 프레임워크</div>
        """, unsafe_allow_html=True)

        skills_lang = {
            "Python": 92,
            "JavaScript / TypeScript": 75,
            "Java": 60,
            "SQL": 88,
            "HTML / CSS": 70,
        }
        for skill, val in skills_lang.items():
            st.markdown(f'<div class="skill-label">{skill} — {val}%</div>', unsafe_allow_html=True)
            st.progress(val)
            st.markdown("<div style='margin-bottom:8px'></div>", unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("""
        <div class="section-card">
            <div class="section-title">☁️ 클라우드 & DevOps</div>
            <span class="skill-badge skill-badge-secondary">AWS EC2</span>
            <span class="skill-badge skill-badge-secondary">AWS S3</span>
            <span class="skill-badge skill-badge-secondary">AWS RDS</span>
            <span class="skill-badge skill-badge-secondary">Azure</span>
            <span class="skill-badge skill-badge-secondary">Docker</span>
            <span class="skill-badge skill-badge-secondary">GitHub Actions</span>
            <span class="skill-badge skill-badge-secondary">Nginx</span>
            <span class="skill-badge skill-badge-secondary">Linux</span>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="section-card">
            <div class="section-title">📊 데이터 & AI</div>
        """, unsafe_allow_html=True)

        skills_data = {
            "Pandas / NumPy": 90,
            "Streamlit": 85,
            "Scikit-learn": 72,
            "Apache Spark": 58,
            "TensorFlow / PyTorch": 50,
        }
        for skill, val in skills_data.items():
            st.markdown(f'<div class="skill-label">{skill} — {val}%</div>', unsafe_allow_html=True)
            st.progress(val)
            st.markdown("<div style='margin-bottom:8px'></div>", unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("""
        <div class="section-card">
            <div class="section-title">🗄️ 데이터베이스 & 기타</div>
            <span class="skill-badge skill-badge-tertiary">PostgreSQL</span>
            <span class="skill-badge skill-badge-tertiary">MySQL</span>
            <span class="skill-badge skill-badge-tertiary">Redis</span>
            <span class="skill-badge skill-badge-tertiary">MongoDB</span>
            <span class="skill-badge skill-badge-tertiary">FastAPI</span>
            <span class="skill-badge skill-badge-tertiary">React</span>
            <span class="skill-badge skill-badge-tertiary">Git</span>
            <span class="skill-badge skill-badge-tertiary">Airflow</span>
        </div>
        """, unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════
# 🎯 프로젝트
# ═══════════════════════════════════════════════════════════════
elif menu == "🎯 프로젝트":
    st.markdown("## 🎯 주요 프로젝트")

    projects = [
        {
            "icon": "⚡",
            "title": "전력 데이터 모니터링 대시보드",
            "period": "2023.06 — 2024.02",
            "desc": "실시간 전력 사용량 데이터를 수집·분석하여 Streamlit 기반 대시보드로 시각화. 이상탐지 알고리즘 적용으로 장애 사전 감지율 40% 향상.",
            "tags": ["Python", "Streamlit", "PostgreSQL", "Pandas", "AWS"],
            "color": "#6d28d9",
        },
        {
            "icon": "🌐",
            "title": "사내 포털 시스템 리뉴얼",
            "period": "2022.09 — 2023.05",
            "desc": "레거시 JSP 시스템을 FastAPI + React 스택으로 전면 재개발. API 응답 속도 60% 개선, 사용자 만족도 점수 4.2/5.0 달성.",
            "tags": ["FastAPI", "React", "PostgreSQL", "Docker", "Nginx"],
            "color": "#0891b2",
        },
        {
            "icon": "🤖",
            "title": "문서 자동 분류 AI 시스템",
            "period": "2023.11 — 2024.03",
            "desc": "자연어 처리 기반 사내 문서 자동 분류 시스템 구축. KoELECTRA 파인튜닝으로 분류 정확도 91% 달성, 수작업 처리 시간 70% 단축.",
            "tags": ["Python", "KoELECTRA", "FastAPI", "Docker", "AWS S3"],
            "color": "#059669",
        },
        {
            "icon": "📦",
            "title": "데이터 파이프라인 자동화",
            "period": "2022.03 — 2022.08",
            "desc": "Apache Airflow를 활용한 ETL 파이프라인 구축. 기존 수동 배치 작업 20여 개를 자동화하여 데이터 적재 지연 90% 감소.",
            "tags": ["Airflow", "Python", "Spark", "AWS", "PostgreSQL"],
            "color": "#d97706",
        },
    ]

    for i in range(0, len(projects), 2):
        cols = st.columns(2)
        for j, col in enumerate(cols):
            if i + j < len(projects):
                p = projects[i + j]
                tags_html = "".join(
                    f'<span style="background:rgba(255,255,255,0.1);color:#e2e8f0;'
                    f'padding:3px 10px;border-radius:12px;font-size:0.78rem;margin:3px;display:inline-block;">'
                    f'{t}</span>'
                    for t in p["tags"]
                )
                with col:
                    st.markdown(f"""
                    <div class="section-card" style="border-left: 4px solid {p['color']};">
                        <div style="font-size:2rem;">{p['icon']}</div>
                        <div style="color:#f1f5f9;font-weight:700;font-size:1.05rem;margin:8px 0 4px;">{p['title']}</div>
                        <div style="color:{p['color']};font-size:0.8rem;font-weight:600;margin-bottom:12px;">{p['period']}</div>
                        <p style="color:#94a3b8;font-size:0.88rem;line-height:1.7;">{p['desc']}</p>
                        <div style="margin-top:12px;">{tags_html}</div>
                    </div>
                    """, unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════
# 📬 연락처
# ═══════════════════════════════════════════════════════════════
elif menu == "📬 연락처":
    st.markdown("## 📬 연락처")

    col1, col2 = st.columns([3, 2])

    with col1:
        st.markdown("""
        <div class="section-card">
            <div class="section-title">💌 메시지 보내기</div>
        """, unsafe_allow_html=True)

        with st.form("contact_form"):
            name = st.text_input("이름", placeholder="홍길동")
            email = st.text_input("이메일", placeholder="example@email.com")
            subject = st.text_input("제목", placeholder="협업 문의드립니다")
            message = st.text_area("메시지", placeholder="안녕하세요! ...", height=160)
            submitted = st.form_submit_button("✉️ 메시지 전송", use_container_width=True)

        if submitted:
            if name and email and message:
                st.success(f"✅ {name}님, 메시지가 전송되었습니다! 빠른 시일 내에 답변 드리겠습니다.")
                st.balloons()
            else:
                st.warning("⚠️ 이름, 이메일, 메시지를 모두 입력해주세요.")

        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="section-card">
            <div class="section-title">📌 연락 정보</div>
            <div class="contact-item">📧 hong@example.com</div>
            <div class="contact-item">📱 010-1234-5678</div>
            <div class="contact-item">📍 서울특별시 강남구</div>
            <div class="contact-item">🏢 KDN 한국전력데이터네트웍스</div>
        </div>

        <div class="section-card">
            <div class="section-title">🔗 소셜 링크</div>
            <div class="contact-item">🐙 github.com/sky940819-alt</div>
            <div class="contact-item">💼 linkedin.com/in/example</div>
            <div class="contact-item">✍️ velog.io/@example</div>
        </div>

        <div class="section-card">
            <div class="section-title">⏰ 응답 가능 시간</div>
            <p style="color:#cbd5e1; font-size:0.9rem; line-height:1.9;">
                🗓️ 평일 09:00 — 18:00<br>
                📩 이메일 응답: 24시간 이내<br>
                🤝 미팅 가능: 사전 협의 후
            </p>
        </div>
        """, unsafe_allow_html=True)
