V1 with smoothing and augmnetion
Best validation checkpoint: checkpoint_14.pt
Validation accuracy: 1.0000
Test macro F1: 0.9650
Test accuracy: 0.9639
{'boxing': 1.0, 'jack': 1.0, 'jump': 0.9076305031776428, 'squats': 0.9790794849395752, 'walk': 0.9383561611175537}

and with 40 epochs:
Best validation checkpoint: checkpoint_33.pt
Validation accuracy: 1.0000
Test macro F1: 0.9651
Test accuracy: 0.9639
{'boxing': 1.0, 'jack': 0.9915966391563416, 'jump': 0.9061224460601807, 'squats': 0.9958506226539612, 'walk': 0.9319728016853333}





V2 without augmentation
Best validation checkpoint: checkpoint_19.pt
Validation accuracy: 1.0000
Test macro F1: 0.9550
Test accuracy: 0.9545
{'boxing': 0.9961089491844177, 'jack': 0.9696969985961914, 'jump': 0.9061224460601807, 'squats': 0.9632652997970581, 'walk': 0.9395973086357117}

V2 with augmentation
Best validation checkpoint: checkpoint_19.pt
Validation accuracy: 1.0000
Test macro F1: 0.9513
Test accuracy: 0.9514
{'boxing': 0.9591078162193298, 'jack': 0.9327354431152344, 'jump': 0.9176470637321472, 'squats': 0.9915966391563416, 'walk': 0.9553264379501343}

V2 with smoothing augmentation and 40 epochs
Best validation checkpoint: checkpoint_39.pt
Validation accuracy: 1.0000
Test macro F1: 0.9648
Test accuracy: 0.9639
{'boxing': 1.0, 'jack': 0.9745762944221497, 'jump': 0.9189189076423645, 'squats': 0.9831932783126831, 'walk': 0.9473684430122375}

