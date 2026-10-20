import { defineConfig } from "cf/config";

export default defineConfig({
  worker: {
    name: "vindam-fitness",
    compatibilityDate: "2026-10-20",
    observability: {
      enabled: true
    }
  }
});
