#! python3
# mclip.py - a multi-clipboard program. 
#   ATBS project for creating multi-clipboard automatic messages.
#

# TEXT dictionary associating keywords to text message values
TEXT = {'agree' : """Yes, that works for me. Thank you.""",
        'busy'  : """Sorry, I can't make that time. Is there an alternative time?""",
        'maybe' : """Let me get back to you on that. I may have a conflict."""}

# Handle command line arguments
import sys, pyperclip

if len(sys.argv) < 2:
    print('Usage: python mclip.py [keyphase]\n')
    sys.exit()

keyphrase = sys.argv[1]     # first command line arg is the 'keyphrase'

# if keyphrase is a key in TEXT dictionary, copy appropriate message to clipboard
if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print('Text for ' + keyphrase + ' copied to clipboard')
else:
    print('There is no text for ' + keyphrase)
