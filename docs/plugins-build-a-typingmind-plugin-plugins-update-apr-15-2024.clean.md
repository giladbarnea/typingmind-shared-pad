[Plugins](https://docs.typingmind.com/plugins)

[Build a TypingMind Plugin](https://docs.typingmind.com/plugins/build-a-typingmind-plugin)

# Plugins Update Apr 15 2024

We’ve made a major improvement around the plugin system for plugin developers and Typing Mind Custom users! Here are the details:

- **Added Icon URL**: you are no longer forced to use the “🧩” emoji as your plugin icon! Click “Edit”, then enter the Icon URL for your plugin, and it will be shown everywhere in the app.

- **Added HTTP Action:** this is a new way to implement your plugin without using JavaScript code. HTTP Action allows you to easily set up a simple HTTP request for external services. Post-processing engines ( **JSMEPath** and **Handlebars.js**) are available to help you customize the output even more.

- **Added Output Options:** You can now render your plugin output directly to the user instead of giving the output to the AI models. The output can be rendered using **Markdown** or **HTML.** This gives you more flexibility to render interactive experiences to the users and, in some cases, saves more tokens!

- **JavaScript code changes:** The `__CUSTOM_OUTPUT` special property is now deprecated (replaced by the **Output Options** feature). If you have developed a plugin that uses this property in your JavaScript implementation, please update your plugins according to the new [Plugins documentation](https://docs.typingmind.com/plugins/build-a-typingmind-plugin) (just updated!).

🟦 For [Typing Mind Custom](https://custom.typingmind.com/) users:

- **✨ Introducing Server Plugins**: Server plugins are plugins that run on the server side and are hidden away from the users. Admin users can enable and set up the plugin settings in advance, then your users just need to use it. The users will not see the plugin source code, settings, credentials, etc. and don’t need to provide any settings to the plugins.

- **Built-in Server Plugins:** We added 3 basic server plugins: **Web Search**, **Image Search**, and **DALL-E 3**. All of these plugins’ source code and settings are available for learning, you can simply “Duplicate” them from the admin panel to create new ones if needed. We’ll continue to add more built-in server plugins soon!

- **Removing settings for Client Plugins from the Admin panel**: If you are an Admin and have previously used the “Plugin Settings” feature for Client plugins, you should go to the Admin Panel and change to use Server Plugins for better user experience and avoid exposing your settings to the users.

📜 Read the newly updated [Plugins Documentation here](https://docs.typingmind.com/plugins/build-a-typingmind-plugin)!

Hope you like this change. If you have any questions, feel free to let discuss here.

Cheers!

[Build a TypingMind Plugin](https://docs.typingmind.com/plugins/build-a-typingmind-plugin)

[User-contributed Plugins](https://docs.typingmind.com/plugins/user-contributed-plugins)