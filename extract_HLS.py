from bs4 import BeautifulSoup

# Пътища към файловете
file_path = "C:\\Users\\a1bg537940\\Desktop\\HLS Downloader.html"  # Вашият HTML файл
result = "C:\\Users\\a1bg537940\\Desktop\\result.txt"  # Резултатен файл за линковете
output = "C:\\Users\\a1bg537940\\Desktop\\standart.m3u8"  # Изходен M3U8 файл

# Отваряне и четене на HTML файла
with open(file_path, "r", encoding="utf-8") as file:
    html = file.read()

# Парсване на HTML с BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Извличане на всички линкове от атрибута title на <td> елементи с клас "url"
m3u8_links = []

# Търсене на <td> елементи с клас "url" и извличане на линковете от атрибута title
for td_tag in soup.find_all('td', class_='url'):
    link = td_tag.get('title')
    if link and '.m3u8' in link:  # Проверка дали линкът съдържа .m3u8
        # Пропускане на линкове, които съдържат 'low', 'mid' или 'hd720'
        if any(exclude in link for exclude in ['low', 'mid', 'hd720']):
            continue
        m3u8_links.append(link)

# Премахване на дубликатите
m3u8_links = list(dict.fromkeys(m3u8_links))

# Премахване на символите &amp; от линковете
m3u8_links = [link.replace('&amp;', '&') for link in m3u8_links]

# Записване на линковете в текстов файл
with open(result, "w", encoding="utf-8") as result_file:
    if m3u8_links:
        for link in m3u8_links:
            result_file.write(f"{link}\n")
    else:
        result_file.write("Не са намерени .m3u8 линкове.\n")

# Път към M3U8 файла за резултата
if m3u8_links:
    try:
        with open(output, 'r+', encoding='utf-8') as standard_file:
            lines = standard_file.readlines()

            # Добавяне на линкове на всеки 4-ти ред
            while len(lines) < 3:
                lines.append("\n")

            for i, link in enumerate(m3u8_links):
                index = 3 + 3 * i  # Индекс за всеки 4-ти ред
                while len(lines) <= index:
                    lines.append("\n")
                lines.insert(index, link + "\n")

            standard_file.seek(0)
            standard_file.writelines(lines)

    except FileNotFoundError:
        print("Файлът 'standart.m3u8' не съществува. Ще го създам.")
        with open(output, 'w', encoding='utf-8') as standard_file:
            for i, link in enumerate(m3u8_links):
                if i == 0:
                    standard_file.write("\n" * 3)  # Добавяме 3 празни реда преди първия линк
                standard_file.write(link + "\n")
                if i < len(m3u8_links) - 1:
                    standard_file.write("\n")  # Добавяме празен ред след всеки линк, освен последния

    print("Линковете са добавени в standart.m3u8.")
else:
    print("Не са намерени .m3u8 линкове.")
