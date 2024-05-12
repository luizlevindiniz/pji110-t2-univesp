const createForm = document.querySelector(".churches-create-form__form");

createForm.addEventListener("submit", async (e) => {
  console.log(e);

  e.preventDefault();

  const churchName = e.target.churchName.value;
  const churchAddress = e.target.churchAddress.value;
  const churchFaith = e.target.churchFaith.value;

  if (!churchName || !churchAddress || !churchFaith) {
    return alert("Todos os campos são obrigatórios!");
  }

  const payload = {
    church: churchName,
    location: churchAddress,
    faith: churchFaith,
  };

  try {
    const response = await fetch("http://localhost:8000/api/churches/create", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(payload),
    });

    if (!response.ok) {
      throw new Error("Erro ao criar igreja");
    }

    alert("Igreja criada com sucesso!");

    e.target.churchName.value = "";
    e.target.churchAddress.value = "";
    e.target.churchFaith.value = "";
  } catch (error) {
    console.error(error);
    alert("Erro ao criar igreja");
  }
});
