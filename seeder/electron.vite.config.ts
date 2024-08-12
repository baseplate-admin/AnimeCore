import { resolve } from "path";
import { defineConfig, externalizeDepsPlugin } from "electron-vite";
import solid from "vite-plugin-solid";
import svg from "vite-plugin-solid-svg";

export default defineConfig({
	main: {
		plugins: [externalizeDepsPlugin()],
		esbuild: {
			target: "esnext",
			legalComments: "external"
		},
		build: {
			commonjsOptions: {
				transformMixedEsModules: true
			},
			chunkSizeWarningLimit: undefined,
			minify: "terser"
		},
		resolve: {
			alias: {
				$constants: resolve(__dirname, "./src/main/constants"),
				$interfaces: resolve(__dirname, "./src/main/interfaces"),
				$backend: resolve(__dirname, "./src/main/backend"),
				$workers: resolve(__dirname, "./src/main/workers"),
				$utils: resolve(__dirname, "./src/main/utils")
			}
		}
	},
	preload: {
		plugins: [externalizeDepsPlugin()],
		esbuild: {
			target: "esnext",
			legalComments: "external"
		},
		build: {
			commonjsOptions: {
				transformMixedEsModules: true
			},
			chunkSizeWarningLimit: undefined,
			minify: "terser"
		},
		resolve: {
			alias: {
				$constants: resolve(__dirname, "./src/main/constants"),
				$interfaces: resolve(__dirname, "./src/main/interfaces"),
				$backend: resolve(__dirname, "./src/main/backend"),
				$workers: resolve(__dirname, "./src/main/workers"),
				$utils: resolve(__dirname, "./src/main/utils")
			}
		}
	},

	renderer: {
		esbuild: {
			legalComments: "external"
		},
		build: {
			commonjsOptions: {
				transformMixedEsModules: true
			},
			chunkSizeWarningLimit: 2048,
			target: "es2022",
			cssTarget: "esnext",
			minify: "terser"
		},
		resolve: {
			alias: {
				"@renderer": resolve(__dirname, "./src/renderer"),
				"@assets": resolve(__dirname, "./src/renderer/assets"),
				"@components": resolve(__dirname, "./src/renderer/components"),
				"@routes": resolve(__dirname, "./src/renderer/routes"),
				"@layouts": resolve(__dirname, "./src/renderer/layouts"),
				"@constants": resolve(__dirname, "./src/renderer/constants"),
				"@utils": resolve(__dirname, "./src/renderer/utils")
			}
		},
		plugins: [solid(), svg()]
	}
});
