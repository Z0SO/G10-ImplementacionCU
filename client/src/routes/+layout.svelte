
<script>
  
  import Navbar from '../components/layout/Navbar.svelte';

</script>

<div 
  class="sombra-div-nav"
>
  <Navbar />
</div>

<main
>
  <slot></slot>
</main>

<style>
  .sombra-div-nav {
    box-shadow: 0 4px 20px;
  }

</style>

