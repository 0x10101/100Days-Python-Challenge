template = "Once upon a time, there was a very sick boy named %(name)s. His tummy hurt, his head hurt, even his %(body_part)s hurt. He puked all over his %(noun)s. When he slept, he had dreams about %(plural_noun)s fighting %(adverb)s"
dictionary = {}
dictionary["name"] = raw_input("Enter a name:")
dictionary["body_part"] = raw_input("Name a body part:")
dictionary["noun"] = raw_input("Enter a noun:")
dictionary["plural_noun"] = raw_input("Enter another noun (plural):")
dictionary["adverb"] = raw_input("Enter an adverb:")
print template % dictionary
