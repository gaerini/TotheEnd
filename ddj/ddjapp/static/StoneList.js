const modal = document.querySelector(".modal");
const openBtn = document.querySelector(".open-button");
function openModal() {
    modal.classList.remove("hidden");
}
openBtn.addEventListener("click", openModal);
const closeBtn = modal.querySelector(".close");
function closeModal() {
    modal.classList.add("hidden");
}
closeBtn.addEventListener("click", closeModal);
