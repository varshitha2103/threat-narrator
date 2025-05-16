import gradio as gr
from log_parser import load_logs
from mitre_mapper import map_to_mitre
from summary_generator import generate_summary

def summarize(file_obj):
    logs = load_logs(file_obj.name)
    summaries = []
    for log in logs:
        log["technique"] = map_to_mitre(log["event_type"])
        summaries.append(generate_summary(log))
    return "\n\n".join(summaries)

gr.Interface(
    fn=summarize,
    inputs="file",
    outputs="text",
    title="🕵️‍♂️ Context-Aware Threat Narrator (Groq-Powered)"
).launch()
