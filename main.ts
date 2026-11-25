/**
 * Post the Meme, Win the Feed — make.fun entry.
 *
 * main.ts copies POST.json from the repository root to /output.
 * That is all the program has to do: the house reads the X post itself
 * (its counts, the @_myronera mention and the make.fun play code).
 */
import { copyFileSync, mkdirSync } from "node:fs";
import { join } from "node:path";

const outDir = process.env.OUTPUT_DIR ?? "/output";
mkdirSync(outDir, { recursive: true });
copyFileSync("POST.json", join(outDir, "POST.json"));
