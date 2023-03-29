import argparse
import stable_whisper

def generate_srt(file_path):
    model = stable_whisper.load_model("small.en")
    result = model.transcribe(file_path, language="en")
    srt_file_path = file_path.replace('.mp3', '.srt')
    result.to_srt_vtt(srt_file_path, word_level=False)


if __name__ == '__main__':
    # get file_path arg from command line, and generate srt file
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file_path', type=str, required=True, help='file path')
    args = parser.parse_args()
    generate_srt(args.file_path)