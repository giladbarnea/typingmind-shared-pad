[Plugins](https://docs.typingmind.com/plugins)

# Server Side vs. Client Side Plugin

Here is the difference between running a plugin on the **Server Side** and on the **Client Side**:

## What is a Server Plugin?

## Run on the Server side:

✅ **How it works:**

- The user can not see the plugin's code, API keys, credentials, and data. Only the plugin's output is shown to the user.

- If the plugin requires sending HTTP requests to external servers, the requests will be sent from the TypingMind server, hidden away from the user.

✅ **When to use it:**

- By default, all plugins are run on the server side if it has an HTTP action implementation.

- Running the plugin on the server side is more convenience for the users, as they don’t need to setup anything to use the plugins.

## Run on the Client side:

**✅ How it works:**

- The plugin will be run on the users’ browser.

- If the plugin has a JavaScript implementation, the code will be executed in a sandboxed browser environment on the user’s device.

- If the plugin requires sending HTTP requests to external servers, the requests will be sent directly from the user’s browser to the external server (be aware of CORS issues in this case).

- The users will need to provide all the plugin settings (e.g., API keys) in order to use the plugin.

**✅ When to use it:**

- Use it if the plugin is designed to be run on the client, for example, rendering interactive charts or running JavaScript on the user’s device.

- Use this if you want to give the users the flexibility of using their own API key in some plugins.

## FAQs

**Can I make a plugin run both on the server side and the client side?**

No, but you can duplicate a plugin and then assign each plugin to run on the client/server side separately. Note that in this case, the user may see 2 plugins with the same name on their UI, which can be confusing.

[Share / Import plugins](https://docs.typingmind.com/plugins/share-import-plugins)

[OAuth 2.0 Authentication for Plugins](https://docs.typingmind.com/plugins/oauth-2.0-authentication-for-plugins)