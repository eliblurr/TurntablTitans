from pathlib import Path
from enum import Enum
import os

BASE_DIR = Path(__file__).resolve().parent
AUDIO_PATH = os.path.join(BASE_DIR, 'tmp', 'audio')
MODEL_PATH = os.path.join(BASE_DIR, 'tmp', 'models')

class STTModel(Enum):
    EN = {
            'target': 'en_stt_model.jit',
            'package': 'https://models.silero.ai/models/en/en_v6.jit',
        }

    def path(self):
        return os.path.join(MODEL_PATH, self.value['target'])

    @classmethod
    def exists(cls, key:str):
        return key.lower() in [key.lower() for key in cls.__members__.keys()]

class TTSModel(Enum):
    EN = {
            'model': 'v3_en',
            'target': 'en_model.pt',
            'package': 'https://models.silero.ai/models/tts/en/v3_en.pt',
            'sample_rate': [8000, 24000, 48000],
            'speaker': 'en_0'
        }

    DE = {
            'model': 'v3_de',
            'target': 'de_model.pt',
            'package': 'https://models.silero.ai/models/tts/de/v3_de.pt',
            'sample_rate': [8000, 24000, 48000],
            'speaker': 'karlsson'
        }

    ES = {
            'model': 'v3_es',
            'target': 'es_model.pt',
            'package': 'https://models.silero.ai/models/tts/es/v3_es.pt',
            'sample_rate': [8000, 24000, 48000],
            'speaker': 'es_0'
        }
    FR = {
            'model': 'v3_fr',
            'target': 'fr_model.pt',
            'package': 'https://models.silero.ai/models/tts/fr/v3_fr.pt',
            'sample_rate': [8000, 24000, 48000],
            'speaker': 'fr_0'
        }

    RU = {
            'model': 'v3_1_ru',
            'target': 'ru_model.pt',
            'package': 'https://models.silero.ai/models/tts/ru/v3_1_ru.pt',
            'sample_rate': [8000, 24000, 48000],
            'speaker': 'baya'
        }

    def path(self):
        return os.path.join(MODEL_PATH, self.value['target'])

    @classmethod
    def exists(cls, key:str):
        return key.lower() in [key.lower() for key in cls.__members__.keys()]

class Document(Enum):
    INSURANCE = 'INSURANCE'
    LAND = 'LAND'
    SERVICE_CONTRACT = 'SERVICE_CONTRACT'
    EMPLOYMENT_CONTRACT = 'EMPLOYMENT_CONTRACT'
    CONFIDENTIALITY_AGREEMENT = 'CONFIDENTIALITY_AGREEMENT'
    SALES_CONTRACT = 'SALES_CONTRACT'
    INDEPENDENT_CONTRACTOR_AGREEMENT = 'INDEPENDENT_CONTRACTOR_AGREEMENT'
    LOAN_AGREEMENT = 'LOAN_AGREEMENT'
    PARTNERSHIP_AGREEMENT = 'PARTNERSHIP_AGREEMENT'

    @classmethod
    def value_of(cls, value):
        for k, v in cls.__members__.items():
            if k == value:
                return v

class Prompts(Enum):
    GREETING = ['hi', 'hello', 'hey', 'howdy', 'yo',
                'sup', 'hiya', 'heya',
                'hi!', 'hello!', 'hey!', 'howdy!', 'yo!',
                'sup!', 'hiya!', 'heya!', "what's up!",
                'greetings', "what's up", 'good morning', 'good afternoon',
                'good evening', 'howdy', 'salutations','pleased to meet you', 'how are you',
                "what's new", "what's happening",
                "how's it going", "how's life", 'how do you do',
                'whats up', 'whats new', 'whats happening', 'hows it going', 'hows life'
            ]
    GREETING_RESPONSE = [
                         "Hey, Great day! I am here to help you! To begin, upload a document.",
                         "Hello, it's my pleasure meeting you! To begin, upload a document.",
                         "Hi, Let's chat! To begin, upload a document.",
                         "Hi there! How can I assist you today? To begin, upload a document.",
                         "Hello! How can I help you?  To begin, upload a document.",
                         "Good to see you! How can I be of service?  To begin, upload a document.",
                         "Welcome! How can I help you today? To begin, upload a document.",
                         "Hey there! What can I help you with? To begin, upload a document.",
                         "Hi, how can I make your day better? To begin, upload a document.",
                         "Greetings! What brings you here today? To begin, upload a document.",
                         "Hello! What can I do for you? To begin, upload a document.",
                         "Salutations! What can I assist you with? To begin, upload a document.",
                         "Hey! How can I be of help today? To begin, upload a document."
                     ]
    APPRECIATION = ['thanks', 'thank you', 'appreciate it',
         'grateful', 'cheers', 'nice one', 'alright', 'cool'
                    'bye', 'exit', 'quit', 'ok', 'okay',
                    'thanks!', 'thank you!', 'appreciate it!',
                    'grateful!', 'cheers!', 'nice one!', 'alright!', 'cool!',
                     'bye!', 'exit!', 'quit!', 'ok!', 'okay!'
                    ]
    APPRECIATION_RESPONSE = [
        'You\'re welcome!', 'No problem, happy to help.', 'Anytime, feel free to reach out if you need anything else.',
        'It was my pleasure.', 'Not a problem at all, glad I could assist you.', 'You\'re most welcome!',
        'Don\'t hesitate to contact me if you have any further questions.', 'I\'m always here to help.',
        'It\'s my job, happy to be of service.', 'Thank you for using our service, have a great day!'
    ]
    NO_DOCUMENT_PROVIDED_REPLY = "I need a document first before I can answer questions"
    SUMMARY = "Can you give me a summary of the document using easy to understand words or non-legal terms"
    INSURANCE = {
        "included_in_cover" : "Describe what is included in the cover",
        "excluded_from_cover" : "Describe what is excluded from the cover",
        "emergency_information" :"Who should I contact in case of emergency?"
    }
    LAND = {
        "description" : "Describe the property briefly",
        "terms_of_use" : "Describe the terms of use",
        "warranties_and_guarantees" : "Describe the warranties and guarantees"
    }
    SERVICE_CONTRACT = {
        "payment_and_services" : "How and what exactly is the vendor being paid for its services?",
        "obligations" : "What are my obligations?",
        "liability" : "Who will be responsible for mistakes?"
    }
    EMPLOYMENT_CONTRACT = {
        "start_date" : "What is the start date?",
        "benefits_and_packages" : "Describe the benefits and packages?",
        "schedule" : "Is there a defined schedule?",
        "response_deadline" :"Am I expected to give my answer before a certain date?"
    }
    CONFIDENTIALITY_AGREEMENT = {
        "confidential_info" : "What constitutes confidential information?",
        "timeframe" : "Within what timeframe does this agreement hold?",
        "breach" : "What constitutes a breach?",
        "obligations" : "Describe my obligations?",
        "steps_upon_violation" : "What steps will be taken if I violate?"
    }
    SALES_CONTRACT = {
        "coverage" : "What goods and services are covered?",
        "payment_plan" : "Is there a payment plan in place?",
        "details_of_delivery" : "Describe the details of delivery?"
    }
    INDEPENDENT_CONTRACTOR_AGREEMENT = {
        "schedule" : "Will I be required to work a set schedule?",
        "payment_terms" : "Describe the payment terms?",
        "details_of_termination" : "What is the minimum notice which will be provided in case of an,"
                                                     "early contract termination?"
    }
    LOAN_AGREEMENT = {
        "loan_amount" : "What is the loan amount?",
        "interest_rate" : "What is the interest rate?",
        "timeframe" : "What is the timeframe of the agreement?",
        "method_of_repayment" : "What is the method of repayment?",
        "late_payment_info" :"What happens in case there are late or missed payments?"
    }
    PARTNERSHIP_AGREEMENT = {
        "responsibilities" : "Describe the responsibilities of the partners?",
        "restrictions" : "What are the restriction on partners",
        "dispute_resolution" : "How will disputes be resolved?"
    }

    @classmethod
    def value_of(cls, value):
        for k, v in cls.__members__.items():
            if k == value:
                return v

class Language(Enum):
    AFRIKAANS = 'af'
    ALBANIAN = 'sq'
    AMHARIC = 'am'
    ARABIC = 'ar'
    ARMENIAN = 'hy'
    AZERBAIJANI = 'az'
    BASQUE = 'eu'
    BELARUSIAN = 'be'
    BENGALI = 'bn'
    BOSNIAN = 'bs'
    BULGARIAN = 'bg'
    CATALAN = 'ca'
    CEBUANO = 'ceb'
    CHICHEWA = 'ny'
    CHINESE_SIMPLIFIED = 'zh-cn'
    CHINESE_TRADITIONAL = 'zh-tw'
    CORSICAN = 'co'
    CROATIAN = 'hr'
    CZECH = 'cs'
    DANISH = 'da'
    DUTCH = 'nl'
    ENGLISH = 'en'
    ESPERANTO = 'eo'
    ESTONIAN = 'et'
    FILIPINO = 'tl'
    FINNISH = 'fi'
    FRENCH = 'fr'
    FRISIAN = 'fy'
    GALICIAN = 'gl'
    GEORGIAN = 'ka'
    GERMAN = 'de'
    GREEK = 'el'
    GUJARATI = 'gu'
    HAITIAN_CREOLE = 'ht'
    HAUSA = 'ha'
    HAWAIIAN = 'haw'
    HEBREW = 'he'
    HINDI = 'hi'
    HMONG = 'hmn'
    HUNGARIAN = 'hu'
    ICELANDIC = 'is'
    IGBO = 'ig'
    INDONESIAN = 'id'
    IRISH = 'ga'
    ITALIAN = 'it'
    JAPANESE = 'ja'
    JAVANESE = 'jw'
    KANNADA = 'kn'
    KAZAKH = 'kk'
    KHMER = 'km'
    KOREAN = 'ko'
    KURDISH_KURMANJI = 'ku'
    KYRGYZ = 'ky'
    LAO = 'lo'
    LATIN = 'la'
    LATVIAN = 'lv'
    LITHUANIAN = 'lt'
    LUXEMBOURGISH = 'lb'
    MACEDONIAN = 'mk'
    MALAGASY = 'mg'
    MALAY = 'ms'
    MALAYALAM = 'ml'
    MALTESE = 'mt'
    MAORI = 'mi'
    MARATHI = 'mr'
    MONGOLIAN = 'mn'
    MYANMAR_BURMESE = 'my'
    NEPALI = 'ne'
    NORWEGIAN = 'no'
    ODIA = 'or'
    PASHTO = 'ps'
    PERSIAN = 'fa'
    POLISH = 'pl'
    PORTUGUESE = 'pt'
    PUNJABI = 'pa'
    ROMANIAN = 'ro'
    RUSSIAN = 'ru'
    SAMOAN = 'sm'
    SCOTS_GAELIC = 'gd'
    SERBIAN = 'sr'
    SESOTHO = 'st'
    SHONA = 'sn'
    SINDHI = 'sd'
    SINHALA = 'si'
    SLOVAK = 'sk'
    SLOVENIAN = 'sl'
    SOMALI = 'so'
    SPANISH = 'es'
    SUNDANESE = 'su'
    SWAHILI = 'sw'
    SWEDISH = 'sv'
    TAJIK = 'tg'
    TAMIL = 'ta'
    TELUGU = 'te'
    THAI = 'th'
    TURKISH = 'tr'
    UKRAINIAN = 'uk'
    URDU = 'ur'
    UYGHUR = 'ug'
    UZBEK = 'uz'
    VIETNAMESE = 'vi'
    WELSH = 'cy'
    XHOSA = 'xh'
    YIDDISH = 'yi'
    YORUBA = 'yo'
    ZULU = 'zu'

    @classmethod
    def value_of(cls, value):
        for k, v in cls.__members__.items():
            if v.value == value:
                return v

    @classmethod
    def name_of(cls, value):
        for k, v in cls.__members__.items():
            if k == value:
                return v

class Product(Enum):
    WEB = 'WEB'
    MESSAGING = "MESSAGING"

l = ["Greetings",
                "What's up",
                "Good morning",
                "Good afternoon",
                "Good evening",
                "Howdy",
                "Salutations",
                "Nice to meet you",
                "Pleased to meet you",
                "How are you",
                "What's new",
                "What's happening",
                "How's it going",
                "How's life",
                "How do you do"]