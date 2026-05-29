idee pour ouverture: teteer à nombre de paraletres egaux et trouver le mielleur compromis nombre de paaprm et accuracy. 
pour comparer il faut aussi le nombre d'epoch et donc le nombre d'operations necessaire au training.

pour la presenation: presnter la diff des ajourts genre smoothing, augmentation, attention etc

pointnet V2 demande peut etre plus d'epcohs de training

conclsuion: fidna radar agnostic model

choose 10 seeds number and repost test scores for those 10 trials


final results:
SEED = 1234
DGUHA/PointNet V2
Best validation checkpoint: checkpoint_38.pt
Validation accuracy: 0.9580
Test macro F1: 0.9449
Test accuracy: 0.9441
{'running': 0.9387755393981934, 'jumping': 0.930232584476471, 'sitting_down_and_standing_up': 1.0, 'both_upper_limb_extension': 0.930232584476471, 'falling_forward': 1.0, 'right_limb_extension': 0.930232584476471, 'left_limb_extension': 0.8846153616905212}

SEED = 1234
DGUHA/Pointnet V1
Best validation checkpoint: checkpoint_35.pt
Validation accuracy: 0.9580
Test macro F1: 0.9263
Test accuracy: 0.9255
{'running': 0.9777777791023254, 'jumping': 0.978723406791687, 'sitting_down_and_standing_up': 1.0, 'both_upper_limb_extension': 0.8260869383811951, 'falling_forward': 1.0, 'right_limb_extension': 0.8780487775802612, 'left_limb_extension': 0.8235294222831726}

SEED = 1235
DGUHA/PointNet V2
Best validation checkpoint: checkpoint_30.pt
Validation accuracy: 0.9832
Test macro F1: 0.9514
Test accuracy: 0.9503
{'running': 1.0, 'jumping': 1.0, 'sitting_down_and_standing_up': 1.0, 'both_upper_limb_extension': 0.8780487775802612, 'falling_forward': 1.0, 'right_limb_extension': 0.930232584476471, 'left_limb_extension': 0.8518518805503845}