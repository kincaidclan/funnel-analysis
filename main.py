import pandas as pd
import plotly.graph_objects as go

# Load the dataset
df = pd.read_csv("user_data.csv")

# Define funnel stages
funnel_stages = ['homepage', 'product_page', 'cart', 'checkout', 'purchase']
stage_order = {stage: i for i, stage in enumerate(funnel_stages)}

# Preprocess
df['stage'] = df['stage'].map(stage_order)
df = df.dropna(subset=['stage'])
df['stage'] = df['stage'].astype(int)
df['stage'] = df['stage'].map({v: k for k, v in stage_order.items()})

# Counts
user_counts = df.groupby('stage')['user_id'].nunique().reindex(funnel_stages).fillna(0).astype(int)
conversion_counts = df[df['conversion'] == 1].groupby('stage')['user_id'].nunique().reindex(funnel_stages).fillna(0).astype(int)

# Downstream probabilities
downstream_probs = {}
for i, stage in enumerate(funnel_stages):
    current_users = user_counts[stage]
    probs = {}
    for next_stage in funnel_stages[i+1:]:
        probs[next_stage] = user_counts[next_stage] / current_users if current_users else 0
    downstream_probs[stage] = probs

# Hover text for users
user_hover = []
for stage in funnel_stages:
    base = f"<b>{stage.replace('_', ' ').title()}</b><br>"
    base += f"{user_counts[stage]}<br>"
    prev_pct = 100 if stage == funnel_stages[0] else user_counts[stage] / user_counts[funnel_stages[funnel_stages.index(stage)-1]] * 100
    base += f"% of previous: {prev_pct:.2f}%<br>"
    base += f"% of initial: {user_counts[stage] / user_counts[funnel_stages[0]] * 100:.2f}%<br>"
    if stage == "purchase":
        print()
    else:
        base += "<b>Downstream Probabilities</b><br>"
        for next_stage, prob in downstream_probs[stage].items():
            base += f"{next_stage.replace('_', ' ').title()}: {prob * 100:.2f}%<br>"
    user_hover.append(base)

# Hover text for conversions
conversion_hover = []
for stage in funnel_stages:
    base = f"<b>{stage.replace('_', ' ').title()}</b><br>"
    base += f"{conversion_counts[stage]}<br>"
    rate = conversion_counts[stage] / user_counts[stage] * 100 if user_counts[stage] else 0
    base += f"<b>Conversion Rate:</b> {rate:.2f}%<br>"
    conversion_hover.append(base)

# Show only label if value is large enough
def get_text_labels(values, threshold=0.05):
    total = max(values)
    return [f"{v:,}" if v / total > threshold else "" for v in values]

# Build the figure
fig = go.Figure()

fig.add_trace(go.Funnel(
    y=funnel_stages,
    x=user_counts.values,
    name='Users',
    textposition='inside',
    hovertext=user_hover,
    hoverinfo='text',
    marker=dict(color='royalblue')
))

fig.add_trace(go.Funnel(
    y=funnel_stages,
    x=conversion_counts.values,
    name='Conversions',
    textposition='inside',
    hovertext=conversion_hover,
    hoverinfo='text',
    marker=dict(color='tomato')
))

# Layout
fig.update_layout(
    title="Funnel Analysis",
    font=dict(size=14),
    height=1000,
    margin=dict(t=100, l=150, r=150)
)

fig.show()
