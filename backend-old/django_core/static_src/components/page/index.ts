import { register } from "$functions/register";

// Pages
const mapping = [
    { tagname: `explore`, component: await import("./explore/Index.svelte") },
    { tagname: `anime-info`, component: await import("./anime/info/Index.svelte") },
    { tagname: `anime-episode`, component: await import("./anime/episode/Index.svelte") },
    { tagname: `upload`, component: await import("./upload/Index.svelte") },
    { tagname: `home`, component: await import("./home/Index.svelte") },
    { tagname: `anime`, component: await import("./anime/Index.svelte") }
];

mapping.forEach((item) => {
    register({
        component: item.component.default,
        tagname: `coreproject-page-${item.tagname}`
    });
});
