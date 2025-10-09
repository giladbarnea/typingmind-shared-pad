[50+ Advanced ChatGPT Prompts. Get It Free!](https://tdinh.lemonsqueezy.com/checkout/buy/ce5f7418-315e-4e38-85dd-bfaec64eda1e)

[TypingMind Docs](https://docs.typingmind.com/)


[Plugins](https://docs.typingmind.com/plugins)

# Share / Import plugins

Looking to share plugins or import shared plugins? This guide will provide the easiest steps to do so.

## **Share a plugin**

### Share as URL and JSON

1. Open **Plugins**

2. Click on the “ **Share**” button on the top right corner of the plugin (under the three dots menu).

![Image without caption](https://image-forwarder.notaku.so/aHR0cHM6Ly93d3cubm90aW9uLnNvL2ltYWdlL2h0dHBzJTNBJTJGJTJGcHJvZC1maWxlcy1zZWN1cmUuczMudXMtd2VzdC0yLmFtYXpvbmF3cy5jb20lMkY4N2NmOTdjZS05OTQ2LTRjM2QtYTdlMC1hNzkxZWVhMmE0ZTIlMkYzNGEwNDZhNC1iZmM4LTQ5ZWEtOTAyOC1hODE1MGY5NmIxMmElMkZVbnRpdGxlZC5wbmc_dGFibGU9YmxvY2smc3BhY2VJZD04N2NmOTdjZS05OTQ2LTRjM2QtYTdlMC1hNzkxZWVhMmE0ZTImaWQ9YWZmOThkZmQtZDUwNC00YmRiLTk2N2MtOTVlNDg2NjgzZWE4JmNhY2hlPXYyJndpZHRoPTE0MTY=)

3. There will be 2 options to share your plugins:

- Share via a unique URL

- Share as JSON

![Image without caption](https://image-forwarder.notaku.so/aHR0cHM6Ly93d3cubm90aW9uLnNvL2ltYWdlL2h0dHBzJTNBJTJGJTJGcHJvZC1maWxlcy1zZWN1cmUuczMudXMtd2VzdC0yLmFtYXpvbmF3cy5jb20lMkY4N2NmOTdjZS05OTQ2LTRjM2QtYTdlMC1hNzkxZWVhMmE0ZTIlMkZmODcwOGRhMy00Y2Q2LTQ0ZDgtOTBiMi1lOTFjZjU3MmYyN2MlMkZVbnRpdGxlZC5wbmc_dGFibGU9YmxvY2smc3BhY2VJZD04N2NmOTdjZS05OTQ2LTRjM2QtYTdlMC1hNzkxZWVhMmE0ZTImaWQ9NDk3MGQwNWUtMGUyMi00M2RiLTgyYjgtNTg0MmJjOWQxNWJlJmNhY2hlPXYyJndpZHRoPTE0MTY=)

4. Simply copy the generated link/JSON file and share

## Share via GitHub

To share a plugin via GitHub (check [this repo](https://github.com/TypingMind/plugin-stable-diffusion-v2-image) as an example):

1. Create a public repo on GitHub

2. Create 3 files: `README.md` , `implementation.js` and `plugin.json`:

   - `README.md`: plugin overview

   - `implementation.js`: this file contains the JS code, it is only required if you use Javascript code implementation. It must contain a function with the name as same as the id in plugin.json file

   - `plugin.json`: a JSON file containing all configs of the plugin, please check [this guide](https://docs.typingmind.com/plugins/build-a-typingmind-plugin) to understand more. It has the following properties:

     - `version`: number, for other users to notice to update
     - `uuid`: string, this is the unique id to distinguish plugins
     - `iconURL`: string
     - `emoji`: string, this will be used if `iconURL` is not available
     - `title`: string, the displayed name of the plugin
     - `userSettings`: JSON string, check details in [this guide](https://docs.typingmind.com/plugins/build-a-typingmind-plugin#0e3d2ca8c78f4b62b1a8504957bbb268)
     - `openaiSpec`: JSON string, check details in [this guide](https://docs.typingmind.com/plugins/build-a-typingmind-plugin#f75675f108634820be70b39319cafb08)
     - `implementationType`: string, `"http"` or `"javascript"`
     - `httpAction`: JSON string, required if the implementation is HTTP, check details in [this guide](https://docs.typingmind.com/plugins/build-a-typingmind-plugin#f8f5759520614775aaf136c279931e76)

       - `id`: string, uuid preferred
       - `method`: string, the request method
       - `url`: string
       - `hasHeaders`: boolean
       - `requestHeaders`: JSON, required if hasHeaders is true
       - `hasBody`: boolean
       - `requestBody`: JSON, required if hasBody is true
       - `requestBodyFormat`: string, `"json"` or `"form-data"`
       - `hasResultTransform`: boolean
       - `resultTransform`: object, required if hasResultTransform is true, its shape is either of these:

```font-medium max-w-screen-2xl

json{
  "engine": "handlebars",
  "templateString": "string template value"
}
```

```font-medium max-w-screen-2xl

json{
  "engine": "jmes",
  "expression": "string expression value"
}
```

       - `outputType`: string, `"render_markdown"` or `"respond_to_ai"` or `"render_html"`

3. Get the GitHub repo link to share, for example: [https://github.com/TypingMind/stable-diffusion-v2-image](https://github.com/TypingMind/stable-diffusion-v2-image)

## **Import a shared plugin**

Find a plugin you'd like to use? Import it with these easy steps:

### **Import a plugin via URL**

To import a plugin using its URL, follow these steps:

1. Open **Plugins**

2. Click on the “ **Import plugins”** button.

3. Paste the plugin URL into the designated field to import the plugin.

![Image without caption](https://image-forwarder.notaku.so/aHR0cHM6Ly93d3cubm90aW9uLnNvL2ltYWdlL2h0dHBzJTNBJTJGJTJGcHJvZC1maWxlcy1zZWN1cmUuczMudXMtd2VzdC0yLmFtYXpvbmF3cy5jb20lMkY4N2NmOTdjZS05OTQ2LTRjM2QtYTdlMC1hNzkxZWVhMmE0ZTIlMkZjNWYyZGUzNS0wNDAxLTQwNzgtYTEzMi0wOGFlZDVkZmI3Y2QlMkZVbnRpdGxlZC5wbmc_dGFibGU9YmxvY2smc3BhY2VJZD04N2NmOTdjZS05OTQ2LTRjM2QtYTdlMC1hNzkxZWVhMmE0ZTImaWQ9MDU1ZTViMGQtNWE1MC00NDVjLWE4YWItYjhkMTMxMDE0Yzk0JmNhY2hlPXYyJndpZHRoPTI0MDA=)

### Import a plugin via GitHub URL

To import a plugin using its URL, follow these steps:

1. Open **Plugins**

2. Click on the “ **Import plugins”** button.

3. Paste the plugin Github URL into the designated field to import the plugin.

![Image without caption](https://image-forwarder.notaku.so/aHR0cHM6Ly93d3cubm90aW9uLnNvL2ltYWdlL2h0dHBzJTNBJTJGJTJGcHJvZC1maWxlcy1zZWN1cmUuczMudXMtd2VzdC0yLmFtYXpvbmF3cy5jb20lMkY4N2NmOTdjZS05OTQ2LTRjM2QtYTdlMC1hNzkxZWVhMmE0ZTIlMkY0NTIzNDc5NS01N2Y5LTQzNzgtYjJlZi04NDgxNWEwZDMyOWQlMkZVbnRpdGxlZC5wbmc_dGFibGU9YmxvY2smc3BhY2VJZD04N2NmOTdjZS05OTQ2LTRjM2QtYTdlMC1hNzkxZWVhMmE0ZTImaWQ9NWI2ZGRjMWQtNWVlZS00ZjA3LTk2YTMtNjdmZGIxMTUzZWEwJmNhY2hlPXYyJndpZHRoPTE0MTY=)

### Import a plugin from a private GitHub repo

1. Generate a new GitHub personal access token ( [https://github.com/settings/tokens?type=beta](https://github.com/settings/tokens?type=beta)). There are 2 types of tokens:

1. Fine-grained token (Recommended): Select that private repo and set **Contents** permission to **Read-only**

![Image without caption](https://image-forwarder.notaku.so/aHR0cHM6Ly93d3cubm90aW9uLnNvL2ltYWdlL2h0dHBzJTNBJTJGJTJGcHJvZC1maWxlcy1zZWN1cmUuczMudXMtd2VzdC0yLmFtYXpvbmF3cy5jb20lMkY4N2NmOTdjZS05OTQ2LTRjM2QtYTdlMC1hNzkxZWVhMmE0ZTIlMkY4ODJkYzc5Ni02OGNlLTRjNGItYmVhMS1hMDE3MGIwM2VmMmIlMkZYbmFwcGVyLTIwMjQtMDktMTUtMTAuMjIuMDEucG5nP3RhYmxlPWJsb2NrJnNwYWNlSWQ9ODdjZjk3Y2UtOTk0Ni00YzNkLWE3ZTAtYTc5MWVlYTJhNGUyJmlkPWNiMmQ5YWFlLWZiNmYtNGQ2ZS1iYWU2LWZiNjE1YjhmZDQ2ZiZjYWNoZT12MiZ3aWR0aD0xMzA0)

![Image without caption](https://image-forwarder.notaku.so/aHR0cHM6Ly93d3cubm90aW9uLnNvL2ltYWdlL2h0dHBzJTNBJTJGJTJGcHJvZC1maWxlcy1zZWN1cmUuczMudXMtd2VzdC0yLmFtYXpvbmF3cy5jb20lMkY4N2NmOTdjZS05OTQ2LTRjM2QtYTdlMC1hNzkxZWVhMmE0ZTIlMkYzNzZkMTg0Yi1kYTNmLTRlZDktODgwNC0yNGQ0OWE2ZTYzZTAlMkZYbmFwcGVyLTIwMjQtMDktMTUtMTAuMjIuNTcucG5nP3RhYmxlPWJsb2NrJnNwYWNlSWQ9ODdjZjk3Y2UtOTk0Ni00YzNkLWE3ZTAtYTc5MWVlYTJhNGUyJmlkPTU1ZGVmMWZiLTNlYzUtNDZlOS04YzU5LWQxOTA3YTA0OWVkMiZjYWNoZT12MiZ3aWR0aD0xMzYw)

b. Classic token: select the scope **repo**

![Image without caption](https://image-forwarder.notaku.so/aHR0cHM6Ly93d3cubm90aW9uLnNvL2ltYWdlL2h0dHBzJTNBJTJGJTJGcHJvZC1maWxlcy1zZWN1cmUuczMudXMtd2VzdC0yLmFtYXpvbmF3cy5jb20lMkY4N2NmOTdjZS05OTQ2LTRjM2QtYTdlMC1hNzkxZWVhMmE0ZTIlMkYzMGMyYjg2My02ZThmLTQ5NDEtYmU4ZC05NmZhNzQyYzhmMzQlMkZYbmFwcGVyLTIwMjQtMDktMTUtMTAuMzEuMzYucG5nP3RhYmxlPWJsb2NrJnNwYWNlSWQ9ODdjZjk3Y2UtOTk0Ni00YzNkLWE3ZTAtYTc5MWVlYTJhNGUyJmlkPWNjZTQ5MDYyLTgwY2UtNDNjZC1hZGNmLTJlM2Y5ZTAxZjFhNiZjYWNoZT12MiZ3aWR0aD0xMzYw)

2. Attach the query `?token=[the-generated-token]` to the URL, for example: [https://github.com/TypingMind/plugin-stable-diffusion-v2-image?token=github\_pat\_xxxxxx](https://github.com/TypingMind/plugin-stable-diffusion-v2-image)

### Import via JSON file

- Create new plugin

- Choose **Import plugin from JSON**

![Image without caption](https://image-forwarder.notaku.so/aHR0cHM6Ly93d3cubm90aW9uLnNvL2ltYWdlL2h0dHBzJTNBJTJGJTJGcHJvZC1maWxlcy1zZWN1cmUuczMudXMtd2VzdC0yLmFtYXpvbmF3cy5jb20lMkY4N2NmOTdjZS05OTQ2LTRjM2QtYTdlMC1hNzkxZWVhMmE0ZTIlMkZlMGFmYWM3NC00ZWMwLTQ4MDctYjQ2OS0wZDRlNDFkMGI4YWMlMkZVbnRpdGxlZC5wbmc_dGFibGU9YmxvY2smc3BhY2VJZD04N2NmOTdjZS05OTQ2LTRjM2QtYTdlMC1hNzkxZWVhMmE0ZTImaWQ9YjJiNWIxYzEtOWIwMS00MWVjLWE1NjEtNjdkZjA4YjIxY2Q1JmNhY2hlPXYyJndpZHRoPTE0MTY=)

### **Direct Plugin Import**

Another way of importing a shared plugin is to use a direct import. Here's how:

1. Click on the shared plugin link that you've received.

2. Click the “ **Import to TypingMind**” button to import to the app and use it effortlessly

![Image without caption](https://image-forwarder.notaku.so/aHR0cHM6Ly93d3cubm90aW9uLnNvL2ltYWdlL2h0dHBzJTNBJTJGJTJGcHJvZC1maWxlcy1zZWN1cmUuczMudXMtd2VzdC0yLmFtYXpvbmF3cy5jb20lMkY4N2NmOTdjZS05OTQ2LTRjM2QtYTdlMC1hNzkxZWVhMmE0ZTIlMkZjODc4M2Q4Yi1iYTM5LTQ0ZmItOGMzYy1hMmFhNzg2YTczNTAlMkZVbnRpdGxlZC5wbmc_dGFibGU9YmxvY2smc3BhY2VJZD04N2NmOTdjZS05OTQ2LTRjM2QtYTdlMC1hNzkxZWVhMmE0ZTImaWQ9ZjYxMjE2NzgtMmEwZS00NjVlLWJiOWEtMDMzYmMxM2QzYmQ5JmNhY2hlPXYyJndpZHRoPTE0MTY=)

[User-contributed Plugins](https://docs.typingmind.com/plugins/user-contributed-plugins)

[Server Side vs. Client Side Plugin](https://docs.typingmind.com/plugins/server-side-vs.-client-side-plugin)

* * *

Powered by[Notaku](https://notaku.so/)

Helpful?

Share

[share on twitter](https://twitter.com/intent/tweet?text=Share+%2F+Import+plugins%0Ahttps%3A%2F%2Fdocs.typingmind.com%2Fplugins%2Fshare-import-plugins)[share on facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fdocs.typingmind.com%2Fplugins%2Fshare-import-plugins)[share on linkedin](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fdocs.typingmind.com%2Fplugins%2Fshare-import-plugins)

Content

[Share / Import plugins](https://docs.typingmind.com/plugins/share-import-plugins#cb8b4262bde441ac9d978ef9f63e9a16)

[Share a plugin](https://docs.typingmind.com/plugins/share-import-plugins#f877a897f95e4c27b892b312e19c36ac)

[Share as URL and JSON](https://docs.typingmind.com/plugins/share-import-plugins#97ab2fede8e4438190781fbd4046ee09)

[Share via GitHub](https://docs.typingmind.com/plugins/share-import-plugins#119162039fe64399bde56d420bf47798)

[Import a shared plugin](https://docs.typingmind.com/plugins/share-import-plugins#ff9bdca2f0d3459bbf0a4ccef47745ac)

[Import a plugin via URL](https://docs.typingmind.com/plugins/share-import-plugins#6f8a369d930a4a5290f2a2b6c5e8da59)

[Import a plugin via GitHub URL](https://docs.typingmind.com/plugins/share-import-plugins#d6857690fda44d93aceadd36f8643da8)

[Import a plugin from a private GitHub repo](https://docs.typingmind.com/plugins/share-import-plugins#3ac5f4d70ce84e3884b05375b60bc243)

[Import via JSON file](https://docs.typingmind.com/plugins/share-import-plugins#0dadfa78b78e4541ba2a90326a535fa8)

[Direct Plugin Import](https://docs.typingmind.com/plugins/share-import-plugins#c63fcc37911b4507be47d83b81a06e82)

![](https://www.typingmind.com/logo.png)

👋 Questions? Chat with our AI!×
