WDS.sampleResult.sampleStart();

var httpProtocol = 'https://';
var mainHost = 'devonshopnew.mileonair.com';
var testPath = '/';

WDS.browser.get(httpProtocol + mainHost + testPath);
java.util.concurrent.TimeUnit.SECONDS.sleep(1);

// ------------------------------------------------------------------------

var fromInput = WDS.browser.findElement(org.openqa.selenium.By.xpath('//div/section[2]/div/div/div/div/div[1]/div[1]'));
fromInput.click();
java.util.concurrent.TimeUnit.SECONDS.sleep(3);

var listFrom = fromInput.findElements(org.openqa.selenium.By.tagName("li"));

java.util.concurrent.TimeUnit.SECONDS.sleep(1)

var targetFrom = Math.floor(Math.random() * listFrom.length+1) + 1;
var targetFromInput = fromInput.findElement(org.openqa.selenium.By.xpath("//div/section[2]/div/div/div/div/div[1]/div[1]/div/ul/li["+ targetFrom +"]"));
targetFromInput.click();
java.util.concurrent.TimeUnit.SECONDS.sleep(1);



var toInput = WDS.browser.findElement(org.openqa.selenium.By.xpath('//div/section[2]/div/div/div/div/div[1]/div[2]'));
toInput.click();
java.util.concurrent.TimeUnit.SECONDS.sleep(3);

var listTo = toInput.findElements(org.openqa.selenium.By.tagName("li"));

java.util.concurrent.TimeUnit.SECONDS.sleep(1);

var targetTo = Math.floor(Math.random() * listTo.length+1) + 1;

while (targetTo == targetFrom){
	targetTo = Math.floor(Math.random() * listTo.length+1) + 1;
}

var targetToInput = toInput.findElement(org.openqa.selenium.By.xpath("//div/section[2]/div/div/div/div/div[1]/div[2]/div/ul/li["+ targetTo +"]"));
targetToInput.click();
java.util.concurrent.TimeUnit.SECONDS.sleep(1);



var date_fromInput = WDS.browser.findElement(org.openqa.selenium.By.xpath('//div/section[2]/div/div/div/div/div[2]/div[1]/input'));
date_fromInput.click();
java.util.concurrent.TimeUnit.SECONDS.sleep(1);

var date_toInput = WDS.browser.findElement(org.openqa.selenium.By.xpath('//div/section[2]/div/div/div/div/div[2]/div[2]/input'));
date_toInput.click();
java.util.concurrent.TimeUnit.SECONDS.sleep(1);



var findBtn = WDS.browser.findElement(org.openqa.selenium.By.xpath('//div/section[2]/div/div/div/div/div[3]'));
findBtn.click()

// ------------------------------------------------------------------------

java.util.concurrent.TimeUnit.SECONDS.sleep(1);
WDS.sampleResult.sampleEnd();
