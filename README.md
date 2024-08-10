# leetcode

## How to connect github with leetcode

https://vjnvisakh.medium.com/leetcode-to-github-sync-acdeffedd8f8

## Issues you may have

### Allow Repo secreats variables permission

Go to REPO > settings > actions and in Workflow Permissions section give actions Read and Write permissions. (At the page end)

### Can not build the project due to below error

If you're coping the seesion and csrftoken from `https://leetcode-cn.com`, plz change to `https://leetcode.com`

```yml

Warning: Unexpected input(s) 'verbose', 'commit-header', valid inputs are ['github-token', 'leetcode-csrf-token', 'leetcode-session', 'filter-duplicate-secs', 'destination-folder'] Run joshcai/leetcode-sync@v1.5 [Sat, 10 Aug 2024 06:53:41 GMT] Getting submission from LeetCode, offset 0 [Sat, 10 Aug 2024 06:53:41 GMT] Error: Request failed with status code 401 at createError (/home/runner/work/_actions/joshcai/leetcode-sync/v1.5/node_modules/axios/lib/core/createError.js:16:15) at settle (/home/runner/work/_actions/joshcai/leetcode-sync/v1.5/node_modules/axios/lib/core/settle.js:17:12) at IncomingMessage.handleStreamEnd (/home/runner/work/_actions/joshcai/leetcode-sync/v1.5/node_modules/axios/lib/adapters/http.js:269:11) at IncomingMessage.emit (node:events:531:35) at endReadableNT (node:internal/streams/readable:1696:12) at process.processTicksAndRejections (node:internal/process/task_queues:82:21)
```
