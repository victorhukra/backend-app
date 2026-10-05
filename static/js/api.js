async function requisicao(url) {
    const resposta = await fetch("/api" + url);

    if (!resposta.ok) {
        throw new Error("Erro na requisição");
    }

    return resposta.json();
}

function buscarProdutos(nome, pagina) {
    return requisicao(`/produtos/busca/${nome}/${pagina}`);
}

function buscarProdutoPorId(id) {
    return requisicao(`/produtos/${id}`);
}

function buscarUsuarios(nome, pagina) {
    return requisicao(`/usuarios/busca/${nome}/${pagina}`);
}

function buscarPerfil(id) {
    return requisicao(`/usuarios/${id}`);
}