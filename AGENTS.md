# TypingMind Shared Pad Plugin

This project revolves around TypingMind, an LLM chat UI that supports writing your own extensions and plugins.
Extensions are plain injected JS with access to the finished UI DOM, allowing client-side manipulation.
Plugins are more complex and powerful. They add functionality for both the LLM and the user. Each plugin is declared in a plugin.json, which can define capabilities ranging from a bare Tool Calling spec the LLM may follow to custom implementations that run on the client side or make requests to a server.
Extensions and plugins can work together in a classic client/server model, but if a task can be done with just one, I prefer that.
The plugin I’m building provides a shared Markdown pad that both the LLM and the user can read and edit. The goal is to deliver the same value as Slack’s Canvas: a persistent, always-available document where everyone sees the same content and can peek at any time. It’s a great fit for meta-information—think roadmaps, important details to remember, a North Star for the conversation to avoid going down rabbit holes—or for artifacts (products of the conversation) that both sides iterate on, like an author-editor back-and-forth.
I recently deployed a Python server to Vercel that also serves the extension and plugin files CDN-style. The public Vercel deployment URL is https://typingmind-plugin-server.vercel.app/.
The TypingMind docs website is docs.typingmind.com.
An important page is https://docs.typingmind.com/plugins/build-a-typingmind-plugin.
The Github repository of my plugin is giladbarnea/typingmind-shared-pad. It is WIP (not everything works).
Among the skills relevant to this effort, my weakest is UI and UX design, usability, and so on. You're welcome to chime in and suggest thoughtful ideas in that regard.