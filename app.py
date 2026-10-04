import streamlit as st
from groq import Groq


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="MeetingMate AI",
    page_icon="🤝",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown(
    """
    <style>
        .stApp {
            background-color: #f4f7f9;
        }

        .block-container {
            max-width: 1250px;
            padding-top: 2rem;
            padding-bottom: 3rem;
        }

        section[data-testid="stSidebar"] {
            background-color: #102a2e;
        }

        section[data-testid="stSidebar"] * {
            color: white;
        }

        div[data-testid="stMetric"] {
            background-color: white;
            padding: 18px;
            border-radius: 14px;
            border: 1px solid #e1e7e9;
        }

        div[data-testid="stVerticalBlockBorderWrapper"] {
            background-color: white;
            border-radius: 16px;
        }

        .stTextArea textarea {
            border-radius: 12px;
        }

        .stButton button {
            border-radius: 10px;
            font-weight: 600;
        }

        h1 {
            color: #16383c;
        }

        h2 {
            color: #16383c;
        }

        h3 {
            color: #16383c;
        }

        .footer-text {
            text-align: center;
            color: #7c898c;
            margin-top: 40px;
            padding: 20px;
        }
    </style>
    """,
    unsafe_allow_html=True
)


# =========================================================
# GROQ CONNECTION
# =========================================================

try:
    api_key = st.secrets["GROQ_API_KEY"]
    client = Groq(api_key=api_key)

except Exception:
    st.error(
        "Groq API key is not configured. "
        "Please add GROQ_API_KEY under Streamlit Secrets."
    )
    st.stop()


# =========================================================
# SESSION STATE
# =========================================================

if "meeting_text" not in st.session_state:
    st.session_state.meeting_text = ""

if "analysis_result" not in st.session_state:
    st.session_state.analysis_result = ""


# =========================================================
# SAMPLE MEETING
# =========================================================

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

Piyansh: We should also consider whether a clearer FAQ section could
reduce repetitive customer queries.

Aarav: I can prepare a list of the ten most frequently asked questions
for the FAQ review by 8 October.

Simran: Once the workflow analysis is complete, I'll discuss the findings
with the support team.

Piyansh: Let's meet again on 11 October to review the findings and decide
which improvements should be implemented first.
"""


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.title("🤝 MeetingMate")

    st.caption("AI Meeting Intelligence Workspace")

    st.divider()

    st.subheader("Workspace")

    st.write("📝 Conversation Analysis")
    st.caption(
        "Transform raw meeting conversations into "
        "structured managerial insights."
    )

    st.divider()

    st.subheader("AI Detects")

    st.write("🎯 Priorities")
    st.write("✅ Assigned Tasks")
    st.write("👤 Responsible People")
    st.write("📅 Deadlines")
    st.write("💡 Decisions")
    st.write("⚠️ Open Issues")

    st.divider()

    st.subheader("AI Engine")

    st.caption("Groq Cloud API")
    st.caption("GPT-OSS 120B")
    st.caption("Python + Streamlit")

    st.divider()

    st.caption("Academic Prototype")
    st.caption("FORE School of Management")


# =========================================================
# MAIN HEADER
# =========================================================

st.subheader("⚡ MEETING INTELLIGENCE WORKSPACE")

st.title("MeetingMate AI")

st.write(
    "Convert meeting conversations into structured priorities, "
    "responsibilities, decisions and follow-up actions — in seconds."
)


# =========================================================
# FEATURE OVERVIEW
# =========================================================

st.divider()

st.subheader("What MeetingMate Can Extract")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        label="🎯 Key Takeaways",
        value="Focus"
    )
    st.caption(
        "Identify the most important discussion points."
    )

with col2:
    st.metric(
        label="✅ Task Tracker",
        value="Actions"
    )
    st.caption(
        "Capture commitments and responsibilities."
    )

with col3:
    st.metric(
        label="💡 Decisions",
        value="Clarity"
    )
    st.caption(
        "Separate decisions from general discussion."
    )

with col4:
    st.metric(
        label="⚠️ Open Issues",
        value="Risks"
    )
    st.caption(
        "Highlight dependencies and unresolved matters."
    )


# =========================================================
# MEETING INPUT
# =========================================================

st.divider()

st.subheader("01 · Meeting Workspace")

st.write(
    "Paste a meeting transcript, discussion, call notes "
    "or conversation below."
)


button1, button2, spacer = st.columns([1.5, 1, 4])


with button1:

    if st.button(
        "📊 Load Demo Meeting",
        use_container_width=True
    ):
        st.session_state.meeting_text = SAMPLE_MEETING
        st.session_state.analysis_result = ""
        st.rerun()


with button2:

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
    )
)

st.session_state.meeting_text = meeting_text


# =========================================================
# ANALYSIS SETTINGS
# =========================================================

st.divider()

st.subheader("02 · Analysis Settings")

st.write(
    "Choose how detailed you want the meeting analysis to be."
)


analysis_mode = st.radio(
    "Analysis depth",
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
Provide a detailed review including relevant context,
dependencies, unresolved issues and follow-up items.
"""

else:

    mode_instruction = """
Provide a balanced professional analysis with useful
context while avoiding unnecessary detail.
"""


# =========================================================
# GENERATE ANALYSIS
# =========================================================

st.write("")

analyse = st.button(
    "⚡ Generate Meeting Intelligence",
    type="primary",
    use_container_width=True
)


# =========================================================
# AI PROCESSING
# =========================================================

if analyse:

    if not meeting_text.strip():

        st.warning(
            "Please add a meeting conversation before "
            "running the analysis."
        )

    else:

        prompt = f"""
You are MeetingMate AI, a professional meeting intelligence assistant.

Analyse the meeting conversation below and convert it into useful
managerial information.

IMPORTANT RULES:

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


# =========================================================
# RESULTS
# =========================================================

if st.session_state.analysis_result:

    st.divider()

    st.subheader("03 · Intelligence Report")

    st.caption(
        "Structured insights generated from the submitted conversation."
    )

    with st.container(border=True):

        st.markdown(
            st.session_state.analysis_result
        )

    st.write("")

    st.info(
        "👤 Human Review Recommended — "
        "AI-generated insights should be checked against "
        "the original meeting conversation before important "
        "decisions are made."
    )


# =========================================================
# FOOTER
# =========================================================

st.divider()

st.caption(
    "🤝 MeetingMate AI  •  From conversation to clarity  •  "
    "Academic Project • FORE School of Management"
)
