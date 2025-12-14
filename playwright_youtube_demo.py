# ...existing code...
import asyncio
from playwright.async_api import async_playwright, TimeoutError as PlaywrightTimeoutError

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()

        # Open Google and handle common consent dialogs
        await page.goto("https://www.google.com/ncr")
        try:
            await page.locator('button#L2AGLb').click(timeout=2000)
        except PlaywrightTimeoutError:
            # fallback labels vary by locale
            for label in ("I agree", "Agree", "Accept all", "Accept"):
                try:
                    await page.get_by_role("button", name=label).click(timeout=1000)
                    break
                except PlaywrightTimeoutError:
                    pass

        # Perform the search
        query = "playwright demo video"
        await page.goto(f"https://www.google.com/search?q={query.replace(' ', '+')}")

        await page.wait_for_load_state("networkidle")

        # Optional: switch to the Videos tab (uses the tbm=vid parameter)
        try:
            await page.locator('a[href*="tbm=vid"]').first.click(timeout=3000)
            await page.wait_for_load_state("networkidle")
        except PlaywrightTimeoutError:
            pass

        # Try to click the first YouTube video result, fallback to first result link
        try:
            yt = page.locator('a[href*="youtube.com/watch"]').first
            await yt.wait_for(timeout=5000)
            await yt.click()
        except PlaywrightTimeoutError:
            # fallback: click the first search result link
            first_result = page.locator('div#search a').first
            await first_result.click()

        # Give the page a moment to load the video page
        await page.wait_for_timeout(5000)

        await browser.close()

if __name__ == "__main__":
    asyncio.run(run())
# ...existing code...
