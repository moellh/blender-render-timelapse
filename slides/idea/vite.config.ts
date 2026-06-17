import { defineConfig } from 'vite'

export default defineConfig({
  server: {
    allowedHosts: ['waldo-sites.internal.moellh.com'],
    hmr: {
      overlay: false
    }
  }
})
