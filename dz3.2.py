import re
from collections import Counter

def top_10_words(text):
    words = re.findall(r'\b\w+\b', text.lower())
    return Counter(words).most_common(10)

text = """Як-1 — советский одномоторный самолёт-истребитель Второй мировой войны. Первый боевой самолёт, разработанный заводом № 115 под управлением Александра Сергеевича Яковлева как опытный истребитель И-26, ранее КБ занимались спортивными и учебными самолётами. Новый самолёт создавали на базе спортивной модели Я-7. В январе 1940 года он совершил первый полёт, а второй полёт привёл к аварии, в результате которой погиб пилот, а самолёт разбился. Было выявлено, что причиной катастрофы был производственный дефект. Несмотря на аварию ещё до завершения государственных испытаний было принято решение о запуске в серийное производство под маркой Як-1.[1] Производился с 1940 по 1944 годы; к 22 июня 1941 года было выпущено 425 самолётов; всего было построено 8734 самолёта всех модификаций"""
print(top_10_words(text))