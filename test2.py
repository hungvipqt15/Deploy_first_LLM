import streamlit as st
from langchain_openai.chat_models import ChatOpenAI
from openai import OpenAI

st.title("🦜🔗 Quickstart App")


template='''You are a social media expert who knows exactly how to keep an audience engaged with great posts. Your mission is to use the tone and style from the given content to transform another piece of content. 
The new content need to be designed and contributed by the social media platform.
Given two content inputs:
- **Original Content:** {input_content}
- **Tone and Style Sample:** {style_content}
Firstly, analyze the style reference to understand its tone, language patterns and writing style. 
Pay attention to elements such as formality, use of humor, sentence structure and vocabulary choices.

Then, rewrite the main content in the style of the reference content.

Secondly, the output should be tailored for the following social media platform of {social_media_type}, adhering to their specific formats and best practices.


Here is some guidance about the structure and template of some social media platforms. Choose 1 in 3 below structure for the social media I ask above.
    1. Facebook:
-Create a post of 1-3 paragraphs
-Include an engaging opening sentence
-Add 2-3 relevant hashtags
-No more 150 words in the post

    2. LinkedIn:
-Write a professional post of 2-4 paragraphs
-Include a attention-grabbing headline
-Add a call-to-action at the end
-Use 3-5 relevant hashtags
-Suggest a related article or resource to link
-No more 200 words in the post

    3. Twitter:
-Craft a thread of 3-5 tweets
-Ensure each tweet is within the 100-word limit
-Use engaging language to encourage retweets and replies
-Include 1-2 relevant hashtags per tweet
-Suggest an appropriate image or GIF for the first tweet (if applicable)
-No more 400 words in the post

You must notice that the total number of words I require in the post must be approximate {number_words}. But if this number of words is higher than the maximum words whose chosen media platform allow, try to shorten them so as not to exceed the platform's word limit. Try to summarize the most important parts. The platform's word limit priority is higher and mandatory
It is not always necessary to form complete sentences, it just needs to be understood by the reader.
'''

openai_api_key = st.sidebar.text_input("OpenAI API Key", type="password")


with st.form("my_form"):
    temperature = st.text_input("",
    placeholder="Temperature"
    )
    print(type(temperature))
    media_type = st.text_input("",
        placeholder="Enter a social media type",
    )
    number_words = st.text_input("",
        placeholder="Enter number of words you want to generate",
    )
    input_content = st.text_input("",
        placeholder="Enter your input content",
    )
    style_content = st.text_input("",
        placeholder="Enter your style content",
    )

    prompt = template.format(input_content=input_content,style_content=style_content,number_words=number_words,social_media_type=media_type)

    client = OpenAI(
        # This is the default and can be omitted
        api_key=openai_api_key,
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="gpt-4o",
        temperature=0.5
    )
    



    submitted = st.form_submit_button("Submit")
    st.write("### Answer")
    output = chat_completion.choices[0].message.content
    st.info(output)

    st.write("### Number words")
    num_words_output = len(output.split())
    st.info(num_words_output)