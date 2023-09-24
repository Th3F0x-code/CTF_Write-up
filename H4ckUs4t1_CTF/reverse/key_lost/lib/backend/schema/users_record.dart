import 'dart:async';

import 'package:collection/collection.dart';

import '/backend/schema/util/firestore_util.dart';
import '/backend/schema/util/schema_util.dart';

import 'index.dart';
import '/flutter_flow/flutter_flow_util.dart';

class UsersRecord extends FirestoreRecord {
  UsersRecord._(
    DocumentReference reference,
    Map<String, dynamic> data,
  ) : super(reference, data) {
    _initializeFields();
  }

  // "created_time" field.
  DateTime? _createdTime;
  DateTime? get createdTime => _createdTime;
  bool hasCreatedTime() => _createdTime != null;

  // "email" field.
  String? _email;
  String get email => _email ?? '';
  bool hasEmail() => _email != null;

  // "display_name" field.
  String? _displayName;
  String get displayName => _displayName ?? '';
  bool hasDisplayName() => _displayName != null;

  // "password" field.
  String? _password;
  String get password => _password ?? '';
  bool hasPassword() => _password != null;

  // "photo_url" field.
  String? _photoUrl;
  String get photoUrl => _photoUrl ?? '';
  bool hasPhotoUrl() => _photoUrl != null;

  // "phone_number" field.
  String? _phoneNumber;
  String get phoneNumber => _phoneNumber ?? '';
  bool hasPhoneNumber() => _phoneNumber != null;

  // "uid" field.
  String? _uid;
  String get uid => _uid ?? '';
  bool hasUid() => _uid != null;

  // "bio" field.
  String? _bio;
  String get bio => _bio ?? '';
  bool hasBio() => _bio != null;

  // "product" field.
  DocumentReference? _product;
  DocumentReference? get product => _product;
  bool hasProduct() => _product != null;

  // "userCity" field.
  String? _userCity;
  String get userCity => _userCity ?? '';
  bool hasUserCity() => _userCity != null;

  void _initializeFields() {
    _createdTime = snapshotData['created_time'] as DateTime?;
    _email = snapshotData['email'] as String?;
    _displayName = snapshotData['display_name'] as String?;
    _password = snapshotData['password'] as String?;
    _photoUrl = snapshotData['photo_url'] as String?;
    _phoneNumber = snapshotData['phone_number'] as String?;
    _uid = snapshotData['uid'] as String?;
    _bio = snapshotData['bio'] as String?;
    _product = snapshotData['product'] as DocumentReference?;
    _userCity = snapshotData['userCity'] as String?;
  }

  static CollectionReference get collection =>
      FirebaseFirestore.instance.collection('users');

  static Stream<UsersRecord> getDocument(DocumentReference ref) =>
      ref.snapshots().map((s) => UsersRecord.fromSnapshot(s));

  static Future<UsersRecord> getDocumentOnce(DocumentReference ref) =>
      ref.get().then((s) => UsersRecord.fromSnapshot(s));

  static UsersRecord fromSnapshot(DocumentSnapshot snapshot) => UsersRecord._(
        snapshot.reference,
        mapFromFirestore(snapshot.data() as Map<String, dynamic>),
      );

  static UsersRecord getDocumentFromData(
    Map<String, dynamic> data,
    DocumentReference reference,
  ) =>
      UsersRecord._(reference, mapFromFirestore(data));

  @override
  String toString() =>
      'UsersRecord(reference: ${reference.path}, data: $snapshotData)';

  @override
  int get hashCode => reference.path.hashCode;

  @override
  bool operator ==(other) =>
      other is UsersRecord &&
      reference.path.hashCode == other.reference.path.hashCode;
}

Map<String, dynamic> createUsersRecordData({
  DateTime? createdTime,
  String? email,
  String? displayName,
  String? password,
  String? photoUrl,
  String? phoneNumber,
  String? uid,
  String? bio,
  DocumentReference? product,
  String? userCity,
}) {
  final firestoreData = mapToFirestore(
    <String, dynamic>{
      'created_time': createdTime,
      'email': email,
      'display_name': displayName,
      'password': password,
      'photo_url': photoUrl,
      'phone_number': phoneNumber,
      'uid': uid,
      'bio': bio,
      'product': product,
      'userCity': userCity,
    }.withoutNulls,
  );

  return firestoreData;
}

class UsersRecordDocumentEquality implements Equality<UsersRecord> {
  const UsersRecordDocumentEquality();

  @override
  bool equals(UsersRecord? e1, UsersRecord? e2) {
    return e1?.createdTime == e2?.createdTime &&
        e1?.email == e2?.email &&
        e1?.displayName == e2?.displayName &&
        e1?.password == e2?.password &&
        e1?.photoUrl == e2?.photoUrl &&
        e1?.phoneNumber == e2?.phoneNumber &&
        e1?.uid == e2?.uid &&
        e1?.bio == e2?.bio &&
        e1?.product == e2?.product &&
        e1?.userCity == e2?.userCity;
  }

  @override
  int hash(UsersRecord? e) => const ListEquality().hash([
        e?.createdTime,
        e?.email,
        e?.displayName,
        e?.password,
        e?.photoUrl,
        e?.phoneNumber,
        e?.uid,
        e?.bio,
        e?.product,
        e?.userCity
      ]);

  @override
  bool isValidKey(Object? o) => o is UsersRecord;
}
