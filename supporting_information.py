url_dict = {"https://www.bbc.com/news/technology?page=1":"ssrcss-1cm0vxx-LinkPostHeadline ej9ium94",
            "https://edition.cnn.com/business/tech":"container__headline-text",
            "https://www.nbcnews.com/tech-media":"styles_headline__ice3t",
            "https://www.theguardian.com/technology/all":"u-faux-block-link__overlay js-headline-text",
            "https://www.npr.org/sections/technology/":"title",
            "https://www.cbsnews.com/technology/":"item__hed",
            "https://abcnews.go.com/Technology":"AnchorLink",
            "https://www.ft.com/technology":"js-teaser-heading-link",
            "https://www.cnbc.com/technology":"Card-title",
            "https://www.bloomberg.com/technology":"hover:underline focus:underline"
            }

exclusion_words = ['A', 'An', 'The',
             "Aboard", "About", "Above", "Across", "After", "Against", "Along", "Amid",
             "Among", "Around", "As", "At", "Before", "Behind", "Below", "Beneath",
             "Beside", "Between", "Beyond", "But", "By", "Concerning", "Despite",
             "During", "Except", "For", "From", "In", "Into", "Near", "Of", "Off", "On",
             "Over", "Past", "Regarding", "Through", "To",
             "Accordingly", "Additionally", "Also", "Anyway", "Besides", "Certainly",
             "Conversely", "Finally", "Hence", "However", "Instead", "In conclusion",
             "Lately", "Likewise", "Moreover", "Namely", "Nevertheless", "So", "Then", "Yet", "How",
             "After", "Is", "I", "You", "He", "She", "It", "We", "They", "What", "Who", "Me", "Him",
             "Her", "It", "Us", "You", "Them", "Whom", "With",
             'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
             'S', 'T', 'U', 'V', 'W', 'Y', 'Z',
             "New", "Big", "Small",
             'All', 'Both', 'Each', 'Every', 'Any', 'Some', 'Few', 'Little', 'Many', 'Much', 'Neither', 'Either', 'No',
             'Another', 'Several', 'What', 'Whatever', 'Which', 'Whichever',
             'Clearly', 'Quickly', 'Carefully', 'Completely', 'Now', 'Well', 'Yesterday', 'Today', 'Always', 'Never',
             'Often', 'Rarely', 'Sometimes', 'Soon', 'Late', 'Early', 'Here', 'There', 'Everywhere', 'Nowhere',
             'Everywhen', 'Nowhen', 'Everyhow', 'Nowhow', 'Somewhere', 'Anywhere', 'Everyday', 'Nowadays', 'Once',
             'Twice', 'Thrice', 'Again', 'Anymore', 'Almost', 'Already', 'Yet', 'Still', 'Just', 'Too', 'Enough',
             'Quite', 'Rather', 'Very', 'So', 'Thus', 'Hence', 'Therefore', 'Otherwise', 'Indeed', 'Surely',
             'Certainly', 'Possibly', 'Probably', 'Likely', 'Unlikely', 'Certainly', 'Definitely', 'Absolutely',
             'Naturally', 'Accidentally', 'Intentionally', 'Gradually', 'Suddenly', 'Briefly', 'Loudly', 'Softly',
             'Silently', 'Quickly', 'Slowly', 'Carefully', 'Roughly', 'Smoothly', 'Effortlessly', 'Frequently',
             'Rarely', 'Occasionally', 'Regularly', 'Randomly', 'Seldom', 'Always', 'Never', 'Often', 'Sometimes',
             'Twice', 'Thrice', 'Once', 'Again', 'Here', 'There', 'Everywhere', 'Nowhere', 'Everywhen', 'Nowhen',
             'Everyhow', 'Nowhow', 'Somewhere', 'Anywhere', 'Everyday', 'Nowadays',
             "Up", "Down", "Why", "Will"
             ]
