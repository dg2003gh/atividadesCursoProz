const nomeProduto = document.getElementById("nome-produto");
const valorProduto = document.getElementById("valor-produto");
const descricaoProduto = document.getElementById("descricao-produto");
const btnEnviar = document.getElementById("btn-enviar");
const feedbackUsuario = document.getElementById("feedback-usuario");
const produtosCadastrados = document.getElementById("produtos-cadastrados");

btnEnviar.addEventListener("click", async (event) => {
	event.preventDefault();

	const produto = {
		nome: nomeProduto.value,
		valor: valorProduto.value,
		descricao: descricaoProduto.value,
	};

	const postData = await fetch("https://httpbin.org/post", {
		method: "POST",
		body: JSON.stringify(produto),
		Headers: {
			Accept: "application.json",
			"Content-Type": "application/json",
		},
	});

	postDataResponse = await postData.json();

	if (postData.ok) {
		feedbackUsuario.innerText = `O produto ${produto.nome} foi adicionado com sucesso!`;
		nomeProduto.value = "";
		valorProduto.value = "";
		descricaoProduto.value = "";
		produtosCadastrado += produto.nome;
	} else {
		feedbackUsuario.innerText = `O produto ${produto.nome} não pode ser adicionado! Tente novamente mais tarde.`;
	}

	setTimeout(() => {
		feedbackUsuario.innerText = "";
	}, 5000);
});
