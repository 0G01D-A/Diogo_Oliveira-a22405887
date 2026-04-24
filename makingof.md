# Making Of — Modelação do Portefólio

## 1. Introdução

Criação do Diário de bordo 

---

## 2. Fotografias do DER e Apontamentos

![DER Final](https://github.com/0G01D-A/Diogo_Oliveira-a22405887/blob/main/media/makingof/Modelo_entidade.jpeg)


---

## 3. Evolução do Modelo


### Versão Inicial

Numa primeira fase, foram identificadas as entidades principais do sistema, nomeadamente:

* Curso  
* UnidadeCurricular    

Os atributos definidos eram ainda básicos e focados na identificação (nome, descrição).  

---

### Versão Intermédia

Numa fase posterior, criei mais entidades como por exemplo:

* Projetos  
* Professor  
* Aluno  
* Inscrição
* Tecnologias
* Competência
* Formações

---

### Versão Final

Na versão final (representada no DER desenhado).

Principais melhorias:

- Estruturação completa das entidades:
  * Projeto
  * Tecnologia
  * TFC
  * Competência
  * Formação
  * Aluno
  * Professor
  * Unidade Curricular
  * Curso

- Definição explícita das cardinalidades (1:N e N:M)

- Criação de relações adequadas entre entidades, nomeadamente:
  * Projeto ↔ Tecnologia (N:M)
  * Projeto ↔ Aluno (N:M)
  * Projeto ↔ Unidade Curricular (N:1)
  * TFC ↔ Tecnologia (N:M)
  * Formação ↔ Competência (N:M)
  * Competência ↔ Projeto (N:M)
  * 
---

## 4. Erros Identificados e Correções


### Erro 1: Relações mal definidas
* Problema: ligações diretas incorretas
* Correção: uso de tabelas associativas

### Erro 2: Ajustes à modelação da entidade TFC

Após análise do ficheiro JSON dos TFCs, verificou-se que a estrutura real dos dados não correspondia totalmente à modelação inicial. O ficheiro contém atributos como `autores`, `orientadores`, `licenciatura`, `sumario`, `pdf`, `imagem`, `palavras_chave`, `areas`, `tecnologias_usadas` e `rating`.

Identifiquei várias diferenças relevantes:
* o JSON não inclui os campos `estado`, `prioridade` e `aluno`
* o ano surge embutido no campo `licenciatura`
* os orientadores não aparecem estruturados como entidade relacionada, mas sim como texto
* o nível de interesse está representado pelo campo `rating`

Após as alterações necessárias, tudo ficou a funcionar como devia



---

## 5. Justificação das Decisões de Modelação

### Projeto
* Separação de tecnologias 

### Tecnologia
* Criação de entidade própria 
* Inclusão de nível de conhecimento

### TFC
* Uso de nível de interesse 
* Ligação a professor 

### Competência
* Separação de tecnologia
* Ligação a projetos 

### Formação
* Uso de datas 
* Classificação por tipo 

---

## 6. Estrutura Final do Modelo

O modelo final inclui as seguintes entidades:

* Projeto
* Tecnologia
* TFC
* Competência
* Formação
* Unidade Curricular
* Professor
* Inscrição
* Aluno
* Professor
* Curso

Com relações N:M e 1:N devidamente estruturadas.

---

## 7. Conclusão

O processo de modelação evoluiu de uma estrutura simples para um modelo mais normalizado e consistente, permitindo representar de forma adequada o portefólio académico e profissional.

## 8. Tradução do DER para Modelos Django

Após a definição do DER, foi realizada a sua implementação em Django através de classes models.Model.

Principais decisões:

Uso de ForeignKey para relações 1:N
Exemplo: UC → Curso, Projeto → UC
Uso de ManyToManyField para relações N:M
Projeto ↔ Aluno
Formação ↔ Competência

Uso de related_name para facilitar navegação reversa:

```python
curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name="ucs")
```

Isto permitiu escrever queries mais eficientes e legíveis:

```python
curso.ucs.all()
```

## ⚠️ 9. Problemas Reais na Implementação
Problema 1: Estrutura de relações mal pensada
Inicialmente algumas relações N:M foram modeladas como 1:N
Resultado: perda de flexibilidade
Correção: substituição por ManyToManyField
Problema 2: Performance (N+1 queries)

Quando comecei a listar dados nos templates, surgiram múltiplas queries à base de dados.

Exemplo:
```python
for aluno in alunos:
    aluno.projetos.all()
```
Problema: uma query por cada aluno.

Correção:

```python
alunos = Aluno.objects.prefetch_related("projetos")
```
E para relações diretas:
```python
select_related("uc", "curso")
```

## 🧠 10. Estratégia de Views (ponto crítico)

Cada modelo passou a ter:

* uma view dedicada
* uma query otimizada
* um template próprio

Exemplo:
```python
def projetos_view(request):
    projetos = Projeto.objects.select_related("uc").prefetch_related("alunos", "tecnologias")
    return render(request, "portfolio/projetos.html", {"projetos": projetos})
```
Isto evita:

queries redundantes
lógica no template

## 🎯 11. Estrutura do Frontend

Foi criada uma estrutura base reutilizável:

base.html com:
* header
* menu de navegação
* footer
* templates por entidade:
* cursos.html
* alunos.html
* professores.html
* etc.

Uso de:
```python
{% extends "base.html" %}
```

## 🎨 12. Gestão de ficheiros estáticos

Erro inicial:

CSS colocado em templates

Correção:

uso de pasta static/

Estrutura final:

portfolio/
├── static/
│   └── portfolio/
│       └── styles.css

Ligação no template:

```python
{% load static %}
<link rel="stylesheet" href="{% static 'portfolio/styles.css' %}">
```

## 📂 13. Gestão de media (imagens)

Para suportar imagens (ex: tecnologias):

uso de ImageField
configuração de:
* MEDIA_ROOT
* MEDIA_URL

E no urls.py:
```python
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```
## 14. Implementação do Portefólio (Interfaces de Consulta)

Após a definição e implementação do modelo de dados, foi desenvolvido o portefólio com o objetivo de permitir a consulta estruturada da informação.

Objetivo

Criar interfaces de listagem que permitam:

visualizar os dados de cada entidade
explorar relações entre entidades
validar a consistência do modelo na prática
Estrutura Implementada

Para cada entidade foi criada uma estrutura completa composta por:

* View (views.py)
* Template (HTML)
* URL (routing)

Este padrão foi aplicado de forma consistente a todos os modelos:

* Curso
* Unidade Curricular
* Professor
* Aluno
* Projeto
* TFC
* Tecnologia
* Competência
* Formação
* Inscrição
* Organização das Views

Cada entidade possui uma view dedicada responsável por:

obter dados da base de dados
otimizar consultas
enviar contexto para o template

Exemplo:
```python
def projetos_view(request):
    projetos = Projeto.objects.select_related("uc").prefetch_related("alunos", "tecnologias")
    return render(request, "portfolio/projetos.html", {"projetos": projetos})
```
Decisão crítica:

uso de select_related para relações 1:N
uso de prefetch_related para relações N:M

Isto permitiu evitar múltiplas queries desnecessárias.

Estrutura dos Templates

Foi criado um template base (base.html) com:

cabeçalho
menu de navegação
rodapé

E templates específicos para cada entidade, reutilizando a estrutura:
```python
{% extends "portfolio/base.html" %}
```
Cada página apresenta:

lista de entidades
atributos principais
relações associadas
Navegação do Portefólio

Foi implementado um menu global que permite navegar entre todas as secções:

* Cursos
* UCs
* Professores
* Alunos
* Projetos
* TFCs
* Tecnologias
* Competências
* Formações
* Inscrições

Isto transformou o sistema num portefólio navegável e explorável.

Problemas Encontrados
1. Rotas não configuradas corretamente
Resultado: erro 404
Correção: inclusão da app no urls.py principal
2. Falta de dados na base de dados
Resultado: páginas vazias
Correção: criação de dados via Django Admin
3. Estrutura de ficheiros estáticos
CSS inicialmente colocado em templates
Correção: uso correto da pasta static/
4. Carregamento de imagens
Necessidade de configurar MEDIA_URL e MEDIA_ROOT
Resultado Final

O portefólio permite:

visualizar todas as entidades do sistema
navegar entre relações (ex: aluno → projetos → tecnologias)
validar o modelo de dados de forma prática

Deixou de ser apenas um modelo teórico, passando a ser um sistema funcional.



## 15. Implementação de CRUD no Portefólio

Após a construção das interfaces de consulta (listagem), foi implementado o conjunto de operações CRUD (Create, Read, Update, Delete) para as entidades:

* Projeto
* Tecnologia
* Competência
* Formação
* Abordagem utilizada

A implementação seguiu o padrão do Django:

utilização de ModelForms
criação de views específicas para cada operação
uso de métodos do ORM:
* get() → obter objeto
* save() → criar/editar
* delete() → apagar

Exemplo:
```python
projeto = Projeto.objects.get(id=id)
form = ProjetoForm(request.POST or None, instance=projeto)

if form.is_valid():
    form.save()
```

## 16. Dificuldades Encontradas
1. Imports em falta

Inicialmente surgiram erros (sublinhados amarelos) devido à ausência de imports como:
```python
from django.shortcuts import redirect
from .forms import ProjetoForm
```

## 16. Erros Identificados
* uso incorreto de .get() sem tratamento de erro
* falta de configuração de MEDIA_URL
* CSS inicialmente colocado na pasta errada (templates em vez de static)
* páginas sem dados devido à base de dados vazia

## 17. O que foi difícil de entender
* diferença entre select_related() e prefetch_related()
* funcionamento interno dos ModelForms
* ciclo completo de uma request (request → view → template → response)
* entender como funciona o CRUD


## 18. Considerações sobre o Django

O Django mostrou-se uma framework muito eficiente para:

* desenvolvimento rápido de aplicações web
* gestão de base de dados através de ORM
* criação de interfaces CRUD com pouco código

Permite passar rapidamente de:

modelo de dados → aplicação funcional

No entanto, exige compreensão da sua estrutura interna para evitar erros e más práticas.
