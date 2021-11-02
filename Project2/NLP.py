import os
from google.cloud import language_v1
# os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=r"path to jason file"

client = language_v1.LanguageServiceClient()
filelist = os.listdir("result")  # make sure no DS.Store file in the folder

filenum = len(filelist)
sequence = {}
M = 0
for i in range(0, filenum):
    filename = filelist[i]
    review_file = os.path.join("result", filename)
    name = os.path.splitext(filename)[0]
    
    with open(review_file, "r") as review_file:
        # Instantiates a plain text document.
        content = review_file.read()

    document = language_v1.Document(content=content, type_=language_v1.Document.Type.PLAIN_TEXT)
    annotations = client.analyze_sentiment(document=document)
    # encoding_type = language_v1.EncodingType.UTF8
    # annotations = client.analyze_sentiment(request = {'document': document, 'encoding_type': encoding_type})
    
    # Print the results
    score = annotations.document_sentiment.score
    magnitude = annotations.document_sentiment.magnitude
    """for index, sentence in enumerate(annotations.sentences):
        sentence_sentiment = sentence.sentiment.score
        print('Sentence {} has a sentiment score of {}'.format(
            index, sentence_sentiment))
    """
    newscore = score + 0.001 * magnitude
    sequence[name] = newscore  # save the popular list
    print(
        "Overall Sentiment of {}: score of {} with magnitude of {}".format(
            name, score, magnitude
        )
    )

sortedsequence = sorted(sequence.items(), key=lambda x: x[1], reverse=True)
b = [i[0] for i in sortedsequence]
result = open("result.txt", "a")
result.write("Top 10 US cities most welcome on Twitter for a short trip" + "\n")
for n in range(0, 10):
    result.write(str(n + 1) + "." + b[n] + "\n")
