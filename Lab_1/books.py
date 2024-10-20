# TODO Найдите количество книг, которое можно разместить на дискете

b_in_kb, kb_in_mb = 1024, 1024

character_size = 4;
characters_in_string = 25;
strings_in_page = 50;
pages_in_book = 100;

book_size = character_size * characters_in_string * strings_in_page * pages_in_book

floppy_size = int(1.44 * kb_in_mb * b_in_kb)

print("Количество книг, помещающихся на дискету:", floppy_size // book_size)
