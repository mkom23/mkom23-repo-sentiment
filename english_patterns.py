# english_patterns.py
import re

EN_PATTERN = re.compile(
    r"""
    \b(
        # ==================================
        # FUNCTION WORDS / GRAMMAR
        # ==================================
        the|a|an|and|or|but|if|then|else|
        with|without|for|from|to|of|in|on|at|by|about|as|

        # ==================================
        # PRONOUNS & DETERMINERS
        # ==================================
        i|you|we|they|he|she|it|
        me|him|her|us|them|
        my|your|his|her|its|our|their|
        this|that|these|those|

        # ==================================
        # AUXILIARY & MODAL VERBS
        # ==================================
        is|am|are|was|were|be|been|being|
        have|has|had|
        do|does|did|
        will|would|can|could|should|may|might|must|

        # ==================================
        # COMMON VERBS (UMUM)
        # ==================================
        make|makes|made|
        get|gets|got|
        take|takes|took|
        give|gives|gave|
        go|goes|went|
        come|comes|came|
        see|saw|seen|
        know|knows|knew|
        think|thought|
        use|used|using|
        work|works|worked|
        study|studied|studying|
        discuss|discussed|discussing|
        show|showed|shown|

        # ==================================
        # ADJECTIVES (UMUM)
        # ==================================
        good|bad|better|best|
        new|old|
        big|small|large|
        important|different|similar|
        possible|simple|clear|

        # ==================================
        # PEOPLE & SOCIAL TERMS (UMUM)
        # ==================================
        people|person|
        woman|women|man|men|
        student|students|
        teacher|teachers|
        group|groups|team|teams|

        # ==================================
        # ACADEMIC TERMS (UMUM)
        # ==================================
        research|study|method|
        result|results|data|paper|

        # ==================================
        # COMMON PHRASE PARTS
        # ==================================
        based|related|focused|included|using
    )\b
    """,
    re.IGNORECASE | re.VERBOSE
)
