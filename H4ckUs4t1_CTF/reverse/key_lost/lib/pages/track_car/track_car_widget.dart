import '/backend/backend.dart';
import '/flutter_flow/flutter_flow_google_map.dart';
import '/flutter_flow/flutter_flow_icon_button.dart';
import '/flutter_flow/flutter_flow_theme.dart';
import '/flutter_flow/flutter_flow_util.dart';
import '/flutter_flow/flutter_flow_widgets.dart';
import 'package:flutter/material.dart';
import 'package:flutter_spinkit/flutter_spinkit.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:provider/provider.dart';
import 'track_car_model.dart';
export 'track_car_model.dart';

class TrackCarWidget extends StatefulWidget {
  const TrackCarWidget({Key? key}) : super(key: key);

  @override
  _TrackCarWidgetState createState() => _TrackCarWidgetState();
}

class _TrackCarWidgetState extends State<TrackCarWidget> {
  late TrackCarModel _model;

  final scaffoldKey = GlobalKey<ScaffoldState>();

  @override
  void initState() {
    super.initState();
    _model = createModel(context, () => TrackCarModel());
  }

  @override
  void dispose() {
    _model.dispose();

    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return StreamBuilder<List<ProductNameRecord>>(
      stream: queryProductNameRecord(
        singleRecord: true,
      ),
      builder: (context, snapshot) {
        // Customize what your widget looks like when it's loading.
        if (!snapshot.hasData) {
          return Scaffold(
            body: Center(
              child: SizedBox(
                width: 50.0,
                height: 50.0,
                child: SpinKitCubeGrid(
                  color: FlutterFlowTheme.of(context).primary,
                  size: 50.0,
                ),
              ),
            ),
          );
        }
        List<ProductNameRecord> trackCarProductNameRecordList = snapshot.data!;
        // Return an empty Container when the item does not exist.
        if (snapshot.data!.isEmpty) {
          return Container();
        }
        final trackCarProductNameRecord =
            trackCarProductNameRecordList.isNotEmpty
                ? trackCarProductNameRecordList.first
                : null;
        return Scaffold(
          key: scaffoldKey,
          resizeToAvoidBottomInset: false,
          body: Stack(
            children: [
              Column(
                mainAxisSize: MainAxisSize.max,
                children: [
                  Expanded(
                    child: Builder(builder: (context) {
                      final _googleMapMarker = trackCarProductNameRecord;
                      return FlutterFlowGoogleMap(
                        controller: _model.googleMapsController,
                        onCameraIdle: (latLng) =>
                            _model.googleMapsCenter = latLng,
                        initialLocation: _model.googleMapsCenter ??=
                            trackCarProductNameRecord!.productLocation!,
                        markers: [
                          if (_googleMapMarker != null)
                            FlutterFlowMarker(
                              _googleMapMarker.reference.path,
                              _googleMapMarker.productLocation!,
                            ),
                        ],
                        markerColor: GoogleMarkerColor.blue,
                        mapType: MapType.normal,
                        style: GoogleMapStyle.standard,
                        initialZoom: 14.0,
                        allowInteraction: true,
                        allowZoom: true,
                        showZoomControls: false,
                        showLocation: true,
                        showCompass: false,
                        showMapToolbar: false,
                        showTraffic: false,
                        centerMapOnMarkerTap: true,
                      );
                    }),
                  ),
                ],
              ),
              Padding(
                padding: EdgeInsetsDirectional.fromSTEB(20.0, 50.0, 20.0, 0.0),
                child: Row(
                  mainAxisSize: MainAxisSize.max,
                  mainAxisAlignment: MainAxisAlignment.start,
                  children: [
                    Card(
                      clipBehavior: Clip.antiAliasWithSaveLayer,
                      color: FlutterFlowTheme.of(context).dark400,
                      elevation: 2.0,
                      shape: RoundedRectangleBorder(
                        borderRadius: BorderRadius.circular(40.0),
                      ),
                      child: FlutterFlowIconButton(
                        borderColor: Colors.transparent,
                        borderRadius: 30.0,
                        buttonSize: 46.0,
                        icon: Icon(
                          Icons.arrow_back_rounded,
                          color: FlutterFlowTheme.of(context).customColor1,
                          size: 20.0,
                        ),
                        onPressed: () async {
                          context.pop();
                        },
                      ),
                    ),
                  ],
                ),
              ),
              Align(
                alignment: AlignmentDirectional(0.00, 1.00),
                child: Padding(
                  padding: EdgeInsetsDirectional.fromSTEB(0.0, 0.0, 0.0, 44.0),
                  child: Row(
                    mainAxisSize: MainAxisSize.max,
                    mainAxisAlignment: MainAxisAlignment.center,
                    children: [
                      Material(
                        color: Colors.transparent,
                        elevation: 3.0,
                        shape: RoundedRectangleBorder(
                          borderRadius: BorderRadius.circular(8.0),
                        ),
                        child: Container(
                          width: MediaQuery.sizeOf(context).width * 0.96,
                          height: 200.0,
                          decoration: BoxDecoration(
                            color: FlutterFlowTheme.of(context).customColor1,
                            borderRadius: BorderRadius.circular(8.0),
                          ),
                          child: Padding(
                            padding: EdgeInsetsDirectional.fromSTEB(
                                16.0, 12.0, 16.0, 12.0),
                            child: Column(
                              mainAxisSize: MainAxisSize.max,
                              crossAxisAlignment: CrossAxisAlignment.start,
                              children: [
                                Text(
                                  'Battery Status',
                                  style:
                                      FlutterFlowTheme.of(context).titleMedium,
                                ),
                                Padding(
                                  padding: EdgeInsetsDirectional.fromSTEB(
                                      0.0, 4.0, 0.0, 8.0),
                                  child: Text(
                                    'Below is the status of your current charge.',
                                    style:
                                        FlutterFlowTheme.of(context).bodySmall,
                                  ),
                                ),
                                Padding(
                                  padding: EdgeInsetsDirectional.fromSTEB(
                                      0.0, 0.0, 0.0, 8.0),
                                  child: Row(
                                    mainAxisSize: MainAxisSize.max,
                                    mainAxisAlignment: MainAxisAlignment.center,
                                    children: [
                                      Stack(
                                        children: [
                                          Container(
                                            width: MediaQuery.sizeOf(context)
                                                    .width *
                                                0.9,
                                            height: 20.0,
                                            constraints: BoxConstraints(
                                              maxWidth: 300.0,
                                            ),
                                            decoration: BoxDecoration(
                                              color:
                                                  FlutterFlowTheme.of(context)
                                                      .grayLighter,
                                              borderRadius:
                                                  BorderRadius.circular(8.0),
                                            ),
                                          ),
                                          Padding(
                                            padding:
                                                EdgeInsetsDirectional.fromSTEB(
                                                    2.0, 2.0, 2.0, 2.0),
                                            child: Container(
                                              width: MediaQuery.sizeOf(context)
                                                      .width *
                                                  0.4,
                                              height: 16.0,
                                              decoration: BoxDecoration(
                                                color:
                                                    FlutterFlowTheme.of(context)
                                                        .primary,
                                                borderRadius:
                                                    BorderRadius.circular(8.0),
                                              ),
                                            ),
                                          ),
                                        ],
                                      ),
                                    ],
                                  ),
                                ),
                                Divider(
                                  height: 3.0,
                                  thickness: 1.0,
                                  color:
                                      FlutterFlowTheme.of(context).grayLighter,
                                ),
                                Padding(
                                  padding: EdgeInsetsDirectional.fromSTEB(
                                      0.0, 12.0, 0.0, 20.0),
                                  child: Row(
                                    mainAxisSize: MainAxisSize.max,
                                    mainAxisAlignment:
                                        MainAxisAlignment.spaceEvenly,
                                    children: [
                                      Column(
                                        mainAxisSize: MainAxisSize.max,
                                        mainAxisAlignment:
                                            MainAxisAlignment.spaceAround,
                                        children: [
                                          Padding(
                                            padding:
                                                EdgeInsetsDirectional.fromSTEB(
                                                    0.0, 0.0, 0.0, 8.0),
                                            child: Text(
                                              'Charge',
                                              style:
                                                  FlutterFlowTheme.of(context)
                                                      .bodySmall,
                                            ),
                                          ),
                                          Text(
                                            '70%',
                                            style: FlutterFlowTheme.of(context)
                                                .displaySmall,
                                          ),
                                        ],
                                      ),
                                      Column(
                                        mainAxisSize: MainAxisSize.max,
                                        mainAxisAlignment:
                                            MainAxisAlignment.spaceAround,
                                        children: [
                                          Padding(
                                            padding:
                                                EdgeInsetsDirectional.fromSTEB(
                                                    0.0, 0.0, 0.0, 8.0),
                                            child: Text(
                                              'Range',
                                              style:
                                                  FlutterFlowTheme.of(context)
                                                      .bodySmall,
                                            ),
                                          ),
                                          Text(
                                            '329m',
                                            style: FlutterFlowTheme.of(context)
                                                .displaySmall,
                                          ),
                                        ],
                                      ),
                                      Column(
                                        mainAxisSize: MainAxisSize.max,
                                        mainAxisAlignment:
                                            MainAxisAlignment.spaceAround,
                                        children: [
                                          Padding(
                                            padding:
                                                EdgeInsetsDirectional.fromSTEB(
                                                    0.0, 0.0, 0.0, 8.0),
                                            child: Text(
                                              'MPH',
                                              style:
                                                  FlutterFlowTheme.of(context)
                                                      .bodySmall,
                                            ),
                                          ),
                                          Text(
                                            '72',
                                            style: FlutterFlowTheme.of(context)
                                                .displaySmall,
                                          ),
                                        ],
                                      ),
                                    ],
                                  ),
                                ),
                              ],
                            ),
                          ),
                        ),
                      ),
                    ],
                  ),
                ),
              ),
            ],
          ),
        );
      },
    );
  }
}
