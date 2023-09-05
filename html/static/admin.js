const url_params = new URLSearchParams(window.location.search);
if (url_params.has("id")) {
    document.querySelector("#id-input").value = url_params.get("id");
    reloadFunction();
}
if (url_params.has("password")) {
    document.querySelector("#password-input").value = url_params.get("password");
}
if (url_params.has("token")) {
    document.querySelector("#token-input").value = url_params.get("token");
}

async function reloadFunction() {
    document.querySelector("#reload-button").style.animation = "";
    await new Promise(r => setTimeout(r, 1));
    document.querySelector("#reload-button").style.animation = "reload-button 1s ease-out";

    document.querySelector("#load").style.transform = "translateY(0dvh)";
    document.querySelector("#load-message").style.color = "white";

    document.querySelector("#id-input").setAttribute("error", "");

    await fetch("/utils/id/"+document.querySelector("#id-input").value).then(response => response.json()).then(data => {
        if (data.error == undefined) {
            document.querySelector("#id-input").value = data.response;
            let to_url_params = new URLSearchParams(window.location.search);
            to_url_params.set("id", data.response);
            window.history.replaceState(null, null, window.location.protocol+"//"+window.location.host+window.location.pathname+"?"+to_url_params.toString());
        }
    });

    await fetch("/api/account?id="+document.querySelector("#id-input").value).then(response => response.json()).then(data => {
        console.log(data);

        if (data.error != undefined) {
            document.querySelector("#id-input").setAttribute("error", data.error);
            document.querySelector("#load-message").innerHTML = data.error;
            document.querySelector("#load-message").style.color = "black";
        } else {
            if (data.account.moderation) document.querySelector("#moderation-account-select option[value='true']").selected = true;
            else document.querySelector("#moderation-account-select option[value='false']").selected = true;
    
            if (data.account.banned) document.querySelector("#banned-account-select option[value='true']").selected = true;
            else document.querySelector("#banned-account-select option[value='false']").selected = true;
    
            if (data.account.admin) document.querySelector("#admin-account-select option[value='true']").selected = true;
            else document.querySelector("#admin-account-select option[value='false']").selected = true;
    
            if (data.country.check) document.querySelector("#check-country-select option[value='"+data.country.check+"']").selected = true;
            else document.querySelector("#check-country-select option[value='query']").selected = true;
    
            if (data.valute.check) document.querySelector("#check-valute-select option[value='"+data.valute.check+"']").selected = true;
            else document.querySelector("#check-valute-select option[value='query']").selected = true;

            document.querySelector("#load-message").innerHTML = "Аккаунт загружен.";
            document.querySelector("#load-message").style.color = "black";
        }
    });

    await new Promise(r => setTimeout(r, 1500));
    document.querySelector("#load").style.transform = "translateY(-100dvh)";
}

async function uploadFunction() {
    document.querySelector("#upload-button").style.animation = "";
    await new Promise(r => setTimeout(r, 1));
    document.querySelector("#upload-button").style.animation = "upload-button 1s ease-out";

    document.querySelector("#load").style.transform = "translateY(0dvh)";
    document.querySelector("#load-message").style.color = "white";

    if (document.querySelector("#password-input").value == "") {
        document.querySelector("#load-message").innerHTML = "Не указан пароль.";
        document.querySelector("#load-message").style.color = "black";
    }
    if (document.querySelector("#id-input").getAttribute("error") != "") {
        document.querySelector("#load-message").innerHTML = "Неверный аккаунт.";
        document.querySelector("#load-message").style.color = "black";
    }

    document.querySelector("#load-message").style.color = "white";
    await fetch("/sapi/admin/account?admin_token="+document.querySelector("#password-input").value+"&token="+document.querySelector("#token-input").value+"&id="+document.querySelector("#id-input").value+"&key=moderation&value="+document.querySelector("#moderation-account-select").value).then(response => response.json()).then(data => {
        if (data.error != undefined) {
            document.querySelector("#load-message").innerHTML = data.error;
        } else {
            document.querySelector("#load-message").innerHTML = "Account: moderation";
        }
        document.querySelector("#load-message").style.color = "black";
    });
    
    await new Promise(r => setTimeout(r, 500));

    document.querySelector("#load-message").style.color = "white";
    await fetch("/sapi/admin/account?admin_token="+document.querySelector("#password-input").value+"&token="+document.querySelector("#token-input").value+"&id="+document.querySelector("#id-input").value+"&key=banned&value="+document.querySelector("#banned-account-select").value).then(response => response.json()).then(data => {
    if (data.error != undefined) {
            document.querySelector("#load-message").innerHTML = data.error;
        } else {
            document.querySelector("#load-message").innerHTML = "Account: banned";
        }
        document.querySelector("#load-message").style.color = "black";
    });

    await new Promise(r => setTimeout(r, 500));
    
    document.querySelector("#load-message").style.color = "white";
    await fetch("/sapi/admin/account?admin_token="+document.querySelector("#password-input").value+"&token="+document.querySelector("#token-input").value+"&id="+document.querySelector("#id-input").value+"&key=admin&value="+document.querySelector("#admin-account-select").value).then(response => response.json()).then(data => {
        if (data.error != undefined) {
            document.querySelector("#load-message").innerHTML = data.error;
        } else {
            document.querySelector("#load-message").innerHTML = "Account: admin";
        }
        document.querySelector("#load-message").style.color = "black";
    });
    
    await new Promise(r => setTimeout(r, 500));

    document.querySelector("#load-message").style.color = "white";
    await fetch("/sapi/admin/country?admin_token="+document.querySelector("#password-input").value+"&token="+document.querySelector("#token-input").value+"&id="+document.querySelector("#id-input").value+"&key=check&value="+document.querySelector("#check-country-select").value).then(response => response.json()).then(data => {
        if (data.error != undefined) {
            document.querySelector("#load-message").innerHTML = data.error;
        } else {
            document.querySelector("#load-message").innerHTML = "Country: check";
        }
        document.querySelector("#load-message").style.color = "black";
    });
    
    await new Promise(r => setTimeout(r, 500));

    document.querySelector("#load-message").style.color = "white";
    await fetch("/sapi/admin/valute?admin_token="+document.querySelector("#password-input").value+"&token="+document.querySelector("#token-input").value+"&id="+document.querySelector("#id-input").value+"&key=check&value="+document.querySelector("#check-valute-select").value).then(response => response.json()).then(data => {
        if (data.error != undefined) {
            document.querySelector("#load-message").innerHTML = data.error;
        } else {
            document.querySelector("#load-message").innerHTML = "Valute: check";
        }
        document.querySelector("#load-message").style.color = "black";
    });
    

    await new Promise(r => setTimeout(r, 1500));
    document.querySelector("#load").style.transform = "translateY(-100dvh)";
}



document.querySelector("#reload-button").addEventListener("click", reloadFunction);
document.querySelector("#upload-button").addEventListener("click", uploadFunction);

document.querySelector("#id-input").addEventListener("input", function() {
    document.querySelector("#id-input").setAttribute("error", "");
});