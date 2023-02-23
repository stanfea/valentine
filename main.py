import logging
from logging.config import fileConfig
from valentine import voice_to_text, text_to_voice, ai

logger = logging.getLogger('sLogger')
fileConfig('log.ini')

PHONE_SAMPLE_RATE = 16000

recorder = voice_to_text.VoiceToText(PHONE_SAMPLE_RATE)
speaker = text_to_voice.TextToVoice()
ai = ai.AI()


def main():
    while True:
        logger.info("recorder: get()")
        user_query = recorder.get()
        logger.debug(user_query)

        logger.info("ai: answer()")
        ai_response = ai.answer(user_query)

        logger.info("speaker: speak()")
        if not speaker.speak(ai_response):
            logger.error("problem with text to speech, restarting")
            continue
        logger.info("ENTER to continue")
        input()


if __name__ == "__main__":
    main()
