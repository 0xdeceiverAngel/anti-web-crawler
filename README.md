# anti-crawler 
## user agent
雖說這題是 user agent 但是只給 host 也是可以 噴200
## cookie
直接要`content.html`會被 302 到`index.html`並且設定cookie成`isfirst=789kq7uc1pp4c`
所以直接cookie設好 戳`content.html`就好
cookie寫死
## sign
按下查看詳情會call `fetch()` 
`fetch()` 被包在`sing.js`裡

```js
function fetch() {
    text = $.ajax({
        type: "GET",
        async: false,
        url: "http://www.porters.vip/verify/sign/fet" + uri()
    });
    $("#content").html(text.responseText);
}

function randints(r, n, tof) {
    /* 生成随机数字，tof决定返回number类型或者字符串类型
    r 代表数字范围 n 代表数量
    */
    var result = [];
    if (tof) {
        return Math.floor(Math.random() * r);
    }
    for (var i = 0; i < n; i++) {
        s = Math.floor(Math.random() * r);
        result.push(s);
    }
    return result.join('');
}

function randstrs(n) {
    // 生成随机字母，n为随机字母的数量
    var result = [];
    for (var i = 0; i < n; i++) {
        s = String.fromCharCode(65 + randints(25, 1, 1));
        result.push(s);
    }
    return result.join('');
}

function uri() {
    var action = randints(9, 5, 0);
    var tim = Math.round(new Date().getTime() / 1000).toString();
    var randstr = randstrs(5);
    var hexs = hex_md5(action + tim + randstr);
    args = '?actions=' + action + '&tim=' + tim + '&randstr=' + randstr + '&sign=' + hexs;
    return args;
}
```
然後就是逆向
戳 `http://www.porters.vip/verify/sign/fet?actions={}&tim={}&randstr={}&sign={}`
## confusion
在安裝 `pytesseract` 踩了坑 numpy要用1.19.3 `pip install numpy==1.19.3`
就是有些網頁會用圖片來表示文字 user看起來沒問題 但是要爬就會有問題
用OCR辨識
## css offset
```html=
<span class="fix_price">
    <span class="prc_wp" style="width:48px">
        <em class="rel">
            <b style="width:48px;left:-48px">
                <i style="width: 16px;">7</i>
                <i style="width: 16px;">7</i>
                <i style="width: 16px;">7</i>
            </b>
            <b style="width: 16px;left:-32px">6</b>
            <b style="width: 16px;left:-48px">4</b>
        </em>
    </span>
 </span>
```
很明顯 css 位移 
~~算這個很煩 乾脆直接OCR~~

## svg
就是利用svg 先畫出一堆數字的背景 然後取位置 顯示前端當成數字來用
載css時會載入svg當背景 再利用class 只顯示某塊數字
手動對應找出關係就好
```css=
d[class^="vhk"] {
  width: 14px;
  height: 30px;
  margin-top: -9px;
  background-image: url(../font/food.svg);
  background-repeat: no-repeat;
  display: inline-block;
  vertical-align: middle;
  margin-left: -6px;
}
.vhk08k {
  background: -274px -141px;
}
.vhk6zl {
  background: -7px -15px;
}
.vhk0ao {
  background: -133px -97px;
}
...略
```
## font-replace
就是先對字型檔案人工下去做分析 爬網頁時再對照回去
## webdriver
- 用webkit開發的工具繞過
- js改webdriver value
- 用proxy過濾 eg. mitproxy
- 設定 selenium
## browser features
```js
    document.getElementById('first').innerHTML = navigator.userAgent;
    document.getElementById('second').innerHTML = navigator.platform;
    document.getElementById('three').innerHTML = screen.width;
    document.getElementById('four').innerHTML = screen.height;
    document.getElementById('five').innerHTML = navigator.cookieEnabled;
    document.getElementById('six').innerHTML = navigator.hardwareConcurrency;
    document.getElementById('seven').innerHTML = new Date().getTimezoneOffset();
    document.getElementById('eight').innerHTML = navigator.plugins.length;
    document.getElementById('nine').innerHTML = window.screen.colorDepth;
```
可以列出特徵
## request frequency
建ip pool or delay request
## fingertprint
- uuid
- canvas fingertprint
- fingerprint js
- webcl fingerprint 
## tools 
- splash
- puppeteer
