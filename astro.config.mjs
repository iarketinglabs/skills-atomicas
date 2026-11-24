import {defineConfig} from 'astro/config';
export default defineConfig({
  site:'https://iarketinglabs.github.io',
  base:'/skills-atomicas',
  trailingSlash:'always',
  publicDir:'./static',
  output:'static',
});
