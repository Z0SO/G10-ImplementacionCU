import { sveltekit } from '@sveltejs/kit/vite';
import { defineConfig } from 'vite';

export default defineConfig({
	plugins: [sveltekit()],
	server: {
		host: '0.0.0.0', // Permitir conexiones desde cualquier IP
		port: 5173, // Puedes cambiar el puerto si es necesario
  },
});
