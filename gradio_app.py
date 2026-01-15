# if you dont use pipenv uncomment the following:
from dotenv import load_dotenv
load_dotenv()

import os
import gradio as gr

from brain_of_the_doctor import encode_image, analyze_image_with_query
from voice_of_the_patient import record_audio, transcribe_with_groq
from voice_of_the_doctor import text_to_speech_with_gtts, text_to_speech_with_elevenlabs

system_prompt="""You have to act as a professional doctor, i know you are not but this is for learning purpose. 
            What's in this image?. Do you find anything wrong with it medically? 
            If you make a differential, suggest some remedies for them. Donot add any numbers or special characters in 
            your response. Your response should be in one long paragraph. Also always answer as if you are answering to a real person.
            Donot say 'In the image I see' but say 'With what I see, I think you have ....'
            Dont respond as an AI model in markdown, your answer should mimic that of an actual doctor not an AI bot, 
            Keep your answer concise (max 2 sentences). No preamble, start your answer right away please"""


def process_inputs(audio_filepath, image_filepath):
    speech_to_text_output = transcribe_with_groq(GROQ_API_KEY=os.environ.get("GROQ_API_KEY"), 
                                                 audio_filepath=audio_filepath,
                                                 stt_model="whisper-large-v3")

    # Handle the image input
    if image_filepath:
        doctor_response = analyze_image_with_query(query=system_prompt+speech_to_text_output, encoded_image=encode_image(image_filepath), model="meta-llama/llama-4-scout-17b-16e-instruct")
    else:
        doctor_response = "No image provided for me to analyze"

    voice_of_doctor = text_to_speech_with_gtts(input_text=doctor_response, output_filepath="final.mp3") 

    return speech_to_text_output, doctor_response, voice_of_doctor


# Custom CSS for professional medical theme
custom_css = """
#main-container {
    background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

.gradio-container {
    max-width: 1200px !important;
    margin: auto !important;
}

#header {
    text-align: center;
    padding: 2rem;
    background: linear-gradient(135deg, #2193b0 0%, #6dd5ed 100%);
    border-radius: 15px;
    margin-bottom: 2rem;
    box-shadow: 0 8px 32px rgba(33, 147, 176, 0.3);
}

#header h1 {
    color: white;
    font-size: 2.5rem;
    margin-bottom: 0.5rem;
    font-weight: 700;
    text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.1);
}

#header p {
    color: #f0f9ff;
    font-size: 1.1rem;
    margin-top: 0.5rem;
}

.input-section, .output-section {
    background: white;
    padding: 2rem;
    border-radius: 15px;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.08);
    margin-bottom: 1.5rem;
}

#component-0, #component-1, #component-2, #component-3, #component-4 {
    border-radius: 10px;
    border: 2px solid #d1e7f0;
}

.gr-button {
    background: linear-gradient(135deg, #06b6d4 0%, #0891b2 100%) !important;
    border: none !important;
    color: white !important;
    font-weight: 600 !important;
    padding: 12px 24px !important;
    border-radius: 8px !important;
    font-size: 1.1rem !important;
    transition: all 0.3s ease !important;
}

.gr-button:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(6, 182, 212, 0.4) !important;
}

footer {
    text-align: center;
    padding: 1.5rem;
    color: #475569;
    margin-top: 2rem;
}

#disclaimer {
    background: linear-gradient(135deg, #fef3c7 0%, #fde68a 100%);
    border-left: 4px solid #f59e0b;
    padding: 1rem;
    border-radius: 8px;
    margin-top: 1rem;
    color: #000000;
    font-weight: 600;
}
"""

# Create the interface with custom theme
with gr.Blocks(css=custom_css, theme=gr.themes.Soft(primary_hue="cyan")) as iface:
    
    gr.HTML("""
        <div id="header">
            <h1>🏥 MediVision AI</h1>
            <p>Advanced Medical Image Analysis with Voice Interaction</p>
            <div id="disclaimer">
                ⚠️ This tool is designed for learning and demonstration purposes. 
                Always consult qualified healthcare professionals for medical advice.
            </div>
        </div>
    """)
    
    with gr.Row():
        with gr.Column(scale=1):
            gr.Markdown("### 🎤 Patient Input")
            with gr.Group(elem_classes="input-section"):
                audio_input = gr.Audio(
                    sources=["microphone"], 
                    type="filepath",
                    label="Record Your Symptoms"
                )
                image_input = gr.Image(
                    type="filepath",
                    label="Upload Medical Image"
                )
                submit_btn = gr.Button("🔍 Analyze", variant="primary", size="lg")
        
        with gr.Column(scale=1):
            gr.Markdown("### 📋 Analysis Results")
            with gr.Group(elem_classes="output-section"):
                text_output = gr.Textbox(
                    label="📝 Your Query",
                    lines=3
                )
                doctor_output = gr.Textbox(
                    label="🩺 Medical Analysis",
                    lines=5
                )
                audio_output = gr.Audio(
                    label="🔊 Voice Response",
                    type="filepath"
                )
    
    gr.HTML("""
        <footer>
            <p>Built by Amartay Kumar Dhar | Built for Learning Purpose</p>
        </footer>
    """)
    
    submit_btn.click(
        fn=process_inputs,
        inputs=[audio_input, image_input],
        outputs=[text_output, doctor_output, audio_output]
    )

iface.launch(debug=True, share=False)