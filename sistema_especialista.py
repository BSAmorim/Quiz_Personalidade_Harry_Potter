from base_dados import baseconhecimento

class SistemaEspecialista:
  def personalidade(self, fatos):
    base_conhecimento = baseconhecimento()
    placar = {casa: 0 for casa in base_conhecimento["casas"]}

    for adj in fatos:
      for casa, dados in base_conhecimento["casas"].items():
        for palavra, num in dados['caracteristicas'].items():
          if(adj == palavra):
            placar[casa] += num
    return max(placar, key=placar.get)