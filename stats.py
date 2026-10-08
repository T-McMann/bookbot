def get_num_words(text: str) -> int:
    words = text.split()
    return len(words)

def get_char_counts(text):
	characters = {}
	for char in text:
		char = char.lower()
		if char in characters:
    			characters[char] += 1
		else:
    			characters[char] = 1
	return characters

def sort_on(item: tuple[str, int]) -> int:
	return item[1]

def chars_dict_to_sorted_list(characters):
	sorted_char = []
	for char in characters:
		count = characters[char]
		sorted_char.append((char, count))
	sorted_char_count = sorted(sorted_char, reverse=True, key=sort_on)
	return sorted_char_count
