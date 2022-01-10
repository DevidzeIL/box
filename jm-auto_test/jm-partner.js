WDS.sampleResult.sampleStart();

var httpProtocol = 'https://';
var mainHost = 'devonshopnew.mileonair.com';
var testPath = '/partners';

WDS.browser.get(httpProtocol + mainHost + testPath);
java.util.concurrent.TimeUnit.SECONDS.sleep(1);

// ------------------------------------------------------------------------


var nameInput = WDS.browser.findElement(org.openqa.selenium.By.xpath('//div/main/div/div/div[1]/form/div/div[1]/input'));
nameInput.sendKeys("Test");
java.util.concurrent.TimeUnit.SECONDS.sleep(1);

var emailInput = WDS.browser.findElement(org.openqa.selenium.By.xpath('//div/main/div/div/div[1]/form/div/div[2]/input'));
emailInput.sendKeys("test@gmail.com");
java.util.concurrent.TimeUnit.SECONDS.sleep(1);

var phoneInput = WDS.browser.findElement(org.openqa.selenium.By.xpath('//div/main/div/div/div[1]/form/div/div[3]/input'));
phoneInput.sendKeys("79777751713");
java.util.concurrent.TimeUnit.SECONDS.sleep(1);

var infoInput = WDS.browser.findElement(org.openqa.selenium.By.xpath('//div/main/div/div/div[1]/form/div/div[4]/input'));
infoInput.sendKeys("Some text about partner");
java.util.concurrent.TimeUnit.SECONDS.sleep(1);

var termsCheckbox = WDS.browser.findElement(org.openqa.selenium.By.xpath('//div/main/div/div/div[1]/form/div/div[5]/label'));
termsCheckbox.click();
java.util.concurrent.TimeUnit.SECONDS.sleep(1);

// var sendBtn = WDS.browser.findElement(org.openqa.selenium.By.xpath('//div/main/div/div/div[1]/form/div/div[6]/button'));
// sendBtn.click();
// java.util.concurrent.TimeUnit.SECONDS.sleep(1);


// ------------------------------------------------------------------------

java.util.concurrent.TimeUnit.SECONDS.sleep(1);
WDS.sampleResult.sampleEnd();
