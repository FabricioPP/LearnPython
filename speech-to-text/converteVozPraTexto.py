from __future__ import print_function
import json
from os.path import join, dirname
from watson_developer_cloud import SpeechToTextV1

# If service instance provides API key authentication
# service = SpeechToTextV1(
#     ## url is optional, and defaults to the URL below. Use the correct URL for your region.
#     url='https://stream.watsonplatform.net/speech-to-text/api',
#     iam_apikey='your_apikey')

service = SpeechToTextV1(
    username='21a3fd5b-881f-42d5-ac1b-5b971e37db2d',
    password='HKPHjtg487MJ',
    url='https://stream.watsonplatform.net/speech-to-text/api/')

models = service.list_models().get_result()
print(json.dumps(models, indent=2))

model = service.get_model('pt-BR_NarrowbandModel').get_result()
print(json.dumps(model, indent=2))

with open(join(dirname(__file__),'reais.flac'),
          'rb') as audio_file:
    print(json.dumps(
        service.recognize(
            audio=audio_file,
            content_type='audio/flac',
            timestamps=True,
            word_confidence=True).get_result(),
        indent=2))
