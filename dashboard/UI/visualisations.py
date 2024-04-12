import matplotlib.pyplot as plt

def plot_va_graph(valence, arousal, recommendations_va):
    fig, ax = plt.subplots()
    ax.scatter(
        [va[0] for va in recommendations_va], 
        [va[1] for va in recommendations_va], 
        color='blue',
        s=3,
        marker='.'
      )
    ax.scatter(
        valence, 
        arousal, 
        color='red',
        s=3,
    )
    ax.axvline(0, color='red')
    ax.axhline(0, color='red')
    ax.grid(True, linestyle='--')
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.text(0.5, 1.02, 'Activated', ha='center', va='bottom', transform=ax.transAxes)
    ax.text(0.5, -0.05, 'Deactivated', ha='center', va='top', transform=ax.transAxes)
    ax.text(1.02, 0.55, 'Positive', ha='center', va='top', transform=ax.transAxes, rotation=-90)
    ax.text(-0.1, 0.55, 'Negative', ha='center', va='top', transform=ax.transAxes, rotation=90)
    ax.text(0.5, 1.15, 'Valence - Arousal Graph', ha='center', va='top', transform=ax.transAxes, fontsize=20)
    ax.text(0.5, 1.09, 'Valence', ha='center', va='top', transform=ax.transAxes, fontsize=15)
    ax.text(-0.15, 0.57, 'Arousal', ha='center', va='top', transform=ax.transAxes, rotation=90, fontsize=15)
    fig.set_size_inches(8, 8)
    return fig
