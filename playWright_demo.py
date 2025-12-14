import playwright
import asyncio

from playwright.async_api import async_playwright

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        #context = await browser.new_context()
        page = await browser.new_page()
        await page.goto("https://google.com")
        input_box = await page.wait_for_selector('/html/body/ntp-app//div/div[2]/cr-searchbox//div[1]/input')
        await page.wait_for_timeout(5000)  # wait for 5 seconds
        await input_box.fill("Playwright Python")
        await input_box.press("Enter")
        await page.wait_for_timeout(5000)  # wait for 5 seconds
        print(await page.title())
        await browser.close()

if __name__ == "__main__":
    
    asyncio.run(run())