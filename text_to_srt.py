import textwrap

def seconds_to_srt_time(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60
    millis = 0
    return f"{int(hours):02}:{int(minutes):02}:{int(secs):02},{millis:03}"

def generate_srt(text, duration_per_chunk=3):
    max_words_per_line = 3  # Limit to 3 words per subtitle line
    words = text.split()
    chunks = [' '.join(words[i:i+max_words_per_line]) for i in range(0, len(words), max_words_per_line)]

    srt_output = ""
    start_time = 0

    for index, chunk in enumerate(chunks, 1):
        end_time = start_time + duration_per_chunk
        start = seconds_to_srt_time(start_time)
        end = seconds_to_srt_time(end_time)
        srt_output += f"{index}\n{start} --> {end}\n{chunk}\n\n"
        start_time = end_time

    return srt_output

# ---- SETTINGS SECTION ----
# Change the subtitle text and duration per chunk here
text = """Paste your full subtitle text here, all in one string."""
duration = 2  # Duration per subtitle in seconds (change this as needed)
# --------------------------

srt_result = generate_srt(text, duration_per_chunk=duration)

with open("output.srt", "w", encoding="utf-8") as file:
    file.write(srt_result)

print("SRT file generated as output.srt")
