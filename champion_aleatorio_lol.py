import random
import datetime

builds = ['Full AD', 'Full AP', 'Letalidade', 'Itens de Suporte', '1 Item de cada categoria', 'Itens Normais', 'Attack Speed', 'Movement Speed', 'Itens de Cura', 'Itens de Tank', 'Os itens mais roubados do jogo', 'Sem míticos']

lanes = ['Top', 'Jungle', 'Mid', 'ADC', 'Sup']

top = ['Aatrox', 'Akali', 'Akshan', 'Camille', 'Cho Gath', 'Darius', 'Dr.Mundo', 'Fiora', 'Gangplank', 'Garen', 'Gnar', 'Gragas', 'Gwen', 'Illaoi', 'Irelia', 'Jax', 'Jayce', 'KSante', 'Kayle', 'Kennen', 'Kled', 'Malphite', 'Maokai', 'Mordekaiser', 'Nasus', 'Olaf', 'Ornn', 'Pantheon', 'Poppy', 'Quinn', 'Renekton', 'Rengar', 'Riven', 'Rumble', 'Sett', 'Shen', 'Singed', 'Sion', 'Teemo', 'Trundle', 'Tryndamere', 'Urgot', 'Vladmir', 'Volibear', 'Warwick', 'Yone', 'Yorick']

jungle = ['Amumu', 'Bel Veth', 'Diana', 'Ekko', 'Elise', 'Evelynn', 'Fiddlesticks', 'Gragas', 'Graves', 'Hecarim', 'Ivern', 'Jarvan IV', 'Karthus', 'Kayn', 'Kha Zix', 'Kindred', 'Lee Sin', 'Lilia', 'Maokai', 'Master Yi', 'Noctune', 'Nidalee', 'Nunu e Willump ou Nunes', 'Poppy', 'Rammus', 'Rek Sai', 'Rengar', 'Sejuani', 'Shaco', 'Shyvana', 'Skarner', 'Sylas', 'Taliyah', 'Talon', 'Trundle', 'Udyr', 'Vi', 'Viego', 'Volibear', 'Warwick', 'Wukong', 'Xin Xhao', 'Zac', 'Zed']

mid = ['Ahri', 'Akali', 'Akshan', 'Anivia', 'Annie', 'Aurelion Sol', 'Azir', 'Cassiopeia', 'Corki', 'Diana', 'Ekko', 'Fizz', 'Galio', 'Irelia', 'Kassadin', 'Katarina', 'LeBlanc', 'Lissandra', 'Lux', 'Malzahar', 'Neeko', 'Orianna', 'Pantheon', 'Qiyana', 'Rumble', 'Ryze', 'Swain', 'Sylas', 'Syndra', 'Taliyah', 'Talon', 'Tristana', 'Twisted Fate', 'Veigar', 'Vel Koz', 'Vex', 'Viktor', 'Xerath', 'Yasuo', 'Yone', 'Zed', 'Ziggs', 'Zoe']

adc = ['Aphelios', 'Ashe', 'Caitlyn', 'Draven', 'Ezreal', 'Jhin', 'Jinx', 'Kai Sa', 'Kalista', 'Karthus', 'Kog Maw', 'Lucian', 'Miss Fortune', 'Nilah', 'Samira', 'Seraphine', 'Sivir', 'Tristana', 'Twitch', 'Varus', 'Vayne', 'Veigar', 'Xayah', 'Zeri', 'Ziggs']

sup = ['Amumu', 'Annie', 'Ashe', 'Bardo', 'Blitzcrank', 'Brand', 'Braum', 'Heimerdinger', 'Janna', 'Karma', 'Leona', 'Lulu ou Lulux', 'Lux', 'Maokai', 'Milio', 'Morgana', 'Nami', 'Nautilus', 'Neeko', 'Pyke', 'Rakan', 'Rell', 'Renata Glasc', 'Senna', 'Seraphine', 'Sona', 'Soraka', 'Swain', 'Tahm Kench', 'Taric', 'Thresh', 'Vel Koz', 'Xerath', 'Yummi', 'Zilean', 'Zyra']

print('Feito por R$L')
print('Programa Atualizado no dia: 20/04/2023')
print(f'Hora e dia executado: {datetime.datetime.now()}\n')

lanes = random.choice(lanes)
print(f'A lane escolhida foi: {lanes}')

if lanes == 'Top':
  print(f'O campeão escolhido foi: {random.choice(top)}')

if lanes == 'Jungle':
  print(f'O campeão escolhido foi: {random.choice(jungle)}')

if lanes == 'Mid':
  print(f'O campeão escolhido foi: {random.choice(mid)}')

if lanes == 'ADC':
  print(f'O campeão escolhido foi: {random.choice(adc)}')

if lanes == 'Sup':
  print(f'O campeão escolhido foi: {random.choice(sup)}')

builds = random.choice(builds)
print(f'A build do campeão será: {builds}')

