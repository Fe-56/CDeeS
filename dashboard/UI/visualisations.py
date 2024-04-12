import matplotlib.pyplot as plt

def plot_va_graph(valence, arousal):
    fig, ax = plt.subplots()
    ax.scatter(valence, arousal, color='red')
    ax.set_xlabel('Valence')
    ax.set_ylabel('Arousal')
    ax.set_title('Valence - Arousal graph')
    ax.axvline(0, color='black', linestyle='--')
    ax.axhline(0, color='black', linestyle='--')
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    return fig

def plot_va_graph_with_recommendations(song, recommended):
    pass