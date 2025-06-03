            /* Création des variables et constantes */
const projetsCompetences = document.querySelectorAll(".projetCompetence");
const competences = document.querySelectorAll(".competence");
const menu = document.querySelectorAll("nav");


for (let i = 0; i < 13; i++){ // testes
    console.log(competences[i]);
    console.log(projetsCompetences[i]);
    console.log(i);
}
for (let i = 0; i < 2; i++){ // testes
    console.log(menu[i]);
    console.log(i);
}

            /* Fonction qui gère la modification du CSS */
const gestionMenu = (competenceSurvoler, listeProjets, menuAmodifier) => {
    //modifacation des éléments mis en avant et afficher
    for (let i = 0; i < 13; i++){
        projetsCompetences[i].classList.remove("listeDesProjets");
        competences[i].style.fontWeight = "normal";
    }
    
    menuAmodifier.classList.add("menu");
    listeProjets.classList.add("listeDesProjets");
    
    //mise en avant de l'élément survoler
    competenceSurvoler.style.fontWeight = "bold";
	
}


            /* Modification des éléments souhaiter en fonction de l'élément survolé */
competences[0].addEventListener("mouseenter", () => {gestionMenu(competences[0], projetsCompetences[0], menu[0])});
competences[1].addEventListener("mouseenter", () => {gestionMenu(competences[1], projetsCompetences[1], menu[0])});
competences[2].addEventListener("mouseenter", () => {gestionMenu(competences[2], projetsCompetences[2], menu[0])});
competences[3].addEventListener("mouseenter", () => {gestionMenu(competences[3], projetsCompetences[3], menu[0])});
competences[4].addEventListener("mouseenter", () => {gestionMenu(competences[4], projetsCompetences[4], menu[0])});
competences[5].addEventListener("mouseenter", () => {gestionMenu(competences[5], projetsCompetences[5], menu[0])});
competences[6].addEventListener("mouseenter", () => {gestionMenu(competences[6], projetsCompetences[6], menu[0])});

competences[7].addEventListener("mouseenter", () => {gestionMenu(competences[7], projetsCompetences[7], menu[1])});
competences[8].addEventListener("mouseenter", () => {gestionMenu(competences[8], projetsCompetences[8], menu[1])});
competences[9].addEventListener("mouseenter", () => {gestionMenu(competences[9], projetsCompetences[9], menu[1])});
competences[10].addEventListener("mouseenter", () => {gestionMenu(competences[10], projetsCompetences[10], menu[1])});
competences[11].addEventListener("mouseenter", () => {gestionMenu(competences[11], projetsCompetences[11], menu[1])});
competences[12].addEventListener("mouseenter", () => {gestionMenu(competences[12], projetsCompetences[12], menu[1])});

        /* Cacher le menu quand il n'est plus survoler */
menu[0].addEventListener("mouseleave", () => {
    // retirer la mise en avant des éléments
    for (let i = 0; i < 7; i++){
        projetsCompetences[i].classList.remove("listeDesProjets");
        competences[i].style.fontWeight = "normal";
    }
    
    // retirer le menu
    menu[0].classList.remove("menu");
});

menu[1].addEventListener("mouseleave", () => {
    // retirer la mise en avant des éléments
    for (let i = 7; i < 13; i++){
        projetsCompetences[i].classList.remove("listeDesProjets");
        competences[i].style.fontWeight = "normal";
    }
    
    // retirer le menu
    menu[1].classList.remove("menu");
});