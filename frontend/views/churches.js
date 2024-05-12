function createChurchCard({ church, location, faith }) {
  return `
    <li class="churches-content__list-item church-card">
        <div class="church-card__text">
            <div class="churches-content__list-item-header">
                <p>${church}</p>
            </div>
            <div class="churches-content__list-item-body">
                <p><span class="p-bold">Localização:</span> ${location}</p>
                <p><span class="p-bold">Fé:</span> ${faith} </p>
            </div>
            <div class="churches-content__list-item-footer">
                <button class="churches-content__details-btn">
                     Detalhes
                </button>
            </div>
        </div>
        <div class="church-card__img">
            <img id="church-card__thumb" src="https://images.unsplash.com/photo-1477672680933-0287a151330e?q=80&w=1740&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D" alt="Igreja">
        </div>
     </li>
  `;
}

const churchList = document.querySelector(".churches-content__list-items");

function renderChurches(churches) {
  churchList.innerHTML = churches.map(createChurchCard).join("");
}

async function getChurches() {
  const res = await fetch("http://localhost:8000/api/churches/all", {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
    },
  });

  if (!res.ok) {
    throw new Error("Failed to fetch churches");
  }

  const churches = await res.json();
  renderChurches(churches.results);
}

getChurches();
