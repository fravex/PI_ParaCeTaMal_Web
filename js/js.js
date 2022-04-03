console.log('ola')


$( "#abrir" ).click(function() {
    $( "nav" ).css( "transition", "1s" );
    $( "nav"  ).css( "height", "200" );
    $( "#abrir"  ).css( "display", "none" );
    $( "#fechar"  ).css( "display", "inline" );
    $( ".lista_menu" ).addClass("lista_menu_show")
}); 


$( "#fechar" ).click(function() {
    $( "nav" ).css( "transition", ".5s" );
    $( "nav"  ).css( "height", "32" );
    $( "#fechar"  ).css( "display", "none" );
    $( "#abrir"  ).css( "display", "inline" );
    $( ".lista_menu_show" ).removeClass("lista_menu_show")



}); 