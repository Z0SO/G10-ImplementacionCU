
<script>
  import { get } from 'svelte/store';
  import { listaTurnos, listaMecanicos } from '../../../store.js';

  // Función para filtrar los turnos sin mecánico asignado
  function filtrarTurnosSinMecanico() {
    return get(listaTurnos).filter(turno => turno.mecanico === null);
  }

  // Obtener turnos filtrados
  const turnosFiltrados = filtrarTurnosSinMecanico();

  // Obtener mecánicos libres
  const mecanicosLibres = get(listaMecanicos).filter(m => m.estado === 'libre');
  
  // Verificar si todos los mecánicos están ocupados
  const todosOcupados = mecanicosLibres.length === 0;

  // Debugging
  console.log('Turnos Filtrados:', turnosFiltrados);
  console.log('Mecánicos Libres:', mecanicosLibres);
  console.log('Todos Ocupados:', todosOcupados);
</script>

<div class="max-w-md mx-auto p-4">
  <h1 class="text-2xl font-semibold mb-4">Turnos disponibles</h1>

  {#if todosOcupados}
    <p class="text-red-600 dark:text-red-400 font-medium">
      Todos los mecánicos están ocupados. No se pueden asignar turnos en este momento.
    </p>
  {:else}
    <p class="mb-4 text-gray-600 dark:text-gray-400">Selecciona un turno para asignar un mecánico</p>
    <ul class="space-y-2">
      {#each turnosFiltrados as turno}
        <li>
          <a href={`/turnos/asignar-mecanico/${turno.id}`} class="block p-4 bg-white dark:bg-gray-700 border border-gray-200 dark:border-gray-600 rounded-lg shadow hover:bg-gray-100 dark:hover:bg-gray-600 transition">
            {turno.fecha} - {turno.hora} - {turno.vehiculo}
          </a>
        </li>
      {/each}
    </ul>
  {/if}

  <h2 class="text-xl font-semibold mt-6 mb-4">Turnos con mecánico asignado</h2>

  <ul class="space-y-2">
    {#each $listaTurnos as turno}
      {#if turno.mecanico !== null}
        <li class="p-4 bg-white dark:bg-gray-700 border border-gray-200 dark:border-gray-600 rounded-lg shadow">
          {turno.fecha} - {turno.hora} - {turno.vehiculo} - {turno.mecanico}
        </li>
      {/if}
    {/each}
  </ul>
</div>
