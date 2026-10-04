async function requisicao(url) {
    const resposta = await fetch("/api" + url);
    }
    if (!resposta.ok) {
        throw new Error("Erro na requisição");
    }