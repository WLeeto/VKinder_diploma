# В этом файле содержатся паттерны, для поиска ключевых слов в сообщениях пользователей в чате
# Можно добавлять свои паттерны, расширяя логику взаимодействия чат-бота


# Привет
hello_patterns = [r"\.?([П|п]ривет)\.?", r"\.?([З|з]дравствуй)\.?", r"\.?([П|п]рив)\.?", r"\.?([З|з]доров[а|\s|о])\.?",
                  r"\.?([H|h]ello)\.?", r"[^|\s|,]([H|h]i[\s|,|!|.]?)\.?", r"(^[H,h]i)"]

# Пока
bye_patterns = [r"\.?([П|п]ока)\.?", r"\.?([Д|д]о\s?свид)\.?", r"\.?([П|п]океда)\.?", r"\.?([B|b]ye)\.?",
                r"\.?([G|g]oodbye)\.?", r"\.?([С|с]частливо)\.?"]