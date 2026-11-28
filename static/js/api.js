async function requisicao(url, opcoes = {}) {
    const resposta = await fetch("/api" + url, {
        credentials: "same-origin",
        ...opcoes,
    });
    const dados = await resposta.json().catch(() => ({}));

    if (!resposta.ok) {
        throw new Error(dados.erro || "Erro na requisição.");
    }

    return dados;
}

function enviarJson(url, metodo, dados) {
    return requisicao(url, {
        method: metodo,
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(dados),
    });
}

function cadastrarUsuario(dados) {
    return enviarJson("/usuarios", "POST", dados);
}

function iniciarSessao(dados) {
    return enviarJson("/sessoes", "POST", dados);
}

function verificarSessao() {
    return requisicao("/sessoes");
}

function encerrarSessao() {
    return requisicao("/sessoes", { method: "DELETE" });
}

function criarProduto(dados) {
    return enviarJson("/produtos", "POST", dados);
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
