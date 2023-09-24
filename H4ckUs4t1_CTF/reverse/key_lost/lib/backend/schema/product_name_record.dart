import 'dart:async';

import 'package:collection/collection.dart';

import '/backend/schema/util/firestore_util.dart';
import '/backend/schema/util/schema_util.dart';

import 'index.dart';
import '/flutter_flow/flutter_flow_util.dart';

class ProductNameRecord extends FirestoreRecord {
  ProductNameRecord._(
    DocumentReference reference,
    Map<String, dynamic> data,
  ) : super(reference, data) {
    _initializeFields();
  }

  // "productName" field.
  String? _productName;
  String get productName => _productName ?? '';
  bool hasProductName() => _productName != null;

  // "productImage" field.
  String? _productImage;
  String get productImage => _productImage ?? '';
  bool hasProductImage() => _productImage != null;

  // "productColor" field.
  String? _productColor;
  String get productColor => _productColor ?? '';
  bool hasProductColor() => _productColor != null;

  // "productDefaulTemp" field.
  String? _productDefaulTemp;
  String get productDefaulTemp => _productDefaulTemp ?? '';
  bool hasProductDefaulTemp() => _productDefaulTemp != null;

  // "productMileage" field.
  String? _productMileage;
  String get productMileage => _productMileage ?? '';
  bool hasProductMileage() => _productMileage != null;

  // "productLocation" field.
  LatLng? _productLocation;
  LatLng? get productLocation => _productLocation;
  bool hasProductLocation() => _productLocation != null;

  // "productUser" field.
  DocumentReference? _productUser;
  DocumentReference? get productUser => _productUser;
  bool hasProductUser() => _productUser != null;

  // "productPayment" field.
  DocumentReference? _productPayment;
  DocumentReference? get productPayment => _productPayment;
  bool hasProductPayment() => _productPayment != null;

  void _initializeFields() {
    _productName = snapshotData['productName'] as String?;
    _productImage = snapshotData['productImage'] as String?;
    _productColor = snapshotData['productColor'] as String?;
    _productDefaulTemp = snapshotData['productDefaulTemp'] as String?;
    _productMileage = snapshotData['productMileage'] as String?;
    _productLocation = snapshotData['productLocation'] as LatLng?;
    _productUser = snapshotData['productUser'] as DocumentReference?;
    _productPayment = snapshotData['productPayment'] as DocumentReference?;
  }

  static CollectionReference get collection =>
      FirebaseFirestore.instance.collection('productName');

  static Stream<ProductNameRecord> getDocument(DocumentReference ref) =>
      ref.snapshots().map((s) => ProductNameRecord.fromSnapshot(s));

  static Future<ProductNameRecord> getDocumentOnce(DocumentReference ref) =>
      ref.get().then((s) => ProductNameRecord.fromSnapshot(s));

  static ProductNameRecord fromSnapshot(DocumentSnapshot snapshot) =>
      ProductNameRecord._(
        snapshot.reference,
        mapFromFirestore(snapshot.data() as Map<String, dynamic>),
      );

  static ProductNameRecord getDocumentFromData(
    Map<String, dynamic> data,
    DocumentReference reference,
  ) =>
      ProductNameRecord._(reference, mapFromFirestore(data));

  @override
  String toString() =>
      'ProductNameRecord(reference: ${reference.path}, data: $snapshotData)';

  @override
  int get hashCode => reference.path.hashCode;

  @override
  bool operator ==(other) =>
      other is ProductNameRecord &&
      reference.path.hashCode == other.reference.path.hashCode;
}

Map<String, dynamic> createProductNameRecordData({
  String? productName,
  String? productImage,
  String? productColor,
  String? productDefaulTemp,
  String? productMileage,
  LatLng? productLocation,
  DocumentReference? productUser,
  DocumentReference? productPayment,
}) {
  final firestoreData = mapToFirestore(
    <String, dynamic>{
      'productName': productName,
      'productImage': productImage,
      'productColor': productColor,
      'productDefaulTemp': productDefaulTemp,
      'productMileage': productMileage,
      'productLocation': productLocation,
      'productUser': productUser,
      'productPayment': productPayment,
    }.withoutNulls,
  );

  return firestoreData;
}

class ProductNameRecordDocumentEquality implements Equality<ProductNameRecord> {
  const ProductNameRecordDocumentEquality();

  @override
  bool equals(ProductNameRecord? e1, ProductNameRecord? e2) {
    return e1?.productName == e2?.productName &&
        e1?.productImage == e2?.productImage &&
        e1?.productColor == e2?.productColor &&
        e1?.productDefaulTemp == e2?.productDefaulTemp &&
        e1?.productMileage == e2?.productMileage &&
        e1?.productLocation == e2?.productLocation &&
        e1?.productUser == e2?.productUser &&
        e1?.productPayment == e2?.productPayment;
  }

  @override
  int hash(ProductNameRecord? e) => const ListEquality().hash([
        e?.productName,
        e?.productImage,
        e?.productColor,
        e?.productDefaulTemp,
        e?.productMileage,
        e?.productLocation,
        e?.productUser,
        e?.productPayment
      ]);

  @override
  bool isValidKey(Object? o) => o is ProductNameRecord;
}
