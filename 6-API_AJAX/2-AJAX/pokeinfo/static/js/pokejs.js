// Iniciar código Jquery para buscar pokemons
$(document).ready(function() {

    $("#form1").submit(function(e) {

        // Previene el funcionamiento por omisión del formulario
        e.preventDefault(); 
    
        var form = $(this);
        var actionUrl = form.attr('action');
        
        $.ajax({
            type: "GET",
            url: actionUrl,
            data: {
                pokemon: $("#nombre").val().toLowerCase()
            },
            dataType: "json",
            success: function(data)
            {
                alert('Pokemon ' + data.name + ' encontrado');
                $("#nombre_pokemon").html(data.name);
                $("#imagen_pokemon").html("<img src='" + data.sprites.front_default + "' width='200px'>");
                $("#tipo_pokemon").html(data.types[0].type.name);
                $("#peso_pokemon").html(data.weight);
                $("#altura_pokemon").html(data.height);
                $("#poketable").show();
            },
            error: function(data)
            {
                alert('Pokemon no encontrado');
            }
        });
        
    });
    
});
