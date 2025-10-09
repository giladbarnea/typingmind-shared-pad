[Plugins](https://docs.typingmind.com/plugins)

# Build a TypingMind Plugin

[Develop your plugin](https://docs.typingmind.com/plugins/build-a-typingmind-plugin#25028e3c3fbb4c01aceb17ca7cc8b493) [OpenAI Function Spec](https://docs.typingmind.com/plugins/build-a-typingmind-plugin#f75675f108634820be70b39319cafb08) [Plugin User Settings (JSON)](https://docs.typingmind.com/plugins/build-a-typingmind-plugin#0e3d2ca8c78f4b62b1a8504957bbb268) [Implementation: JavaScript Code](https://docs.typingmind.com/plugins/build-a-typingmind-plugin#074a51fe7a7f406ab6dbbf1c613cb80b) [Access User Settings in Plugin JavaScript Code](https://docs.typingmind.com/plugins/build-a-typingmind-plugin#80f2f9e5228d4c2c839520dd0a4eb33d) [Implementation: HTTP Action](https://docs.typingmind.com/plugins/build-a-typingmind-plugin#f8f5759520614775aaf136c279931e76) [Access User Settings in HTTP Action](https://docs.typingmind.com/plugins/build-a-typingmind-plugin#f4fd6a7178fb474bbadd26c7f8742577) [Built-in variables for HTTP Action on server side](https://docs.typingmind.com/plugins/build-a-typingmind-plugin#fa8d51b1169e44d0bcfa1dd883129e92) [HTTP Action Post-Processing](https://docs.typingmind.com/plugins/build-a-typingmind-plugin#d41e59fa90f3411b98bb6d373f30c1b1) [Test your HTTP Action](https://docs.typingmind.com/plugins/build-a-typingmind-plugin#c2d39976ad8943bfa18a66dcca3900c4) [Output Options](https://docs.typingmind.com/plugins/build-a-typingmind-plugin#2f5737f436bc43ac91732b0cd1e18dc8) [When to use custom output](https://docs.typingmind.com/plugins/build-a-typingmind-plugin#7e425d5891234d758be880c9cde69caf) [Test your plugin](https://docs.typingmind.com/plugins/build-a-typingmind-plugin#32324aff653c4bfdbc0bbe9e4313330b) [Limitations](https://docs.typingmind.com/plugins/build-a-typingmind-plugin#a182d193cebc44a797b6f36163520e37) [Example plugins](https://docs.typingmind.com/plugins/build-a-typingmind-plugin#9ea9a86a39464966a2dbe504f47601e4)

**TypingMind Plugins** allow you to extend the capabilities of the AI assistant by providing external tools. To get started, click the “Plugins” button on the start screen.

🧪

**Note:** TypingMind Plugins is currently in beta. This document will soon have more sections.

👋

Explore and share your awesome plugins here! 👉 [github.com/TypingMind/awesome-typingmind](https://github.com/TypingMind/awesome-typingmind)

![Image without caption](https://image-forwarder.notaku.so/aHR0cHM6Ly93d3cubm90aW9uLnNvL2ltYWdlL2h0dHBzJTNBJTJGJTJGcHJvZC1maWxlcy1zZWN1cmUuczMudXMtd2VzdC0yLmFtYXpvbmF3cy5jb20lMkY4N2NmOTdjZS05OTQ2LTRjM2QtYTdlMC1hNzkxZWVhMmE0ZTIlMkYzZGMxNmVhMC03N2FlLTQwNjgtYjM0Ni0yMTQ0MjJjYWFhYzglMkZVbnRpdGxlZC5wbmc_dGFibGU9YmxvY2smc3BhY2VJZD04N2NmOTdjZS05OTQ2LTRjM2QtYTdlMC1hNzkxZWVhMmE0ZTImaWQ9NjJhZDNmZjgtNWU4YS00YjhhLWE0N2UtYTI3OTRiNWVhMjBkJmNhY2hlPXYyJndpZHRoPTE0MTY=)

![Image without caption](https://image-forwarder.notaku.so/aHR0cHM6Ly93d3cubm90aW9uLnNvL2ltYWdlL2h0dHBzJTNBJTJGJTJGczMtdXMtd2VzdC0yLmFtYXpvbmF3cy5jb20lMkZzZWN1cmUubm90aW9uLXN0YXRpYy5jb20lMkY3ODg4MzU5OC02MTQyLTQ0YjQtYjgwZS01MTZhNmJiNjYyYzQlMkZVbnRpdGxlZC5wbmc_dGFibGU9YmxvY2smc3BhY2VJZD04N2NmOTdjZS05OTQ2LTRjM2QtYTdlMC1hNzkxZWVhMmE0ZTImaWQ9Yjk1MzM2MzktMjZiZC00ZjM1LTkxZjEtNThiZjZhZjcyYzAxJmNhY2hlPXYyJndpZHRoPTI0MDA=)

## Develop your plugin

Typing Mind Plugins allow you to add new capabilities for the AI models. Plugins works using the OpenAI Function Calling API specifications. Typing Mind also support running plugins for other models like Gemini and Claude.

Plugins can be implemented using **JavaScript code** or define a **HTTP Actions**.

Requirements for developing a plugin:

- You can write code in JavaScript (if implemented via JavaScript)

- Basic understand of HTTP requests (if implemented via HTTP Actions)

- You understand the [OpenAI Function Calling API](https://openai.com/blog/function-calling-and-other-api-updates)

Click “Create New Plugin” to start creating your own plugins.

⚠️

At the moment you can only create new plugins manually. Later, we will add a plugins marketplace and a way to import your plugins from GitHub soon.

![Image without caption](https://image-forwarder.notaku.so/aHR0cHM6Ly93d3cubm90aW9uLnNvL2ltYWdlL2h0dHBzJTNBJTJGJTJGczMtdXMtd2VzdC0yLmFtYXpvbmF3cy5jb20lMkZzZWN1cmUubm90aW9uLXN0YXRpYy5jb20lMkZlNjEzMGIyYy1hYzY1LTQyYWEtYmNkMS05NDZjMzA3YjhmYjQlMkZVbnRpdGxlZC5wbmc_dGFibGU9YmxvY2smc3BhY2VJZD04N2NmOTdjZS05OTQ2LTRjM2QtYTdlMC1hNzkxZWVhMmE0ZTImaWQ9NDQwNzI3N2YtYWYxMS00NTc1LTkxNzctOTY2OGRkNzk0NDM0JmNhY2hlPXYyJndpZHRoPTE0MTY=)

Enter the relevant information about the plugin.

- **Plugin Name:** to be shown to the user.

- **Overview:** introduction about the plugin and how to use it. Markdown is supported.

The two most important parts of developing a plugin is to provide an **OpenAI Function Spec** and the **Code Implementation**.

### **OpenAI Function Spec**

✅ **Make sure it’s in the correct JSON format.**

Follow the instructions in [OpenAI document](https://openai.com/blog/function-calling-and-other-api-updates) to understand how to write one. You can see the spec of existing plugins like Simple Calculator, JavaScript Interpreter, or the Generate Random Number example plugin below for reference.

✅ **Unique Function Name**

Note that the `name` field of the spec must be **unique across all plugins you currently have**. This is because OpenAI API will use this name to call the function, having multiple functions with the same name will confuse the AI.

✅ **Use meaningful names & descriptions**

It’s important to provide a meaningful function name, function description, parameter name, parameter description, etc.

The AI will use these names and descriptions to understand and decide when to use your function. Providing a meaningful and accurate name will help the AI use your function/plugin better.

✅ **Example of a JSON OpenAI Function Spec:**

```font-medium max-w-screen-2xl

json{
  "name": "generate_random_number_in_range",
  "description": "Generate a random integer number between number 'a' and number 'b'.",
  "parameters": {
    "type": "object",
    "properties": {
      "a": {
        "type": "number",
        "description": "The number a (the smaller number)"
      },
      "b": {
        "type": "number",
        "description": "The number b (the larger number)"
      }
    },
    "required": [\
      "a",\
      "b"\
    ]
  }
}
```

### Plugin User Settings (JSON)

User Settings allows you to define necessary input fields for your plugin which would be filled by the users. The parameters in this section accept JSON formatted strings.

An example of the JSON format:

```font-medium max-w-screen-2xl

json[\
  {\
    "name": "searchEngineID",\
    "label": "Search Engine ID"\
  },\
  {\
    "name": "searchEngineAPIKey",\
    "label": "Search Engine API Key",\
    "type": "password"\
  },\
	{\
	  "name": "quality",\
	  "label": "Quality",\
	  "description": "Optional, default: \"standard\"",\
	  "type": "enum",\
	  "values": [\
	    "standard",\
	    "hd"\
	  ]\
	}\
]
```

This tells the UI to render input fields where users can enter their own specific data. Each object in the array represents a single user input field.

Here's what each key represents:

- **name:** This is the identifier the plugin will use to retrieve the user's input.

- **label:** This is the label displayed to the user to help identify what information should be entered. Try to make this intuitive and relevant to the data you're asking for.

- **required (optional)**: must be a boolean value of `true` or `false` , indicate whether the field is required or not. Default `false`.

- **description (optional):** Displayed as a small text under the label. Use this to clarify other information related to the field.

- **type (optional):** This is used to specify the type of data expected from the users. For instance, input type could be `password`, `email`, `number`, `enum` . By default, if not specified, the type is assumed to be `text`.

- **placeholder (optional):** The placeholder text to be shown in the input field.

- **values (optional):** Only take effect when type is `enum`, this must be an array of strings of allowed value for the field.

- **defaultValue (optional):** the default value if not provided by the user

To use these settings within your plugin, you can access them from the user's input and either store them for later use or use them immediately as needed.

### Implementation: JavaScript Code

You can implement your plugin using JavaScript code. The code will be run directly on the user’s browser. Below are the details.

✅ **Make sure it’s a valid JavaScript**

Write the function implementation in JavaScript. You can use `async` functions if necessary.

✅ **Make sure the function name match**

It’s important that you define a function with the exact same name as defined in the JSON spec at the top level. For example, if you have `"name": "get_calculation_result"` in your JSON spec, then the code must have a function named `get_calculation_result` defined at the top level.

**✅ Only two parameters**

By OpenAI’s convention, your function always accept only twoparameters, both of type `object`.

- First parameter ( `params`): The parameter created by the AI assistant everytime your function is created. The object contains multiple key/value pairs that the AI will decide when they execute your function.

- Second parameter ( `userSettings`): If your plugin has a User Settings (discussed in a later section), the key/value pair of the user settings will be passed into this object.

Example:

```font-medium max-w-screen-2xl

javascriptasync function get_search_results(params, userSettings) {
  const { keyword, pages } = params;
  const { searchAPIKey } = userSettings;
  const result = ...  // your code here...
  return result;
}
```

✅ **Execution Environment**

The code will be executed directly in your local browser, there is no server component.

A sandbox environment will be created for the code by using `<iframe sandbox="allow-scripts">`. This sandbox environment provides some level of isolation, privacy, and security for the plugin code. Learn what you can and cannot do in an iframe sandbox [here](https://web.dev/sandboxed-iframes/).

If you are using someone else’s code, make sure you read and understand what it does. Never use untrusted code in your plugin.

**✅ Be aware of CORS issues**

Because the code is executed locally on your browser, if you decide to send a request to an external server, make sure that external server is configurated correctly to accept the requests without any CORS related issues.

**✅ Example code of a plugin:**

```font-medium max-w-screen-2xl

javascriptfunction generate_random_number_in_range({a, b}) {
    var min = Math.ceil(a);
    var max = Math.floor(b);
    return Math.floor(Math.random() * (max - min + 1) + min);
}
```

**✅ Error & Exception handling**

If there is an error or exception while running your plugin, you should throw it using `throw new Error("User friendly message here")`. This way, the app will show the message `"User friendly message here"` to the end user. The AI will also see this error message and may attempt to run the plugins again with a different parameter if needed.

If your error is throw correctly, the app will display the error message like this:

![Image without caption](https://image-forwarder.notaku.so/aHR0cHM6Ly93d3cubm90aW9uLnNvL2ltYWdlL2h0dHBzJTNBJTJGJTJGcHJvZC1maWxlcy1zZWN1cmUuczMudXMtd2VzdC0yLmFtYXpvbmF3cy5jb20lMkY4N2NmOTdjZS05OTQ2LTRjM2QtYTdlMC1hNzkxZWVhMmE0ZTIlMkZkMWY2YTdmNC02YWQ3LTQ2ZTMtOTYwOC04NmMyMjkwYmI2MmIlMkZVbnRpdGxlZC5wbmc_dGFibGU9YmxvY2smc3BhY2VJZD04N2NmOTdjZS05OTQ2LTRjM2QtYTdlMC1hNzkxZWVhMmE0ZTImaWQ9YzBlMGRlY2ItNDUzYi00OGI2LTliMTgtYjQxNTczYzViOTliJmNhY2hlPXYyJndpZHRoPTE0MTY=)

### Access User Settings in Plugin JavaScript Code

Once you've defined user settings for your plugin, the next step is to retrieve those values within your plugin's function. User settings are passed into your function as its second parameter.

Here's how you can access user settings from your function:

```font-medium max-w-screen-2xl

javascriptfunction search_images_via_google(params, userSettings) {
  // Your code here
}

```

In the above example, `search_images_via_google` is the function that gets called in your plugin. You see that `params` is the first parameter and `userSettings` is the second parameter:

- `params` is an object that contains the runtime parameters passed by the AI or users.

- `userSettings` is the object that contains all the custom settings configured by the user.

The `userSettings` parameter is essentially an object where the keys are the names of the user settings you previously defined and the value is whatever the user provided for those settings.

For instance, if you have the following user settings:

```font-medium max-w-screen-2xl

json[\
  {\
    "name": "searchEngineID",\
    "label": "Search Engine ID"\
  },\
  {\
    "name": "searchEngineAPIKey",\
    "label": "Search Engine API Key",\
    "type": "password"\
  }\
]

```

You can retrieve those settings in your function as follows:

```font-medium max-w-screen-2xl

javascriptfunction search_images_via_google(params, userSettings) {
  const searchEngineID = userSettings.searchEngineID;
  const searchEngineAPIKey = userSettings.searchEngineAPIKey;

  // Now you can use these values in your code
}
```

In this example, `searchEngineID` and `searchEngineAPIKey` are keys within the `userSettings` object, and the corresponding values are what the user provided in the settings fields.

By accessing user settings in this way, you add a layer of customization to your plugin, enabling it to cater to the specific needs and preferences of different users.

### Implementation: HTTP Action

Another option to implement your plugin is **HTTP Action**.

![Image without caption](https://image-forwarder.notaku.so/aHR0cHM6Ly93d3cubm90aW9uLnNvL2ltYWdlL2h0dHBzJTNBJTJGJTJGcHJvZC1maWxlcy1zZWN1cmUuczMudXMtd2VzdC0yLmFtYXpvbmF3cy5jb20lMkY4N2NmOTdjZS05OTQ2LTRjM2QtYTdlMC1hNzkxZWVhMmE0ZTIlMkZlNzUwMDFlNS0xNjJmLTQ1NzctOWJmYy1kYzFhOGY3NTQwZGElMkZVbnRpdGxlZC5wbmc_dGFibGU9YmxvY2smc3BhY2VJZD04N2NmOTdjZS05OTQ2LTRjM2QtYTdlMC1hNzkxZWVhMmE0ZTImaWQ9M2VhODNjNTAtMDE0Yi00YWJjLWJiNTktMmZjYjgzNTdlZTYyJmNhY2hlPXYyJndpZHRoPTE0MTY=)

When the plugin runs, it will send a request from the user’s browser using the information provided.

- HTTP Method

- Endpoint URL

- Headers (optional)

- Body (optional)

- Post-Processing (optional)

### Access User Settings in HTTP Action

User settings and call parameters are accessible via template parameters like `{param1}`, `{param2}`, etc.

Within the endpoint URL, headers, and body, you can use these variables to customize the requests. Variables comes from OpenAI Function Spec’s parameters and from User Settings.

For example, in the DALL-E 3 server plugin:

- the variable `{openaikey}` is used in the request headers

- the variables `{prompt}`, `{resolution}`, `{quality}` is used the request body.

The `{prompt}` parameter is provided by the AI when using the plugin, the other parameters are provided by the user via the plugin setting UI.

![Image without caption](https://image-forwarder.notaku.so/aHR0cHM6Ly93d3cubm90aW9uLnNvL2ltYWdlL2h0dHBzJTNBJTJGJTJGcHJvZC1maWxlcy1zZWN1cmUuczMudXMtd2VzdC0yLmFtYXpvbmF3cy5jb20lMkY4N2NmOTdjZS05OTQ2LTRjM2QtYTdlMC1hNzkxZWVhMmE0ZTIlMkYxYWM3ZmUzMC1mNmMzLTQ4ZmQtODAxOS1kMGJhOWI0MzQ1NWIlMkZVbnRpdGxlZC5wbmc_dGFibGU9YmxvY2smc3BhY2VJZD04N2NmOTdjZS05OTQ2LTRjM2QtYTdlMC1hNzkxZWVhMmE0ZTImaWQ9Mzc2MjUyN2UtZDg4Ny00MTEwLWE0ZDktMjk2MWM2ODFmMTcxJmNhY2hlPXYyJndpZHRoPTE0MTY=)

In the example above, all variables are used in a string value to be valid in JSON format. But for number variables, you might want to use them directly as a value, not between the double quotes, we support an exception for that case:

![Image without caption](https://image-forwarder.notaku.so/aHR0cHM6Ly93d3cubm90aW9uLnNvL2ltYWdlL2h0dHBzJTNBJTJGJTJGcHJvZC1maWxlcy1zZWN1cmUuczMudXMtd2VzdC0yLmFtYXpvbmF3cy5jb20lMkY4N2NmOTdjZS05OTQ2LTRjM2QtYTdlMC1hNzkxZWVhMmE0ZTIlMkZiNzIwZTk0NC04NWJlLTQyMGUtOTZhYi0xZjk1MWUxZWEyM2ElMkZVbnRpdGxlZC5wbmc_dGFibGU9YmxvY2smc3BhY2VJZD04N2NmOTdjZS05OTQ2LTRjM2QtYTdlMC1hNzkxZWVhMmE0ZTImaWQ9ODZhZjA2ODktNzczZi00MmUzLWE0MjUtNDI5ZmUyZjBjNzRkJmNhY2hlPXYyJndpZHRoPTE0MTY=)

### Built-in variables for HTTP Action on server side

When running an HTTP Action on server side (server plugin), your plugin has access to the following built-in variables:

|                             |                                                                                                                                                                                |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Variable                    | Description                                                                                                                                                                    |
| `CHAT_ID`                   | Unique identifier of a chat (current conversation) where the plugin is used.                                                                                                   |
| `USER_ID`                   | Unique identifier of the user who is using the plugin.                                                                                                                         |
| `OAUTH_USER_ID_TOKEN`       | The `id_token` of the user. Only available if the current user is authenticated using [OAuth](https://docs.typingmind.com/typingmind-team/user-management/oauth-2.0).          |
| `OAUTH_USER_ACCESS_TOKEN`   | The `access_token` of the user. Only available if the current user is authenticated using [OAuth](https://docs.typingmind.com/typingmind-team/user-management/oauth-2.0).      |
| `OAUTH_PLUGIN_ACCESS_TOKEN` | When the plugin authentication type is set to **OAuth**, the plugin will ask the user to authenticate before using. This is the access token of the user after authentication. |

### HTTP Action Post-Processing

**Post-Processing** can be used to transform the HTTP response to your desired output. This is helpful to trim the response down only the useful information, saving the number of tokens used.

Typing Mind supports two Post-Processing engines:

- **JMESPath Transform** ( [docs](https://jmespath.org/)): Useful to filter a big JSON response to a smaller JSON.

- **Handlebars.js Template** ( [docs](https://handlebarsjs.com/guide/)): Useful to rewrite the JSON response into a different format like Markdown or HTML.

For example, here is how the DALLE-3 plugin uses Handlebars.js template to transform the JSON response into a Markdown document to be rendered to the user:

![Image without caption](https://image-forwarder.notaku.so/aHR0cHM6Ly93d3cubm90aW9uLnNvL2ltYWdlL2h0dHBzJTNBJTJGJTJGcHJvZC1maWxlcy1zZWN1cmUuczMudXMtd2VzdC0yLmFtYXpvbmF3cy5jb20lMkY4N2NmOTdjZS05OTQ2LTRjM2QtYTdlMC1hNzkxZWVhMmE0ZTIlMkZhZmZiNDVjZS05NzQyLTQ5NmEtYTk3OC0wMmU2MTNiNWU0NWElMkZVbnRpdGxlZC5wbmc_dGFibGU9YmxvY2smc3BhY2VJZD04N2NmOTdjZS05OTQ2LTRjM2QtYTdlMC1hNzkxZWVhMmE0ZTImaWQ9YTUwZDNiYmQtMDI4MS00MThiLWI2NGMtODNmNDllNGI2OTg4JmNhY2hlPXYyJndpZHRoPTE0MTY=)

You can also use all variables in this post-processing via a special property called `__VARIABLES` (Only support for object responses):

![Image without caption](https://image-forwarder.notaku.so/aHR0cHM6Ly93d3cubm90aW9uLnNvL2ltYWdlL2h0dHBzJTNBJTJGJTJGcHJvZC1maWxlcy1zZWN1cmUuczMudXMtd2VzdC0yLmFtYXpvbmF3cy5jb20lMkY4N2NmOTdjZS05OTQ2LTRjM2QtYTdlMC1hNzkxZWVhMmE0ZTIlMkY4NmEwMTQxYi1hNDE1LTQ2ODMtOTVmNS01N2I2MmZhNGUyZWIlMkZVbnRpdGxlZC5wbmc_dGFibGU9YmxvY2smc3BhY2VJZD04N2NmOTdjZS05OTQ2LTRjM2QtYTdlMC1hNzkxZWVhMmE0ZTImaWQ9ZjI0YWNkN2MtNTYzNC00MDkwLTljN2MtMjVjOTkyOTM1Njc5JmNhY2hlPXYyJndpZHRoPTE0MTY=)

### Test your HTTP Action

To make sure the HTTP requests are working normally, you can send a test request with test variables.

The test result will be what the AI model see (or what will be rendered to the user, depends on your plugin setting).

![Image without caption](https://image-forwarder.notaku.so/aHR0cHM6Ly93d3cubm90aW9uLnNvL2ltYWdlL2h0dHBzJTNBJTJGJTJGcHJvZC1maWxlcy1zZWN1cmUuczMudXMtd2VzdC0yLmFtYXpvbmF3cy5jb20lMkY4N2NmOTdjZS05OTQ2LTRjM2QtYTdlMC1hNzkxZWVhMmE0ZTIlMkY1NjQ5NWYyMy1lNTJkLTRhMjYtYWEyZC01YmVlMjFhYWNmMzIlMkZVbnRpdGxlZC5wbmc_dGFibGU9YmxvY2smc3BhY2VJZD04N2NmOTdjZS05OTQ2LTRjM2QtYTdlMC1hNzkxZWVhMmE0ZTImaWQ9ODI5ZTYzODktOTE2ZS00MGQwLWI5ZmMtYTBlY2E4MTdkNDY2JmNhY2hlPXYyJndpZHRoPTE0MTY=)

## Output Options

You can setup your plugin to output the result directly to the AI, or render the output directly to the users using Markdown or HTML.

This can be configured in the Output Options. The supported output types are:

- Give plugin output to the AI

- Render plugin output as markdown

- Render plugin output as interactive HTML

![Image without caption](https://image-forwarder.notaku.so/aHR0cHM6Ly93d3cubm90aW9uLnNvL2ltYWdlL2h0dHBzJTNBJTJGJTJGcHJvZC1maWxlcy1zZWN1cmUuczMudXMtd2VzdC0yLmFtYXpvbmF3cy5jb20lMkY4N2NmOTdjZS05OTQ2LTRjM2QtYTdlMC1hNzkxZWVhMmE0ZTIlMkY1YmEwYTJiZi01MDc2LTRiNDktOTE1MC0xNGRiM2Y4ZmRhNDAlMkZVbnRpdGxlZC5wbmc_dGFibGU9YmxvY2smc3BhY2VJZD04N2NmOTdjZS05OTQ2LTRjM2QtYTdlMC1hNzkxZWVhMmE0ZTImaWQ9MjBmNWJjY2QtNTZhMy00OTUyLTk5MDctOTExYWI5MjU1OTE3JmNhY2hlPXYyJndpZHRoPTE0MTY=)

### When to use custom output

Normally, the return value of your plugin will be passed directly to the AI, then the AI will decide how to answer the user based on the returned value.

However, in some cases, you prefer to render the output to the users directly by yourself.

For example, the **DALL-E 3** plugin will render the generated images directly to the users in Markdown format. This saves time for the users because the AI will not need to “type” the long image URLs manually after it received the return value from the plugin.

![Image without caption](https://image-forwarder.notaku.so/aHR0cHM6Ly93d3cubm90aW9uLnNvL2ltYWdlL2h0dHBzJTNBJTJGJTJGcHJvZC1maWxlcy1zZWN1cmUuczMudXMtd2VzdC0yLmFtYXpvbmF3cy5jb20lMkY4N2NmOTdjZS05OTQ2LTRjM2QtYTdlMC1hNzkxZWVhMmE0ZTIlMkY4NjZkNDAwNS1kZDliLTRmNDgtOWFkNS00YWE3ZTYzMmYwNDYlMkZVbnRpdGxlZC5wbmc_dGFibGU9YmxvY2smc3BhY2VJZD04N2NmOTdjZS05OTQ2LTRjM2QtYTdlMC1hNzkxZWVhMmE0ZTImaWQ9MzE3YzJkNDgtYjBkMS00NDVkLWEwZTUtYjZkNTFkN2E3MDNkJmNhY2hlPXYyJndpZHRoPTE0MTY=)

In order to do this, the **DALL-E 3** plugin uses the “ **Render plugin output as markdown**” option.

![Image without caption](https://image-forwarder.notaku.so/aHR0cHM6Ly93d3cubm90aW9uLnNvL2ltYWdlL2h0dHBzJTNBJTJGJTJGcHJvZC1maWxlcy1zZWN1cmUuczMudXMtd2VzdC0yLmFtYXpvbmF3cy5jb20lMkY4N2NmOTdjZS05OTQ2LTRjM2QtYTdlMC1hNzkxZWVhMmE0ZTIlMkZkMmRmNDMxMS0yZDk4LTQ5YmMtODQ0Mi0xODM4NWEzMGExODIlMkZVbnRpdGxlZC5wbmc_dGFibGU9YmxvY2smc3BhY2VJZD04N2NmOTdjZS05OTQ2LTRjM2QtYTdlMC1hNzkxZWVhMmE0ZTImaWQ9NjNmMDRhMDUtMTJlMi00ZjRiLTk1ZDgtZTRhMTZmYWRkZGZjJmNhY2hlPXYyJndpZHRoPTE0MTY=)

## Test your plugin

After filling in all the information, click “Save” and enable your newly created plugin.

Then, you can process to chat with the AI.

Note that the AI will decide to use your plugin only when necessary. Make sure your JSON spec has meaningful and accurate names and description.

💡

**Hallucination problem**: Sometimes, the AI assistant hallucinates and try to call your function with incorrect parameter, or even attempt to call function names that does not exists. This is a known issue and there is not much we can do about this. Just click “Regenerate” and let the AI assistant try again.

![Image without caption](https://image-forwarder.notaku.so/aHR0cHM6Ly93d3cubm90aW9uLnNvL2ltYWdlL2h0dHBzJTNBJTJGJTJGczMtdXMtd2VzdC0yLmFtYXpvbmF3cy5jb20lMkZzZWN1cmUubm90aW9uLXN0YXRpYy5jb20lMkY5YzUyZWQzMy0zZTUxLTRiY2MtYmJkMS0xN2I0MzhkNTg5OTMlMkZVbnRpdGxlZC5wbmc_dGFibGU9YmxvY2smc3BhY2VJZD04N2NmOTdjZS05OTQ2LTRjM2QtYTdlMC1hNzkxZWVhMmE0ZTImaWQ9Y2U1MDQ2MzEtZTIwYS00NjQ3LWFjZmEtODhlZWU4NjQwMWMxJmNhY2hlPXYyJndpZHRoPTE0MTY=)

![Image without caption](https://image-forwarder.notaku.so/aHR0cHM6Ly93d3cubm90aW9uLnNvL2ltYWdlL2h0dHBzJTNBJTJGJTJGczMtdXMtd2VzdC0yLmFtYXpvbmF3cy5jb20lMkZzZWN1cmUubm90aW9uLXN0YXRpYy5jb20lMkYwYTA0MDdkNS04ZWYyLTRiMzktODlhYy1iNTQ1ZGMwN2ZmMTMlMkZVbnRpdGxlZC5wbmc_dGFibGU9YmxvY2smc3BhY2VJZD04N2NmOTdjZS05OTQ2LTRjM2QtYTdlMC1hNzkxZWVhMmE0ZTImaWQ9ZjM5OTkwYmUtZDYzOC00NDJiLWIwZGEtMTgzN2ZjYzAyNzcxJmNhY2hlPXYyJndpZHRoPTE0MTY=)

## Limitations

- When using JavaScript implementation, your plugins are run on a sandboxed browser environment. Some JavaScript features may not be available.

- In TypingMind personal version, your plugins can send HTTP requests to external services, however, the destination server must be configured to allow CORS requests from Typing Mind. If CORS requests are not allowed, you will need an intermediate server to process the requests. Some API servers allow CORS requests from everywhere – like Perplexity API, or Open AI – so the intermediate server is not needed in these cases.

## Example plugins

Click here to see some example plugins created by the community: