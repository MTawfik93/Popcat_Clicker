from selenium import webdriver

driver = webdriver.Chrome("lib\chromedriver.exe")
driver.get("https://popcat.click/")
driver.execute_script('const app=document.querySelector("#app").__vue__;function click(){app.accumulator=600,app.bot=!1,app.sequential_max_pops=0,pop()}function pop(){for(var e=0;e<=800;e++)setTimeout(()=>{document.dispatchEvent(new KeyboardEvent("keydown",{key:"g",ctrlKey:!0}))},5)}document.cookie="country=EG;expires=Sat, 31 Dec 2022 12:00:00 UTC;path=/",document.dispatchEvent(new KeyboardEvent("keydown",{key:"g",ctrlKey:!0})),setInterval(()=>{click()},29e3);')

