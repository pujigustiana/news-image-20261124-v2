// News-24 v2 entry program (make.fun, news-image-20261124).
// The front-page image is rendered at build time by render.py (Python + PIL)
// from the 30 stories in stories.py, and shipped in this repository as
// entry.png. This program copies that image to the grader's output
// directory. It uses only the Node standard library, needs no network, and
// writes the same bytes on every run.
import { copyFileSync, mkdirSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const here = dirname(fileURLToPath(import.meta.url));
const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
mkdirSync(outDir, { recursive: true });
copyFileSync(join(here, "entry.png"), join(outDir, "entry.png"));
