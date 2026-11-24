import {readFileSync} from 'node:fs';
import {writeDownloads} from './packages.mjs';
writeDownloads(JSON.parse(readFileSync('src/data/catalog.json','utf8').replace(/^\uFEFF/, '')));
