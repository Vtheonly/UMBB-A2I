import { PageLayout, SharedLayout } from "./quartz/cfg"
import * as Component from "./quartz/components"

// components shared across all pages
export const sharedPageComponents: SharedLayout = {
  head: Component.Head(),
  header: [],
  afterBody: [],
  footer: Component.Footer({
    links: {
      GitHub: "https://github.com/Vtheonly",
      Linkedin: "https://www.linkedin.com/in/mersel-fares-baa8aa268/",
    },
  }),
}

// components for pages that display a single page (e.g. a single note)
export const defaultContentPageLayout: PageLayout = {
  beforeBody: [
    Component.ConditionalRender({
      component: Component.Breadcrumbs(),
      condition: (page) => page.fileData.slug !== "index",
    }),
    Component.ArticleTitle(),
    Component.ContentMeta(),
    Component.TagList(),
  ],
  left: [
    Component.PageTitle(),
    Component.MobileOnly(Component.Spacer()),
    Component.Flex({
      components: [
        {
          Component: Component.Search(),
          grow: true,
        },
        { Component: Component.Darkmode() },
        { Component: Component.ReaderMode() },
      ],
    }),
    Component.Explorer(),
  ],
  right: [
    // In quartz.layout.ts, inside the 'right:' array

    Component.Graph({
      localGraph: {
        // BEHAVIORAL properties are VALID and should stay
        drag: true,
        zoom: true,
        depth: 1,
        scale: 1.1,
        repelForce: 0.7,
        centerForce: 0.3,
        linkDistance: 30,
        fontSize: 0.6,
        opacityScale: 3,
        showTags: false, // Set to false for a cleaner look, or true if you want them
        focusOnHover: true,

        // REMOVE ALL COLOR PROPERTIES FROM HERE
      },
      globalGraph: {
        // BEHAVIORAL properties are VALID and should stay
        drag: true,
        zoom: true,
        depth: -1,
        scale: 0.9,
        repelForce: 0.8,
        centerForce: 0.3,
        linkDistance: 30,
        fontSize: 0.6,
        opacityScale: 1,
        showTags: false,
        focusOnHover: true,

        // REMOVE ALL COLOR PROPERTIES FROM HERE
      },
    }),
    Component.DesktopOnly(Component.TableOfContents()),
    Component.Backlinks(),
  ],
}

// components for pages that display lists of pages  (e.g. tags or folders)
export const defaultListPageLayout: PageLayout = {
  beforeBody: [Component.Breadcrumbs(), Component.ArticleTitle(), Component.ContentMeta()],
  left: [
    Component.PageTitle(),
    Component.MobileOnly(Component.Spacer()),
    Component.Flex({
      components: [
        {
          Component: Component.Search(),
          grow: true,
        },
        { Component: Component.Darkmode() },
      ],
    }),
    Component.Explorer(),
  ],
  right: [],
}
