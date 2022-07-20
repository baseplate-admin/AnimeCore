module.exports = {
    root: true,
    parser: "@typescript-eslint/parser",
    extends: ["eslint:recommended", "plugin:@typescript-eslint/recommended", "prettier"],
    plugins: ["svelte3", "@typescript-eslint", "simple-import-sort"],
    ignorePatterns: ["*.cjs"],
    overrides: [{ files: ["*.svelte"], processor: "svelte3/svelte3" }],
    settings: {
        "svelte3/typescript": () => require("typescript")
    },
    parserOptions: {
        sourceType: "module",
        ecmaVersion: 2020
    },
    rules: {
        /** Sort imports */
        "simple-import-sort/imports": "warn",
        "simple-import-sort/exports": "warn"
    },
    env: {
        browser: true,
        es2017: true,
        node: true
    }
};
