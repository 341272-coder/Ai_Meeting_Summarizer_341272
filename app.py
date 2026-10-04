import streamlit as st
from groq import Groq

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------

st.set_page_config(
    page_title="MeetingMate AI",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------

st.markdown(
    """
    <style>

    .stApp {
        background: #f4f7f9;
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 1250px;
    }

    section[data-testid="stSidebar"] {
        background: #102a2e;
    }

    section[data-testid="stSidebar"] * {
        color: #f4f7f9;
    }

    .hero {
        padding: 38px 42px;
        border-radius: 22px;
        background:
            radial-gradient(
                circle at top right,
                rgba(63, 209, 177, 0.35),
                transparent 35%
            ),
            linear-gradient(135deg, #102a2e, #17484d);
        color: white;
        margin-bottom: 28px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.10);
    }

    .hero-badge {
        display: inline-block;
        padding: 7px 14px;
        border-radius: 30px;
        background: rgba(255,255,255,0.12);
        font-size: 13px;
        font-weight: 600;
        margin-bottom: 15px;
    }

    .hero h1 {
        font-size: 42px;
        margin: 0 0 8px 0;
        font-weight: 750;
    }

    .hero p {
        font-size: 17px;
        opacity: 0.90;
        margin: 0;
        max-width: 720px;
        line-height: 1.6;
    }

    .stat-card {
        background: white;
        padding: 20px;
        border-radius: 16px;
        border: 1px solid #e4e9ec;
        min-height: 115px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.04);
    }

    .stat-icon {
        font-size: 25px;
        margin-bottom: 8px;
    }

    .stat-title {
        font-size: 15px;
        font-weight: 700;
        color: #16383c;
    }

    .stat-text {
        font-size: 13px;
        color: #68777b;
        margin-top: 5px;
    }

    .section-label {
        font-size: 13px;
        font-weight: 700;
        color: #15836f;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 3px;
    }

    .section-title {
        font-size: 27px;
        font-weight: 750;
        color: #16383c;
        margin-bottom: 7px;
    }

    .section-subtitle {
        color: #718084;
        font-size: 14px;
        margin-bottom: 20px;
    }

    .result-box {
        background: white;
        padding: 28px;
        border-radius: 18px;
        border-left: 5px solid #1b9c85;
        box-shadow: 0 6px 22px rgba(0,0,0,0.05);
        margin-top: 15px;
    }

    .stTextArea textarea {
        border-radius: 14px !important;
        border: 1px solid #d9e2e4 !important;
        background: white !important;
    }

    .stButton > button {
        border-radius: 10px;
        font-weight: 650;
        min-height: 43px;
    }

    div[data-testid="stButton"] button[kind="primary"] {
        background: #168b77;
        border: none;
    }

    .footer {
        text-align: center;
        color: #879396;
        font-size: 13px;
        padding-top: 40px;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# ---------------------------------------------------
# GROQ CONNECTION
# ---------------------------------------------------

try:
    api_key = st.secrets["GROQ_API_KEY"]
    client = Groq(api_key=api_key)

except Exception:
    st.error(
        "Groq API connection is not configured. "
        "Please add GROQ_API_KEY to Streamlit Secrets."
    )
    st.stop()


# ---------------------------------------------------
# SESSION STATE
# ---------------------------------------------------

if "meeting_text" not in st.session_state:
    st.session_state.meeting_text = ""

if "analysis_result" not in st.session_state:
    st.session_state.analysis_result = ""


# ---------------------------------------------------
# NEW SAMPLE MEETING
# ---------------------------------------------------

SAMPLE_MEETING = """Customer Experience Improvement Meeting
Date: 4 October 2026

Participants:
Piyansh Bhutani – Project Coordinator
Aarav Mehta – Customer Experience Lead
Simran Kapoor – Operations Manager
Devansh Rao – Product Manager

Piyansh: Thanks everyone. The purpose of today's meeting is to understand
why customer complaints have increased during the last month and decide
what we should improve first.

Aarav: The biggest issue appears to be delayed responses from customer
support. Customers are waiting too long for their queries to be resolved.

Simran: Operations can review the current support workflow. I believe some
requests are being transferred between teams unnecessarily.

Devansh: We should also look at the product side. A number of complaints
are related to customers finding the return process confusing.

Piyansh: Can we separate the complaints into support-related and
product-related categories before deciding on a solution?

Aarav: Yes. I'll prepare a complaint-category analysis by 7 October.

Simran: I'll map the existing customer-support workflow and identify
where delays are occurring by 9 October.

Devansh: I'll review the current return process and suggest improvements
after seeing the complaint analysis.

Piyansh: Good. We should also consider whether a clearer FAQ section
could reduce repetitive customer queries.

Aarav: I can prepare a list of the ten most frequently asked questions
for the FAQ review by 8 October.

Simran: Once the workflow analysis is complete, I'll discuss the findings
with the support team.

Piyansh: Let's meet again on 11 October to review the findings and decide
which improvements should be implemented first.
"""


# ---------------------------------------------------
# SIDEBAR
# ---------------------------------------------------

with st.sidebar:

    st.markdown("## ⚡ MeetingMate")

    st.caption("AI Meeting Intelligence Workspace")

    st.markdown("---")

    st.markdown("### Workspace")

    st.markdown(
        """
        **📝 Conversation Analysis**

        Transform raw meeting conversations into
        structured managerial insights.
        """
    )

    st.markdown("---")

    st.markdown("### AI Detects")

    st.markdown(
        """
        🎯 Priorities

        ✅ Assigned Tasks

        👤 Responsible People

        📅 Deadlines

        💡 Decisions

        ⚠️ Open Issues
        """
    )

    st.markdown("---")

    st.markdown("### AI Engine")

    st.caption("Groq Cloud API")
    st.caption("GPT-OSS 120B")
    st.caption("Python + Streamlit")

    st.markdown("---")

    st.caption("Academic Prototype")
    st.caption("FORE School of Management")


# ---------------------------------------------------
# HERO
# ---------------------------------------------------

st.markdown(
    """
    <div class="hero">
        <div class="hero-badge">
            ⚡ MEETING INTELLIGENCE WORKSPACE
        </div>

        <h1>MeetingMate AI</h1>

        <p>
        Convert meeting conversations into structured priorities,
        responsibilities, decisions and follow-up actions — in seconds.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)


# ---------------------------------------------------
# FEATURE CARDS
# ---------------------------------------------------

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown(
        """
        <div class="stat-card">
            <div class="stat-icon">🎯</div>
            <div class="stat-title">Key Takeaways</div>
            <div class="stat-text">
                Identify the most important points discussed.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

with c2:
    st.markdown(
        """
        <div class="stat-card">
            <div class="stat-icon">✅</div>
            <div class="stat-title">Task Tracker</div>
            <div class="stat-text">
                Capture commitments and responsibilities.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

with c3:
    st.markdown(
        """
        <div class="stat-card">
            <div class="stat-icon">💡</div>
            <div class="stat-title">Decision Capture</div>
            <div class="stat-text">
                Separate decisions from general discussion.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

with c4:
    st.markdown(
        """
        <div class="stat-card">
            <div class="stat-icon">⚠️</div>
            <div class="stat-title">Open Issues</div>
            <div class="stat-text">
                Highlight dependencies and unresolved matters.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


st.write("")
st.write("")


# ---------------------------------------------------
# MEETING INPUT
# ---------------------------------------------------

st.markdown(
    """
    <div class="section-label">01 / INPUT</div>

    <div class="section-title">
        Meeting Workspace
    </div>

    <div class="section-subtitle">
        Paste a meeting transcript, discussion, call notes or conversation below.
    </div>
    """,
    unsafe_allow_html=True
)


button_col1, button_col2, empty_col = st.columns(
    [1.6, 1, 4]
)


with button_col1:

    if st.button(
        "📊 Load Demo Meeting",
        use_container_width=True
    ):

        st.session_state.meeting_text = SAMPLE_MEETING
        st.session_state.analysis_result = ""

        st.rerun()


with button_col2:

    if st.button(
        "↻ Reset",
        use_container_width=True
    ):

        st.session_state.meeting_text = ""
        st.session_state.analysis_result = ""

        st.rerun()


meeting_text = st.text_area(
    "Meeting conversation",
    value=st.session_state.meeting_text,
    height=330,
    placeholder=(
        "Paste your meeting conversation here...\n\n"
        "Example:\n"
        "Rohan: I'll prepare the report by Friday.\n"
        "Meera: Great. We'll review it next Monday."
    ),
    label_visibility="collapsed"
)

st.session_state.meeting_text = meeting_text


# ---------------------------------------------------
# ANALYSIS MODE
# ---------------------------------------------------

st.write("")

st.markdown(
    """
    <div class="section-label">
        02 / ANALYSIS SETTINGS
    </div>

    <div class="section-title">
        Choose Analysis Depth
    </div>
    """,
    unsafe_allow_html=True
)


analysis_mode = st.radio(
    "Analysis mode",
    [
        "Quick Scan",
        "Standard Analysis",
        "Detailed Review"
    ],
    horizontal=True,
    index=1
)


if analysis_mode == "Quick Scan":

    mode_instruction = """
    Keep the analysis concise. Focus on the most important
    takeaways, confirmed tasks and decisions.
    """

elif analysis_mode == "Detailed Review":

    mode_instruction = """
    Provide a detailed review including context,
    dependencies, unresolved issues and follow-up items.
    """

else:

    mode_instruction = """
    Provide a balanced professional analysis with useful
    context while avoiding unnecessary detail.
    """


# ---------------------------------------------------
# ANALYSE BUTTON
# ---------------------------------------------------

st.write("")

analyse = st.button(
    "⚡ Generate Meeting Intelligence",
    type="primary",
    use_container_width=True
)


# ---------------------------------------------------
# AI ANALYSIS
# ---------------------------------------------------

if analyse:

    if not meeting_text.strip():

        st.warning(
            "Please add a meeting conversation before running the analysis."
        )

    else:

        prompt = f"""
You are MeetingMate AI, a professional meeting intelligence assistant.

Analyse the meeting conversation below and convert it into useful
managerial information.

RULES:

1. Use ONLY information provided in the conversation.
2. Never invent people, dates, tasks or decisions.
3. Distinguish confirmed commitments from suggestions.
4. Questions should not automatically be treated as decisions.
5. If a task has no owner, write "Not specified".
6. If a task has no deadline, write "Not specified".
7. Clearly separate confirmed decisions from unresolved issues.
8. Preserve names and dates accurately.
9. Do not make assumptions.

ANALYSIS DEPTH:

{mode_instruction}

Return the result using exactly this structure:

## 🎯 Meeting Brief

Give a concise overview of the meeting and its main purpose.

## ⭐ Priority Takeaways

Give the most important points as bullet points.

## ✅ Commitment Tracker

Create a Markdown table:

| Commitment / Task | Owner | Deadline | Status |

Use "Confirmed" only when the speaker clearly commits
to completing the task.

## 💡 Decisions Confirmed

List only decisions that were clearly agreed upon.

## ⚠️ Open Issues & Dependencies

List unresolved matters, dependencies and topics
that require additional discussion.

## 🔜 Follow-Up Plan

Explain the next follow-up steps based only on
what was explicitly mentioned.

MEETING CONVERSATION:

{meeting_text}
"""

        with st.spinner(
            "MeetingMate is analysing the conversation..."
        ):

            try:

                response = client.chat.completions.create(
                    model="openai/gpt-oss-120b",

                    messages=[
                        {
                            "role": "system",
                            "content": (
                                "You are a professional meeting analysis "
                                "assistant. Accuracy and faithful extraction "
                                "are more important than creativity."
                            )
                        },
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ],

                    temperature=0.2,
                    max_tokens=1800
                )

                st.session_state.analysis_result = (
                    response.choices[0].message.content
                )

            except Exception as e:

                st.error(
                    "The AI service could not process the meeting. "
                    "Please try again."
                )

                st.caption(
                    f"Technical details: {e}"
                )


# ---------------------------------------------------
# OUTPUT
# ---------------------------------------------------

if st.session_state.analysis_result:

    st.write("")
    st.write("")

    st.markdown(
        """
        <div class="section-label">
            03 / INTELLIGENCE REPORT
        </div>

        <div class="section-title">
            Meeting Analysis
        </div>

        <div class="section-subtitle">
            Structured insights generated from the submitted conversation.
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="result-box">',
        unsafe_allow_html=True
    )

    st.markdown(
        st.session_state.analysis_result
    )

    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )

    st.write("")

    st.info(
        "👤 Human Review Recommended — "
        "AI-generated insights should be checked against "
        "the original meeting conversation before important "
        "decisions are made."
    )


# ---------------------------------------------------
# FOOTER
# ---------------------------------------------------

st.markdown(
    """
    <div class="footer">

        <b>MeetingMate AI</b><br>

        From conversation to clarity.<br><br>

        Academic Project • FORE School of Management

    </div>
    """,
    unsafe_allow_html=True
)
