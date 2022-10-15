# from translate import Translator #doesn't work well
from deep_translator import GoogleTranslator


def translate(strVal):
    # translator = Translator(from_lang='English', to_lang='Hindi')
    print(strVal)
    # translation = translator.translate(strVal)
    # print(translation)
    return GoogleTranslator(source='auto', target='hi').translate(strVal)


def readXmlAndTranslate():
    from xml.dom import minidom

    # parse a xml file by name
    file = minidom.parse('strings.xml')

    # use getElementsByTagName() to get tag
    models = file.getElementsByTagName('string')

    # one specific item attribute
    # print('model #2 attribute:')
    # print(models[1].attributes['name'].value)

    # all item attributes
    # print('\nAll attributes:')
    # for elem in models:
    #     print(elem.attributes['name'].value)

    # one specific item's data
    # print('\nmodel #2 data:')
    # print(models[1].firstChild.data)
    # print(models[1].childNodes[0].data)

    # all items data
    print('\nAll model data:')
    for elem in models:
        print(f"<string>{translate(str(elem.firstChild.data))}</string>")


readXmlAndTranslate()
