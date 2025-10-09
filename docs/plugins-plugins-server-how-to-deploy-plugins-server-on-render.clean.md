[Plugins](https://docs.typingmind.com/plugins)

[Create a Plugin Server URL](https://docs.typingmind.com/plugins/create-a-plugin-server-url)

# How to deploy Plugins Server on Render

**Plugins Server** provides a proxy server for [Typing Mind's Plugins](https://docs.typingmind.com/plugins). A proxy server is needed for complex use cases where a server is required for processing data that cannot be done from the client side in Typing Mind.

Plugins Server is open-source. See the code on GitHub: [https://github.com/TypingMind/plugins-server](https://github.com/TypingMind/plugins-server)

On this page, we’ll guide you on how to deploy the Plugins Server on Render.com. You can deploy on any other hosting providers you want, the steps are almost identical.

## **Step-by-Step Guide**

1. **Make a Home on Render:**

   - Go to Render's website and create your free account.

   - Click to create a new "Web Service"

![Image without caption](https://image-forwarder.notaku.so/aHR0cHM6Ly93d3cubm90aW9uLnNvL2ltYWdlL2h0dHBzJTNBJTJGJTJGcHJvZC1maWxlcy1zZWN1cmUuczMudXMtd2VzdC0yLmFtYXpvbmF3cy5jb20lMkY4N2NmOTdjZS05OTQ2LTRjM2QtYTdlMC1hNzkxZWVhMmE0ZTIlMkY4ODFmYjZhOC00MWE3LTRjZGYtYjgxZS04YjY1MWQzZmM5NzElMkZTY3JlZW5zaG90XzIwMjQtMDMtMTVfYXRfMDkuMTYuMTYucG5nP3RhYmxlPWJsb2NrJnNwYWNlSWQ9ODdjZjk3Y2UtOTk0Ni00YzNkLWE3ZTAtYTc5MWVlYTJhNGUyJmlkPTUzZDA4MjMxLWM2ZjgtNDdhYS1iYmM0LTdmZjNlOGI2OTcwOCZjYWNoZT12MiZ3aWR0aD0xMzA3LjkzNzU=)

   - on the next screen enter the URL of the TypingMind plugin repository `https://github.com/TypingMind/plugins-server` to continue

![Image without caption](https://image-forwarder.notaku.so/aHR0cHM6Ly93d3cubm90aW9uLnNvL2ltYWdlL2h0dHBzJTNBJTJGJTJGcHJvZC1maWxlcy1zZWN1cmUuczMudXMtd2VzdC0yLmFtYXpvbmF3cy5jb20lMkY4N2NmOTdjZS05OTQ2LTRjM2QtYTdlMC1hNzkxZWVhMmE0ZTIlMkYyZjVkZmE1My0wZGUwLTQ5ODktYjIyMS04ZDQ5OGYyMTk1ZTQlMkZjcmVhdGVfbmV3LnBuZz90YWJsZT1ibG9jayZzcGFjZUlkPTg3Y2Y5N2NlLTk5NDYtNGMzZC1hN2UwLWE3OTFlZWEyYTRlMiZpZD1kMjNmYWEyZC04ZWUwLTQ3YzItYTk5YS02Y2NlYzZiOGY5MjYmY2FjaGU9djImd2lkdGg9MjQwMA==)

2. **Make sure the value looks right**

   - The project requires configuration settings. The **Branch** should be set to `main`, **Runtime** to `Docker`. You may set the region to any desired region.

![Image without caption](https://image-forwarder.notaku.so/aHR0cHM6Ly93d3cubm90aW9uLnNvL2ltYWdlL2h0dHBzJTNBJTJGJTJGcHJvZC1maWxlcy1zZWN1cmUuczMudXMtd2VzdC0yLmFtYXpvbmF3cy5jb20lMkY4N2NmOTdjZS05OTQ2LTRjM2QtYTdlMC1hNzkxZWVhMmE0ZTIlMkYzZWZlYTQzNy04YzY3LTRmMzUtYWZiZi00Y2FmNjc1MWIwNmYlMkZzZXR0aW5nLnBuZz90YWJsZT1ibG9jayZzcGFjZUlkPTg3Y2Y5N2NlLTk5NDYtNGMzZC1hN2UwLWE3OTFlZWEyYTRlMiZpZD01ZjNjZDQ4Zi0xYmFmLTQyNTYtOTVhOC04MWMyYWU3MTJkYTMmY2FjaGU9djImd2lkdGg9MTMwNy45Njg3NQ==)

   - There is no requirement to include environment variables.

⚠️

**If you are using a free tier hosting, your server may sleep when not in use which can cause a delay of up to 30 seconds for the first request.**
**You can visit the link below to check your free usage.**

[Cloud Application Hosting for Developers \| Render\\
\\
Render is a unified cloud to build and run all your apps and websites with free SSL, global CDN, private networks and automatic deploys from Git.\\
\\
https://dashboard.render.com/billing#free-usage\\
\\
![Cloud Application Hosting for Developers | Render](https://render.com/og-img.png)](https://dashboard.render.com/billing#free-usage)

3. **Complete the deployment process.**

   - Look for the "Create Web Service" button on Render. Click it and wait a little bit – it's building your project!

![Image without caption](https://image-forwarder.notaku.so/aHR0cHM6Ly93d3cubm90aW9uLnNvL2ltYWdlL2h0dHBzJTNBJTJGJTJGcHJvZC1maWxlcy1zZWN1cmUuczMudXMtd2VzdC0yLmFtYXpvbmF3cy5jb20lMkY4N2NmOTdjZS05OTQ2LTRjM2QtYTdlMC1hNzkxZWVhMmE0ZTIlMkY0NjRmMWIxMC0zNDQ2LTRmNDctYTg4ZS0yZmY4Nzc0OGI0ZDklMkZ1cmwucG5nP3RhYmxlPWJsb2NrJnNwYWNlSWQ9ODdjZjk3Y2UtOTk0Ni00YzNkLWE3ZTAtYTc5MWVlYTJhNGUyJmlkPWViOWY5OTU4LTY0YzktNDZhNy1hZDFlLWYxY2NhMDlkZDI1ZCZjYWNoZT12MiZ3aWR0aD0xMzE1Ljk2ODc1)

🚨

You should keep your plugin server URL confidential and manage your server independently. Never share or publish it, as others may misuse it or occupy all of your free tier usage.

4. **Configure the plugin to use your server.**

   - Inside your TypingMind Plugin settings, there's probably a place to put the address of your project that's now live on Render.

![Image without caption](https://image-forwarder.notaku.so/aHR0cHM6Ly93d3cubm90aW9uLnNvL2ltYWdlL2h0dHBzJTNBJTJGJTJGcHJvZC1maWxlcy1zZWN1cmUuczMudXMtd2VzdC0yLmFtYXpvbmF3cy5jb20lMkY4N2NmOTdjZS05OTQ2LTRjM2QtYTdlMC1hNzkxZWVhMmE0ZTIlMkZhODQwNWM0YS05OGMwLTQ3NjAtYjU5Zi05NGY3ZjI3MDc5MzclMkZwbHVnaW4ucG5nP3RhYmxlPWJsb2NrJnNwYWNlSWQ9ODdjZjk3Y2UtOTk0Ni00YzNkLWE3ZTAtYTc5MWVlYTJhNGUyJmlkPWI3YjNhNzAwLTEyMWItNGU3OC05NGNmLWVkYmEyYzdhOGRmMyZjYWNoZT12MiZ3aWR0aD0xMzA3LjkzNzU=)

## Need help?

Contact us for support at **support@typingmind.com**

[Create a Plugin Server URL](https://docs.typingmind.com/plugins/create-a-plugin-server-url)

[Interactive Canvas (Artifacts)](https://docs.typingmind.com/plugins/interactive-canvas-(artifacts))