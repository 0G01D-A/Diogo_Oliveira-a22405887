# Making Of — Modelação do Portefólio

## 1. Introdução

Criação do Diário de bordo 

---

## 2. Fotografias do DER e Apontamentos

![DER Final]()


---

## 3. Evolução do Modelo


### Versão Inicial

Numa primeira fase, foram identificadas as entidades principais do sistema, nomeadamente:

- Curso  
- UnidadeCurricular    

Os atributos definidos eram ainda básicos e focados na identificação (nome, descrição).  

---

### Versão Intermédia

Numa fase posterior, criei mais entidades como por exemplo:

- Projetos  
- Professor  
- Aluno  
- Inscrição
- Tecnologias
- Competência
- Formações

---

### Versão Final

Na versão final (representada no DER desenhado).

Principais melhorias:

- Estruturação completa das entidades:
  - Projeto
  - Tecnologia
  - TFC
  - Competência
  - Formação
  - Aluno
  - Professor
  - Unidade Curricular
  - Curso

- Definição explícita das cardinalidades (1:N e N:M)

- Criação de relações adequadas entre entidades, nomeadamente:
  - Projeto ↔ Tecnologia (N:M)
  - Projeto ↔ Aluno (N:M)
  - Projeto ↔ Unidade Curricular (N:1)
  - TFC ↔ Tecnologia (N:M)
  - Formação ↔ Competência (N:M)
  - Competência ↔ Projeto (N:M)
  - 
---

## 4. Erros Identificados e Correções


### Erro 1: Relações mal definidas
- Problema: ligações diretas incorretas
- Correção: uso de tabelas associativas

---

## 5. Justificação das Decisões de Modelação

### Projeto
- Separação de tecnologias 

### Tecnologia
- Criação de entidade própria 
- Inclusão de nível de conhecimento

### TFC
- Uso de nível de interesse 
- Ligação a professor 

### Competência
- Separação de tecnologia
- Ligação a projetos 

### Formação
- Uso de datas 
- Classificação por tipo 

---

## 6. Estrutura Final do Modelo

O modelo final inclui as seguintes entidades:

- Projeto
- Tecnologia
- TFC
- Competência
- Formação
- Unidade Curricular
- Professor
- Inscrição
- Aluno
- Professor
- Curso

Com relações N:M e 1:N devidamente estruturadas.

---

## 7. Conclusão

O processo de modelação evoluiu de uma estrutura simples para um modelo mais normalizado e consistente, permitindo representar de forma adequada o portefólio académico e profissional.
