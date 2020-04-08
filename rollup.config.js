import resolve from "@rollup/plugin-node-resolve";
import commonjs from "@rollup/plugin-commonjs";
import { terser } from "rollup-plugin-terser";
import css from "rollup-plugin-scss";

const production = process.env.NODE_ENV === "production";

const config = {
  input: "wetter/static/wetter/js/wetter.js",
  output: {
    dir: "wetter/static/js",
    format: "iife",
    sourcemap: !production
  },
  plugins: [
    css({
      output: "wetter/static/css/bundle.css",
      outFile: "wetter/static/css/bundle.css",
      outputStyle: production ? "compressed" : "expanded",
      sourceMap: !production
    }),
    resolve(),
    commonjs(),
    production && terser()
  ]
};

export default [config];
