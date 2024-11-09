$(document).ready(function() {
    $('#pokemon-form').on('submit', function(event) {
        event.preventDefault(); // Evita que el formulario se envíe de la manera tradicional

        $.ajax({
            type: 'GET',
            url: '/pokemon',
            data: $(this).serialize(), // Serializa los datos del formulario
            success: function(response) {
                $('#pokemon-result').html(response); // Actualiza el div con los resultados
            },
            error: function() {
                $('#pokemon-result').html('<p>Error al buscar el Pokémon. Intenta de nuevo.</p>');
            }
        });
    });
});