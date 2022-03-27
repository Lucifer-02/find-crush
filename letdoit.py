from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, NoTranscriptAvailable, NoTranscriptFound, CouldNotRetrieveTranscript

# get id from file
file = open("dlp_ids.txt", "r")
ids = file.readlines()
index = 0

# check keyword in transcript
for i in ids:
    index += 1
    try:
        transcript = YouTubeTranscriptApi.get_transcript(i)
    except (TranscriptsDisabled, NoTranscriptFound, NoTranscriptAvailable, CouldNotRetrieveTranscript):
        print(index)
        print("Error: ", i)
        continue
    for data in transcript:
        if data["text"].find("freshman") != -1:
            print(index)
            print("                                                 ITS HERE!!!: ", i)
            break
    print(index)
    print("its not here!", i)
