
<script>
  import { page } from '$app/stores';
  import { listaTurnos, listaMecanicos } from '../../../../store.js';
  import { get } from 'svelte/store';
  import { goto } from '$app/navigation';

  // Obtén el id de la URL desde el objeto page
  let { id } = $page.params;

  let turno = null;
  let selectedMecanico = null;

  // Asegúrate de que id sea un número entero
  const turnoId = parseInt(id);

  // Obtén la lista de turnos
  const turnos = get(listaTurnos);
  // Busca el turno por id
  turno = turnos.find(t => t.id === turnoId);

  if (!turno) {
    // Redirige a una página de error o muestra un mensaje
  
    console.error('Turno no encontrado');

  }

  // Obtén los mecánicos libres
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

<h1>
  {#if turno}
    Asignar Mecánico al Turno {turno.fecha} - {turno.hora}
  {:else}
    Turno no encontrado
  {/if}
</h1>

{#if turno}
  <select bind:value={selectedMecanico}>
    <option value="" disabled>Seleccione un mecánico</option>
    {#each mecanicosLibres as mecanico}
      <option value={mecanico.nombre}>{mecanico.nombre}</option>
    {/each}
  </select>
  <button on:click={asignarMecanico}>Asignar Mecánico</button>
{/if}
