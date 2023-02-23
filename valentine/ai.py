import logging
import openai
import os

logger = logging.getLogger('sLogger')


class AI:

    openai.api_key = os.environ.get('OPENAI_API_KEY')

    def answer(self, input):

        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=f"The following is a conversation with an AI bonds salesman. You will answer with short sentences\n\nHuman: {input}\nAI: ",
            temperature=0.9,
            max_tokens=150,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0.6,
            stop=[" Human:", " AI:"]
        )

        return response.get('choices')[0]['text']