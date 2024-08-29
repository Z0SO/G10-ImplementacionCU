

<script>
  import { page } from '$app/stores';
  import { listaTurnos, listaMecanicos } from '../../../../store.js';
  import { get } from 'svelte/store';
  import { goto } from '$app/navigation';

  let { id } = $page.params;
  let turno = null;
  let selectedMecanico = null;
  const turnoId = parseInt(id);
  const turnos = get(listaTurnos);
  turno = turnos.find(t => t.id === turnoId);

  if (!turno) {
    console.error('Turno no encontrado');
  }

  let mecanicosLibres = get(listaMecanicos).filter(m => m.estado === 'libre');

  function asignarMecanico() {
    listaTurnos.update(turnos => {
      const turnoIndex = turnos.findIndex(t => t.id === turnoId);
      if (turnoIndex !== -1) {
        turnos[turnoIndex].mecanico = selectedMecanico;
      }
      return turnos;
    });

    listaMecanicos.update(mecanicos => {
      const mecanicoIndex = mecanicos.findIndex(m => m.nombre === selectedMecanico);
      if (mecanicoIndex !== -1) {
        mecanicos[mecanicoIndex].estado = 'ocupado';
      }
      return mecanicos;
    });

    goto('/turnos/list');
  }
</script>

<div class="max-w-md mx-auto p-4 bg-white dark:bg-gray-800 shadow-lg rounded-lg">
  <h1 class="text-2xl font-semibold mb-4">
    {#if turno}
      Asignar Mecánico al Turno {turno.fecha} - {turno.hora}
    {:else}
      Turno no encontrado
    {/if}
  </h1>

  {#if turno}
    <div class="mb-4">
      <select bind:value={selectedMecanico} class="block w-full p-2 border border-gray-300 rounded-lg bg-white dark:bg-gray-700 dark:border-gray-600 text-gray-900 dark:text-gray-100">
        <option value="" disabled>Seleccione un mecánico</option>
        {#each mecanicosLibres as mecanico}
          <option value={mecanico.nombre}>{mecanico.nombre}</option>
        {/each}
      </select>
    </div>
    <button on:click={asignarMecanico} class="w-full px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 dark:bg-blue-500 dark:hover:bg-blue-600">
      Asignar Mecánico
    </button>
  {/if}
</div>
