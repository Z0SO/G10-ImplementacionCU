
<script>
    import { createTurno } from '../../api/turnos.api.js';
    import { onMount } from 'svelte';

    let turno = {
        nombre: '',
        fecha: '',
        hora: '',
        mecanico: ''
    };
    
    let successMessage = '';
    let errorMessage = '';

    const handleSubmit = async () => {
        try {
            const response = await createTurno(turno);
            if (response) {
                successMessage = 'Turno creado exitosamente';
                turno = { nombre: '', fecha: '', hora: '', mecanico: '' }; // Reiniciar el formulario
            } else {
                errorMessage = 'Hubo un problema al crear el turno';
            }
        } catch (error) {
            errorMessage = 'Error al crear el turno: ' + error.message;
        }
    };
</script>

<!-- el on su:submit | preventDefault = {handleSubmit} la directiva se utiliza para prevenir el comportamiento predeterminado del formulario, que es recargar la página. En su lugar, handleSubmit se ejecuta cuando se envía el formulario. -->
<form on:submit|preventDefault={handleSubmit} class="max-w-md mx-auto p-4">
    <div class="mb-4">
        <label for="nombre" class="block text-sm font-medium">Nombre:</label>
        <input id="nombre" bind:value={turno.nombre} class="mt-1 block w-full" required>
    </div>

    <div class="mb-4">
        <label for="fecha" class="block text-sm font-medium">Fecha:</label>
        <input id="fecha" type="date" bind:value={turno.fecha} class="mt-1 block w-full" required>
    </div>

    <div class="mb-4">
        <label for="hora" class="block text-sm font-medium">Hora:</label>
        <input id="hora" type="time" bind:value={turno.hora} class="mt-1 block w-full" required>
    </div>

    <div class="mb-4">
        <label for="mecanico" class="block text-sm font-medium">Mecánico:</label>
        <input id="mecanico" bind:value={turno.mecanico} class="mt-1 block w-full" required>
    </div>

    {#if successMessage}
        <p class="text-green-600">{successMessage}</p>
    {/if}

    {#if errorMessage}
        <p class="text-red-600">{errorMessage}</p>
    {/if}

    <button type="submit" class="px-4 py-2 bg-blue-600 text-white rounded">Crear Turno</button>
</form>
