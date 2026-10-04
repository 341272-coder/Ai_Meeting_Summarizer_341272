import streamlit as st
from groq import Groq
import textwrap

# ---------------------------------------------------------
# PAGE CONFIGURATION
# ---------------------------------------------------------
st.set_page_config(
    page_title="MeetingMate AI",
    page_icon="🤝",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------------
st.markdown(
    """
    <style>

    .stApp {
        background-color: #f5f7fb;
    }

    /* Hero */
    .hero {
        background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
        padding: 38px 42px;
        border-radius: 20px;
        color: white;
        margin-bottom: 28px;
        box-shadow: 0 8px 25px rgba(0,0,0,0.08);
    }

    .hero-badge {
        display: inline-block;
        background: rgba(255,255,255,0.14);
        padding: 7px 14px;
        border-radius: 20px;
        font-size: 13px;
        margin-bottom: 13px;
    }

    .hero h1 {
        font-size: 40px;
        margin: 0;
        font-weight: 700;
    }

    .hero p {
        font-size: 17px;
        margin-top: 11px;
        opacity: 0.9;
    }

    /* Cards */
    .card {
        background: white;
        padding: 26px;
        border-radius: 16px;
        box-shadow: 0 4px 18px rgba(0,0,0,0.05);
        margin-bottom: 22px;
    }

    /* Section headings */
    .section-title {
        font-size: 22px;
        font-weight: 700;
        color: #203a43;
        margin-bottom: 8px;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background-color: #ffffff;
    }

    /* Buttons */
    .stButton > button {
        border-radius: 10px;
        font-weight: 600;
        padding: 10px 18px;
    }

    /* Text area */
    textarea {
        border-radius: 12px !important;
    }

    /* Footer */
    .footer {
        text-align: center;
        color: #777;
        font-size: 13px;
        margin-top: 45px;
        padding: 20px;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# ---------------------------------------------------------
# HERO SECTION
# ---------------------------------------------------------
st.markdown(
    textwrap.dedent(
        """
        <div class="hero">
            <div class="hero-badge">🤝 AI-Powered Meeting Assistant</div>
            <h1>MeetingMate AI</h1>
            <p>
                Turn meeting conversations into clear decisions,
                responsibilities and next steps.
            </p>
        </div>
        """
    ),
    unsafe_allow_html=True
)

# ---------------------------------------------------------
# SIDEBAR
# ---------------------------------------------------------
with st.sidebar:

    st.markdown("## 🤝 MeetingMate AI")

    st.markdown(
        """
        MeetingMate AI transforms meeting conversations into:

        - 📝 Key Takeaways
        - ✅ Action Items
        - 👤 Responsible People
        - 📅 Deadlines
        - 🎯 Decisions
        - ⚠️ Risks & Dependencies
        """
    )

    st.divider()

    st.markdown("### 🔄 How It Works")

    st.markdown(
        """
        **1. Add Meeting Notes**

        Paste your meeting conversation.

        **2. Analyse**

        Let AI identify the important information.

        **3. Review**

        Check the generated tasks, decisions and next steps.
        """
    )

    st.divider()

    st.markdown("### 🧠 Technology")

    st.markdown(
        """
        **Built with:** Python + Streamlit

        **AI Provider:** Groq

        **AI Model:** GPT-OSS 120B
        """
    )

    st.divider()

    st.caption("Academic Project • FORE School of Management")


# ---------------------------------------------------------
# GROQ API CONNECTION
# ---------------------------------------------------------
try:

    api_key = st.secrets["GROQ_API_KEY"]

    client = Groq(
        api_key=api_key
    )

except Exception:

    st.error(
        "⚠️ Groq API key is not configured. "
        "Please add GROQ_API_KEY in Streamlit Secrets."
    )

    st.stop()


# ---------------------------------------------------------
# SAMPLE MEETING TRANSCRIPT
# ---------------------------------------------------------
sample_transcript = """
Meeting Title: Quarterly Marketing Performance Review
Date: 3 October 2026

Attendees:
Piyansh Bhutani – Project Coordinator
Riya Sharma – Marketing Lead
Karan Mehta – Sales Manager
Aditya Kapoor – Finance Lead

Piyansh:
Let's review the performance of our recent digital marketing campaign and identify what needs to change for the October campaign.

Riya:
The campaign generated strong website traffic, but our conversion rate was lower than expected. I think the landing page needs improvement.

Karan:
From the sales side, we noticed that leads from Instagram were higher in volume, but leads from LinkedIn were more likely to convert.

Aditya:
We have some flexibility in the marketing budget, but I would like the next campaign to have a clearer return-on-investment target.

Riya:
I can redesign the landing page and prepare two alternative versions for testing by 8 October.

Karan:
I will share the channel-wise lead conversion data with the marketing team by 6 October.

Aditya:
Once we have that data, I can recommend how the additional budget should be allocated.

Piyansh:
Let's also test a LinkedIn-focused campaign instead of increasing spending equally across all channels.

Riya:
That works. I'll prepare the campaign concept and revised landing-page copy by 10 October.

Karan:
The sales team can provide feedback on the quality of leads during the first week of the campaign.

Piyansh:
Good. Let's review the revised campaign plan and budget allocation on 12 October.
"""


# ---------------------------------------------------------
# INPUT SECTION
# ---------------------------------------------------------
st.markdown(
    '<div class="section-title">💬 Meeting Conversation</div>',
    unsafe_allow_html=True
)

st.write(
    "Add your meeting conversation below, or load the sample marketing review "
    "to test the application."
)

col1, col2 = st.columns([1, 1])

with col1:

    if st.button(
        "📊 Load Sample Marketing Review",
        use_container_width=True
    ):

        st.session_state["transcript"] = sample_transcript


with col2:

    if st.button(
        "🗑️ Clear Conversation",
        use_container_width=True
    ):

        st.session_state["transcript"] = ""


# ---------------------------------------------------------
# SESSION STATE
# ---------------------------------------------------------
if "transcript" not in st.session_state:

    st.session_state["transcript"] = ""


transcript = st.text_area(
    "Meeting Conversation",
    value=st.session_state["transcript"],
    height=360,
    placeholder="Paste your meeting conversation here...",
    label_visibility="collapsed"
)


# ---------------------------------------------------------
# ANALYSE BUTTON
# ---------------------------------------------------------
st.write("")

generate = st.button(
    "🚀 Analyse Meeting",
    type="primary",
    use_container_width=True
)


# ---------------------------------------------------------
# AI PROCESSING
# ---------------------------------------------------------
if generate:

    if not transcript.strip():

        st.warning(
            "⚠️ Please enter a meeting conversation before analysing it."
        )

    else:

        with st.spinner(
            "🤖 Analysing the meeting and identifying important outcomes..."
        ):

            prompt = f"""
You are MeetingMate AI, an intelligent meeting-analysis assistant.

Your job is to convert the meeting conversation below into a concise,
business-friendly set of insights that a manager can immediately act upon.

Analyse the conversation carefully and distinguish between:

- confirmed commitments
- suggestions
- questions
- decisions
- unresolved issues

IMPORTANT RULES:

- Never invent an owner.
- Never invent a deadline.
- If ownership is unclear, write "Not specified".
- If no deadline is mentioned, write "Not specified".
- Do not treat questions or suggestions as confirmed commitments.
- Base your answer only on information contained in the conversation.
- Keep the output concise and professional.

Return the answer using EXACTLY this structure:

## 1. Meeting Snapshot

Give 3–5 concise bullet points describing the most important outcomes.

## 2. Action Tracker

Create a Markdown table:

| Task / Follow-Up | Responsible Person | Deadline |
|---|---|---|

Only include genuine action items or confirmed commitments.

## 3. Decisions Made

List the decisions that were actually agreed upon.

## 4. Open Issues & Dependencies

Identify unresolved questions, dependencies, risks or information that is still required.

## 5. Next Steps

Give a concise list of what should happen next.

MEETING CONVERSATION:

{transcript}
"""

            try:

                response = client.chat.completions.create(

                    model="openai/gpt-oss-120b",

                    messages=[

                        {
                            "role": "system",
                            "content": (
                                "You are MeetingMate AI, a professional "
                                "meeting-analysis assistant. Accuracy and "
                                "faithful extraction are more important "
                                "than creativity."
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

                result = response.choices[0].message.content


                # -------------------------------------------------
                # RESULTS
                # -------------------------------------------------
                st.markdown(
                    '<div class="section-title">🚀 Meeting Analysis</div>',
                    unsafe_allow_html=True
                )

                st.markdown(
                    '<div class="card">',
                    unsafe_allow_html=True
                )

                st.markdown(result)

                st.markdown(
                    '</div>',
                    unsafe_allow_html=True
                )


                # -------------------------------------------------
                # HUMAN REVIEW MESSAGE
                # -------------------------------------------------
                st.info(
                    "👤 **Human Review Recommended:** "
                    "AI-generated meeting insights should be reviewed "
                    "against the original conversation before being used "
                    "for important business decisions."
                )


            except Exception as e:

                st.error(
                    "❌ Unable to analyse the meeting right now."
                )

                st.caption(
                    f"Technical details: {str(e)}"
                )


# ---------------------------------------------------------
# FOOTER
# ---------------------------------------------------------
st.markdown(
    textwrap.dedent(
        """
        <div class="footer">
            <b>MeetingMate AI</b><br>
            Turning meeting conversations into clear next steps<br><br>
            Academic Project • FORE School of Management
        </div>
        """
    ),
    unsafe_allow_html=True
)
