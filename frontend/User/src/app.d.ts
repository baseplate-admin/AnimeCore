// See https://kit.svelte.dev/docs/types#app
// for information about these interfaces
// and what to do when importing types
declare namespace App {
	// interface Locals {}
	// interface PageData {}
	// interface Error {}
	// interface Platform {}
}

interface Window {
	django: {
		IMAGE_CHOICES: Array<{
			type: 'pixiv' | 'anime';
			name: string;
			image: string;
		}>;
		URLS: {
			SIGNUP: string;
		};
		DEBUG: string;
		CSRFTOKEN: string;
		USER_IS_AUTHENTICATED: boolean;
	};
}
