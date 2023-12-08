# Import necessary libraries
import streamlit as st

# Define the data structure with articles and categories
article_data = {
    'Podcasts': [
        {'title': 'Mental Health', 'link': 'https://www.feedspot.com/infiniterss.php?_src=feed_title&followfeedid=5372377&q=site:https%3A%2F%2Fanchor.fm%2Fs%2Fe31ae954%2Fpodcast%2Frss'},
        {'title': " Today's Heartlift with Janell", 'link': 'https://www.feedspot.com/infiniterss.php?_src=feed_title&followfeedid=5397758&q=site:https%3A%2F%2Ffeeds.resonaterecordings.com%2Ftodays-heartlift-with-janell'},
        {'title': 'Mental Health Foundation Podcast', 'link': 'https://www.feedspot.com/infiniterss.php?_src=feed_title&followfeedid=5397758&q=site:https%3A%2F%2Ffeeds.resonaterecordings.com%2Ftodays-heartlift-with-janell'},
        {'title': 'Terrible, Thanks For Asking Podcast', 'link': 'https://example.com/podcast2'},
        {'title': 'The OCD Stories', 'link': 'https://example.com/podcast2'},
        {'title': 'Leaving Toxic', 'link': 'https://example.com/podcast2'},
        {'title': 'Anxiety Slayer', 'link': 'https://example.com/podcast2'},
        {'title': 'How to be Happy?', 'link': 'https://example.com/podcast2'},
    ],
    'Videos': [
        {'title': 'Motivation Video 1', 'link': 'https://youtu.be/bYfq22PzaOA?si=vr9c8QzlrmebCqhy'},
        {'title': 'Motivation Video 2', 'link': 'https://youtu.be/85NqnTHOmBE?si=b1OoocR8s0HJUxHa'},
        {'title': 'Motivation Video 3', 'link': 'https://youtu.be/wnHW6o8WMas?si=oi5jdyyRvxpbM7WP'},
        {'title': 'Motivation Video 4', 'link': 'https://youtu.be/l1XM5ifaMEA?si=cJebqMUY-8TY4N2M'},
        {'title': 'Motivation Video 5', 'link': 'https://youtu.be/NSQVsvYH9xo?si=Sffp0Vf0lYrva3sd'},
        {'title': 'Motivation Video 6', 'link': 'https://youtu.be/mgmVOuLgFB0?si=ew52gBNrFqbpUOPD'},
    ],
    'Awareness Hub': [
        {'title': 'Your Mental Health Pal', 'link': 'hhttps://yourmentalhealthpal.com'},
        {'title': 'The Mighty Mental Health', 'link': 'https://themighty.com/topic/mental-health'},
        {'title': 'The OCD Stories', 'link': 'https://theocdstories.com/'},
        {'title': 'Chipur Healing for Depression, Anxiety, Bipolarity, Stress', 'link': 'https://chipur.com/'},
        {'title': 'Lawyers with Depression', 'link': 'https://www.lawyerswithdepression.com/'},
        {'title': 'The Worry Games', 'link': 'https://theworrygames.com/'},
        {'title': 'The Art of Healing Trauma', 'link': 'https://www.new-synapse.com/aps/wordpress/'},
    ],
    'Shorts':[
        {'title': 'Best Motivation Shorts 1', 'link': 'https://youtube.com/shorts/dvCV_9F8rTc?si=iESEo8l1KI3Uodcf'},
        {'title': 'Motivation Shorts 2', 'link': 'https://youtube.com/shorts/Zy7ulOB7oCY?si=P__yyqQPulcs4LFg'},
        {'title': 'Motivation Shorts 3', 'link': 'https://youtube.com/shorts/b5DOsAdAjxc?si=xVReCmKPKmd8-Q3h'},
        {'title': 'Motivation Shorts 4', 'link': 'https://youtube.com/shorts/E--2uVZEdN4?si=TGpySHA2nRoQlqcv'},
        {'title': 'Motivation Shorts 5', 'link': 'https://youtube.com/shorts/i8kgJv8ykho?si=qqDNnif92Z_WUl2c'},
        {'title': 'Motivation Shorts 6', 'link': 'https://youtube.com/shorts/YJctWppjTX0?si=yUB4TLj7Dbasg0_x'},
        {'title': 'Motivation Shorts 7', 'link': 'https://youtube.com/shorts/KHrfydOZBFk?si=xyYvPjGplsgySfgA'}
    ]
}

# Create Streamlit app


# Display articles by category
category = st.sidebar.selectbox('Select Category', list(article_data.keys()))

st.header(f'{category} Articles')

for article in article_data[category]:
    st.write(f"[{article['title']}]({article['link']})")

# Add a link to the source code
st.sidebar.markdown('### Source Code')
st.sidebar.write("[GitHub Repository](https://github.com/yourusername/your-repo)")

# Run the app with `streamlit run your_app_name.py` in the terminal
