
var isPushEnabled = false,
  registration,
  subBtn;

window.addEventListener('load', function () {
  subBtn = document.getElementById('webpush-subscribe-button');
  subBtn.textContent = ' الإشعارات';
  subBtn.addEventListener('click',
    function () {
      subBtn.disabled = true;
      if (isPushEnabled) {
        return;
      }
      return subscribe(registration);
    }
  );

  if ('serviceWorker' in navigator) {
    const serviceWorker = document.querySelector('meta[name="service-worker-js"]').content;
    navigator.serviceWorker.register(serviceWorker).then(
      function (reg) {
        registration = reg;
        initialiseState(reg);
      });
  }

  else {
    alert('Service workers are not supported in your browser.');
  }

  function initialiseState(reg) {

    if (!(reg.showNotification)) {
      alert('Showing notifications are not supported in your browser.');
      return;
    }


    if (Notification.permission === 'denied') {

      subBtn.disabled = false;
      alert('Push notifications are blocked by your browser.');
      return;
    }

    if (!('PushManager' in window)) {

      subBtn.disabled = false;
      alert('Push notifications are not available in your browser.');
      return;
    }


    reg.pushManager.getSubscription().then(
      function (subscription) {
        if (subscription) {
          postSubscribeObj('subscribe', subscription,
            function (response) {
              if (response.status === 201) {
                subBtn.disabled = true;
                subBtn.style.display = 'none';
                isPushEnabled = true;
              }
            });
        }
      });
  }
}
);


function subscribe(reg) {
  reg.pushManager.getSubscription().then(
    function (subscription) {
      var metaObj, applicationServerKey, options;
      if (subscription) {
        return subscription;
      }
      metaObj = document.querySelector('meta[name="django-webpush-vapid-key"]');
      applicationServerKey = metaObj.content;
      options = {
        userVisibleOnly: true
      };
      if (applicationServerKey) {
        options.applicationServerKey = urlB64ToUint8Array(applicationServerKey)
      }

      reg.pushManager.subscribe(options)
        .then(
          function (subscription) {
            postSubscribeObj('subscribe', subscription,
              function (response) {

                if (response.status === 201) {
                  subBtn.disabled = true;
                  subBtn.style.display = 'none';
                  isPushEnabled = true;
                }
              });
          })
        .catch(
          function () {
            alert('Error while subscribing to push notifications');
          })
    }
  );
}

function urlB64ToUint8Array(base64String) {
  const padding = '='.repeat((4 - base64String.length % 4) % 4);
  const base64 = (base64String + padding)
    .replace(/\-/g, '+')
    .replace(/_/g, '/');

  const rawData = window.atob(base64);
  const outputArray = new Uint8Array(rawData.length);

  for (var i = 0; i < rawData.length; ++i) {
    outputArray[i] = rawData.charCodeAt(i);
  }
  return outputArray;
}

function unsubscribe(reg) {
  return;
}

function postSubscribeObj(statusType, subscription, callback) {
  var browser = navigator.userAgent.match(/(firefox|msie|chrome|safari|trident)/ig)[0].toLowerCase(),
    user_agent = navigator.userAgent,
    data = {
      status_type: statusType,
      subscription: subscription.toJSON(),
      browser: browser,
      user_agent: user_agent,
      group: subBtn.dataset.group
    };

  fetch(subBtn.dataset.url, {
    method: 'post',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data),
    credentials: 'include'
  }).then(callback);
}
