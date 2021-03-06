#  Copyright (c) 2010 Howard Hughes Medical Institute.
#  All rights reserved.
#  Use is subject to Janelia Farm Research Campus Software Copyright 1.1 license terms.
#  http://license.janelia.org/license/jfrc_copyright_1_1.html

"""
This script recreates a circuit diagram from a paper.

Connectivity and layout from:
    "Information processing in the primate visual system: an integrated systems perspective."
    Van Essen DC, Anderson CH, Felleman DJ.
    Science. 1992 Jan 24;255(5043):419-23. Review.
    <http://dx.doi.org/10.1126/science.1734518>
"""


# Create the regions

region1 = network.createRegion(abbreviation = 'HC', name = 'Hippocampus')
region2 = network.createRegion(abbreviation = 'ERC', name = 'Entorhinal cortex')
region3 = network.createRegion(abbreviation = '36', name = 'Brodmann area 36')
region4 = network.createRegion(abbreviation = '46', name = 'Brodmann area 46')
region5 = network.createRegion(abbreviation = 'TF', name = 'parahippocampal cortex TF')
region6 = network.createRegion(abbreviation = 'TH', name = 'parahippocampal cortex TH')
region7 = network.createRegion(abbreviation = 'STPa', name = 'STPa')
region8 = network.createRegion(abbreviation = 'AITd', name = 'AITd')
region9 = network.createRegion(abbreviation = 'AITv', name = 'AITv')
region10 = network.createRegion(abbreviation = '7b', name = 'Brodmann area 7b')
region11 = network.createRegion(abbreviation = '7a', name = 'Brodmann area 7a')
region12 = network.createRegion(abbreviation = 'FEF', name = 'Frontal eye field')
region13 = network.createRegion(abbreviation = 'STPp', name = 'STPp')
region14 = network.createRegion(abbreviation = 'CIT Region', name = 'CIT Region')
region15 = network.createRegion(abbreviation = 'CITd', parentRegion = region14, name = 'CITd')
region16 = network.createRegion(abbreviation = 'CIT', parentRegion = region14, name = 'CIT CIT')
region17 = network.createRegion(abbreviation = 'CITv', parentRegion = region14, name = 'CITv')
region18 = network.createRegion(abbreviation = 'VIP', name = 'VIP')
region19 = network.createRegion(abbreviation = 'LIP', name = 'LIP')
region20 = network.createRegion(abbreviation = 'MSTl', name = 'MSTl')
region21 = network.createRegion(abbreviation = 'MSTd', name = 'MSTd')
region22 = network.createRegion(abbreviation = 'FST', name = 'FST')
region23 = network.createRegion(abbreviation = 'PIT Region', name = 'PIT Region')
region24 = network.createRegion(abbreviation = 'PITd', parentRegion = region23, name = 'PITd')
region25 = network.createRegion(abbreviation = 'PIT', parentRegion = region23, name = 'PIT PIT')
region26 = network.createRegion(abbreviation = 'PITv', parentRegion = region23, name = 'PITv')
region27 = network.createRegion(abbreviation = 'DP', name = 'DP')
region28 = network.createRegion(abbreviation = 'VOT', name = 'VOT')
region29 = network.createRegion(abbreviation = 'MDP', name = 'MDP')
region30 = network.createRegion(abbreviation = 'MIP', name = 'MIP')
region31 = network.createRegion(abbreviation = 'PO', name = 'PO')
region32 = network.createRegion(abbreviation = 'MT', name = 'MT')
region33 = network.createRegion(abbreviation = 'V4t', name = 'V4t')
region34 = network.createRegion(abbreviation = 'v4Area', name = 'V4 Region')
region35 = network.createRegion(abbreviation = 'P-B', parentRegion = region34, name = 'P-B V4')
region36 = network.createRegion(abbreviation = 'V4', parentRegion = region34, name = 'V4')
region37 = network.createRegion(abbreviation = 'P-I', parentRegion = region34, name = 'P-I V4')
region38 = network.createRegion(abbreviation = 'PIP', name = 'PIP')
region39 = network.createRegion(abbreviation = 'V3A', name = 'V3A')
region40 = network.createRegion(abbreviation = 'V3', name = 'V3')
region41 = network.createRegion(abbreviation = 'VP', name = 'VP')
region42 = network.createRegion(abbreviation = 'v2Area', name = 'V2 Region')
region43 = network.createRegion(abbreviation = 'M', parentRegion = region42, name = 'M V2')
region44 = network.createRegion(abbreviation = 'V2', parentRegion = region42, name = 'V2')
region45 = network.createRegion(abbreviation = 'P-B', parentRegion = region42, name = 'P-B V2')
region46 = network.createRegion(abbreviation = 'P-I', parentRegion = region42, name = 'P-I V2')
region47 = network.createRegion(abbreviation = 'PULV', name = 'Pulvinar')
region48 = network.createRegion(abbreviation = 'v1Area', name = 'V1 Region')
region49 = network.createRegion(abbreviation = 'M', parentRegion = region48, name = 'Magnocellular V1')
region50 = network.createRegion(abbreviation = 'V1', parentRegion = region48, name = 'V1')
region51 = network.createRegion(abbreviation = 'P-B', parentRegion = region48, name = 'P-B V1')
region52 = network.createRegion(abbreviation = 'P-I', parentRegion = region48, name = 'P-I V1')
region53 = network.createRegion(abbreviation = 'LGN', name = 'Lateral geniculate nucleus')
region54 = network.createRegion(abbreviation = 'M LGN', parentRegion = region53, name = 'Magnocellular LGN')
region55 = network.createRegion(abbreviation = 'I LGN', parentRegion = region53, name = 'I LGN')
region56 = network.createRegion(abbreviation = 'P LGN', parentRegion = region53, name = 'Parvocellular LGN')
region57 = network.createRegion(abbreviation = 'SC', name = 'Superior colliculus')
region58 = network.createRegion(abbreviation = 'Retina', name = 'Retina')
region59 = network.createRegion(abbreviation = 'M Ret', parentRegion = region58, name = 'Magnocellular Retina')
region60 = network.createRegion(abbreviation = 'P Ret', parentRegion = region58, name = 'Parvocellular Retina')
region61 = network.createRegion(abbreviation = 'other', parentRegion = region58, name = 'other Retina')

# Create the pathways

region59.projectToRegion(region54, bidirectional = False)
region60.projectToRegion(region56, bidirectional = False)
region61.projectToRegion(region57, bidirectional = False)
region57.projectToRegion(region55, bidirectional = False)
region57.projectToRegion(region47, bidirectional = False)
region54.projectToRegion(region49, bidirectional = True)
region56.projectToRegion(region51, bidirectional = True)
region56.projectToRegion(region52, bidirectional = True)
region49.projectToRegion(region40, bidirectional = True)
region49.projectToRegion(region32, bidirectional = True)
region49.projectToRegion(region43, bidirectional = False)
region50.projectToRegion(region38, bidirectional = False)
region50.projectToRegion(region31, bidirectional = False)
region50.projectToRegion(region20, bidirectional = False)
region50.projectToRegion(region33, bidirectional = True)
region50.projectToRegion(region39, bidirectional = True)
region50.projectToRegion(region36, bidirectional = True)
region50.projectToRegion(region47, bidirectional = False)
region51.projectToRegion(region45, bidirectional = False)
region52.projectToRegion(region46, bidirectional = False)
region47.projectToRegion(region44, bidirectional = False)
region43.projectToRegion(region40, bidirectional = True)
region43.projectToRegion(region32, bidirectional = True)
region44.projectToRegion(region38, bidirectional = False)
region44.projectToRegion(region31, bidirectional = False)
region44.projectToRegion(region18, bidirectional = False)
region44.projectToRegion(region20, bidirectional = False)
region44.projectToRegion(region21, bidirectional = False)
region44.projectToRegion(region22, bidirectional = True)
region44.projectToRegion(region33, bidirectional = False)
region44.projectToRegion(region28, bidirectional = True)
region44.projectToRegion(region39, bidirectional = True)
region44.projectToRegion(region41, bidirectional = True)
region45.projectToRegion(region35, bidirectional = True)
region46.projectToRegion(region37, bidirectional = True)
region40.projectToRegion(region44, bidirectional = False)
region40.projectToRegion(region18, bidirectional = False)
region40.projectToRegion(region38, bidirectional = False)
region40.projectToRegion(region19, bidirectional = False)
region40.projectToRegion(region21, bidirectional = False)
region40.projectToRegion(region12, bidirectional = False)
region40.projectToRegion(region22, bidirectional = True)
region40.projectToRegion(region33, bidirectional = True)
region40.projectToRegion(region32, bidirectional = True)
region40.projectToRegion(region36, bidirectional = True)
region40.projectToRegion(region39, bidirectional = True)
region40.projectToRegion(region5, bidirectional = False)
region40.projectToRegion(region41, bidirectional = True)
region41.projectToRegion(region32, bidirectional = True)
region41.projectToRegion(region38, bidirectional = False)
region41.projectToRegion(region18, bidirectional = False)
region41.projectToRegion(region31, bidirectional = False)
region41.projectToRegion(region21, bidirectional = False)
region41.projectToRegion(region19, bidirectional = False)
region41.projectToRegion(region22, bidirectional = True)
region41.projectToRegion(region28, bidirectional = True)
region41.projectToRegion(region12, bidirectional = False)
region41.projectToRegion(region36, bidirectional = False)
region41.projectToRegion(region39, bidirectional = True)
region41.projectToRegion(region5, bidirectional = False)
region39.projectToRegion(region36, bidirectional = True)
region39.projectToRegion(region32, bidirectional = True)
region39.projectToRegion(region22, bidirectional = True)
region39.projectToRegion(region21, bidirectional = False)
region39.projectToRegion(region20, bidirectional = False)
region39.projectToRegion(region31, bidirectional = False)
region39.projectToRegion(region27, bidirectional = False)
region39.projectToRegion(region12, bidirectional = False)
region39.projectToRegion(region19, bidirectional = False)
region29.projectToRegion(region11, bidirectional = False)
region29.projectToRegion(region31, bidirectional = False)
region36.projectToRegion(region33, bidirectional = True)
region36.projectToRegion(region32, bidirectional = True)
region36.projectToRegion(region22, bidirectional = True)
region36.projectToRegion(region24, bidirectional = True)
region36.projectToRegion(region26, bidirectional = True)
region36.projectToRegion(region15, bidirectional = True)
region36.projectToRegion(region17, bidirectional = True)
region36.projectToRegion(region9, bidirectional = True)
region36.projectToRegion(region5, bidirectional = True)
region36.projectToRegion(region6, bidirectional = True)
region36.projectToRegion(region38, bidirectional = True)
region36.projectToRegion(region19, bidirectional = True)
region36.projectToRegion(region27, bidirectional = True)
region36.projectToRegion(region4, bidirectional = False)
region36.projectToRegion(region28, bidirectional = True)
region28.projectToRegion(region24, bidirectional = False)
region28.projectToRegion(region26, bidirectional = False)
region33.projectToRegion(region32, bidirectional = True)
region33.projectToRegion(region22, bidirectional = True)
region33.projectToRegion(region20, bidirectional = True)
region33.projectToRegion(region31, bidirectional = False)
region33.projectToRegion(region21, bidirectional = True)
region33.projectToRegion(region12, bidirectional = False)
region32.projectToRegion(region22, bidirectional = True)
region32.projectToRegion(region21, bidirectional = True)
region32.projectToRegion(region20, bidirectional = True)
region32.projectToRegion(region31, bidirectional = True)
region32.projectToRegion(region38, bidirectional = True)
region32.projectToRegion(region19, bidirectional = True)
region32.projectToRegion(region18, bidirectional = True)
region32.projectToRegion(region12, bidirectional = True)
region32.projectToRegion(region4, bidirectional = False)
region22.projectToRegion(region25, bidirectional = True)
region22.projectToRegion(region13, bidirectional = True)
region22.projectToRegion(region5, bidirectional = True)
region22.projectToRegion(region6, bidirectional = False)
region22.projectToRegion(region21, bidirectional = True)
region22.projectToRegion(region20, bidirectional = True)
region22.projectToRegion(region19, bidirectional = True)
region22.projectToRegion(region18, bidirectional = True)
region22.projectToRegion(region12, bidirectional = True)
region22.projectToRegion(region11, bidirectional = False)
region24.projectToRegion(region17, bidirectional = True)
region24.projectToRegion(region8, bidirectional = True)
region24.projectToRegion(region9, bidirectional = True)
region25.projectToRegion(region21, bidirectional = True)
region25.projectToRegion(region12, bidirectional = False)
region25.projectToRegion(region4, bidirectional = False)
region26.projectToRegion(region17, bidirectional = True)
region26.projectToRegion(region8, bidirectional = True)
region26.projectToRegion(region9, bidirectional = True)
region26.projectToRegion(region6, bidirectional = True)
region26.projectToRegion(region5, bidirectional = True)
region15.projectToRegion(region8, bidirectional = True)
region15.projectToRegion(region9, bidirectional = True)
region16.projectToRegion(region12, bidirectional = True)
region16.projectToRegion(region4, bidirectional = True)
region17.projectToRegion(region8, bidirectional = True)
region17.projectToRegion(region9, bidirectional = True)
region17.projectToRegion(region5, bidirectional = True)
region8.projectToRegion(region7, bidirectional = True)
region8.projectToRegion(region11, bidirectional = True)
region8.projectToRegion(region4, bidirectional = True)
region8.projectToRegion(region12, bidirectional = True)
region9.projectToRegion(region6, bidirectional = True)
region9.projectToRegion(region5, bidirectional = True)
region13.projectToRegion(region7, bidirectional = True)
region13.projectToRegion(region5, bidirectional = True)
region13.projectToRegion(region6, bidirectional = True)
region13.projectToRegion(region21, bidirectional = True)
region13.projectToRegion(region20, bidirectional = True)
region13.projectToRegion(region12, bidirectional = True)
region13.projectToRegion(region4, bidirectional = True)
region7.projectToRegion(region5, bidirectional = True)
region7.projectToRegion(region6, bidirectional = True)
region7.projectToRegion(region4, bidirectional = True)
region5.projectToRegion(region21, bidirectional = True)
region5.projectToRegion(region11, bidirectional = True)
region5.projectToRegion(region3, bidirectional = True)
region5.projectToRegion(region4, bidirectional = True)
region5.projectToRegion(region2, bidirectional = True)
region6.projectToRegion(region11, bidirectional = True)
region6.projectToRegion(region3, bidirectional = True)
region6.projectToRegion(region4, bidirectional = True)
region6.projectToRegion(region2, bidirectional = True)
region21.projectToRegion(region31, bidirectional = True)
region21.projectToRegion(region19, bidirectional = True)
region21.projectToRegion(region18, bidirectional = True)
region21.projectToRegion(region27, bidirectional = True)
region21.projectToRegion(region11, bidirectional = True)
region21.projectToRegion(region12, bidirectional = True)
region20.projectToRegion(region31, bidirectional = True)
region20.projectToRegion(region19, bidirectional = True)
region20.projectToRegion(region18, bidirectional = True)
region20.projectToRegion(region27, bidirectional = True)
region20.projectToRegion(region11, bidirectional = True)
region20.projectToRegion(region12, bidirectional = True)
region31.projectToRegion(region19, bidirectional = True)
region31.projectToRegion(region18, bidirectional = True)
region31.projectToRegion(region38, bidirectional = True)
region31.projectToRegion(region30, bidirectional = True)
region31.projectToRegion(region27, bidirectional = True)
region31.projectToRegion(region11, bidirectional = True)
region31.projectToRegion(region12, bidirectional = True)
region38.projectToRegion(region27, bidirectional = True)
region38.projectToRegion(region19, bidirectional = True)
region38.projectToRegion(region11, bidirectional = True)
region19.projectToRegion(region18, bidirectional = True)
region19.projectToRegion(region27, bidirectional = True)
region19.projectToRegion(region11, bidirectional = True)
region19.projectToRegion(region12, bidirectional = True)
region19.projectToRegion(region4, bidirectional = True)
region18.projectToRegion(region11, bidirectional = True)
region18.projectToRegion(region12, bidirectional = True)
region30.projectToRegion(region11, bidirectional = False)
region27.projectToRegion(region11, bidirectional = True)
region27.projectToRegion(region12, bidirectional = True)
region27.projectToRegion(region3, bidirectional = True)
region27.projectToRegion(region4, bidirectional = True)
region11.projectToRegion(region12, bidirectional = True)
region11.projectToRegion(region3, bidirectional = True)
region11.projectToRegion(region4, bidirectional = True)
region11.projectToRegion(region10, bidirectional = True)
region12.projectToRegion(region4, bidirectional = True)
region4.projectToRegion(region3, bidirectional = True)
region4.projectToRegion(region2, bidirectional = True)
region3.projectToRegion(region2, bidirectional = True)
region10.projectToRegion(region3, bidirectional = True)
region2.projectToRegion(region1, bidirectional = True)

# Create a display

display.setBackgroundColor((0.7215, 0.7686, 0.8, 1.0))
display.setDefaultFlowColor((1.0, 1.0, 1.0))
display.setDefaultFlowSpacing(0.05)
display.setDefaultFlowSpeed(0.05)
display.setDefaultFlowSpread(0.5)
display.setViewDimensions(2)
display.setShowRegionNames(True)

display.setVisiblePosition(region1, (0.0, 0.0, 0.0), fixed = True)
display.setVisibleSize(region1, (0.05, 0.02, 0.1))
display.setVisibleColor(region1, (0.9803, 0.8745, 1.0))
display.setVisiblePosition(region2, (0.0, -0.035, 0.0), fixed = True)
display.setVisibleSize(region2, (0.05, 0.02, 0.1))
display.setVisibleColor(region2, (0.9333, 0.9333, 1.0))
display.setVisiblePosition(region3, (-0.15, -0.09, 0.0), fixed = True)
display.setVisibleSize(region3, (0.05, 0.02, 0.1))
display.setVisibleColor(region3, (0.898, 1.0, 0.8156))
display.setVisiblePosition(region4, (-0.05, -0.09, 0.0), fixed = True)
display.setVisibleSize(region4, (0.05, 0.02, 0.1))
display.setVisibleColor(region4, (0.5019, 0.145, 0.1607))
display.setVisiblePosition(region5, (0.05, -0.09, 0.0), fixed = True)
display.setVisibleSize(region5, (0.05, 0.02, 0.1))
display.setVisibleColor(region5, (0.5215, 0.5843, 1.0))
display.setVisiblePosition(region6, (0.15, -0.09, 0.0), fixed = True)
display.setVisibleSize(region6, (0.05, 0.02, 0.1))
display.setVisibleColor(region6, (0.5725, 0.6705, 1.0))
display.setVisiblePosition(region7, (0.07, -0.145, 0.0), fixed = True)
display.setVisibleSize(region7, (0.05, 0.02, 0.1))
display.setVisibleColor(region7, (1.0, 0.8078, 0.7215))
display.setVisiblePosition(region8, (0.15, -0.145, 0.0), fixed = True)
display.setVisibleSize(region8, (0.05, 0.02, 0.1))
display.setVisibleColor(region8, (0.6705, 1.0, 0.6901))
display.setVisiblePosition(region9, (0.23, -0.145, 0.0), fixed = True)
display.setVisibleSize(region9, (0.05, 0.02, 0.1))
display.setVisibleColor(region9, (0.5686, 0.4705, 1.0))
display.setVisiblePosition(region10, (-0.25, -0.2, 0.0), fixed = True)
display.setVisibleSize(region10, (0.05, 0.02, 0.1))
display.setVisibleColor(region10, (1.0, 0.9098, 0.8313))
display.setVisiblePosition(region11, (-0.15, -0.2, 0.0), fixed = True)
display.setVisibleSize(region11, (0.05, 0.02, 0.1))
display.setVisibleColor(region11, (1.0, 0.7529, 0.3803))
display.setVisiblePosition(region12, (-0.05, -0.2, 0.0), fixed = True)
display.setVisibleSize(region12, (0.05, 0.02, 0.1))
display.setVisibleColor(region12, (0.5137, 0.5529, 0.647))
display.setVisiblePosition(region13, (0.05, -0.2, 0.0), fixed = True)
display.setVisibleSize(region13, (0.05, 0.02, 0.1))
display.setVisibleColor(region13, (1.0, 0.7529, 0.3803))
display.setVisiblePosition(region14, (0.2, -0.2, 0.0), fixed = True)
display.setVisibleSize(region14, (0.2, 0.02, 0.1))
display.setLabel(region14, 'CIT')
display.setLabelPosition(region14, (0.0, 0.5, 0.0))
display.setVisibleColor(region14, (0.8117, 0.8666, 1.0))
display.setArrangedAxis(region14, 'largest')
display.setArrangedSpacing(region14, 0.01)
display.setVisibleColor(region15, (0.6588, 0.8156, 1.0))
display.setVisibleColor(region16, (0.6588, 0.8156, 1.0))
display.setVisibleColor(region17, (0.6588, 0.8156, 1.0))
display.setVisiblePosition(region18, (-0.35, -0.25, 0.0), fixed = True)
display.setVisibleSize(region18, (0.05, 0.02, 0.1))
display.setVisibleColor(region18, (1.0, 0.5294, 0.2627))
display.setVisiblePosition(region19, (-0.25, -0.25, 0.0), fixed = True)
display.setVisibleSize(region19, (0.05, 0.02, 0.1))
display.setVisibleColor(region19, (1.0, 0.9333, 0.6509))
display.setVisiblePosition(region20, (-0.15, -0.25, 0.0), fixed = True)
display.setVisibleSize(region20, (0.05, 0.02, 0.1))
display.setVisibleColor(region20, (1.0, 0.5294, 0.2627))
display.setVisiblePosition(region21, (-0.05, -0.25, 0.0), fixed = True)
display.setVisibleSize(region21, (0.05, 0.02, 0.1))
display.setVisibleColor(region21, (1.0, 0.1098, 0.9058))
display.setVisiblePosition(region22, (0.05, -0.25, 0.0), fixed = True)
display.setVisibleSize(region22, (0.05, 0.02, 0.1))
display.setVisibleColor(region22, (1.0, 0.7529, 0.3803))
display.setVisiblePosition(region23, (0.2, -0.25, 0.0), fixed = True)
display.setVisibleSize(region23, (0.2, 0.02, 0.1))
display.setLabel(region23, 'PIT')
display.setLabelPosition(region23, (0.0, 0.5, 0.0))
display.setVisibleColor(region23, (0.8117, 0.8666, 1.0))
display.setArrangedAxis(region23, 'largest')
display.setArrangedSpacing(region23, 0.01)
display.setVisibleColor(region24, (0.596, 0.698, 1.0))
display.setVisibleColor(region25, (0.596, 0.698, 1.0))
display.setVisibleColor(region26, (0.596, 0.698, 1.0))
display.setVisiblePosition(region27, (-0.2, -0.3, 0.0), fixed = True)
display.setVisibleSize(region27, (0.05, 0.02, 0.1))
display.setVisibleColor(region27, (1.0, 0.5058, 0.7843))
display.setVisiblePosition(region28, (0.3, -0.3, 0.0), fixed = True)
display.setVisibleSize(region28, (0.05, 0.02, 0.1))
display.setVisibleColor(region28, (0.3058, 0.3607, 1.0))
display.setVisiblePosition(region29, (-0.35, -0.35, 0.0))
display.setVisibleSize(region29, (0.05, 0.02, 0.1))
display.setVisibleColor(region29, (1.0, 0.3764, 0.5294))
display.setVisiblePosition(region30, (-0.25, -0.35, 0.0), fixed = True)
display.setVisibleSize(region30, (0.05, 0.02, 0.1))
display.setVisibleColor(region30, (1.0, 0.3843, 0.6666))
display.setVisiblePosition(region31, (-0.15, -0.35, 0.0), fixed = True)
display.setVisibleSize(region31, (0.05, 0.02, 0.1))
display.setVisibleColor(region31, (1.0, 0.3843, 0.6666))
display.setVisiblePosition(region32, (-0.05, -0.35, 0.0), fixed = True)
display.setVisibleSize(region32, (0.05, 0.02, 0.1))
display.setVisibleColor(region32, (1.0, 0.0784, 0.6196))
display.setVisiblePosition(region33, (0.05, -0.35, 0.0), fixed = True)
display.setVisibleSize(region33, (0.05, 0.02, 0.1))
display.setVisibleColor(region33, (1.0, 0.6588, 0.7372))
display.setVisiblePosition(region34, (0.25, -0.35, 0.0), fixed = True)
display.setVisibleSize(region34, (0.2, 0.02, 0.1))
display.setLabel(region34, 'V4')
display.setLabelPosition(region34, (0.0, 0.5, 0.0))
display.setVisibleColor(region34, (0.8117, 0.8666, 1.0))
display.setArrangedAxis(region34, 'largest')
display.setArrangedSpacing(region34, 0.01)
display.setVisibleColor(region35, (0.2352, 0.3176, 1.0))
display.setVisibleColor(region36, (0.2352, 0.3176, 1.0))
display.setVisibleColor(region37, (0.2352, 0.3176, 1.0))
display.setVisiblePosition(region38, (-0.3, -0.4, 0.0), fixed = True)
display.setVisibleSize(region38, (0.05, 0.02, 0.1))
display.setVisibleColor(region38, (1.0, 0.4313, 0.5764))
display.setVisiblePosition(region39, (0.25, -0.4, 0.0), fixed = True)
display.setVisibleSize(region39, (0.05, 0.02, 0.1))
display.setVisibleColor(region39, (0.8431, 0.3607, 1.0))
display.setVisiblePosition(region40, (-0.22, -0.45, 0.0), fixed = True)
display.setVisibleSize(region40, (0.05, 0.02, 0.1))
display.setVisibleColor(region40, (1.0, 0.4431, 0.4431))
display.setVisiblePosition(region41, (0.2, -0.45, 0.0), fixed = True)
display.setVisibleSize(region41, (0.05, 0.02, 0.1))
display.setVisibleColor(region41, (0.6745, 0.3725, 1.0))
display.setVisiblePosition(region42, (-0.05, -0.5, 0.0), fixed = True)
display.setVisibleSize(region42, (0.3, 0.02, 0.1))
display.setLabel(region42, 'V2')
display.setLabelPosition(region42, (0.0, 0.5, 0.0))
display.setVisibleColor(region42, (0.8117, 0.8666, 1.0))
display.setArrangedAxis(region42, 'largest')
display.setArrangedSpacing(region42, 0.005)
display.setVisibleColor(region43, (1.0, 0.4117, 0.5882))
display.setVisibleColor(region44, (1.0, 0.4117, 0.5882))
display.setVisibleColor(region45, (1.0, 0.4117, 0.5882))
display.setVisibleColor(region46, (1.0, 0.4117, 0.5882))
display.setVisiblePosition(region47, (0.25, -0.55, 0.0), fixed = True)
display.setVisibleSize(region47, (0.05, 0.02, 0.1))
display.setVisibleColor(region47, (0.7019, 0.7019, 0.7019))
display.setVisiblePosition(region48, (-0.05, -0.6, 0.0), fixed = True)
display.setVisibleSize(region48, (0.3, 0.02, 0.1))
display.setLabel(region48, 'V1')
display.setLabelPosition(region48, (0.0, 0.5, 0.0))
display.setVisibleColor(region48, (0.8117, 0.8666, 1.0))
display.setArrangedAxis(region48, 'largest')
display.setArrangedSpacing(region48, 0.005)
display.setVisibleColor(region49, (1.0, 0.2313, 0.4274))
display.setVisibleColor(region50, (1.0, 0.2313, 0.4274))
display.setVisibleColor(region51, (1.0, 0.2313, 0.4274))
display.setVisibleColor(region52, (1.0, 0.2313, 0.4274))
display.setVisiblePosition(region53, (-0.05, -0.65, 0.0), fixed = True)
display.setVisibleSize(region53, (0.3, 0.02, 0.1))
display.setLabelPosition(region53, (0.0, 0.5, 0.0))
display.setVisibleColor(region53, (0.8117, 0.8666, 1.0))
display.setArrangedAxis(region53, 'largest')
display.setArrangedSpacing(region53, 0.005)
display.setLabel(region54, 'M')
display.setVisibleColor(region54, (0.6, 0.6, 0.6))
display.setLabel(region55, 'I')
display.setVisibleColor(region55, (0.6, 0.6, 0.6))
display.setLabel(region56, 'P')
display.setVisibleColor(region56, (0.6, 0.6, 0.6))
display.setVisiblePosition(region57, (0.25, -0.7, 0.0), fixed = True)
display.setVisibleSize(region57, (0.05, 0.02, 0.1))
display.setVisibleColor(region57, (0.6, 0.6, 0.6))
display.setVisiblePosition(region58, (-0.05, -0.75, 0.0))
display.setVisibleSize(region58, (0.3, 0.02, 0.1))
display.setLabel(region58, 'Retina')
display.setLabelPosition(region58, (0.0, 0.5, 0.0))
display.setVisibleColor(region58, (0.8117, 0.8666, 1.0))
display.setArrangedAxis(region58, 'largest')
display.setArrangedSpacing(region58, 0.005)
display.setLabel(region59, 'M')
display.setVisibleColor(region59, (0.7215, 0.7215, 0.7215))
display.setLabel(region60, 'P')
display.setVisibleColor(region60, (0.7215, 0.7215, 0.7215))
display.setLabel(region61, 'Other')
display.setVisibleColor(region61, (0.7215, 0.7215, 0.7215))

display.zoomToFit()
