## Paper Trail
### 50 points, 636 solves

`Something is suspicious about defund's math papers. See if you can find anything in the `<a href='https://files.actf.co/8e1122c1c15f2373fb6e98c207c3218ecd322796a2e2275f4b99e7bb21b9e253/paper_trail.pcapng'>network packets</a>` we've intercepted from his computer.`

`Author: defund`

Downloading the pcapng and opening it in wireshark, we can see a bunch of IRC and TCP protocol packets. The IRC packets appear to have a conversation over IRC between defund and himself. Feels bad man. Filtering by IRC:

<IMG SRC='https://cdn.discordapp.com/attachments/532350033241309226/571735101151510528/unknown.png'>

Starting from the highlighted packet, defund sends a single letter. Every packet with a length of 85 continues this pattern, so going through them (filter is '`frame.len == 85`') we can build up the flag.

flag: `actf{fake_math_papers}`
