const cssnano = require("cssnano");
const postcss_preset_env = require("postcss-preset-env");
const purgecss = require("@fullhuman/postcss-purgecss");

const dev = process.env.NODE_ENV === "development";

const config = {
    plugins: [
        postcss_preset_env({
            stage: 0,
            autoprefixer: {
                grid: true
            }
        }),
        cssnano({
            autoprefixer: false,
            preset: ["default"]
        }),
        // Run on buld
        !dev &&
        purgecss({
            content: ["./src/**/**/*.{svelte,html,js,ts}"],
            defaultExtractor: (content) => content.match(/[A-Za-z0-9-_:/]+/g) || [],
            safelist: {
                deep: [],
                greedy: [/swiper/, /svelte/]
            }
        })
    ]
};

module.exports = config;
