# Automation framework for Mobile

## About

An automation framework for Android Applications built with Appium and Python.

## Requires
* NPM & Node
* Python (version > 3)
* ADB command line tool
* Appium
* appium-doctor (Attempts to diagnose and fix common Node, iOS and Android configuration issues before starting Appium.If you
 do not have it in your system install it using the following command)
 ```bash
    npm install appium-doctor -g
```
* Virtualenv (If your system do not have virtualenv please set it up using the following command)
```bash
    pip install virtualenv
```


## How to start

Once you have above requirements satisfied and a android device connected with your system in usb debugging mode, we can start the automation tests(Make sure that device 
is not locked and Onefootball app is not installed this framework will install the given APK file).
Steps :-
 
* Check if appium setup is proper before starting appium using appium doctor. Check if everything is proper using the following command:
```bash
    appium-doctor
```
* Check if your device is connected properly using adb command:
```bash
    adb devices
```

* Start Appium
```bash
    appium
```

* Clone this repository and go to the root directory.

```bash
    git clone https://github.com/ranit-geek/mobile-automation-framework.git
    
    cd mobile-automation-framework
```

    
* Create and activate virtual environment using python3.

```bash
    virtualenv -p python3 venv
    
    source venv/bin/activate
```

    
    
* Install requirements from requirements.txt  

```bash
    pip install -r requirements.txt
```



* Run the automated tests   

```bash
    ptest3 -t tests
```




* To see test result report check the HTML report path generated after test run in the terminal and append `/index.html` and then open it in browser
.For example it looks like this in my system :  

```bash
    /Users/ranit/documentation/mobile-automation-framework/test-output/html-report/index.html   
   
```
     


## Test cases automated  

#### Following Page Tests
   * test_001: Complete the onboarding flow using the user given favourite nation and club.
   
   * test_002: Navigate to the following page and follow and unfollow user given team , competition
   and player using search.Validate if the followed content is coming properly in the follwing page.
   Also validate that after unfollowing a content it gets removed from the following page. (This test case is running with a data provider
    , which means it will run multiple times depending on the data provided)
    
   * test_003: Clear user's favourite club selection and on the remove confirmation popup select keep.
   Check that the favourite club should not get cleared.
    
   * test_004: Clear user's favourite nation selection and on the remove confirmation popup select keep.
   Check that the favourite nation should not get cleared.
    
   * test_005: Clear user's favourite club selection.
   Check that the favourite club should get cleared in the following page.
    
   * test_006: Clear user's favourite nation selection.
   Check that the favourite nation should get cleared in the following page.
    

    

