
<script>
    import { createTurno } from '../../api/turnos.api.js';

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

<form on:submit|preventDefault={handleSubmit} class="max-w-md mx-auto p-4 mt-16 bg-white dark:bg-gray-800 rounded-lg">
    <div class="mb-4">
        <label for="nombre" class="block text-sm font-medium text-gray-900 dark:text-white">Nombre</label>
        <input id="nombre" bind:value={turno.nombre} class="mt-1 block w-full px-3 py-2 bg-gray-50 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" required>
    </div>

    <div class="mb-4">
        <label for="fecha" class="block text-sm font-medium text-gray-900 dark:text-white">Fecha</label>
        <input id="fecha" type="date" bind:value={turno.fecha} class="mt-1 block w-full px-3 py-2 bg-gray-50 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" required>
    </div>

    <div class="mb-4">
        <label for="hora" class="block text-sm font-medium text-gray-900 dark:text-white">Hora</label>
        <input id="hora" type="time" bind:value={turno.hora} class="mt-1 block w-full px-3 py-2 bg-gray-50 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" required>
    </div>

    <div class="mb-4">
        <label for="mecanico" class="block text-sm font-medium text-gray-900 dark:text-white">Mecánico</label>
        <input id="mecanico" bind:value={turno.mecanico} class="mt-1 block w-full px-3 py-2 bg-gray-50 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" required>
    </div>

    {#if successMessage}
        <p class="text-green-600 dark:text-green-400">{successMessage}</p>
    {/if}

    {#if errorMessage}
        <p class="text-red-600 dark:text-red-400">{errorMessage}</p>
    {/if}

    <button type="submit" class="w-full px-4 py-2 bg-blue-600 text-white rounded-lg shadow-md hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-opacity-50">Crear Turno</button>
</form>
