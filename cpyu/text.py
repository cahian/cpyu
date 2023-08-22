from difflib import SequenceMatcher
import unicodedata


def title(str):
    return str.strip().title()


def tsv(l):
    """Tab-delimited Text (or Tab Separated Values)"""
    # return "\t".join([str(v) for v in l]) + "\n"
    return "\t".join(l) + "\n"


def removeprefix(str, prefix):
    if str.startswith(prefix):
        return str[len(prefix):]
    return str


def removesuffix(str, suffix):
    if str.endswith(suffix):
        return str[:-len(suffix)]
    return str


def removeaccents(str):
    nfkd_form = unicodedata.normalize('NFKD', str)
    return u"".join([c for c in nfkd_form if not unicodedata.combining(c)])


def lowerstrcmp(str1, str2):
    """Compara se as duas strings em minúsculo são iguais."""
    return str1.lower() == str2.lower()


def sloppystrcmp(str1, str2):
    """Compara se uma string em minúsculo contém a outra e vice-versa.
    
    *Essa função ela ignora os acentos das strings.
    """
    if str1 and str2:
        newstr1, newstr2 = removeaccents(str1), removeaccents(str2)
        return newstr1.lower() in newstr2.lower() or newstr2.lower() in newstr1.lower()
    return False


def sloppycmp(str1, str2):
    """Alias to sloppystrcmp."""
    return sloppystrcmp(str1, str2)


def strtobool(str, true="sim"):
    """Converte string para boleano."""
    return lowerstrcmp(str, true)


def findsimilar(lista: list[str], b: str) -> str:
    maxratio = 0.0
    maxvalue = ""
    for a in lista:
        ratio = SequenceMatcher(None, a.lower(), b.lower()).ratio()
        if ratio > maxratio:
            maxratio = ratio
            maxvalue = a
    return maxvalue
