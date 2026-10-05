let paginaProdutos = 1;
let paginaUsuarios = 1;

// PRODUTOS

async function pesquisarProdutos() {
    const nome = document.getElementById("termo-produtos").value;

    if (!nome) return;

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

    if (!nome) return;

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