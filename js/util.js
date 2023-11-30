var curSideNavSel = null;

var sideNavButtons = document.querySelectorAll('#side-nav button');
for(sideNavButton of sideNavButtons) {
	console.log(sideNavButton);
	sideNavButton.addEventListener('click', sideNavButtonPress);
}

function sideNavButtonPress() {
	console.log("pressed " + this.id);
	if(this.className != "pure-action") {
		sideNavUnselectEnableAndHide(curSideNavSel);
		sideNavSelectDisableAndUnhide(this.id);
	}

	switch(this.id) {
	case "regen-button":
		postEndpoint("regen");
        // intentionally not breaking to fall through
        // to call displayLatestTargetInput()
    case "target-input-button":
        displayLatestHtml("target-input");
        break;
	}
}

function sideNavUnselectEnableAndHide(buttonId) {
	if(buttonId == null) return;

	leavingElt = document.getElementById(buttonId);
	leavingElt.disable = false;
	leavingElt.style.color = "#818181";
	switch(buttonId) {
	case "target-input-button":
		document.getElementById("regen-button").style.display = "none";
		document.getElementById("run-button").style.display = "none";
		break;
	case "target-button":
		document.getElementById("target-copy-button").style.display = "none";
		document.getElementById("target-send-button").style.display = "none";
	case "target-summary-button":
		document.getElementById("target-summary-button").style.display = "none";
		break;
	case "slice-button":
		document.getElementById("slice-copy-button").style.display = "none";
		document.getElementById("slice-send-button").style.display = "none";
	case "slice-summary-button":
		document.getElementById("slice-summary-button").style.display = "none";
		break;
	case "trim-button":
		document.getElementById("trim-copy-button").style.display = "none";
		document.getElementById("trim-send-button").style.display = "none";
	case "trim-summary-button":
		document.getElementById("trim-summary-button").style.display = "none";
		break;
	default:
	}

}

function sideNavSelectDisableAndUnhide(buttonId) {
	curSideNavSel = buttonId;
	curElt = document.getElementById(buttonId);
	curElt.style.color = "#f1f1f1";
	curElt.disable = true;
	switch(buttonId) {
	case "target-input-button":
		document.getElementById("regen-button").style.display = "block";
		document.getElementById("run-button").style.display = "block";
		break;
	case "target-button":
		document.getElementById("target-copy-button").style.display = "block";
		document.getElementById("target-send-button").style.display = "block";
	case "target-summary-button":
		document.getElementById("target-summary-button").style.display = "block";
		break;
	case "slice-button":
		document.getElementById("slice-copy-button").style.display = "block";
		document.getElementById("slice-send-button").style.display = "block";
	case "slice-summary-button":
		document.getElementById("slice-summary-button").style.display = "block";
		break;
	case "trim-button":
		document.getElementById("trim-copy-button").style.display = "block";
		document.getElementById("trim-send-button").style.display = "block";
	case "trim-summary-button":
		document.getElementById("trim-summary-button").style.display = "block";
		break;
	default:
	}

}

var navWidth = 140;
function toggleNav() {
  w = document.getElementById("side-nav").offsetWidth;
  if(w == 0)
    w = navWidth;   
  else
	w = 0;

  document.getElementById("side-nav").style.width = w + "px";
  document.getElementById("open-close-button").style.marginLeft = w + "px";

  ocButtonWidth = document.getElementById("open-close-button").offsetWidth;
  document.getElementById("main-content").style.marginLeft = w + ocButtonWidth + "px";
}

/*
function displayLatestTargetInput() {
  var xhttp = new XMLHttpRequest();
  xhttp.onload = function() {
    console.log("Function Name: " + displayLatestTargetInput.name);
    console.log("Line Number: " + new Error().lineNumber);
    console.log(this.responseText);
    document.getElementById("main-content").innerHTML = this.responseText;
  }
  console.log(window.location.origin);
  xhttp.open('GET', window.location.origin + '/target-input.html', true);
  xhttp.send();
}
*/

function displayLatestHtml(pageName) {
  var xhttp = new XMLHttpRequest();
  xhttp.onload = function() {
    console.log("Function Name: " + displayLatestHtml.name);
    console.log("Line Number: " + new Error().lineNumber);
    console.log(this.responseText);
    document.getElementById("main-content").innerHTML = this.responseText;
  }
  console.log(window.location.origin);
  xhttp.open("GET", window.location.origin + "/" + pageName + ".html", true);
  xhttp.send();

}

function postEndpoint(endpoint) {
    fetch("/" + endpoint, {
      method: "POST",
      // Optionally, include headers or a request body with data
    })
      .then(response => {
        if (response.ok) {
          console.log(endpoint + " executed successfully");
        } else {
          console.error(endpoint + " execution failed");
        }
      })
      .catch(error => console.error("Error:", error));
}
