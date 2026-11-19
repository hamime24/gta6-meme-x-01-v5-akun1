// gta6-meme-x-01 entry (akun 1): the grader scores the X post, not this
// program. This file exists only to put POST.json (the post's address) into
// /output, where the gate can read it. One file in, one file out.
import { copyFileSync, mkdirSync, readFileSync } from "node:fs";
import { join } from "node:path";

const BOT_DIR = process.env.MAKEFUN_BOT_DIR ?? "/bot";
const OUT_DIR = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
const SRC = join(BOT_DIR, "POST.json");

// Read first so a corrupt POST.json fails here, not at the gate.
const parsed = JSON.parse(readFileSync(SRC, "utf-8"));
if (typeof parsed.url !== "string" || !parsed.url.startsWith("https://x.com/")) {
  console.error(`POST.json has no valid x.com URL: ${SRC}`);
  process.exit(1);
}

mkdirSync(OUT_DIR, { recursive: true });
copyFileSync(SRC, join(OUT_DIR, "POST.json"));

// Guard: the URL check above is the real guard — it proves POST.json names
// an x.com post before anything is copied to the output directory.
