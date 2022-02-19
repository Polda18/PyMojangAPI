# PyMojangAPI
Mojang API automation in Python - collection of Python scripts to parse Mojang API JSON

## Usage
There are 4 different Mojang API scripts:
- `mojang_status.py`
- `mojang_username_to_uuid.py`
- `mojang_uuid_to_profile_skin_cape.py`
- `mojang_uuid_to_username_history.py`

### `mojang_status.py`
~~This one simply just checks status. Just run `$ python mojang_status.py` and it will display status of various API servers.
Status is color coded, `down` shows red, `fully operational` shows green and `partially down` shows yellow. Unrecognised
server status shows white.~~

Example:
```
$ python mojang_status.py
API Server `minecraft.net`                        status `down`
API Server `session.minecraft.net`                status `fully operational`
API Server `account.mojang.com`                   status `fully operational`
API Server `authserver.mojang.com`                status `fully operational`
API Server `sessionserver.mojang.com`             status `down`
API Server `api.mojang.com`                       status `fully operational`
API Server `textures.minecraft.net`               status `fully operational`
API Server `mojang.com`                           status `down`
```

#### Update 2022-02-19
Since 2021-10-08, Mojang has closed this service down and is unabailable. So in reaction to that, running
`$ python mojang_status.py` will now display this instead:

```
This service was closed down by Mojang, due to incorrect responses.
Status check was made for a legacy system that is currently not up to date.
```

### `mojang_username_to_uuid.py`
This one checks given username and retrieves Mojang user profile UUID associated with this account.
Run `$ python mojang_username_to_uuid.py <username>` where `<username>` is the username you want to check.

Example #1:
```
$ python mojang_username_to_uuid.py czghost
Username            UUID
--------------------------------------------------------
CZghost             0e428eba-d5ab-4f63-b2ee-1d48d14d6f86
```

Example #2:
```
$ python mojang_username_to_uuid.py karlos3
Username            UUID
--------------------------------------------------------
Karlos3             dd52d47c-3349-4302-b4bd-ac4c768ff731
```

### `mojang_uuid_to_profile_skin_cape.py`
This one fetches skin and cape data from provided user profile UUID. Run `$ python mojang_uuid_to_profile_skin_cape.py <uuid>`
where `<uuid>` is the UUID of the user profile you want to check.

Example #1:
```
$ python mojang_uuid_to_profile_skin_cape.py 0e428eba-d5ab-4f63-b2ee-1d48d14d6f86
Username            UUID
--------------------------------------------------------
CZghost             0e428eba-d5ab-4f63-b2ee-1d48d14d6f86

Texture hash URL prefix: http://textures.minecraft.net/texture/
        If given response is in parenthesis, there is default value

Skin type  : Steve
Skin hash  : fe45072df5ffc38f2fb44f00a6be3851899d86627eade2778c15ec94f186dfd8
Cape hash  : 2340c0e03dd24a11b15a8b33c2a7e9e32abb2051b2481d0ba7defd635ca7a933
```

Example #2:
```
$ python mojang_uuid_to_profile_skin_cape.py dd52d47c-3349-4302-b4bd-ac4c768ff731
Username            UUID
--------------------------------------------------------
Karlos3             dd52d47c-3349-4302-b4bd-ac4c768ff731

Texture hash URL prefix: http://textures.minecraft.net/texture/
        If given response is in parenthesis, there is default value

Skin type  : Steve
Skin hash  : 267f2d141ae588ef5a5889dc06ea8d6b0c334570c1e4dbddb4379762dc7800a2
Cape hash  : 2340c0e03dd24a11b15a8b33c2a7e9e32abb2051b2481d0ba7defd635ca7a933
```

### `mojang_uuid_to_username_history.py`
This one checks username change history of provided user profile UUID. Run `$ python mojang_uuid_to_username_history.py <uuid>`
where `<uuid>` is the UUID of the user profile you want to check.

Example #1:
```
$ python mojang_uuid_to_username_history.py 0e428eba-d5ab-4f63-b2ee-1d48d14d6f86
UUID: 0e428eba-d5ab-4f63-b2ee-1d48d14d6f86

Username                      Change Timestamp
-------------------------------------------------------------------
CZghost                       n/a
```

Example #2:
```
$ python mojang_uuid_to_username_history.py dd52d47c-3349-4302-b4bd-ac4c768ff731
UUID: dd52d47c-3349-4302-b4bd-ac4c768ff731

Username                      Change Timestamp
-------------------------------------------------------------------
Karlos3                       n/a
monthh_                       08th November 2020 15:53:22 UTC
Karlos3                       07th January 2021 17:57:13 UTC
```
