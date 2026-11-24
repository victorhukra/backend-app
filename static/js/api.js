async function requisicao(url) {
    const resposta = await fetch("/api" + url);

    if (!resposta.ok) {
        throw new Error("Erro na requisição");
    }

    return resposta.json();
}

function buscarProdutos(nome, pagina) {
    const parametros = new URLSearchParams({ nome, pagina });
    return requisicao(`/produtos?${parametros}`);
}

function buscarProdutoPorId(id) {
    return requisicao(`/produtos/${id}`);
}

function buscarUsuarios(nome, pagina) {
    const parametros = new URLSearchParams({ nome, pagina });
    return requisicao(`/usuarios?${parametros}`);
}

function buscarPerfil(id) {
    return requisicao(`/usuarios/${id}`);
}
