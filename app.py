import streamlit as st
import time
from dotenv import load_dotenv

# Import the agents and chains defined in your project
from src.Agents.agents import (
    build_search_agent,
    build_reader_agent,
    writer_chain,
    critic_chain
)

# Load environment variables
load_dotenv()

# ==========================================
# PAGE CONFIGURATION & CUSTOM CSS
# ==========================================
st.set_page_config(
    page_title="Agentic Research AI",
    page_icon="🌌",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for a modern, sleek UI
st.markdown("""
<style>
    /* Gradient Hero Text */
    .hero-title {
        background: -webkit-linear-gradient(45deg, #4facfe, #00f2fe);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 3.5rem;
        font-weight: 800;
        text-align: center;
        margin-bottom: 0px;
        padding-bottom: 0px;
    }

    .hero-subtitle {
        text-align: center;
        font-size: 1.2rem;
        color: #888888;
        margin-bottom: 30px;
    }

    /* Custom Cards for Agents */
    .agent-card {
        border-radius: 12px;
        padding: 20px;
        background-color: var(--secondary-background-color);
        border: 1px solid rgba(128, 128, 128, 0.2);
        margin-bottom: 15px;
        transition: transform 0.2s ease-in-out;
    }
    .agent-card:hover {
        transform: translateY(-2px);
        border: 1px solid #4facfe;
    }

    .agent-title {
        font-size: 1.2rem;
        font-weight: 600;
        margin-bottom: 8px;
        color: var(--text-color);
    }

    /* Style the main report container */
    .report-container {
        padding: 30px;
        border-radius: 15px;
        background-color: var(--secondary-background-color);
        border-left: 5px solid #00f2fe;
    }

    /* Critic container */
    .critic-container {
        padding: 25px;
        border-radius: 15px;
        background-color: rgba(255, 75, 75, 0.1);
        border-left: 5px solid #ff4b4b;
    }
</style>
""", unsafe_allow_html=True)


# ==========================================
# SIDEBAR DESIGN
# ==========================================
def build_sidebar():
    with st.sidebar:
        st.markdown("## 🤖 Agent Swarm")
        st.markdown("A synchronized pipeline of specialized AI agents.")

        st.markdown("""
        <div class="agent-card">
            <div class="agent-title">🕵️‍♂️ Search Agent</div>
            <div style="font-size: 0.9rem; color: #888;">Scours the web for the most recent, reliable data and URLs.</div>
        </div>
        <div class="agent-card">
            <div class="agent-title">📖 Reader Agent</div>
            <div style="font-size: 0.9rem; color: #888;">Scrapes and extracts deep contextual information from sources.</div>
        </div>
        <div class="agent-card">
            <div class="agent-title">✍️ Writer Agent</div>
            <div style="font-size: 0.9rem; color: #888;">Synthesizes raw data into a cohesive, structured research report.</div>
        </div>
        <div class="agent-card">
            <div class="agent-title">🧐 Critic Agent</div>
            <div style="font-size: 0.9rem; color: #888;">Evaluates the draft for accuracy, bias, and completeness.</div>
        </div>
        """, unsafe_allow_html=True)


# ==========================================
# PIPELINE EXECUTION FUNCTION
# ==========================================
def run_pipeline(topic):
    state = {}

    # UI Elements for dynamic updates
    progress_bar = st.progress(0)
    status_text = st.empty()
    metrics_cols = st.columns(4)

    # 1. Search Agent
    status_text.markdown("### ⏳ Phase 1/4: Initiating Search Agent...")
    with st.spinner("🕵️‍♂️ Querying web sources..."):
        search_result = build_search_agent().invoke({
            "messages": [("user", f"Find recent and reliable information on {topic} along with URLs")]
        })
        state['search_result'] = search_result['messages'][-1].content
    progress_bar.progress(25)
    metrics_cols[0].metric(label="Search Status", value="Done ✅")
    st.toast("Search Agent finished collecting sources!", icon="🕵️‍♂️")

    # 2. Reader Agent
    status_text.markdown("### ⏳ Phase 2/4: Initiating Reader Agent...")
    with st.spinner("📖 Extracting and reading web content..."):
        reader_result = build_reader_agent().invoke({
            "messages": [("user",
                          f"Based on the following search results about {topic} "
                          f"Extract deeper information from relevant urls "
                          f"Search results : {state['search_result']}")]
        })
        state['scraped_content'] = reader_result['messages'][-1].content
    progress_bar.progress(50)
    metrics_cols[1].metric(label="Reader Status", value="Done ✅")
    st.toast("Reader Agent finished scraping content!", icon="📖")

    # 3. Writer Agent
    status_text.markdown("### ⏳ Phase 3/4: Initiating Writer Agent...")
    with st.spinner("✍️ Drafting the comprehensive report..."):
        research_results = {
            "SEARCH_RESULTS": state['search_result'],
            "DETAILED_RESULTS": state['scraped_content']
        }
        state['writer_content'] = writer_chain.invoke({
            'topic': topic,
            'research': research_results
        })
    progress_bar.progress(75)
    metrics_cols[2].metric(label="Writer Status", value="Done ✅")
    st.toast("Writer Agent finished drafting the report!", icon="✍️")

    # 4. Critic Agent
    status_text.markdown("### ⏳ Phase 4/4: Initiating Critic Agent...")
    with st.spinner("🧐 Reviewing and analyzing the draft..."):
        state['critic_results'] = critic_chain.invoke({
            'research_paper': state['writer_content']
        })
    progress_bar.progress(100)
    metrics_cols[3].metric(label="Critic Status", value="Done ✅")
    st.toast("Critic Agent finished the review!", icon="🧐")

    status_text.empty()
    time.sleep(0.5)  # Slight pause for UX
    progress_bar.empty()

    return state


# ==========================================
# MAIN APP LAYOUT
# ==========================================
def main():
    build_sidebar()

    # Hero Section
    st.markdown('<p class="hero-title">Deep Research AI</p>', unsafe_allow_html=True)
    st.markdown('<p class="hero-subtitle">An intelligent swarm that searches, reads, writes, and critiques.</p>',
                unsafe_allow_html=True)

    # Input Area
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        topic = st.text_input(
            "Topic Input",
            placeholder="e.g., The Evolution and Future of LLMs",
            label_visibility="collapsed"
        )

        # Centered Button
        btn_cols = st.columns([1, 1, 1])
        with btn_cols[1]:
            start_run = st.button("🚀 Launch Swarm", type="primary", use_container_width=True)

    st.markdown("---")

    # Execution & Results
    if start_run:
        if not topic.strip():
            st.error("Please enter a research topic to begin.")
            return

        try:
            # Run the backend
            state = run_pipeline(topic)
            st.balloons()

            # -----------------------------------------
            # RESULTS DASHBOARD
            # -----------------------------------------

            # Top row: Main Report and Critic Analysis side-by-side
            st.markdown(f"## 📑 Research Complete: {topic}")

            report_col, critic_col = st.columns([2, 1])  # 66% width for report, 33% for critic

            with report_col:
                st.markdown("#### ✍️ Final Drafted Report")
                st.markdown(f'<div class="report-container">{state["writer_content"]}</div>', unsafe_allow_html=True)
                st.download_button(
                    label="📥 Download Report (.md)",
                    data=state['writer_content'],
                    file_name=f"{topic.replace(' ', '_')}_Final_Report.md",
                    mime="text/markdown",
                    use_container_width=True
                )

            with critic_col:
                st.markdown("#### 🧐 Critic's Review")
                st.markdown(f'<div class="critic-container">{state["critic_results"]}</div>', unsafe_allow_html=True)
                st.download_button(
                    label="📥 Download Review (.md)",
                    data=state['critic_results'],
                    file_name=f"{topic.replace(' ', '_')}_Critic_Review.md",
                    mime="text/markdown",
                    use_container_width=True
                )

            st.markdown("<br><br>", unsafe_allow_html=True)

            # Bottom row: "Under the Hood" Expander for messy logs
            with st.expander("🛠️ View Under the Hood (Raw Data & Scrapes)", expanded=False):
                tab1, tab2 = st.tabs(["🔍 Search Agent Results", "📖 Reader Agent Scrapes"])

                with tab1:
                    st.info("Raw URLs and search data retrieved by the Search Agent.")
                    st.markdown(state['search_result'])

                with tab2:
                    st.info("Raw text scraped from the URLs by the Reader Agent.")
                    st.markdown(state['scraped_content'])

        except Exception as e:
            st.error(f"An error occurred during execution: {e}")


if __name__ == "__main__":
    main()