Render Deployment Checklist for student-system

1) Render service setup
- Repository: connect to your GitHub repo
- Branch: main (or whichever branch you use for deployment)
- Root Directory (Build Context): set to the repository root (recommended for current Dockerfile)
- Dockerfile Path: `frontend/Dockerfile`
- Environment: set the following environment variables (Build & Runtime where applicable):
  - `VITE_API_BASE_URL` (value: your API base URL)
- Port: 80 (nginx listens on 80)

2) Build and cache
- When making Dockerfile or related file changes, use "Clear Cache & Deploy" in Render to force a full rebuild
- If using Render's build logs, search for the first error message (it is usually the root cause)

3) Local reproduction
- From repo root (this matches the Dockerfile that expects `frontend/` relative paths):
  - docker build --no-cache -f frontend/Dockerfile -t student-frontend .
- Alternative (use `frontend` as build context):
  - docker build -t student-frontend frontend/
- Run locally for quick check:
  - docker run --rm -p 8080:80 student-frontend
  - curl http://localhost:8080

4) Inspect build context and files
- Ensure `frontend/package.json` and `frontend/nginx.conf` exist in repo.
- Ensure no `.dockerignore` excludes `frontend/` or the files used by Dockerfile (there is no `.dockerignore` in this repo by default).
- If a file is missing during build, temporarily add a debug step in the Dockerfile before `npm install`:
  - RUN ls -la /app || true
  - This prints directory contents to build log to help debug missing files on Render.

5) Common failure modes and fixes
- "Could not read package.json: ENOENT" → fix: `COPY frontend/package*.json ./` (done)
- "/nginx.conf: not found" → ensure `COPY frontend/nginx.conf /etc/nginx/conf.d/default.conf` or adjust build Root Directory
- Build succeeds locally but fails on Render → likely cache or Root Directory mismatch; clear cache and confirm Dockerfile path and build context in Render settings

6) Optional: Make Dockerfile robust
- Ensure `package-lock.json` is copied: `COPY frontend/package*.json ./` already matches both `package.json` and `package-lock.json`.
- Consider adding `RUN npm ci --production` (or `npm ci`) depending on your needs.

7) Logs to provide when asking for help
- Full build log from Render (not just the error snippet)
- If local build fails, the full `docker build` output (use `--no-cache`) and terminal output

8) Quick checklist to run before deploy
- [ ] Dockerfile at `frontend/Dockerfile` points to `frontend/...` paths (or change Root Directory to `frontend/` and remove `frontend/` prefixes)
- [ ] `frontend/package.json` present and has `build` script
- [ ] `frontend/nginx.conf` present and correct
- [ ] Env var `VITE_API_BASE_URL` set in Render
- [ ] Clear cache & deploy

If you want, I can:
- Add a temporary debug `RUN ls -la /app` to the Dockerfile to collect build-time file listings on Render (I will revert it afterwards), or
- Help you run the `docker build --no-cache -f frontend/Dockerfile -t student-frontend .` command locally and analyze the output if you paste the logs here.

---
