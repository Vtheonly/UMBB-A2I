import { QuartzConfig } from "./quartz/cfg"
import * as Plugin from "./quartz/plugins"

/**
 * Quartz 4 Configuration
 *
 * See https://quartz.jzhao.xyz/configuration for more information.
 */
const config: QuartzConfig = {
  configuration: {
    pageTitle: "UMBB A2I",
    pageTitleSuffix: "",
    enableSPA: true,
    enablePopovers: true,
    analytics: {
      provider: "plausible",
    },
    locale: "en-US",
    // baseUrl: "quartz.jzhao.xyz",
    ignorePatterns: ["private", "templates", ".obsidian"],
    defaultDateType: "modified",
    theme: {
      fontOrigin: "googleFonts",
      cdnCaching: true,
      typography: {
        header: "Roboto Slab", // A strong, modern header font
        body: "Inter", // A very clean and readable body font
        code: "JetBrains Mono", // One of the best coding fonts
      },
      colors: {
        lightMode: {
          // Dracula Light (hypothetical)
          light: "#f8f8f2", // Background
          lightgray: "#e3e3e0", // Borders
          gray: "#8e8e8e", // Medium text
          darkgray: "#44475a", // Body text
          dark: "#282a36", // Headings
          secondary: "#ff79c6", // Links (Pink)
          tertiary: "#8be9fd", // Metadata, special text (Cyan)
          highlight: "rgba(255, 121, 198, 0.15)", // Highlight background
          textHighlight: "#00000000",
        },
        darkMode: {
          // Classic Dracula Theme
          light: "#282a36", // Background
          lightgray: "#44475a", // Component backgrounds
          gray: "#94a3b8", // Medium text
          darkgray: "#e2e8f0", // Body text
          dark: "#f8f8f2", // Headings
          secondary: "#bd93f9", // Links (Purple)
          tertiary: "#50fa7b", // Metadata, special text (Green)
          highlight: "rgba(189, 147, 249, 0.15)", // Highlight background
          textHighlight: "#00000000",
        },
      },
    },
  },
  plugins: {
    transformers: [
      Plugin.FrontMatter(),
      Plugin.CreatedModifiedDate({
        priority: ["frontmatter", "git", "filesystem"],
      }),
      Plugin.SyntaxHighlighting({
        theme: {
          light: "github-light",
          dark: "github-dark",
        },
        keepBackground: false,
      }),
      Plugin.ObsidianFlavoredMarkdown({ enableInHtmlEmbed: false }),
      Plugin.GitHubFlavoredMarkdown(),
      Plugin.TableOfContents(),
      Plugin.CrawlLinks({ markdownLinkResolution: "shortest" }),
      Plugin.Description(),
      Plugin.Latex({ renderEngine: "katex" }),
    ],
    filters: [Plugin.RemoveDrafts()],
    emitters: [
      Plugin.AliasRedirects(),
      Plugin.ComponentResources(),
      Plugin.ContentPage(),
      Plugin.FolderPage(),
      Plugin.TagPage(),
      Plugin.ContentIndex({
        enableSiteMap: true,
        enableRSS: true,
      }),
      Plugin.Assets(),
      Plugin.Static(),
      Plugin.Favicon(),
      Plugin.NotFoundPage(),
      // Comment out CustomOgImages to speed up build time
      Plugin.CustomOgImages(),
    ],
  },
}

export default config
