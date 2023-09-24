import '/flutter_flow/flutter_flow_theme.dart';
import '/flutter_flow/flutter_flow_util.dart';
import '/flutter_flow/flutter_flow_widgets.dart';
import 'package:flutter/material.dart';
import 'package:flutter_spinkit/flutter_spinkit.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:provider/provider.dart';
import 'past_payment_model.dart';
export 'past_payment_model.dart';

class PastPaymentWidget extends StatefulWidget {
  const PastPaymentWidget({Key? key}) : super(key: key);

  @override
  _PastPaymentWidgetState createState() => _PastPaymentWidgetState();
}

class _PastPaymentWidgetState extends State<PastPaymentWidget> {
  late PastPaymentModel _model;

  final scaffoldKey = GlobalKey<ScaffoldState>();

  @override
  void initState() {
    super.initState();
    _model = createModel(context, () => PastPaymentModel());
  }

  @override
  void dispose() {
    _model.dispose();

    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      key: scaffoldKey,
      backgroundColor: FlutterFlowTheme.of(context).background,
      appBar: AppBar(
        backgroundColor: FlutterFlowTheme.of(context).customColor1,
        automaticallyImplyLeading: false,
        leading: InkWell(
          splashColor: Colors.transparent,
          focusColor: Colors.transparent,
          hoverColor: Colors.transparent,
          highlightColor: Colors.transparent,
          onTap: () async {
            context.pop();
          },
          child: Icon(
            Icons.arrow_back,
            color: FlutterFlowTheme.of(context).dark400,
            size: 24.0,
          ),
        ),
        title: Text(
          'Transaction Details',
          style: FlutterFlowTheme.of(context).bodyMedium,
        ),
        actions: [],
        centerTitle: true,
        elevation: 0.0,
      ),
      body: SafeArea(
        top: true,
        child: Column(
          mainAxisSize: MainAxisSize.max,
          mainAxisAlignment: MainAxisAlignment.start,
          children: [
            Row(
              mainAxisSize: MainAxisSize.max,
              children: [
                Container(
                  width: MediaQuery.sizeOf(context).width * 1.0,
                  height: 450.0,
                  decoration: BoxDecoration(
                    color: Colors.white,
                  ),
                  child: Container(
                    width: 100.0,
                    height: 100.0,
                    decoration: BoxDecoration(
                      color: FlutterFlowTheme.of(context).customColor1,
                    ),
                    child: Column(
                      mainAxisSize: MainAxisSize.max,
                      children: [
                        Padding(
                          padding: EdgeInsetsDirectional.fromSTEB(
                              0.0, 12.0, 0.0, 0.0),
                          child: Row(
                            mainAxisSize: MainAxisSize.max,
                            mainAxisAlignment: MainAxisAlignment.center,
                            children: [
                              Container(
                                width: 330.0,
                                height: 180.0,
                                decoration: BoxDecoration(
                                  color: Color(0xFF3326A2),
                                  borderRadius: BorderRadius.circular(12.0),
                                ),
                                child: Card(
                                  clipBehavior: Clip.antiAliasWithSaveLayer,
                                  color: FlutterFlowTheme.of(context).secondary,
                                  elevation: 6.0,
                                  shape: RoundedRectangleBorder(
                                    borderRadius: BorderRadius.circular(8.0),
                                  ),
                                  child: Stack(
                                    children: [
                                      Align(
                                        alignment:
                                            AlignmentDirectional(-0.80, -0.65),
                                        child: Image.asset(
                                          'assets/images/logoFleetWhite@3x.png',
                                          width: 170.0,
                                          height: 40.0,
                                          fit: BoxFit.fitHeight,
                                        ),
                                      ),
                                      Align(
                                        alignment:
                                            AlignmentDirectional(-0.80, 0.55),
                                        child: Padding(
                                          padding:
                                              EdgeInsetsDirectional.fromSTEB(
                                                  0.0, 0.0, 0.0, 4.0),
                                          child: Text(
                                            'Andrew Daniels',
                                            textAlign: TextAlign.start,
                                            style: FlutterFlowTheme.of(context)
                                                .titleMedium
                                                .override(
                                                  fontFamily: 'Outfit',
                                                  color: FlutterFlowTheme.of(
                                                          context)
                                                      .alternate,
                                                ),
                                          ),
                                        ),
                                      ),
                                      Align(
                                        alignment:
                                            AlignmentDirectional(-0.85, 0.80),
                                        child: Text(
                                          '•••• •••• •••• 3452',
                                          style: FlutterFlowTheme.of(context)
                                              .bodyMedium
                                              .override(
                                                fontFamily: 'Outfit',
                                                color: Color(0xB2FFFFFF),
                                                fontSize: 14.0,
                                                fontWeight: FontWeight.normal,
                                              ),
                                        ),
                                      ),
                                      Align(
                                        alignment:
                                            AlignmentDirectional(0.80, 0.65),
                                        child: ClipRRect(
                                          borderRadius:
                                              BorderRadius.circular(8.0),
                                          child: Image.network(
                                            'https://usa.visa.com/dam/VCOM/regional/ve/romania/blogs/hero-image/visa-logo-800x450.jpg',
                                            width: 50.0,
                                            height: 30.0,
                                            fit: BoxFit.fitHeight,
                                          ),
                                        ),
                                      ),
                                    ],
                                  ),
                                ),
                              ),
                            ],
                          ),
                        ),
                        Padding(
                          padding: EdgeInsetsDirectional.fromSTEB(
                              16.0, 20.0, 0.0, 4.0),
                          child: Row(
                            mainAxisSize: MainAxisSize.max,
                            children: [
                              Text(
                                'Amount',
                                style: FlutterFlowTheme.of(context).bodySmall,
                              ),
                            ],
                          ),
                        ),
                        Padding(
                          padding: EdgeInsetsDirectional.fromSTEB(
                              16.0, 0.0, 0.0, 0.0),
                          child: Row(
                            mainAxisSize: MainAxisSize.max,
                            children: [
                              Padding(
                                padding: EdgeInsetsDirectional.fromSTEB(
                                    4.0, 4.0, 4.0, 4.0),
                                child: Icon(
                                  Icons.download_rounded,
                                  color: FlutterFlowTheme.of(context).primary,
                                  size: 32.0,
                                ),
                              ),
                              Padding(
                                padding: EdgeInsetsDirectional.fromSTEB(
                                    12.0, 0.0, 0.0, 0.0),
                                child: Text(
                                  '+\$502.20',
                                  style:
                                      FlutterFlowTheme.of(context).displaySmall,
                                ),
                              ),
                            ],
                          ),
                        ),
                        Padding(
                          padding: EdgeInsetsDirectional.fromSTEB(
                              0.0, 12.0, 0.0, 12.0),
                          child: Container(
                            width: 330.0,
                            height: 2.0,
                            decoration: BoxDecoration(
                              color: FlutterFlowTheme.of(context).grayLighter,
                              borderRadius: BorderRadius.circular(4.0),
                            ),
                          ),
                        ),
                        Padding(
                          padding: EdgeInsetsDirectional.fromSTEB(
                              16.0, 12.0, 0.0, 0.0),
                          child: Row(
                            mainAxisSize: MainAxisSize.max,
                            children: [
                              Text(
                                'Business Name',
                                style: FlutterFlowTheme.of(context).bodySmall,
                              ),
                            ],
                          ),
                        ),
                        Padding(
                          padding: EdgeInsetsDirectional.fromSTEB(
                              16.0, 4.0, 0.0, 0.0),
                          child: Row(
                            mainAxisSize: MainAxisSize.max,
                            children: [
                              Text(
                                'Cedar Coffee Supply',
                                style: FlutterFlowTheme.of(context).titleMedium,
                              ),
                            ],
                          ),
                        ),
                        Padding(
                          padding: EdgeInsetsDirectional.fromSTEB(
                              16.0, 12.0, 0.0, 0.0),
                          child: Row(
                            mainAxisSize: MainAxisSize.max,
                            children: [
                              Text(
                                'Purchase Date',
                                style: FlutterFlowTheme.of(context).bodySmall,
                              ),
                            ],
                          ),
                        ),
                        Padding(
                          padding: EdgeInsetsDirectional.fromSTEB(
                              16.0, 4.0, 0.0, 0.0),
                          child: Row(
                            mainAxisSize: MainAxisSize.max,
                            children: [
                              Text(
                                'May 4th, 4:49pm - 2021',
                                style: FlutterFlowTheme.of(context).titleMedium,
                              ),
                            ],
                          ),
                        ),
                      ],
                    ),
                  ),
                ),
              ],
            ),
          ],
        ),
      ),
    );
  }
}
