# Technical Details

## Patching the APK

### Changing server URIs
Relevant server hostnames can be found in these files:
- smali_classes2/com/kakao/sdk/partner/model/PhasedServerHosts.smali
  - kapi: `kapi.kakao.com`
  - kauth: `kauth.kakao.com`
- smali_classes2/com/kakaogame/config/ConfigLoader.smali
  - infodesk: `https://infodesk-zinny3.game.kakao.com` (kr), `https://gc-infodesk-zinny3.game.kakao.com` (global)
  - session: `wss://session-zinny3.game.kakao.com` (kr), `wss://gc-session-zinny3.kakaogames.com` (global)
  - openapi: `https://openapi-zinny3.game.kakao.com` (kr), `https://gc-openapi-zinny3.kakaogames.com` (global)

Other server URIs (e.g. cdn, game) are provided by [the infodesk response to /v2/app](krdori/servers/kakao_server.py). 

All of these hostnames can be changed into IP addresses. Ports can be added at the end of these hostnames. For kapi and kauth, change both occurrences of `->authority(` to `->encodedAuthority(` in smali_classes2/com/kakao/sdk/auth/UriUtility.smali so that the `:` between hostname and port is not converted into `%3a`. For session server, the default port number 443 (`0x1bb` in hex) needs be changed inside smali_classes3/com/kakaogame/session/websocket/WebSocketClient.smali as well.

Changing the URI schemes to their corresponding insecure variants (e.g. https to http) can be done directly for URIs that are specified in full. For kapi and kauth, change `"https"` to `"http"` in these files:
- smali_classes2/com/kakao/sdk/auth/UriUtility.smali (two occurrences of `"https"`)
- smali_classes2/com/kakao/sdk/auth/network/ApiFactoryKt$kapiWithOAuth$2.smali
- smali_classes2/com/kakao/sdk/auth/network/ApiFactoryKt$kauth$2.smali

If the URI scheme for session server is changed from wss to ws, the default port number now becomes 80 (`0x50` in hex). Changing the session server port number now requires changing this value in smali_classes3/com/kakaogame/session/websocket/WebSocketClient.smali.

### Changing the Kakao custom scheme
When the APK requests an oauth token from the servers, it opens a browser that redirects to a URI in this format:
```
kakaodbd722857fec44d74100673ff569c5a6://oauth?code=XXXXXXX
```
This is known as [deep linking](https://developer.android.com/training/app-links/deep-linking). If multiple versions of the APK are installed (e.g. having both the original and modded versions installed) and they can handle the same URI, the user will be asked to select which app to use. To prevent this, the local server uses this URI instead:
```
kakao00000000000000000000000000000000://oauth?code=XXXXXXX
```

Mod these files to use this new scheme:
- asset/kakao_game_sdk_configuration.xml

  change `dbd722857fec44d74100673ff569c5a6` to `00000000000000000000000000000000`

- res/values/strings.xml

  change `kakaodbd722857fec44d74100673ff569c5a6` to `kakao00000000000000000000000000000000`

### Fixing the non-compliant WebSocket HTTP header
The HTTP header of the WebSocket session requests made by the APK contains a line that ends with "\n" instead of "\r\n", which refuses to work with certain WebSocket server implementations such as Python's [websockets](https://websockets.readthedocs.io/en/stable/). To fix this issue, the following changes need to be made in smali_classes3/com/kakaogame/session/websocket/WebSocketClient.smali:
- replace `"\n                                Host: "` with `"Host: "`
- replace `"\n                                \n                                "` with `"\r\n"`
- delete these consecutive lines:
```
            .line 74
            invoke-static {v5}, Lkotlin/text/StringsKt;->trimIndent(Ljava/lang/String;)Ljava/lang/String;

            move-result-object v5
```
