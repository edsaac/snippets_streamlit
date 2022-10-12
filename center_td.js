const tds = document.getElementsByTagName("td")
for (var i = 0; i < tds.length; i++){
    tds.item(i).style.textAlign = "center";
    console.log({"MyLog:":i});
}