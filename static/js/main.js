let paginaProdutos = 1;
let paginaUsuarios = 1;

// CONTA

async function atualizarSessao() {
    const status = document.getElementById("status-sessao");
    const botaoSair = document.getElementById("sair-conta");
    const formularioProduto = document.getElementById("form-cadastro-produto");
    const avisoLoginProduto = document.getElementById("aviso-login-produto");

    try {
        const sessao = await verificarSessao();
        botaoSair.hidden = !sessao.autenticado;
        formularioProduto.hidden = !sessao.autenticado;
        avisoLoginProduto.hidden = sessao.autenticado;

        status.textContent = sessao.autenticado
            ? `Sessão iniciada como ${sessao.usuario.nome}.`
            : "Você não está conectado.";
    } catch (erro) {
        botaoSair.hidden = true;
        formularioProduto.hidden = true;
        avisoLoginProduto.hidden = false;
        status.textContent = erro.message;
    }
}

document.getElementById("form-cadastro").addEventListener("submit", async evento => {
    evento.preventDefault();

    const formulario = evento.currentTarget;
    const status = document.getElementById("status-cadastro");
    const dados = {
        nome: document.getElementById("nome-cadastro").value,
        email: document.getElementById("email-cadastro").value,
        senha: document.getElementById("senha-cadastro").value,
    };

    status.textContent = "";
    status.dataset.estado = "";

    try {
        await cadastrarUsuario(dados);
        formulario.reset();
        document.getElementById("email-login").value = dados.email;
        status.textContent = "Conta criada. Entre com seu e-mail e senha.";
        status.dataset.estado = "sucesso";
    } catch (erro) {
        status.textContent = erro.message;
        status.dataset.estado = "erro";
    }
});

document.getElementById("form-login").addEventListener("submit", async evento => {
    evento.preventDefault();

    const formulario = evento.currentTarget;
    const status = document.getElementById("status-login");
    const dados = {
        email: document.getElementById("email-login").value,
        senha: document.getElementById("senha-login").value,
    };

    status.textContent = "";
    status.dataset.estado = "";

    try {
        await iniciarSessao(dados);
        formulario.reset();
        status.textContent = "Login realizado com sucesso.";
        status.dataset.estado = "sucesso";
        await atualizarSessao();
    } catch (erro) {
        status.textContent = erro.message;
        status.dataset.estado = "erro";
    }
});

document.getElementById("sair-conta").addEventListener("click", async () => {
    const status = document.getElementById("status-login");

    try {
        await encerrarSessao();
        status.textContent = "Sessão encerrada.";
        status.dataset.estado = "sucesso";
        await atualizarSessao();
    } catch (erro) {
        status.textContent = erro.message;
        status.dataset.estado = "erro";
    }
});

atualizarSessao();

// PRODUTOS

document.getElementById("form-cadastro-produto").addEventListener("submit", async evento => {
    evento.preventDefault();

    const formulario = evento.currentTarget;
    const status = document.getElementById("status-cadastro-produto");
    const dados = {
        nome: document.getElementById("nome-produto-cadastro").value,
        descricao: document.getElementById("descricao-produto-cadastro").value,
        preco: Number(document.getElementById("preco-produto-cadastro").value),
    };

    status.textContent = "";
    status.dataset.estado = "";

    try {
        const produto = await criarProduto(dados);
        formulario.reset();
        status.textContent = `Produto cadastrado com sucesso (ID: ${produto.id}).`;
        status.dataset.estado = "sucesso";
    } catch (erro) {
        status.textContent = erro.message;
        status.dataset.estado = "erro";
    }
});

async function pesquisarProdutos() {
    const nome = document.getElementById("termo-produtos").value;

    try {
        const produtos = await buscarProdutos(nome, paginaProdutos);
        const lista = document.getElementById("resultados-produtos");

        lista.innerHTML = "";

        produtos.forEach(produto => {
            const item = document.createElement("li");

            item.innerHTML = `
                <strong>ID: ${produto.id}</strong><br>
                <strong>${produto.nome}</strong><br>
                ${produto.descricao}<br>
                R$ ${produto.preco}
            `;

            lista.appendChild(item);
        });

        document.getElementById("paginacao-produtos").hidden = false;

        document.getElementById("pagina-produtos").textContent =
            `Página ${paginaProdutos}`;

        document.getElementById("anterior-produtos").disabled =
            paginaProdutos === 1;

        document.getElementById("proxima-produtos").disabled =
            produtos.length < 5;

    } catch (erro) {
        document.getElementById("status-produtos").textContent =
            "Erro ao buscar produtos.";
    }
}

document.getElementById("buscar-produtos").addEventListener("click", () => {
    paginaProdutos = 1;
    pesquisarProdutos();
});

document.getElementById("anterior-produtos").addEventListener("click", () => {
    if (paginaProdutos > 1) {
        paginaProdutos--;
        pesquisarProdutos();
    }
});

document.getElementById("proxima-produtos").addEventListener("click", () => {
    paginaProdutos++;
    pesquisarProdutos();
});

// Buscar produto por ID

async function pesquisarProdutoPorId() {
    const id = document.getElementById("id-produto").value;

    if (!id) return;

    try {
        const produto = await buscarProdutoPorId(id);

        document.getElementById("resultado-produto-id").innerHTML = `
            <strong>ID: ${produto.id}</strong><br>
            <strong>${produto.nome}</strong><br>
            ${produto.descricao}<br>
            R$ ${produto.preco}
        `;

    } catch (erro) {
        document.getElementById("resultado-produto-id").textContent =
            "Produto não encontrado.";
    }
}

document.getElementById("buscar-produto-id").addEventListener("click", () => {
    pesquisarProdutoPorId();
});

// USUÁRIOS

async function pesquisarUsuarios() {
    const nome = document.getElementById("termo-usuarios").value;

    try {
        const usuarios = await buscarUsuarios(nome, paginaUsuarios);
        const lista = document.getElementById("resultados-usuarios");

        lista.innerHTML = "";

        usuarios.forEach(usuario => {
            const item = document.createElement("li");

            item.innerHTML = `
                <strong>${usuario.nome}</strong><br>
                ${usuario.email}
            `;

            const botao = document.createElement("button");
            botao.textContent = "Ver perfil";

            botao.addEventListener("click", () => {
                mostrarPerfil(usuario.id);
            });

            item.appendChild(botao);
            lista.appendChild(item);
        });

        document.getElementById("paginacao-usuarios").hidden = false;

        document.getElementById("pagina-usuarios").textContent =
            `Página ${paginaUsuarios}`;

        document.getElementById("anterior-usuarios").disabled =
            paginaUsuarios === 1;

        document.getElementById("proxima-usuarios").disabled =
            usuarios.length < 5;

    } catch (erro) {
        document.getElementById("status-usuarios").textContent =
            "Erro ao buscar usuários.";
    }
}

document.getElementById("buscar-usuarios").addEventListener("click", () => {
    paginaUsuarios = 1;
    pesquisarUsuarios();
});

document.getElementById("anterior-usuarios").addEventListener("click", () => {
    if (paginaUsuarios > 1) {
        paginaUsuarios--;
        pesquisarUsuarios();
    }
});

document.getElementById("proxima-usuarios").addEventListener("click", () => {
    paginaUsuarios++;
    pesquisarUsuarios();
});

// Buscar usuário por ID

async function pesquisarUsuarioPorId() {
    const id = document.getElementById("id-usuario").value;

    if (!id) return;

    mostrarPerfil(id);
}

// Mostrar perfil

async function mostrarPerfil(id) {
    try {
        const usuario = await buscarPerfil(id);
        const resultado = document.getElementById("resultado-usuario-id");

        resultado.innerHTML = `
            <strong>${usuario.nome}</strong><br>
            ${usuario.email}<br><br>
            <strong>Produtos:</strong>
        `;

        usuario.produtos.forEach(produto => {
            resultado.innerHTML += `
                <br>ID: ${produto.id} - ${produto.nome} - R$ ${produto.preco}
            `;
        });

    } catch (erro) {
        document.getElementById("resultado-usuario-id").textContent =
            "Usuário não encontrado.";
    }
}

document.getElementById("buscar-usuario-id").addEventListener("click", () => {
    pesquisarUsuarioPorId();
});
