# Documentação do Projeto "Blog-Django"
## Introdução
O "Blog" é uma aplicação desenvolvida utilizando Python com o framework Django, HTML e CSS, foi utilizado também o docker com docker-compose, complexidade extra para fins educacionais. O projeto tem como objetivo fornecer uma plataforma de publicação de artigos, gerenciamento de páginas estáticas e categorização de conteúdo. Cada componente do projeto é organizado em apps individuais, focados em funcionalidades específicas.

## Estrutura do Projeto
### Apps do Projeto
**Blog:**

+ Responsável pela gestão e exibição de posts, categorias e tags. Possui funcionalidades relacionadas à criação, edição, exclusão e visualização de posts.

**Site_Setup:**

+ Lida com as configurações gerais do site, como títulos, descrições e opções de exibição. Gerencia também a configuração do menu de navegação.

### Funcionalidades Gerais
**Dashboard Principal (Index):**

+ A página principal exibe uma lista de posts, geralmente organizados por data de publicação. Exibe também categorias e tags populares, proporcionando uma visão geral do conteúdo do blog.

**Criar Post:**

+ A funcionalidade permite a criação de novos posts, utilizando o formulário adequado para coletar informações como título, conteúdo, categoria, tags e imagem de capa.

**Editar e Excluir Post:**

+ Permite aos autores do blog editar e excluir posts existentes. Os posts podem ser atualizados para refletir alterações no conteúdo ou na categoria.

**Exibição de Categorias e Tags:**

+ Os posts são categorizados por temas específicos (categorias) e marcados com palavras-chave (tags), facilitando a navegação e descoberta de conteúdo relacionado.

### Detalhes dos Módulos

### Blog:
**Posts:**

+ Gerencia a criação, edição e exclusão de posts. Utiliza o modelo Post para representar as informações essenciais de um artigo.

**Categorias e Tags:**

+ Gerencia as categorias e tags associadas aos posts. Cada categoria e tag possui um nome e um slug, utilizado para construir URLs amigáveis.

### Site_Setup:
**Menu:**

+ Lida com a gestão do menu de navegação do site. Cada link no menu é representado pelo modelo MenuLink, contendo informações como texto, URL ou caminho, e se deve ser aberto em uma nova aba.

## Considerações Finais
O sistema oferece uma interface intuitiva e flexível para a publicação de conteúdo em formato de blog, possibilitando aos autores criar, editar e excluir posts de maneira eficiente. A configuração do site, incluindo o menu de navegação, é facilmente gerenciada pelos módulos específicos.

Contribuições são bem-vindas! Sinta-se à vontade para abrir pull requests ou relatar problemas através de issues.

**Autor:** Flauziino - Desenvolvedor




