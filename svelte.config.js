import adapter from '@sveltejs/adapter-static';
import preprocess from 'svelte-preprocess';
export default config;


/** @type {import('@sveltejs/kit').Config} */
const config = {
  // Consult the docs to learn more about preprocessors
  // https://kit.svelte.dev/docs/integrations#preprocessors
  preprocess: preprocess(),

  kit: {
    adapter: adapter({
      // default options are shown
      pages: 'build',
      assets: 'build',
      fallback: null,
      precompress: false,
      strict: true
    }),
  }
};


