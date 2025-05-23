import textwrap

def seconds_to_srt_time(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60
    millis = 0
    return f"{int(hours):02}:{int(minutes):02}:{int(secs):02},{millis:03}"

def generate_srt(text, chunk_size=5, duration_per_chunk=3):
    words = text.split()
    chunks = [' '.join(words[i:i+chunk_size]) for i in range(0, len(words), chunk_size)]
    
    srt_output = ""
    start_time = 0
    
    for index, chunk in enumerate(chunks, 1):
        end_time = start_time + duration_per_chunk
        start = seconds_to_srt_time(start_time)
        end = seconds_to_srt_time(end_time)
        srt_output += f"{index}\n{start} --> {end}\n{chunk}\n\n"
        start_time = end_time

    return srt_output

# Example subtitle input
text = """Paste your full subtitle text here, all in one string."""
srt_result = generate_srt(text)

with open("output.srt", "w", encoding="utf-8") as file:
    file.write(srt_result)

print("SRT file generated as output.srt")

