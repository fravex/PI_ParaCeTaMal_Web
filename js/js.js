function espandeMenu(){
    barraMenu.classList.add('nav_espandido')
    btnAbrirMenu.style.display = "none"
    btnFecharMenu.style.display = "inline"
    setTimeout(function(){
        infoMenu.classList.add('lista_menu_show')
    }, 600); 
}


function fechaMenu(){
    barraMenu.classList.remove('nav_espandido')
    btnFecharMenu.style.display = "none"
    btnAbrirMenu.style.display = "inline"
    infoMenu.classList.remove('lista_menu_show')

}


const barraMenu = document.querySelector('nav');
const btnAbrirMenu = document.querySelector('#btn_abrir')
const btnFecharMenu = document.querySelector('#btn_fechar')
const infoMenu = document.querySelector('.lista_menu')

btnAbrirMenu.addEventListener("click", espandeMenu);
btnFecharMenu.addEventListener("click", fechaMenu);


function abrirMenu(){

}