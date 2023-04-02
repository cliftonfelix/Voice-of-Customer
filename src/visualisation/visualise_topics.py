import itertools

import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction import text


def get_top_words(corpus, custom_sw=[]):
    '''
    Computes the Tf-idf scores of the list of the words in the corpus.
    ------------
    Parameters:
        corpus (list): list
        custom_sw (list): list of custom stopwords
    Returns:
        dataframe (dataframe): dataframe consisting top words and
                            its tf-idf score
    '''
    my_stop_words = list(text.ENGLISH_STOP_WORDS.union(custom_sw))

    vec = TfidfVectorizer(stop_words=my_stop_words).fit(corpus)
    bag_of_words = vec.transform(corpus)
    sum_words = bag_of_words.sum(axis=0)
    words_freq = [(word, sum_words[0, idx])
                  for word, idx in vec.vocabulary_.items()]
    words_freq = sorted(words_freq, key=lambda x: x[1], reverse=True)
    return pd.DataFrame(words_freq[5::-1],
                        columns=["top words", "tf-idf score"])


def visualise_top_words(df,
                        topics,
                        specific=False,
                        custom_sw=[],
                        inc_size=False):
    '''
    Plots bar chart showing distribution of top words in each topic
    using the tf-idf scores.
    ------------
    Parameters:
        df (dataframe): dataframe
        topics (list): list of topics
        specific (boolean): specifying whether to create plot for a selected
                        topic or all the topics in the list.
    Returns:
        fig (graph object): plotly figure
    '''
    colors = itertools.cycle(px.colors.qualitative.Plotly)
    # colors = itertools.cycle(["#D55E00", "#0072B2", "#CC79A7", "#E69F00",
    # "#56B4E9", "#009E73", "#F0E442"])

    if specific:
        topic_corpus = df[df["topic"] == topics[0]]
        freq_df = get_top_words(topic_corpus["cleaned_text"], custom_sw)
        fig = px.bar(freq_df, x="tf-idf score", y="top words",
                     title=f"Top Words for {topics[0]}")

        rows = 1
        columns = 1
    else:
        subplot_titles = [str(topic) for topic in topics]
        columns = 4
        rows = int(np.ceil(len(topics)/columns))
        fig = make_subplots(rows=rows,
                            cols=columns,
                            shared_xaxes=False,
                            horizontal_spacing=.1,
                            vertical_spacing=.4 / rows if rows > 1 else 0,
                            subplot_titles=subplot_titles)

        row = 1
        column = 1
        for topic in topics:
            topic_corpus = df[df["topic"] == topic]
            freq_df = get_top_words(topic_corpus["cleaned_text"], custom_sw)

            fig.add_trace(
                go.Bar(x=freq_df["tf-idf score"],
                       y=freq_df["top words"],
                       orientation='h',
                       marker_color=next(colors)),
                row=row, col=column)

            if column == columns:
                column = 1
                row += 1
            else:
                column += 1

    fig.update_layout(
        template="plotly_white",
        showlegend=False,
        # title={
        #     'text': "Top Words",
        #     'x': 0,
        #     'y': 1,
        #     'xanchor': 'left',
        #     'yanchor': 'top',
        #     'font': dict(
        #         size=22,
        #         color="Black")
        # },
        # width= 1000 if columns > 1 else 400,
        # height=250*rows if rows > 1 else 250 * 1.3,
        hoverlabel=dict(
            bgcolor="white",
            font_size=16,
            font_family="Rockwell"
        ),
    )

    if inc_size:
        fig.update_layout(
            width=1000 if columns > 1 else 400,
            height=250*rows if rows > 1 else 250 * 1.3
        )

    fig.update_yaxes(dtick=1)

    return fig
