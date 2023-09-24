import '/auth/firebase_auth/auth_util.dart';
import '/backend/backend.dart';
import '/flutter_flow/flutter_flow_credit_card_form.dart';
import '/flutter_flow/flutter_flow_theme.dart';
import '/flutter_flow/flutter_flow_util.dart';
import '/flutter_flow/flutter_flow_widgets.dart';
import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:flutter/material.dart';
import 'package:flutter_spinkit/flutter_spinkit.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:provider/provider.dart';
import 'payment_modal_model.dart';
export 'payment_modal_model.dart';

class PaymentModalWidget extends StatefulWidget {
  const PaymentModalWidget({
    Key? key,
    this.paymentRef,
  }) : super(key: key);

  final double? paymentRef;

  @override
  _PaymentModalWidgetState createState() => _PaymentModalWidgetState();
}

class _PaymentModalWidgetState extends State<PaymentModalWidget> {
  late PaymentModalModel _model;

  @override
  void setState(VoidCallback callback) {
    super.setState(callback);
    _model.onUpdate();
  }

  @override
  void initState() {
    super.initState();
    _model = createModel(context, () => PaymentModalModel());
  }

  @override
  void dispose() {
    _model.maybeDispose();

    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Container(
      width: MediaQuery.sizeOf(context).width * 1.0,
      height: MediaQuery.sizeOf(context).height * 1.0,
      decoration: BoxDecoration(
        color: FlutterFlowTheme.of(context).customColor1,
      ),
      child: Padding(
        padding: EdgeInsetsDirectional.fromSTEB(0.0, 16.0, 0.0, 0.0),
        child: SingleChildScrollView(
          child: Column(
            mainAxisSize: MainAxisSize.max,
            children: [
              Padding(
                padding: EdgeInsetsDirectional.fromSTEB(20.0, 0.0, 20.0, 0.0),
                child: Row(
                  mainAxisSize: MainAxisSize.max,
                  children: [
                    Text(
                      'Pay Early',
                      style: FlutterFlowTheme.of(context).headlineMedium,
                    ),
                  ],
                ),
              ),
              Padding(
                padding: EdgeInsetsDirectional.fromSTEB(20.0, 0.0, 20.0, 0.0),
                child: Row(
                  mainAxisSize: MainAxisSize.max,
                  children: [
                    Expanded(
                      child: Padding(
                        padding:
                            EdgeInsetsDirectional.fromSTEB(0.0, 4.0, 0.0, 0.0),
                        child: Text(
                          'Fill out your information in order to pay early.',
                          style: FlutterFlowTheme.of(context).bodySmall,
                        ),
                      ),
                    ),
                  ],
                ),
              ),
              Padding(
                padding: EdgeInsetsDirectional.fromSTEB(0.0, 20.0, 0.0, 0.0),
                child: Text(
                  'Your Payment',
                  style: FlutterFlowTheme.of(context).bodySmall,
                ),
              ),
              Padding(
                padding: EdgeInsetsDirectional.fromSTEB(0.0, 12.0, 0.0, 0.0),
                child: Text(
                  formatNumber(
                    widget.paymentRef,
                    formatType: FormatType.decimal,
                    decimalType: DecimalType.automatic,
                    currency: '\$',
                  ),
                  textAlign: TextAlign.center,
                  style: GoogleFonts.getFont(
                    'Lexend Deca',
                    color: FlutterFlowTheme.of(context).dark400,
                    fontWeight: FontWeight.w100,
                    fontSize: 56.0,
                  ),
                ),
              ),
              Padding(
                padding: EdgeInsetsDirectional.fromSTEB(0.0, 4.0, 0.0, 24.0),
                child: Text(
                  'Due Sep 1, 2021',
                  style: FlutterFlowTheme.of(context).bodyMedium.override(
                        fontFamily: 'Outfit',
                        color: FlutterFlowTheme.of(context).grayDark,
                      ),
                ),
              ),
              Divider(
                height: 4.0,
                thickness: 1.0,
                indent: 20.0,
                endIndent: 20.0,
                color: FlutterFlowTheme.of(context).grayLighter,
              ),
              Padding(
                padding: EdgeInsetsDirectional.fromSTEB(12.0, 8.0, 12.0, 0.0),
                child: FlutterFlowCreditCardForm(
                  formKey: _model.creditCardFormKey,
                  creditCardModel: _model.creditCardInfo,
                  obscureNumber: true,
                  obscureCvv: false,
                  spacing: 10.0,
                  textStyle: FlutterFlowTheme.of(context).bodyMedium,
                  inputDecoration: InputDecoration(
                    enabledBorder: OutlineInputBorder(
                      borderSide: BorderSide(
                        color: FlutterFlowTheme.of(context).grayLighter,
                        width: 2.0,
                      ),
                      borderRadius: BorderRadius.circular(8.0),
                    ),
                    focusedBorder: OutlineInputBorder(
                      borderSide: BorderSide(
                        color: FlutterFlowTheme.of(context).grayLighter,
                        width: 2.0,
                      ),
                      borderRadius: BorderRadius.circular(8.0),
                    ),
                  ),
                ),
              ),
              Padding(
                padding: EdgeInsetsDirectional.fromSTEB(0.0, 20.0, 0.0, 40.0),
                child: FFButtonWidget(
                  onPressed: () async {
                    await PaymentsRecord.collection
                        .doc()
                        .set(createPaymentsRecordData(
                          paymentUser: currentUserReference,
                          paymentProduct: currentUserDocument?.product,
                          paymentDate: getCurrentTimestamp,
                          paymentStatus: 'Complete',
                          paymentAmount: widget.paymentRef,
                        ));

                    context.pushNamed(
                      'paymentComplete',
                      extra: <String, dynamic>{
                        kTransitionInfoKey: TransitionInfo(
                          hasTransition: true,
                          transitionType: PageTransitionType.bottomToTop,
                          duration: Duration(milliseconds: 250),
                        ),
                      },
                    );
                  },
                  text: 'Pay Now',
                  options: FFButtonOptions(
                    width: 300.0,
                    height: 50.0,
                    padding: EdgeInsetsDirectional.fromSTEB(0.0, 0.0, 0.0, 0.0),
                    iconPadding:
                        EdgeInsetsDirectional.fromSTEB(0.0, 0.0, 0.0, 0.0),
                    color: FlutterFlowTheme.of(context).secondary,
                    textStyle: FlutterFlowTheme.of(context).titleSmall.override(
                          fontFamily: 'Outfit',
                          color: Colors.white,
                        ),
                    elevation: 2.0,
                    borderSide: BorderSide(
                      color: Colors.transparent,
                      width: 1.0,
                    ),
                    borderRadius: BorderRadius.circular(50.0),
                  ),
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
