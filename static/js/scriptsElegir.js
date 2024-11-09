$(document).ready(function() {
    $('#pokemon-select-form').on('submit', function(event) {
        event.preventDefault(); // Evita que el formulario se envíe de la manera tradicional

        $.ajax({
            type: 'GET',
            url: '/pokemonsElegir',
            data: $(this).serialize(), // Serializa los datos del formulario
            success: function(response) {
                $('#pokemon-result-elegir').html(response); // Actualiza el div con los resultados
            },
            error: function() {
                $('#pokemon-result-elegir').html('<p>Error al buscar el Pokémon. Intenta de nuevo.</p>');
            }
        });
    });
});