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

function ferchaAlerta(){
    alertaInteracao.style.display = 'none'
}

const barraMenu = document.querySelector('nav');
const btnAbrirMenu = document.querySelector('#btn_abrir')
const btnFecharMenu = document.querySelector('#btn_fechar')
const infoMenu = document.querySelector('.lista_menu')
const btnConsultaInteracoes = document.querySelector('.botao_consultar_interacoes')
const btnFecharAlerta = document.querySelector('#btn_fechar_alerta')
const alertaInteracao = document.querySelector('.resultado_interacao_fundo')

btnAbrirMenu.addEventListener("click", espandeMenu);
btnFecharMenu.addEventListener("click", fechaMenu);
btnFecharAlerta.addEventListener("click", ferchaAlerta);

