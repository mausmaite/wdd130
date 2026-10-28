# Estrutura básica de HTML:

<!DOCTYPE html> #informa ao navegador o tipo de documento e html que estará sendo usado
<html> #conteiner das outras tags

    <head> #contém informações sobre a página, e nao sobre o conteudo dela
    # o head serve para dar informações da página, mas o que tem dentro dele não aparece na página.
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width">
        <title>Título da Página</title> #Esse título não aparece diretamente na página em si, 
                                        # mas deve corresponder exatamente ao conteúdo incluído no elemento título 1,
                                        # <h1>, no elemento <body> do documento.
    </head>

    <body> # contem tudo o que aparece na pagina
        <h1> #título principal
        <h2> #subtítulo
        
        <header> #é o que aparece no topo da página, tipo o cabeçalho, se repete de uma página para outra. 
                # Logotipo, menu do site        
            <nav> #menu de navegação
                <a href="index.html">Página Inicial</a> #fica o hiperlink, que leva para outra página do site
                <a href="sobremim.html">Sobre mim</a> #também podemos chamar de atributos
                # tag <a> indica um link
            </nav>
        </header>

        <main> #conteúdo que é único para cada página
            <img src=(caminho e nome do arquivo da imagem)"voyager.jpg" alt= (texto alternativo, que exibe se a imagem não carregar)"estação espacial">

        </main>

        <footer> # Elementos que ficam no final da página: inf de contato, direitos autorais e links adicionais. é igual em todas as páginas
        </footer>

    </body>

</html>