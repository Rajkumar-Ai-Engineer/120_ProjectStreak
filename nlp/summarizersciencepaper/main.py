import streamlit as st 
from helper import ResearchPaperSummarizerAgent
def main():
    st.title("Research Paper Summarizer Agent")
    st.write("Enter the research paper title, DOI, or arXiv ID to get a structured summary.")

    research_paper = st.text_input("Research Paper Input", placeholder="Enter title, DOI, or arXiv ID")

    if st.button("Summarize"):
        if research_paper:
            with st.spinner("Summarizing..."):
                summary = ResearchPaperSummarizerAgent(research_paper)
                st.subheader("Summary")
                st.write(summary)
        else:
            st.error("Please enter a valid research paper input.")

if __name__ == "__main__":
    main()