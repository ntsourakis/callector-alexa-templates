"""
This sample demonstrates a simple skill built with the Amazon Alexa Skills Kit.

"""

# --------------- Helpers that build all of the responses ----------------------

def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'SSML',
            'ssml': "<speak>" + output + "</speak>"
        },
        'card': {
            'type': 'Simple',
            'title': "SessionSpeechlet - " + title,
            'content': "SessionSpeechlet - " + output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'SSML',
                'ssml': "<speak>" + reprompt_text + "</speak>"
            }
        },
        'shouldEndSession': should_end_session
    }


def build_speechlet_response_without_card(output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'SSML',
            'ssml': "<speak>" + output + "</speak>"
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'SSML',
                'ssml': "<speak>" + reprompt_text + "</speak>"
            }
        },
        'shouldEndSession': should_end_session
    }

# --------------- Functions that control the skill's behavior ------------------

def get_welcome_response(userId):
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """
    
    return build_response(session_attributes, build_speechlet_response(
        "Welcome", "Welcome", "I didn't understand", False))



def handle_intent_request(intent, session, standard_intent_or_not):
    
    return build_response(session_attributes, build_speechlet_response_without_card(
            "Hello", "Can you repeat?", False))

    
# --------------- Events ------------------

def on_session_started(session_started_request, session):
    """ Called when the session starts """

    return

def on_launch(launch_request, session):
    """ Called when the user launches the skill without specifying what they
    want
    """
	
	# Dispatch to your skill's launch
    return get_welcome_response(get_userId_from_session(session))

def on_intent(intent_request, session):
    """ Called when the user specifies an intent for this skill """

    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']

    # If we get a standard intent, we just pass the intent name
    if is_standard_intent(intent_name):
        return handle_intent_request(intent_name, session, 'standard_intent')
    # Otherwise, we pass the whole intent
    else:
        return handle_intent_request(intent, session, 'not_standard_intent')

def is_standard_intent(intent_name):
    return intent_name.startswith('AMAZON.')

def on_session_ended(session_ended_request, session):
    """ Called when the user ends the session.
	
    Is not called when the skill returns should_end_session=true
    """

	# add cleanup logic here
	return

# --------------- Main handler ------------------

def lambda_handler(event, context):
    """ Route the incoming request based on type (LaunchRequest, IntentRequest,
    etc.) The JSON body of the request is provided in the event parameter.
    """

    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
   

