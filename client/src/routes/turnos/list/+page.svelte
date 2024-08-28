

<script>
  // /turnos/list

  // Importamos la fucnion get de svelte/store para obtener los valores de los arrays turnosFiltrados y mecanicosFiltrados
  import { get } from 'svelte/store';

  import { listaTurnos, listaMecanicos } from '../../../store.js';



  // Función para filtrar los turnos sin mecánico asignado
  function filtrarTurnosSinMecanico() {
    return get(listaTurnos).filter(turno => turno.mecanico === null);
  }

  // Llamada a la función para obtener los turnos sin mecánico asignado
  const turnosFiltrados = filtrarTurnosSinMecanico();

</script>

<!-- la asignacion de turnos a mecanicos se hara en otra pagina (en /turnos/asignar-mecanico/{id}), por lo que se debe mostrar solo los turnos sin asignar mecanico -->

<h1>Turnos disponibles</h1>
<p>Selecciona un turno para asignar un mecánico</p>
 
<ul>
  {#each turnosFiltrados as turno}
    <li>
      <a href={`/turnos/asignar-mecanico/${turno.id}`}>
        {turno.fecha} - {turno.hora} - {turno.vehiculo}
      </a>
    </li>
  {/each}
</ul>

<h2>Lista de turnos con mecánico asignado</h2>

<ul>
  <!-- el $ indica que es una variable de svelte de store.js -->
  {#each $listaTurnos as turno}
    {#if turno.mecanico !== null}
      <li>
        {turno.fecha} - {turno.hora} - {turno.vehiculo} - {turno.mecanico}
      </li>
    {/if}
  {/each}
</ul>
