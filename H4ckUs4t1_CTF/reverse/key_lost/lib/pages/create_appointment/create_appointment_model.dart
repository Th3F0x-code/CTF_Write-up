import '/auth/firebase_auth/auth_util.dart';
import '/backend/backend.dart';
import '/flutter_flow/flutter_flow_drop_down.dart';
import '/flutter_flow/flutter_flow_icon_button.dart';
import '/flutter_flow/flutter_flow_theme.dart';
import '/flutter_flow/flutter_flow_util.dart';
import '/flutter_flow/flutter_flow_widgets.dart';
import '/flutter_flow/form_field_controller.dart';
import '/flutter_flow/random_data_util.dart' as random_data;
import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:flutter/material.dart';
import 'package:flutter_datetime_picker_plus/flutter_datetime_picker_plus.dart';
import 'package:flutter_spinkit/flutter_spinkit.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:provider/provider.dart';

class CreateAppointmentModel extends FlutterFlowModel {
  ///  State fields for stateful widgets in this page.

  final unfocusNode = FocusNode();
  final formKey = GlobalKey<FormState>();
  // State field(s) for userName widget.
  TextEditingController? userNameController;
  String? Function(BuildContext, String?)? userNameControllerValidator;
  // State field(s) for shortBio widget.
  TextEditingController? shortBioController;
  String? Function(BuildContext, String?)? shortBioControllerValidator;
  // State field(s) for serviceType widget.
  String? serviceTypeValue;
  FormFieldController<String>? serviceTypeValueController;
  // State field(s) for statusType widget.
  String? statusTypeValue;
  FormFieldController<String>? statusTypeValueController;
  DateTime? datePicked;

  /// Initialization and disposal methods.

  void initState(BuildContext context) {}

  void dispose() {
    unfocusNode.dispose();
    userNameController?.dispose();
    shortBioController?.dispose();
  }

  /// Action blocks are added here.

  /// Additional helper methods are added here.
}
