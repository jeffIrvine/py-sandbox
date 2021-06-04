const {Builder, By, Key, until, WebDriver} = require('selenium-webdriver');

const scrape = async () => {
  const PATH = "C:\Program Files (x86)\chromedriver.exe"
  const driver = WebDriver.Chrome(PATH);
  await driver.get('https://store.hermanmiller.com/');
}

scrape()