// Screenshots OG cards: node _build/og.js '[["url","out.png"], ...]'
const { chromium } = require('playwright');

(async () => {
  const jobs = JSON.parse(process.argv[2]);
  const browser = await chromium.launch(process.env.CHROME_PATH ? { executablePath: process.env.CHROME_PATH } : {});
  const page = await browser.newPage({ viewport: { width: 1200, height: 630 } });
  for (const [url, out] of jobs) {
    await page.goto(url, { waitUntil: 'networkidle' });
    await page.waitForSelector('body[data-ready]');
    await page.screenshot({ path: out });
  }
  await browser.close();
})();
