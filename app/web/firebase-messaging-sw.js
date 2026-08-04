importScripts('https://www.gstatic.com/firebasejs/10.7.0/firebase-app-compat.js');
importScripts('https://www.gstatic.com/firebasejs/10.7.0/firebase-messaging-compat.js');

firebase.initializeApp({
  apiKey: "AIzaSyB2ztnjmB8KGzcgicaSSt8_ovxLAbMcf1g",
  authDomain: "thanqyou-0303m.firebaseapp.com",
  projectId: "thanqyou-0303m",
  storageBucket: "thanqyou-0303m.firebasestorage.app",
  messagingSenderId: "929066663904",
  appId: "1:929066663904:web:0816a70228795979e53585"
});

const messaging = firebase.messaging();

messaging.onBackgroundMessage(function(payload) {
  console.log('Background message:', payload);
  const notification = payload.notification;
  if (notification) {
    self.registration.showNotification(notification.title || '', {
      body: notification.body || '',
      icon: '/icons/Icon-192.png'
    });
  }
});
