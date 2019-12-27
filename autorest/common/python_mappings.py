# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
primary_types = {
    None: "",
    "long": "long",
    "double": "float",
    "decimal": "decimal.Decimal",
    "stream": "Generator",
    "datetimerfc1123": "datetime.datetime",
    "timespan": "timedelta",
    # "base64url": "bytes",
    # "duration": "datetime.timedelta",
    "boolean": "bool",
    # "byte-array": "bytearray",
    "char": "str",
    "constant": "constant",
    "credential": "azure.core.credentials.TokenCredential",
    # "date": "datetime.datetime",
    # "date-time": "datetime.datetime",
    # "duration": "datetime.timedelta",
    # "flag",
    # "integer": "int",
    # "not",
    # "number": "float",
    "object": "object",
    # "odata-query",
    # "or",
    # "parameter-group",
    # "string": "str",
    # "unixtime": "unix-time",
    # TODO: is uri a string?
    # "uri",
    "uuid": "str"
    # "xor"
}

basic_latin_chars = {
    ' ': "Space",
    '!': "ExclamationMark",
    '"': "QuotationMark",
    '#': "NumberSign",
    '$': "DollarSign",
    '%': "PercentSign",
    '&': "Ampersand",
    "'": "Apostrophe",
    '(': "LeftParenthesis",
    ')': "RightParenthesis",
    '*': "Asterisk",
    '+': "PlusSign",
    ',': "Comma",
    '-': "HyphenMinus",
    '.': "FullStop",
    '/': "Slash",
    '0': "Zero",
    '1': "One",
    '2': "Two",
    '3': "Three",
    '4': "Four",
    '5': "Five",
    '6': "Six",
    '7': "Seven",
    '8': "Eight",
    '9': "Nine",
    ':': "Colon",
    ';': "Semicolon",
    '<': "LessThanSign",
    '=': "EqualSign",
    '>': "GreaterThanSign",
    '?': "QuestionMark",
    '@': "AtSign",
    '[': "LeftSquareBracket",
    '\\': "Backslash",
    ']': "RightSquareBracket",
    '^': "CircumflexAccent",
    '`': "GraveAccent",
    '{': "LeftCurlyBracket",
    '|': "VerticalBar",
    '}': "RightCurlyBracket",
    '~': "Tilde"
}

reserved_words = [
    "and","as","assert","break","class","continue",
    "def","del","elif","else","except","exec",
    "finally","for","from","global","if","import",
    "in","is","lambda","not","or","pass",
    "print","raise","return","try","while","with",
    "yield", "async", "await",
    "int","bool","bytearray","date","datetime","float",
    "long","object","decimal","str","timedelta", "mro", "self"
]
