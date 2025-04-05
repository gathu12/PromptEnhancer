import streamlit as st
import openai
import os

# Set your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")  # or use st.secrets["openai_api_key"]

st.title("Prompt Enhancer using GPT 🚀")

role = st.text_input("🔹 Role", placeholder="e.g., You are an experienced UX designer")
context = st.text_area("🔹 Context", placeholder="e.g., I'm building a mobile app for mental health tracking.")
task = st.text_area("🔹 Task", placeholder="e.g., I need help designing the onboarding flow.")

if st.button("✨ Enhance Prompt"):
    if not (role and context and task):
        st.warning("Please fill all the fields.")
    else:
        enhanced_prompt = f"""
You are {role}.
Context: {context}
Task: {task}

Your response must:
- Clarify any assumptions before providing an answer.
- Use the following format in your reply:

---
**Assumptions Clarified**: <List the assumptions you are making>

**Answer**: <Your response here>

**Next Steps or Suggestions**: <Optional ideas or suggestions to go further>
---
"""
        st.subheader("🔍 Enhanced Prompt Sent to GPT:")
        st.code(enhanced_prompt.strip())

        try:
            response = openai.chat.completions.create(
                model="gpt-4",
                messages=[{"role": "user", "content": enhanced_prompt}],
                temperature=0.7
            )
            reply = response.choices[0].message.content
            st.subheader("✅ GPT Response:")
            st.write(reply)
        except Exception as e:
            st.error(f"❌ Error calling OpenAI API: {e}")
