import 'package:firebase_core/firebase_core.dart';
import 'package:flutter/foundation.dart';

Future initFirebase() async {
  if (kIsWeb) {
    await Firebase.initializeApp(
        options: FirebaseOptions(
            apiKey: "AIzaSyBCRfndg5aJAP8pdxTW83Fv4qQECcQtCNk",
            authDomain: "ctfs-32342.firebaseapp.com",
            projectId: "ctfs-32342",
            storageBucket: "ctfs-32342.appspot.com",
            messagingSenderId: "720312795861",
            appId: "1:720312795861:web:92c7bbf5d26d07ab37985c",
            measurementId: "G-6DSP6D5XKL"));
  } else {
    await Firebase.initializeApp();
  }
}
