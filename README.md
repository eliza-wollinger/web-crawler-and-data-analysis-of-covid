![Covid Banner](https://user-images.githubusercontent.com/57842220/149853924-1f839493-7871-4da9-a273-b59d18fac8bb.png)

<div align="center" id="badges"> 
  <img id="python" src="https://img.shields.io/badge/Python-v3.9.0-lightgrey" alt="python badge"/>
  <img id="beautiful-soup" src="https://img.shields.io/badge/Beautiful%20Soup-v4.9.0-lightgrey" alt="beautiful soup badge"/>
  <img id="pandas" src="https://img.shields.io/badge/Pandas-v1.3.5-lightgrey" alt="pandas badge"/>
  <img id="numpy" src="https://img.shields.io/badge/Numpy-v1.22.1-lightgrey" alt="numpy badge"/>
  <img id="matplotlib" src="https://img.shields.io/badge/Matplotlib-v3.5.1-lightgrey" alt="matplotlib badge"/>
</div>


### English version 🇬🇧 🇺🇸

In this program I used the beautiful soup library to perform the web scraping of the worldometers.info site, in order to obtain updated data on covid. After the web scraping I received all the html from the site, and with the help of the browser's inspect tool, looked for the part of the code I wanted to work with, and converted it to an Excel spreadsheet.

With the spreadsheet in hand, I used the pandas library to process the collected data, modifying null data and excluding columns that would not be necessary. After, with the help of the numpy and matplotlib library, I gave a visual to my data, making it simpler for understanding.


### Portuguese translation 🇧🇷 🇵🇹

Neste programa utilizei a biblioteca beautiful soup para realizar o web scraping do site worldometers.info, com o intuito de obter dados atualizados sobre a covid. Após o web scraping recebi todo o html do site, e com o auxilio da ferramenta de inspecionar do navegador, procurei em que parte do código estava os dados com os quais queria trabalhar, e os converti para uma planilha Excel.

Com a planilha em mãos, utilizei a biblioteca pandas para realizar o tratamento dos dados coletados, modificando dados nulos e excluindo as colunas que não seriam necessárias. Após com o auxilio da biblioteca numpy e matplotlib, dei um visual para meus dados, deixando assim mas simples para a compreensão.

### How to run the code? 🏃‍♀️

After clone the repository, you can use these commands in the terminal to run the code (Portuguese translation - após clonar o repositório, você pode usar estes comandos no terminal para executar o código):

On Windows:
```sh
py -3 main.py
```

On other systems:
```sh
python3 main.py
```
