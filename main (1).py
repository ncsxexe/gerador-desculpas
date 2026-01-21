import streamlit as st
import random

st.title("=-=-=-= Gerador de Desculpas =-=-=-=")

gifs = [
    'https://media.giphy.com/media/QMHoU66sBXqqLqYvGO/giphy.gif',
    'https://media4.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3czF3aDd2MDBrdmR3ZjJ1YWN6YmQxcGdnbXF6NjgxOTlzNXZxN2I1ayZlcD12MV9naWZzX3NlYXJjaCZjdD1n/szaTML0LZFAQa3do7Y/giphy.webp',
    'https://media4.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3Y216MWpiempxaDI1eXU1emZyeG5nMm9zcTFtdmRibW13dmNteTYyZiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/8b5d9cNMtxfOfq0LrW/giphy.webp',
    'https://media2.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3bTN6eHE5YnFpcG5leG82OGIyZmI3eDZubzEwaGV6MDk2M3RkNG9hNyZlcD12MV9naWZzX3NlYXJjaCZjdD1n/ocMluvVcZh773gy6Ri/200.webp',
    'https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExemY1dmhmMW1lMzRqOW4waHR2Y3pyNHYyYWYwZzVubndhN2F1NGl0MiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/JgXt2JvnFhoxW/200w.webp'
]

desculpas = [
    'Não vou nessa merda', 'No. FUCK YOU!', 'Quero que se foda tudo isso',
    'Me esquece'
]

nome = st.text_input('Digite o nome da pessoa que você quer se desculpar: ')

if st.button('Gerar desculpa'):
  desculpa_escolhida = random.choice(desculpas)
  st.write(f"## Desculpa para o(a) {nome}: {desculpa_escolhida}")
  st.image(random.choice(gifs))
