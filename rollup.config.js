import resolve from "@rollup/plugin-node-resolve";
import commonjs from "@rollup/plugin-commonjs";
import { terser } from "rollup-plugin-terser";

const production = process.env.NODE_ENV === "production";

export default {
  input: "wetter/static/wetter/js/wetter.js",
  output: {
    dir: "wetter/static/js",
    format: "iife",
    sourcemap: !production
  },
  plugins: [resolve(), commonjs(), !production && terser()]
};
