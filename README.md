# MemberList

Red-DiscordBot cog for listing Discord server members and their IDs.

## Commands

| Command | Description |
|---------|-------------|
| `[p]memberids` | List all member IDs in the server (paged, IDs only) |
| `[p]memberinfo` | List all members with IDs, display names, and full usernames (paged) |

### Usage

```
[p]memberids       # Outputs member IDs in backtick format, ~60 per message
[p]memberinfo      # Outputs `ID Display Name (username#0000)` format, ~40 per message
```

## Planned Features

### 📋 Member Export
- `[p]memberexport --format json` — Export all members to a downloadable JSON file
- `[p]memberexport --format csv` — Export all members to a downloadable CSV (ID, username, roles, join date)
- `[p]memberexport --format text` — Export to plain text list
- `[p]memberexport --format embed` — Export in a formatted embed (no paged messages)

### 🔍 Filtering
- `[p]memberids --role "Moderator"` — Filter by role
- `[p]memberids --status online` — Filter by status (online, idle, dnd, offline)
- `[p]memberids --bot` / `--no-bot` — Toggle bot account filtering
- `[p]memberids --nickname` — Include nicknames in output
- `[p]memberids --color` — Output colored text (terminal/console)

### 📊 Stats & Analytics
- `[p]memberstats` — Show server stats (total, online, bots, humans, roles)
- `[p]memberstats --joined-today` — Count members who joined today
- `[p]memberstats --joined-date YYYY-MM-DD` — Count members joined on a specific date
- `[p]memberstats --avatar` — Count members with custom avatars

### 🏷️ Role Management
- `[p]memberids --not-role "VIP"` — Exclude members with a specific role
- `[p]memberids --both-role "Moderator" --any-role "Mod,Helper"` — Complex role filters
- `[p]memberids --oldest-first` / `--newest-first` — Sort by join date

### 🔎 Search & Lookup
- `[p]memberids --search "John"` — Search by username or display name
- `[p]memberids --exact @User` — Exact user match
- `[p]memberids --partial "John"` — Partial name match (fuzzy)

### 📤 Web Integration
- `[p]memberids --channel #log-channel` — Send output to a specific channel instead of current
- `[p]memberids --dm` — DM the list to the command invoker (for privacy)
- `[p]memberids --webhook` — Send to a webhook URL

### 🛡️ Security & Privacy
- `[p]memberids --hide-bot` — Always hide bot accounts (safety option)
- `[p]memberids --require-permission manage_messages` — Require permission to use
- `[p]memberids --private-channel-only` — Restrict to private channels
- `[p]memberids --rate-limit 5` — Set per-user rate limit (messages per minute)

### 🎨 Formatting & Output
- `[p]memberids --plain` — Output plain text (no markdown formatting)
- `[p]memberids --compact` — Output only IDs, no headers or page markers
- `[p]memberids --with-mentions` — Include Discord mentions (`<@ID>`) alongside IDs
- `[p]memberids --with-timestamps` — Include Discord timestamp formatting
- `[p]memberids --linesize 80` — Control characters per line for custom formatting

### 🔌 Integration
- `[p]memberids --copy` — Copy the output to clipboard
- `[p]memberids --save` — Save output to a file in the bot's data folder
- `[p]memberids --upload` — Upload as a file attachment (avoids message limits)
- `[p]memberids --channel #log-channel` — Send output to a specific channel

### 📖 Help
- `[p]help MemberList` — Show command help with examples
