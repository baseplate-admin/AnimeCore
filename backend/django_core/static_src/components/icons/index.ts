import type { ComponentType } from "svelte";

// @ts-ignore
import svelteRetag from "svelte-retag";

import AnimeCore from "./AnimeCore/index.svelte";
import ArrowUpRight from "./ArrowUpRight/Index.svelte";
import Bold from "./Bold/Index.svelte";
import Book from "./Book/Index.svelte";
import Calender from "./Calender/Index.svelte";
import Circle from "./Circle/Index.svelte";
import Code from "./Code/Index.svelte";
import Dot from "./Dot/Index.svelte";
import Hyperlink from "./Hyperlink/Index.svelte";
import Info from "./Info/Index.svelte";
import Italic from "./Italic/Index.svelte";
import Play from "./Play/Index.svelte";
import Star from "./Star/Index.svelte";
import Strike from "./Strike/Index.svelte";
import Underline from "./Underline/Index.svelte";

const icon_map: Record<string, ComponentType> = {
    "arrow-up-right": ArrowUpRight,
    animecore: AnimeCore,
    bold: Bold,
    book: Book,
    calender: Calender,
    circle: Circle,
    code: Code,
    dot: Dot,
    hyperlink: Hyperlink,
    info: Info,
    italic: Italic,
    play: Play,
    star: Star,
    strike: Strike,
    underline: Underline
};

// Register Icons
Object.entries(icon_map).forEach((item) => {
    svelteRetag({
        component: item[1],
        tagname: `coreproject-icon-${item[0]}`,
        attributes: ["class", "style"],
        shadow: false,
        hydratable: false
    });
});
