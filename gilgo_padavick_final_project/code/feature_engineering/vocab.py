neutral_sentiment = [
    "news",
    "update",
    "alert",
    "company",
    "2021",
    "available",
    "#stocks",
    "free",
    ":brain:",
    "hold"
]

positive_sentiment = [
    ":rocket:",
    ":fire:",
    "rocket",
    ":moneybag:",
    "buy",
    ":pray:",
    ":dollar:",
    "moon",
    ":bangbang:",
    ":gem:",
    ":slot_machine:"
    "house",
    "rich",
    ":eyes:",
    ":collision:",
    "ath"

]

negative_sentiment = [
    "offering",
    "dump",
    "short",
    "public",
    "proposed",
    "down",
    "red",
    "dip",
    "diamond",
    "pump and dump",
    "out",
    "sell",
    "sold"
]

inflection_point = [
    "current",
    "list",
    "gold",
    "excited",
    "cheap",
    "merger",
    "bad",
    "underwritten",
    "wait",
    "see",
    "annouces",
    "profit"
]

def get_all_vocab():
    vocab = neutral_sentiment
    vocab.extend(positive_sentiment)
    vocab.extend(negative_sentiment)
    vocab.extend(inflection_point)
    return vocab
