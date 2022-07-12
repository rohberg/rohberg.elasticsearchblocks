from plone.i18n.normalizer.interfaces import IIDNormalizer
from zope.component import getUtility
from zope.interface import provider
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleVocabulary


@provider(IVocabularyFactory)
def InformationtypeVocabularyFactory(context=None):
    """Vocabulary."""
    normalizer = getUtility(IIDNormalizer)

    terms = []
    registryvalue = {
        "manual": "Manual",
        "release-note": "Release Note",
    }
    for el in registryvalue:
        el_lower = normalizer.normalize(el)
        terms.append(SimpleVocabulary.createTerm(el_lower, el_lower, registryvalue[el]))
    return SimpleVocabulary(terms)
