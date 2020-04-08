import resolve from "@rollup/plugin-node-resolve";
import commonjs from "@rollup/plugin-commonjs";
import { terser } from "rollup-plugin-terser";
import css from "rollup-plugin-scss";
import copy from "rollup-plugin-copy";

const production = process.env.NODE_ENV === "production";

const config = {
  input: "wetter/static/wetter/js/wetter.js",
  output: {
    dir: "wetter/static",
    format: "iife",
    sourcemap: !production
  },
  plugins: [
    copy({
      targets: [
        {
          src: "node_modules/leaflet/dist/images/*",
          dest: "wetter/static/images"
        }
      ]
    }),
    css({
      output: "wetter/static/bundle.css",
      outFile: "wetter/static/bundle.css",
      outputStyle: production ? "compressed" : "expanded",
      sourceMap: !production
    }),
    resolve(),
    commonjs(),
    production && terser()
  ]
};

export default [config];
