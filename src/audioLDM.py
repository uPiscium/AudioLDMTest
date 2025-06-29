import subprocess


def run_audioldm(prompt: str, output_path: str, model_name: str = "audioldm_48k"):
    """
    Run the AudioLDM script with the specified output path.

    Args:
        prompt (str): The text prompt to guide the audio generation.
        output_path (str): The path where the output will be saved.
        model_name (str): The name of the AudioLDM model to use. Default is "audioldm_48k". Available models are [audioldm_48k, audioldm_16k_crossattn_t5, audioldm2-full, audioldm2-music-665k, audioldm2-full-large-1150k, audioldm2-speech-ljspeech, audioldm2-speech-gigaspeech].
    """
    command = ["audioldm2", "-model_name", model_name, "-s", output_path, "-t", prompt]

    try:
        subprocess.run(command, check=True)
        print(f"AudioLDM completed successfully. Output saved to {output_path}")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running AudioLDM: {e}")
