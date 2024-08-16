import { ElectronAPI } from "@electron-toolkit/preload";
// import { COMMANDS as SHIINOBI_COMMANDS } from "$interfaces/shiinobi";

// NOTE: only relative imports work on declaration files
// see: https://github.com/microsoft/TypeScript/issues/30952
import { EXPRESS_URLS } from "../main/interfaces/express_urls";

declare global {
	interface Window {
		electron: ElectronAPI;
		api: {
			get_app_version: () => Promise<string>;
			get_express_urls: () => Promise<typeof EXPRESS_URLS>;
			// Shiinobi
			// [key in typeof SHIINOBI_COMMANDS[number]]: (...args: any[]) => Promise<object>;
		};
	}
}
