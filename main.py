from sistema_especialista import SistemaEspecialista
from regras import comparadorResposta
import os
import subprocess

def limpa_tela():
  command = 'cls' if os.name == 'nt' else 'clear'
  subprocess.run([command], shell=True)

se = SistemaEspecialista()
fatos = []
opcaoEscolhida = ''
numQuestao = 1

while True:
  nome = input("Digite seu nome: ")
  
  # Questão 1
  print("Qual é a sua maior motivação no dia a dia?\n")
  opcaoEscolhida = input(
      "A) Alcançar grandes objetivos e ter o meu valor reconhecido por todos.\n" + 
      "B) Compreender como o mundo funciona e expandir meus conhecimentos.\n" +
      "C) Dedicar-me com afinco às minhas tarefas e ver o resultado do meu esforço.\n" +
      "D) Agir com bravura diante do desconhecido e proteger meus ideais.\n\n" +
      "Insira a Resposta: "
      )
  fatos.append(comparadorResposta(numQuestao, opcaoEscolhida.lower()))
  numQuestao += 1
  limpa_tela()
  
  # Questão 2
  print("Como você lida com problemas complexos e inesperados?\n")
  opcaoEscolhida = input(
      "A) Analiso a situação friamente usando a lógica para tomar a decisão correta.\n" + 
      "B) Mantenho a calma, sou tolerante e espero o momento certo para agir.\n" +
      "C) Encontro atalhos inteligentes e contorno as regras para resolver rápido.\n" +
      "D) Mantenho o foco inabalável no objetivo e não desisto até superar o obstáculo.\n\n" +
      "Insira a Resposta: "
      )
  fatos.append(comparadorResposta(numQuestao, opcaoEscolhida.lower()))
  numQuestao += 1
  limpa_tela()
  
  # Questão 3
  print("Qual destas qualidades você considera indispensável em si mesmo?\n")
  opcaoEscolhida = input(
      "A) Ser uma pessoa autêntica, transparente e que cumpre o que diz.\n" + 
      "B) Ser destemido, ousado e disposto a correr riscos que outros evitam.\n" +
      "C) Ter capacidade de pensar por conta própria sem depender da aprovação alheia.\n" +
      "D) Ter garra constante para continuar em frente, mesmo quando tudo dá errado.\n\n" +
      "Insira a Resposta: "
      )
  fatos.append(comparadorResposta(numQuestao, opcaoEscolhida.lower()))
  numQuestao += 1
  limpa_tela()
  
  # Questão 4
  print("O que torna um líder verdadeiramente respeitável?\n")
  opcaoEscolhida = input(
      "A) A habilidade de guiar o grupo com visão clara e autoridade firme.\n" + 
      "B) A capacidade de ter ideias fora do padrão e inovar nos momentos difíceis.\n" +
      "C) O compromisso inabalável de apoiar seus companheiros em qualquer situação.\n" +
      "D) A disposição para ser o primeiro a enfrentar o perigo em favor da equipe.\n\n" +
      "Insira a Resposta: "
      )
  fatos.append(comparadorResposta(numQuestao, opcaoEscolhida.lower()))
  numQuestao += 1
  limpa_tela()
  
  # Questão 5
  print("Como você prefere passar o seu tempo livre?\n")
  opcaoEscolhida = input(
      "A) Lendo, aprendendo novas habilidades ou explorando assuntos complexos.\n" + 
      "B) Traçando metas para o futuro e organizando meus projetos pessoais.\n" +
      "C) Ajudando pessoas próximas ou me dedicando a causas em que acredito.\n" +
      "D) Aprendendo algo prático com paciência até dominar perfeitamente.\n\n" +
      "Insira a Resposta: "
      )
  fatos.append(comparadorResposta(numQuestao, opcaoEscolhida.lower()))
  numQuestao += 1
  limpa_tela()
  
  # Questão 6
  print("Um amigo cometeu um erro grave em um projeto em grupo. Qual é o seu posicionamento?\n")
  opcaoEscolhida = input(
      "A) Permaneço leal a ele até o fim e assumo a responsabilidade com determinação.\n" + 
      "B) Analiso o erro com razão e ajudo-o com paciência a corrigir o problema.\n" +
      "C) Assumo a liderança da situação para salvar o projeto e garanto a nossa vitória.\n" +
      "D) Penso em uma solução criativa e independente sem precisar depender do grupo.\n\n" +
      "Insira a Resposta: "
      )
  fatos.extend(comparadorResposta(numQuestao, opcaoEscolhida.lower()))
  limpa_tela()
  print(fatos)

  print(f"Parabéns {nome}, quiz concluído \n\nSua casa é: {se.personalidade(fatos)}")

  fimloop = input("Deseja fazer novamente? (S/N)")
  if(fimloop.lower() == 's'):
    numQuestao = 1
    fatos.clear()
    limpa_tela()
    continue
  else:
    break
  
  