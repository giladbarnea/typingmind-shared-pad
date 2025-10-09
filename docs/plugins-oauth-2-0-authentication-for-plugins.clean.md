[Plugins](https://docs.typingmind.com/plugins)

# OAuth 2.0 Authentication for Plugins

TypingMind Plugins support OAuth 2.0 authentication type. This help plugin developers create plugins that act on behalf of the user using the user’s account.

![Image without caption](https://image-forwarder.notaku.so/aHR0cHM6Ly93d3cubm90aW9uLnNvL2ltYWdlL2h0dHBzJTNBJTJGJTJGcHJvZC1maWxlcy1zZWN1cmUuczMudXMtd2VzdC0yLmFtYXpvbmF3cy5jb20lMkY4N2NmOTdjZS05OTQ2LTRjM2QtYTdlMC1hNzkxZWVhMmE0ZTIlMkZiODA5MWQyNy0yN2Q1LTRlOTItODk2NS1mZGRmMDE3Yjc0NjYlMkZpbWFnZS5wbmc_dGFibGU9YmxvY2smc3BhY2VJZD04N2NmOTdjZS05OTQ2LTRjM2QtYTdlMC1hNzkxZWVhMmE0ZTImaWQ9MTEwN2MzZjEtNzU3YS04MGQ1LTk5Y2UtZDRiNzgxMTFhMjJkJmNhY2hlPXYyJndpZHRoPTE0MTUuOTY4NzU=)

This authentication type make it easy to work with external services that requires OAuth.

Some example plugins you can create using OAuth authentication:

- A Google Calendar plugin that allows the AI to read events from user’s Google calendar.

- A Slack message plugin that all allows the AI to send a message to the user’s Slack channel.

## **Glossary**

|                  |                                                                                                                                                                                                          |
| ---------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Term**         | Description                                                                                                                                                                                              |
| Plugin Developer | The person who create the Google Calendar plugin.                                                                                                                                                        |
| Admin User       | The person who is the admin of a TypingMind instance ( [TypingMind Custom](https://custom.typingmind.com/)), this person have access to the admin panel to create new AI agents and install new plugins. |
| End User         | The person who use the TypingMind instance, chat with the AI models, using the AI agents and plugins created by the Admin users.                                                                         |

💡

**Looking for a step-by-step guide?**

Read our tutorial: [create a Google Calendar plugin with OAuth 2.0](https://docs.typingmind.com/plugins/google-calendar).

## Overview and facts

- Creating a plugin with OAuth requires the plugin developer to setup Authorization URL, Token URL, Scopes, Prompt, Access Type. These parameters are different depending on which OAuth provider is used.

- When install a plugin with OAuth, the plugin will requires setting up OAuth Client ID and OAuth Client Secret. The admin user who install the plugin will need to set this up with their own OAuth app.

- When the plugin is being used by the end users, they will need to authorize first. The authorization process is handled by TypingMind automatically.

- Plugin developer can use the `{OAUTH_PLUGIN_ACCESS_TOKEN}` variable in their plugin source code as a placeholder for the user’s access token. If the user have not authorized or the access token has expired, the variable will hold an empty value.

Here is a diagram of the full flow (excluding the refresh token process):

![Image without caption](https://image-forwarder.notaku.so/aHR0cHM6Ly93d3cubm90aW9uLnNvL2ltYWdlL2h0dHBzJTNBJTJGJTJGcHJvZC1maWxlcy1zZWN1cmUuczMudXMtd2VzdC0yLmFtYXpvbmF3cy5jb20lMkY4N2NmOTdjZS05OTQ2LTRjM2QtYTdlMC1hNzkxZWVhMmE0ZTIlMkY3MWY4M2Q3YS01OWJjLTRiYTAtYTdjNy1iNDA1YTZhNzBjYmIlMkZ0eXBpbmdtaW5kLXBsdWdpbi1vYXV0aC5kcmF3aW8uc3ZnP3RhYmxlPWJsb2NrJnNwYWNlSWQ9ODdjZjk3Y2UtOTk0Ni00YzNkLWE3ZTAtYTc5MWVlYTJhNGUyJmlkPTExMDdjM2YxLTc1N2EtODA4Ny04NTExLWYyOWY2MTIwZjZkZCZjYWNoZT12MiZ3aWR0aD0xNDE1Ljk4NDM3NQ==)

## Refresh Tokens

Access tokens are typically short-lived. A **refresh token** allows new access tokens to be obtained without reauthentication, ensuring a smooth user experience even when access tokens expire quickly (e.g., in one hour).

TypingMind manages refresh tokens internally if they are provided by the OAuth provider. However, **whether a refresh token is issued depends on your OAuth configuration.** To make sure refresh tokens are issued, it is often necessary to set specific parameters:

- **Access Type:** Setting `access_type=offline` to explicitly request a refresh token.

- **Prompt:** Many providers (like Google) only issue a refresh token the first time a user grants consent. Using `prompt=consent` ensures a refresh token is issued even if the user has previously authorized the app.

**Note**: Some OAuth providers automatically issue refresh tokens without requiring `access_type` or `prompt`, while others are strict about these parameters, or expect different values. Always consult the documentation of the specific provider.

Example OAuth Configuration:

```font-medium max-w-screen-2xl

json"oauthConfig": {
	  "scopes": "https://www.googleapis.com/auth/calendar.readonly",
	  "tokenURL": "https://oauth2.googleapis.com/token",
	  "contentType": "json",
	  "authorizationURL": "https://accounts.google.com/o/oauth2/v2/auth",
	  "prompt": "consent",
	  "accessType": "offline"
}
```

![Image without caption](https://image-forwarder.notaku.so/aHR0cHM6Ly93d3cubm90aW9uLnNvL2ltYWdlL2h0dHBzJTNBJTJGJTJGaW1hZ2UtZm9yd2FyZGVyLm5vdGFrdS5zbyUyRmFIUjBjSE02THk5bWFXeGxMbTV2ZEdsdmJpNXpieTltTDJZdk9EZGpaamszWTJVdE9UazBOaTAwWXpOa0xXRTNaVEF0WVRjNU1XVmxZVEpoTkdVeUx6QTVZVFExWXpOaUxXVTFPVEl0TkROak9TMDVPR0U1TFdRM056aGlObUZtT1dNeVl5OVlibUZ3Y0dWeUxUSXdNalV0TURRdE1qVXRNakV1TXpRdU5UQXVjRzVuUDNSaFlteGxQV0pzYjJOckptbGtQVEZsTURkak0yWXhMVGMxTjJFdE9EQTRNaTA1Tm1abUxXTXdOMlUyWXpVeE1XWXlNaVp6Y0dGalpVbGtQVGczWTJZNU4yTmxMVGs1TkRZdE5HTXpaQzFoTjJVd0xXRTNPVEZsWldFeVlUUmxNaVpsZUhCcGNtRjBhVzl1VkdsdFpYTjBZVzF3UFRFM05UWXpORFkwTURBd01EQW1jMmxuYm1GMGRYSmxQV2hpYVdGTVZEQnBVSHBsTFMxRVQzSkRZekE1VFhkRVptZFlNQzFMUXpCVlpHUkdTWE5VY1RKR1JqZyUzRC5wbmclM0Z3b3Jrc3BhY2VJZCUzRDg3Y2Y5N2NlLTk5NDYtNGMzZC1hN2UwLWE3OTFlZWEyYTRlMj90YWJsZT1ibG9jayZzcGFjZUlkPTg3Y2Y5N2NlLTk5NDYtNGMzZC1hN2UwLWE3OTFlZWEyYTRlMiZpZD0xZTA3YzNmMS03NTdhLTgwODItOTZmZi1jMDdlNmM1MTFmMjImY2FjaGU9djImd2lkdGg9MjAw)

## **Shared OAuth Connections**

TypingMind supports **Shared OAuth Connections**, allowing multiple plugins to share a single OAuth configuration. This simplifies plugin management and reduces repetitive OAuth setups, ensuring users only authenticate once across multiple plugins with the same OAuth settings.

**Note:** The Shared OAuth Connections feature is only available in **TypingMind Custom**. It is not available in the TypingMind License version.

### **Key Benefits:**

- **Centralized OAuth Setup**: Admins configure OAuth credentials just once for multiple plugins.

- **Simplified User Experience**: Users authenticate once and gain seamless access across all plugins sharing the OAuth connection.

### **Setup Guide:**

1. **Create a Shared Connection**:

   - Navigate to the Plugins Manager

   - Select the **"Shared OAuth Connections"** tab

   - Click **"Add New Connection"** to create a new OAuth connection

![Image without caption](https://image-forwarder.notaku.so/aHR0cHM6Ly93d3cubm90aW9uLnNvL2ltYWdlL2h0dHBzJTNBJTJGJTJGaW1hZ2UtZm9yd2FyZGVyLm5vdGFrdS5zbyUyRmFIUjBjSE02THk5bWFXeGxMbTV2ZEdsdmJpNXpieTltTDJZdk9EZGpaamszWTJVdE9UazBOaTAwWXpOa0xXRTNaVEF0WVRjNU1XVmxZVEpoTkdVeUx6Y3dPVE0zTlRReExUY3pZVFV0TkRsbVl5MDVOek0yTFROaU9Ea3haamd6TldNeVpTOXBiV0ZuWlM1d2JtY19kR0ZpYkdVOVlteHZZMnNtYVdROU1XVTBOMk16WmpFdE56VTNZUzA0TUdFNUxUazNaRFl0WmpGaFltSmhNak5oTkdReUpuTndZV05sU1dROU9EZGpaamszWTJVdE9UazBOaTAwWXpOa0xXRTNaVEF0WVRjNU1XVmxZVEpoTkdVeUptVjRjR2x5WVhScGIyNVVhVzFsYzNSaGJYQTlNVGMxTmpNME5qUXdNREF3TUNaemFXZHVZWFIxY21VOVp6VnVVRWhtTVdzeVZ6WjFSRkF4ZGtSVlkzcG5RbWg0V0RBNGIzWlBTVXh3UkhkclFXTjNhM05LUlElM0QlM0QucG5nJTNGd29ya3NwYWNlSWQlM0Q4N2NmOTdjZS05OTQ2LTRjM2QtYTdlMC1hNzkxZWVhMmE0ZTI_dGFibGU9YmxvY2smc3BhY2VJZD04N2NmOTdjZS05OTQ2LTRjM2QtYTdlMC1hNzkxZWVhMmE0ZTImaWQ9MWU0N2MzZjEtNzU3YS04MGE5LTk3ZDYtZjFhYmJhMjNhNGQyJmNhY2hlPXYyJndpZHRoPTEzNjQ=)

2. **Configure OAuth Credentials**:

   - Enter necessary details such as Authorization URL, Token URL, Client ID, Client Secret, Scopes, Prompt, and Access Type

![Image without caption](https://image-forwarder.notaku.so/aHR0cHM6Ly93d3cubm90aW9uLnNvL2ltYWdlL2h0dHBzJTNBJTJGJTJGaW1hZ2UtZm9yd2FyZGVyLm5vdGFrdS5zbyUyRmFIUjBjSE02THk5bWFXeGxMbTV2ZEdsdmJpNXpieTltTDJZdk9EZGpaamszWTJVdE9UazBOaTAwWXpOa0xXRTNaVEF0WVRjNU1XVmxZVEpoTkdVeUwyUXdPV05oWkRZNExXSTVPRFF0TkdGaFpTMWhOV0kxTFRJeVlUTXpPVGcyT0RFeE1DOXBiV0ZuWlM1d2JtY19kR0ZpYkdVOVlteHZZMnNtYVdROU1XVTBOMk16WmpFdE56VTNZUzA0TURSaExUZ3hNemt0WTJNNVpqSm1PRE00TVdRNEpuTndZV05sU1dROU9EZGpaamszWTJVdE9UazBOaTAwWXpOa0xXRTNaVEF0WVRjNU1XVmxZVEpoTkdVeUptVjRjR2x5WVhScGIyNVVhVzFsYzNSaGJYQTlNVGMxTmpNME5qUXdNREF3TUNaemFXZHVZWFIxY21VOWFXRk5XbWhSVDFad2JVUm1VbUpZY0ZaNWQyOHpiaTFrTUZsbmRrZG5TbU54YWpGaWREVTVNbFo1UVElM0QlM0QucG5nJTNGd29ya3NwYWNlSWQlM0Q4N2NmOTdjZS05OTQ2LTRjM2QtYTdlMC1hNzkxZWVhMmE0ZTI_dGFibGU9YmxvY2smc3BhY2VJZD04N2NmOTdjZS05OTQ2LTRjM2QtYTdlMC1hNzkxZWVhMmE0ZTImaWQ9MWU0N2MzZjEtNzU3YS04MDRhLTgxMzktY2M5ZjJmODM4MWQ4JmNhY2hlPXYyJndpZHRoPTI0MDA=)

3. **Apply Shared OAuth to Plugins**:

   - Edit the desired plugin

   - Under the **"Authentication"** section, select **OAuth 2.0**

   - Choose your **"OAuth Configuration Source"** from the dropdown menu, selecting your newly created shared OAuth connection

   - Plugin credentials will automatically apply from the shared connection—no further setup required

![Image without caption](https://image-forwarder.notaku.so/aHR0cHM6Ly93d3cubm90aW9uLnNvL2ltYWdlL2h0dHBzJTNBJTJGJTJGaW1hZ2UtZm9yd2FyZGVyLm5vdGFrdS5zbyUyRmFIUjBjSE02THk5bWFXeGxMbTV2ZEdsdmJpNXpieTltTDJZdk9EZGpaamszWTJVdE9UazBOaTAwWXpOa0xXRTNaVEF0WVRjNU1XVmxZVEpoTkdVeUwyRTBOamxtTURoa0xUY3laV0l0TkdNMFppMWhPVFV6TFRBellUSmtZVGRrWmpReE9DOXBiV0ZuWlM1d2JtY19kR0ZpYkdVOVlteHZZMnNtYVdROU1XVTBOMk16WmpFdE56VTNZUzA0TURneExXSmxZamN0WldRMFpqVmlNRE5tTlRJMkpuTndZV05sU1dROU9EZGpaamszWTJVdE9UazBOaTAwWXpOa0xXRTNaVEF0WVRjNU1XVmxZVEpoTkdVeUptVjRjR2x5WVhScGIyNVVhVzFsYzNSaGJYQTlNVGMxTmpNME5qUXdNREF3TUNaemFXZHVZWFIxY21VOVgxUjZjRzFrVUdWek9FOXBSR3BDT0VoRFowb3RaV3h6U3pWamEzUnVWakZxUlRkb1dXRm1hbTFKWnclM0QlM0QucG5nJTNGd29ya3NwYWNlSWQlM0Q4N2NmOTdjZS05OTQ2LTRjM2QtYTdlMC1hNzkxZWVhMmE0ZTI_dGFibGU9YmxvY2smc3BhY2VJZD04N2NmOTdjZS05OTQ2LTRjM2QtYTdlMC1hNzkxZWVhMmE0ZTImaWQ9MWU0N2MzZjEtNzU3YS04MDgxLWJlYjctZWQ0ZjViMDNmNTI2JmNhY2hlPXYyJndpZHRoPTEzNjMuOTg0Mzc1)

![Image without caption](https://image-forwarder.notaku.so/aHR0cHM6Ly93d3cubm90aW9uLnNvL2ltYWdlL2h0dHBzJTNBJTJGJTJGaW1hZ2UtZm9yd2FyZGVyLm5vdGFrdS5zbyUyRmFIUjBjSE02THk5bWFXeGxMbTV2ZEdsdmJpNXpieTltTDJZdk9EZGpaamszWTJVdE9UazBOaTAwWXpOa0xXRTNaVEF0WVRjNU1XVmxZVEpoTkdVeUwyVTNOakF6TmpCaExXSXlaRGd0TkdZek1pMWlaR00yTFRBM1kySTRPRGM0TkRObFppOXBiV0ZuWlM1d2JtY19kR0ZpYkdVOVlteHZZMnNtYVdROU1XVTBOMk16WmpFdE56VTNZUzA0TURFeExXSTBabUl0WTJJd05XRXhOR1kxWkRFMUpuTndZV05sU1dROU9EZGpaamszWTJVdE9UazBOaTAwWXpOa0xXRTNaVEF0WVRjNU1XVmxZVEpoTkdVeUptVjRjR2x5WVhScGIyNVVhVzFsYzNSaGJYQTlNVGMxTmpNME5qUXdNREF3TUNaemFXZHVZWFIxY21VOVZsWkJWMlJKYm5wSGFDMWxWWEJzZVd4RlZGOXNMVnBOVjNRME1XRkpTM2RuVVdKblQwdzBiMWhvWnclM0QlM0QucG5nJTNGd29ya3NwYWNlSWQlM0Q4N2NmOTdjZS05OTQ2LTRjM2QtYTdlMC1hNzkxZWVhMmE0ZTI_dGFibGU9YmxvY2smc3BhY2VJZD04N2NmOTdjZS05OTQ2LTRjM2QtYTdlMC1hNzkxZWVhMmE0ZTImaWQ9MWU0N2MzZjEtNzU3YS04MDExLWI0ZmItY2IwNWExNGY1ZDE1JmNhY2hlPXYyJndpZHRoPTEzNjMuOTg0Mzc1)

### **Built-in OAuth Plugins:**

- Built-in plugins provided by the system come with predefined OAuth settings and cannot be directly modified.

- To apply a shared OAuth connection:

  - Duplicate the built-in plugin
  - Edit your duplicated plugin to select the shared OAuth connection

## OAuth in the TypingMind License version

If you are using the license version (individual version) at www.typingmind.com, everything is almost the same with some important difference:

- You must provide the OAuth app by your own before using the plugin. You are acting as both admin user and end user (because there is no admin user in the TypingMind license version).

- When authenticating, all steps of the [OAuth authentication flow](https://oauth.net/2/) is run on the client side (your browser). The TypingMind license version does not have a server or a backend. Note that some OAuth providers may not allow this behavior. We tested the OAuth flow of Google and it seems to work on the browser side, but some other providers may not.

- The TypingMind License Version is intended for single-user use. We don’t recommend sharing the license version to other users as they will have access to your OAuth Client Secret, which is not secure.

- To share access to other users in a secure way, please use **[TypingMind Custom](https://custom.typingmind.com/)**.

💡

TypingMind License Version does not have a built-in OAuth app for plugins. This is because having an OAuth app means that we (TypingMind) will have access to your Google account after you authorize, and we don’t want to have access your data.

We are committed to make TypingMind License Version a truly static web app where all of your data is only stored locally on your device. By using your own OAuth credentials, you can still use all of the OAuth features without giving await access to your data.

[Server Side vs. Client Side Plugin](https://docs.typingmind.com/plugins/server-side-vs.-client-side-plugin)

[Create a Plugin Server URL](https://docs.typingmind.com/plugins/create-a-plugin-server-url)