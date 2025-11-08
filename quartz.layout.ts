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

    // in quartz.layout.ts
    Component.Graph({
      localGraph: {
        // Increase repel force to prevent nodes from overlapping as much
        repelForce: 0.8,
        // Increase the default link distance to give nodes more breathing room
        linkDistance: 50,
        // Lower the centering force to allow the graph to spread out more
        centerForce: 0.2,
        // Increase the number of connection hops to show for a richer local view
        depth: 2,
        // Other settings
        drag: true,
        zoom: true,
        scale: 1.1,
        fontSize: 0.6,
        opacityScale: 3,
        showTags: true,
        focusOnHover: true,
      },
      globalGraph: {
        repelForce: 0.8,
        linkDistance: 50,
        centerForce: 0.2,
        depth: -1, // Show all nodes in global view
        drag: true,
        zoom: true,
        scale: 0.9,
        fontSize: 0.6,
        opacityScale: 1,
        showTags: true,
        focusOnHover: true,
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
