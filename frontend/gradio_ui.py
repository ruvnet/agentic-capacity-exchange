import gradio as gr

def admin_ui():
    """
    This function represents the administrative UI for managing worker nodes, job submissions, and system monitoring.
    """
    return "Admin UI: Manage worker nodes, job submissions, and system monitoring."

def user_ui():
    """
    This function represents the end user UI for submitting jobs, monitoring job status, and retrieving results.
    """
    return "User UI: Submit jobs, monitor job status, and retrieve results."

def main_interface():
    with gr.Blocks() as demo:
        with gr.Tabs():
            with gr.Tab("Admin"):
                gr.Markdown(admin_ui())
            with gr.Tab("User"):
                gr.Markdown(user_ui())
    return demo

if __name__ == "__main__":
    main_interface().launch()
