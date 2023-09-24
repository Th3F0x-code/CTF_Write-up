import '/flutter_flow/flutter_flow_theme.dart';
import '/flutter_flow/flutter_flow_util.dart';
import 'package:flutter/material.dart';
import 'package:flutter_spinkit/flutter_spinkit.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:provider/provider.dart';
import 'appointment_empty_copy_model.dart';
export 'appointment_empty_copy_model.dart';

class AppointmentEmptyCopyWidget extends StatefulWidget {
  const AppointmentEmptyCopyWidget({Key? key}) : super(key: key);

  @override
  _AppointmentEmptyCopyWidgetState createState() =>
      _AppointmentEmptyCopyWidgetState();
}

class _AppointmentEmptyCopyWidgetState
    extends State<AppointmentEmptyCopyWidget> {
  late AppointmentEmptyCopyModel _model;

  @override
  void setState(VoidCallback callback) {
    super.setState(callback);
    _model.onUpdate();
  }

  @override
  void initState() {
    super.initState();
    _model = createModel(context, () => AppointmentEmptyCopyModel());
  }

  @override
  void dispose() {
    _model.maybeDispose();

    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Container(
      width: double.infinity,
      height: 90.0,
      decoration: BoxDecoration(
        color: FlutterFlowTheme.of(context).primaryBackground,
        borderRadius: BorderRadius.circular(8.0),
      ),
      child: Padding(
        padding: EdgeInsetsDirectional.fromSTEB(12.0, 12.0, 12.0, 12.0),
        child: Row(
          mainAxisSize: MainAxisSize.max,
          children: [
            Icon(
              Icons.access_time_rounded,
              color: FlutterFlowTheme.of(context).secondaryText,
              size: 36.0,
            ),
            Expanded(
              child: Padding(
                padding: EdgeInsetsDirectional.fromSTEB(12.0, 0.0, 12.0, 0.0),
                child: Column(
                  mainAxisSize: MainAxisSize.max,
                  mainAxisAlignment: MainAxisAlignment.center,
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Text(
                      'No Pending',
                      textAlign: TextAlign.center,
                      style: FlutterFlowTheme.of(context).titleSmall,
                    ),
                    Padding(
                      padding:
                          EdgeInsetsDirectional.fromSTEB(0.0, 4.0, 0.0, 0.0),
                      child: Text(
                        'You doin\'t have any upcoming appointments.',
                        textAlign: TextAlign.start,
                        style: FlutterFlowTheme.of(context).bodySmall,
                      ),
                    ),
                  ],
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }
}
