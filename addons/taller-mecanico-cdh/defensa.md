# Modificaciones respecto al enunciado

- **Vista Reparaciones/Nuevo:** Se ha añadido el botón "Iniciar reparación" para poder cambiar el estado a "En proceso"
- **Modelo taller_reparacion:** El metodo con la anotacion @api.onchange() ha sido modificado puesto que dicha anotacion no percibia los cambios realizados 
en la propiedad "Estado" a partir de los botones de la vista