idee pour ouverture: teteer à nombre de paraletres egaux et trouver le mielleur compromis nombre de paaprm et accuracy. 
pour comparer il faut aussi le nombre d'epoch et donc le nombre d'operations necessaire au training.

pour la presenation: presnter la diff des ajourts genre smoothing, augmentation, attention etc

pointnet V2 demande peut etre plus d'epcohs de training

conclsuion: fidna radar agnostic model

choose 10 seeds number and repost test scores for those 10 trials



# DGUHA/Pointnet V1
SEED = 1234
DGUHA/Pointnet V1
Best validation checkpoint: checkpoint_35.pt
Validation accuracy: 0.9580
Test macro F1: 0.9263
Test accuracy: 0.9255
{'running': 0.9777777791023254, 'jumping': 0.978723406791687, 'sitting_down_and_standing_up': 1.0, 'both_upper_limb_extension': 0.8260869383811951, 'falling_forward': 1.0, 'right_limb_extension': 0.8780487775802612, 'left_limb_extension': 0.8235294222831726}

SEED = 1235
DGUHA/Pointnet V1
Best validation checkpoint: checkpoint_39.pt
Validation accuracy: 0.9832
Test macro F1: 0.9199
Test accuracy: 0.9193
{'running': 0.9387755393981934, 'jumping': 0.930232584476471, 'sitting_down_and_standing_up': 1.0, 'both_upper_limb_extension': 0.782608687877655, 'falling_forward': 1.0, 'right_limb_extension': 0.930232584476471, 'left_limb_extension': 0.8571428656578064}

SEED = 1236
DGUHA/Pointnet V1
Best validation checkpoint: checkpoint_31.pt
Validation accuracy: 0.9832
Test macro F1: 0.8981
Test accuracy: 0.8944
{'running': 0.9333333373069763, 'jumping': 0.9545454382896423, 'sitting_down_and_standing_up': 1.0, 'both_upper_limb_extension': 0.7317073345184326, 'falling_forward': 1.0, 'right_limb_extension': 0.930232584476471, 'left_limb_extension': 0.7368420958518982}

SEED = 1237
DGUHA/Pointnet V1
Best validation checkpoint: checkpoint_39.pt
Validation accuracy: 0.9496
Test macro F1: 0.9363
Test accuracy: 0.9379
{'running': 0.9777777791023254, 'jumping': 0.95652174949646, 'sitting_down_and_standing_up': 0.978723406791687, 'both_upper_limb_extension': 0.7894737124443054, 'falling_forward': 1.0, 'right_limb_extension': 1.0, 'left_limb_extension': 0.8518518805503845}

SEED = 1238
DGUHA/Pointnet V1
Best validation checkpoint: checkpoint_37.pt
Validation accuracy: 0.9664
Test macro F1: 0.9217
Test accuracy: 0.9193
{'running': 0.930232584476471, 'jumping': 1.0, 'sitting_down_and_standing_up': 1.0, 'both_upper_limb_extension': 0.7916666865348816, 'falling_forward': 1.0, 'right_limb_extension': 0.930232584476471, 'left_limb_extension': 0.800000011920929}



# DGUHA/PointNet V2 with 400 frames
final results:
SEED = 1234
DGUHA/PointNet V2 with 400 frames
Best validation checkpoint: checkpoint_38.pt
Validation accuracy: 0.9580
Test macro F1: 0.9449
Test accuracy: 0.9441
{'running': 0.9387755393981934, 'jumping': 0.930232584476471, 'sitting_down_and_standing_up': 1.0, 'both_upper_limb_extension': 0.930232584476471, 'falling_forward': 1.0, 'right_limb_extension': 0.930232584476471, 'left_limb_extension': 0.8846153616905212}

SEED = 1235
DGUHA/PointNet V2 with 400 frames
Best validation checkpoint: checkpoint_30.pt
Validation accuracy: 0.9832
Test macro F1: 0.9514
Test accuracy: 0.9503
{'running': 1.0, 'jumping': 1.0, 'sitting_down_and_standing_up': 1.0, 'both_upper_limb_extension': 0.8780487775802612, 'falling_forward': 1.0, 'right_limb_extension': 0.930232584476471, 'left_limb_extension': 0.8518518805503845}

SEED = 1236
DGUHA/PointNet V2 with 400 frames
Best validation checkpoint: checkpoint_33.pt
Validation accuracy: 0.9664
Test macro F1: 0.8960
Test accuracy: 0.9006
{'running': 0.8627451062202454, 'jumping': 0.7027027010917664, 'sitting_down_and_standing_up': 0.9200000166893005, 'both_upper_limb_extension': 0.930232584476471, 'falling_forward': 1.0, 'right_limb_extension': 0.9545454382896423, 'left_limb_extension': 0.9019607901573181}

SEED = 1237
DGUHA/PointNet V2 with 400 frames
Best validation checkpoint: checkpoint_39.pt
Validation accuracy: 0.9496
Test macro F1: 0.9448
Test accuracy: 0.9441
{'running': 0.9545454382896423, 'jumping': 0.95652174949646, 'sitting_down_and_standing_up': 0.978723406791687, 'both_upper_limb_extension': 0.930232584476471, 'falling_forward': 1.0, 'right_limb_extension': 0.9090909361839294, 'left_limb_extension': 0.8846153616905212}

SEED = 1238
DGUHA/PointNet V2 with 400 frames
Best validation checkpoint: checkpoint_38.pt
Validation accuracy: 0.9580
Test macro F1: 0.9001
Test accuracy: 0.9006
{'running': 0.8399999737739563, 'jumping': 0.8205128312110901, 'sitting_down_and_standing_up': 0.9583333134651184, 'both_upper_limb_extension': 0.9090909361839294, 'falling_forward': 1.0, 'right_limb_extension': 0.9047619104385376, 'left_limb_extension': 0.8679245114326477}


# Radatatouille/ pointnet V2
SEED = 1234
Radatatouille/ pointnet V2
Best validation checkpoint: checkpoint_25.pt
Validation accuracy: 0.9599
Test macro F1: 0.8674
Test accuracy: 0.8685
{'sit': 0.8790637254714966, 'stand_up': 0.8558139801025391}

SEED = 1235
Radatatouille/ pointnet V2
Best validation checkpoint: checkpoint_26.pt
Validation accuracy: 0.8856
Test macro F1: 0.8412
Test accuracy: 0.8430
{'sit': 0.8582375645637512, 'stand_up': 0.8240887522697449}

SEED = 1236 (gradient loss exploding)
Radatatouille/ pointnet V2
Best validation checkpoint: checkpoint_00.pt
Validation accuracy: 0.8390
Test macro F1: 0.6902
Test accuracy: 0.6959
{'sit': 0.6481178402900696, 'stand_up': 0.7322540283203125}

SEED = 1237
Radatatouille/ pointnet V2
Best validation checkpoint: checkpoint_11.pt
Validation accuracy: 0.8983
Test macro F1: 0.7890
Test accuracy: 0.7893
{'sit': 0.796169638633728, 'stand_up': 0.7818447947502136}

SEED = 1238
Radatatouille/ pointnet V2
Best validation checkpoint: checkpoint_22.pt
Validation accuracy: 0.8475
Test macro F1: 0.8113
Test accuracy: 0.8119
{'sit': 0.8219544887542725, 'stand_up': 0.8005996942520142}


# Radatatouille/ pointnet V1
SEED = 1234
Radatatouille/ pointnet V1
Best validation checkpoint: checkpoint_39.pt
Validation accuracy: 0.9964
Test macro F1: 0.8222
Test accuracy: 0.8274
{'sit': 0.8526570200920105, 'stand_up': 0.7918089032173157}

SEED = 1235
Radatatouille/ pointnet V1
Best validation checkpoint: checkpoint_39.pt
Validation accuracy: 0.9958
Test macro F1: 0.8222
Test accuracy: 0.8274
{'sit': 0.8526570200920105, 'stand_up': 0.7918089032173157}

SEED = 1236
Radatatouille/ pointnet V1
Best validation checkpoint: checkpoint_34.pt
Validation accuracy: 1.0000
Test macro F1: 0.8359
Test accuracy: 0.8402
{'sit': 0.8623629808425903, 'stand_up': 0.8094435334205627}

SEED = 1237
Radatatouille/ pointnet V1
Best validation checkpoint: checkpoint_30.pt
Validation accuracy: 1.0000
Test macro F1: 0.7992
Test accuracy: 0.8062
{'sit': 0.8367103934288025, 'stand_up': 0.7617391347885132}

SEED = 1238
Radatatouille/ pointnet V1
Best validation checkpoint: checkpoint_39.pt
Validation accuracy: 0.9958
Test macro F1: 0.8222
Test accuracy: 0.8274
{'sit': 0.8526570200920105, 'stand_up': 0.7918089032173157}


# MARS / pointnetV1
SEED = 1234
MARS/ pointnet V1
Best validation checkpoint: checkpoint_37.pt
Validation accuracy: 1.0000
Test macro F1: 0.7891
Test accuracy: 0.8917
{'Left_upper_limb_extension': 1.0, 'Right_upper_limb_extension': 1.0, 'Both_upper_limb_extension': 0.9811320900917053, 'Left_front_lunge': 0.9811320900917053, 'Right_front_lunge': 1.0, 'Squad': 0.9824561476707458, 'Left_side_lunge': 0.9642857313156128, 'Right_side_lunge': 0.9824561476707458, 'Left_limb_extension': 0.0, 'Right_limb_extension': 0.0}

SEED = 1235
MARS/ pointnet V1
Best validation checkpoint: checkpoint_37.pt
Validation accuracy: 1.0000
Test macro F1: 0.7928
Test accuracy: 0.8958
{'Left_upper_limb_extension': 1.0, 'Right_upper_limb_extension': 1.0, 'Both_upper_limb_extension': 1.0, 'Left_front_lunge': 0.9811320900917053, 'Right_front_lunge': 1.0, 'Squad': 0.9818181991577148, 'Left_side_lunge': 1.0, 'Right_side_lunge': 0.9655172228813171, 'Left_limb_extension': 0.0, 'Right_limb_extension': 0.0}

SEED = 1236
MARS/ pointnet V1
Best validation checkpoint: checkpoint_39.pt
Validation accuracy: 1.0000
Test macro F1: 0.7777
Test accuracy: 0.8792
{'Left_upper_limb_extension': 1.0, 'Right_upper_limb_extension': 0.936170220375061, 'Both_upper_limb_extension': 1.0, 'Left_front_lunge': 1.0, 'Right_front_lunge': 1.0, 'Squad': 0.9491525292396545, 'Left_side_lunge': 0.9090909361839294, 'Right_side_lunge': 0.9824561476707458, 'Left_limb_extension': 0.0, 'Right_limb_extension': 0.0}

SEED = 1237
MARS/ pointnet V1
Best validation checkpoint: checkpoint_39.pt
Validation accuracy: 0.9964
Test macro F1: 0.7837
Test accuracy: 0.8833
{'Left_upper_limb_extension': 1.0, 'Right_upper_limb_extension': 1.0, 'Both_upper_limb_extension': 0.9811320900917053, 'Left_front_lunge': 0.9811320900917053, 'Right_front_lunge': 1.0, 'Squad': 0.9491525292396545, 'Left_side_lunge': 0.9259259104728699, 'Right_side_lunge': 1.0, 'Left_limb_extension': 0.0, 'Right_limb_extension': 0.0}

SEED = 1238
MARS/ pointnet V1
Best validation checkpoint: checkpoint_39.pt
Validation accuracy: 1.0000
Test macro F1: 0.7964
Test accuracy: 0.9000
{'Left_upper_limb_extension': 1.0, 'Right_upper_limb_extension': 1.0, 'Both_upper_limb_extension': 1.0, 'Left_front_lunge': 0.9811320900917053, 'Right_front_lunge': 1.0, 'Squad': 1.0, 'Left_side_lunge': 1.0, 'Right_side_lunge': 0.9824561476707458, 'Left_limb_extension': 0.0, 'Right_limb_extension': 0.0}

# MARS / pointnetV2
SEED = 1234
MARS/ pointnet V2
Best validation checkpoint: checkpoint_34.pt
Validation accuracy: 0.9929
Test macro F1: 0.7718
Test accuracy: 0.8689
{'Left_upper_limb_extension': 1.0, 'Right_upper_limb_extension': 1.0, 'Both_upper_limb_extension': 0.9230769276618958, 'Left_front_lunge': 1.0, 'Right_front_lunge': 1.0, 'Squad': 0.9285714030265808, 'Left_side_lunge': 0.9629629850387573, 'Right_side_lunge': 0.9032257795333862, 'Left_limb_extension': 0.0, 'Right_limb_extension': 0.0}

SEED = 1235
MARS/ pointnet V2
Best validation checkpoint: checkpoint_39.pt
Validation accuracy: 0.9929
Test macro F1: 0.7103
Test accuracy: 0.7951
{'Left_upper_limb_extension': 1.0, 'Right_upper_limb_extension': 1.0, 'Both_upper_limb_extension': 0.7272727489471436, 'Left_front_lunge': 0.9629629850387573, 'Right_front_lunge': 1.0, 'Squad': 0.800000011920929, 'Left_side_lunge': 0.6842105388641357, 'Right_side_lunge': 0.9285714030265808, 'Left_limb_extension': 0.0, 'Right_limb_extension': 0.0}

SEED = 1236
MARS/ pointnet V2
Best validation checkpoint: checkpoint_36.pt
Validation accuracy: 1.0000
Test macro F1: 0.8000
Test accuracy: 0.9016
{'Left_upper_limb_extension': 1.0, 'Right_upper_limb_extension': 1.0, 'Both_upper_limb_extension': 1.0, 'Left_front_lunge': 1.0, 'Right_front_lunge': 1.0, 'Squad': 1.0, 'Left_side_lunge': 1.0, 'Right_side_lunge': 1.0, 'Left_limb_extension': 0.0, 'Right_limb_extension': 0.0}

SEED = 1237
MARS/ pointnet V2
Best validation checkpoint: checkpoint_37.pt
Validation accuracy: 1.0000
Test macro F1: 0.7224
Test accuracy: 0.8115
{'Left_upper_limb_extension': 1.0, 'Right_upper_limb_extension': 1.0, 'Both_upper_limb_extension': 0.7272727489471436, 'Left_front_lunge': 0.9333333373069763, 'Right_front_lunge': 1.0, 'Squad': 0.8333333134651184, 'Left_side_lunge': 0.7647058963775635, 'Right_side_lunge': 0.9655172228813171, 'Left_limb_extension': 0.0, 'Right_limb_extension': 0.0}

SEED = 1238
MARS/ pointnet V2
Best validation checkpoint: checkpoint_30.pt
Validation accuracy: 0.9857
Test macro F1: 0.7573
Test accuracy: 0.8525
{'Left_upper_limb_extension': 1.0, 'Right_upper_limb_extension': 1.0, 'Both_upper_limb_extension': 0.9230769276618958, 'Left_front_lunge': 1.0, 'Right_front_lunge': 1.0, 'Squad': 0.8799999952316284, 'Left_side_lunge': 0.9032257795333862, 'Right_side_lunge': 0.8666666746139526, 'Left_limb_extension': 0.0, 'Right_limb_extension': 0.0}