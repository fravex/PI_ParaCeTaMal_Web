console.log('Ok')


$( "#btn_abrir" ).click(function() {
    $( "nav" ).css( "transition", "1s" );
    $( "nav"  ).css( "height", "200" );
    $( "#btn_abrir"  ).css( "display", "none" );
    $( "#btn_fechar"  ).css( "display", "inline" );
    $( ".lista_menu" ).addClass("lista_menu_show")
}); 


$( "#btn_fechar" ).click(function() {
    $( "nav" ).css( "transition", ".5s" );
    $( "nav"  ).css( "height", "32" );
    $( "#btn_fechar"  ).css( "display", "none" );
    $( "#btn_abrir"  ).css( "display", "inline" );
    $( ".lista_menu_show" ).removeClass("lista_menu_show")



}); 