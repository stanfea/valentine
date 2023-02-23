import logging
import azure.cognitiveservices.speech as speechsdk
import os

logger = logging.getLogger('sLogger')


class TextToVoice:

    # This example requires environment variables named "SPEECH_KEY" and "SPEECH_REGION"
    speech_config = speechsdk.SpeechConfig(subscription=os.environ.get('SPEECH_KEY'), region=os.environ.get('SPEECH_REGION'))
    audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)

    # The language of the voice that speaks.
    speech_config.speech_synthesis_voice_name='en-US-SteffanNeural'

    speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

    def speak(self, text_input):

        speech_synthesis_result = self.speech_synthesizer.speak_text_async(text_input).get()

        if speech_synthesis_result.reason == speechsdk.ResultReason.Canceled:
            cancellation_details = speech_synthesis_result.cancellation_details
            if cancellation_details.reason == speechsdk.CancellationReason.Error:
                if cancellation_details.error_details:
                    logger.error("Error details: {}".format(cancellation_details.error_details))
                    return False
            logger.error("Speech synthesis canceled: {}".format(cancellation_details.reason_))
            return False

        if speech_synthesis_result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
            logger.info("Speech synthesized for text [{}]".format(text_input))
            a = speech_synthesis_result
            return True

        return False


