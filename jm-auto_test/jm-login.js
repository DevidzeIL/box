WDS.sampleResult.sampleStart();

var httpProtocol = 'https://';
var mainHost = 'devonshopnew.mileonair.com';
var testPath = '/login';

WDS.browser.get(httpProtocol + mainHost + testPath);
java.util.concurrent.TimeUnit.SECONDS.sleep(1);

// ------------------------------------------------------------------------

// var phoneInput = WDS.browser.findElement(org.openqa.selenium.By.xpath('//div/main/div/div/div[2]/div/div/div/div[1]/input'));
// phoneInput.sendKeys("9777751713");
java.util.concurrent.TimeUnit.SECONDS.sleep(5);

var getBtn = WDS.browser.findElement(org.openqa.selenium.By.xpath('//div/main/div/div/div[2]/div/div/div/div[4]/button'));
getBtn.click();
java.util.concurrent.TimeUnit.SECONDS.sleep(3);

var codeInput = WDS.browser.findElement(org.openqa.selenium.By.xpath('//div/main/div/div/div[2]/div/div/div/div[2]/input'));
codeInput.sendKeys("22222");
java.util.concurrent.TimeUnit.SECONDS.sleep(1);

var logBtn = WDS.browser.findElement(org.openqa.selenium.By.xpath('//div/main/div/div/div[2]/div/div/div/div[4]/button[1]'));
logBtn.click();
java.util.concurrent.TimeUnit.SECONDS.sleep(3);



// ------------------------------------------------------------------------

java.util.concurrent.TimeUnit.SECONDS.sleep(1);
WDS.sampleResult.sampleEnd();
