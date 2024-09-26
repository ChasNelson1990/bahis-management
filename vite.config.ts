import {defineConfig} from 'vite'
import react from '@vitejs/plugin-react-swc'

// https://vitejs.dev/config/
export default defineConfig({
    build: {
        manifest: true,
        outDir: './frontend/static/frontend',
    },
    base: '/static/frontend',
    plugins: [react()],
    server: {
        proxy: {
            '/api': {
                target: 'http://kf.sharful.com/', // Backend server URL
                changeOrigin: true,
                secure: false,
            },
        },
    }
})
