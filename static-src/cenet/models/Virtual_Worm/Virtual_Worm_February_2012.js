/*******************************************************************************
 * The MIT License (MIT)
 *
 * Copyright (c) 2011, 2013 OpenWorm.
 * http://openworm.org
 *
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the MIT License
 * which accompanies this distribution, and is available at
 * http://opensource.org/licenses/MIT
 *
 * Contributors:
 *     	OpenWorm - http://openworm.org/people.html
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in
 * all copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
 * IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
 * DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
 * OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE
 * USE OR OTHER DEALINGS IN THE SOFTWARE.
 *******************************************************************************/

MODELS['Virtual_Worm_February_2012.obj'] = {
  materials: {
    'interneuron': {
      Ka: [0, 0, 0],
      Kd: [204, 40, 0],
      Ks: [0, 0, 0],
      Ns: 96.078430,
      d: 12
    },
    'polymodalneuron': {
      Ka: [0, 0, 0],
      Kd: [196, 1, 1],
      Ks: [0, 0, 0],
      Ns: 96.078430,
      d: 12
    },
    'motor_neuron': {
      Ka: [0, 0, 0],
      Kd: [122, 81, 190],
      Ks: [0, 0, 0],
      Ns: 96.078430,
      d: 12
    },
    'neurunkfunc': {
      Ka: [0, 0, 0],
      Kd: [122, 0, 40],
      Ks: [0, 0, 0],
      Ns: 96.078430,
      d: 12
    },
    'sensoryneuron': {
      Ka: [0, 0, 0],
      Kd: [204, 81, 190],
      Ks: [0, 0, 0],
      Ns: 96.078430,
      d: 12
    }
  },
  decodeParams: {
    decodeOffsets: [-619,-1417,-8191,0,0,-511,-511,-511],
    decodeScales: [0.000498,0.000498,0.000498,0.000978,0.000978,0.001957,0.001957,0.001957]
  },
  urls: {
    '9ef380e0.Virtual_Worm_February_2012.utf8': [
      { material: 'interneuron',
        attribRange: [0, 55294],
        indexRange: [442352, 110383],
        bboxes: 3215376,
        names: ['siavr', 'sdqr', 'sdql', 'bdur', 'pvnr', 'pvwr', 'pvcr', 'luar', 'pvpl', 'ripr', 'urbr', 'aibr', 'adar', 'mi', 'i6', 'i5', 'i4', 'i3', 'i2r', 'i1r', 'pvnl', 'pvcl'],
        lengths: [19392, 7872, 13632, 8256, 31680, 6336, 23232, 5472, 19776, 13248, 5184, 12480, 7872, 7488, 9792, 36480, 16320, 5568, 12096, 10560, 37440, 20973]
      },
      { material: 'interneuron',
        attribRange: [773501, 55294],
        indexRange: [1215853, 110422],
        bboxes: 3215508,
        names: ['pvcl', 'pvql', 'pvt', 'pvpr', 'pvwl', 'lual', 'pvqr', 'bdul', 'i1l', 'i2l', 'rivr', 'avjr', 'ricr', 'sibvr', 'siadr', 'aiar', 'saadl', 'ribr', 'avkr', 'avkl', 'avfl', 'avfr'],
        lengths: [1491, 24384, 22848, 19008, 6336, 5472, 24000, 8256, 10560, 12096, 9792, 22080, 9888, 25632, 19872, 5568, 14496, 12480, 24864, 24864, 25152, 2127]
      },
      { material: 'interneuron',
        attribRange: [1547119, 55295],
        indexRange: [1989479, 107288],
        bboxes: 3215640,
        names: ['avfr', 'avar', 'avbr', 'avdl', 'avbl', 'aval', 'avdr', 'saadr', 'rir', 'sibdr', 'aver', 'riar', 'saavr', 'ainr', 'avhr', 'urxr', 'ris', 'ripl', 'urbl', 'adal', 'rid'],
        lengths: [23409, 22176, 25728, 22176, 25728, 22176, 22176, 14496, 10176, 20256, 13248, 10176, 14400, 6816, 22080, 8256, 8736, 13248, 5184, 7872, 3351]
      },
      { material: 'interneuron',
        attribRange: [2311343, 55294],
        indexRange: [2753695, 100535],
        bboxes: 3215766,
        names: ['rid', 'urxl', 'rivl', 'avhl', 'avjl', 'ainl', 'saavl', 'rial', 'avel', 'sibdl', 'ribl', 'aizl', 'ricl', 'aiyr', 'aimr', 'aibl', 'rigl', 'sabd', 'avg', 'rifl', 'rigr', 'rifr', 'sabvr', 'sabvl', 'aiml', 'aiyl', 'siadl'],
        lengths: [24105, 8256, 9792, 22080, 22464, 6816, 14400, 10176, 13248, 20256, 12480, 8640, 9888, 5568, 5952, 12480, 5568, 15936, 19776, 5952, 5568, 5952, 5184, 5184, 5952, 5568, 14364]
      },
      { material: 'interneuron',
        attribRange: [3055300, 11485],
        indexRange: [3147180, 22732],
        bboxes: 3215928,
        names: ['siadl', 'aial', 'siavl', 'sibvl', 'rih'],
        lengths: [5508, 5568, 19392, 25632, 12096]
      }
    ],
    '1266f863.Virtual_Worm_February_2012.utf8': [
      { material: 'motor_neuron',
        attribRange: [0, 55294],
        indexRange: [442352, 110400],
        bboxes: 3231456,
        names: ['va11', 'hsnr', 'dd6', 'dd4', 'dd3', 'dd5', 'dd2', 'db7', 'db6', 'da9', 'da7', 'da6', 'da5', 'as11', 'as10', 'as9', 'as8', 'as7', 'as6', 'as5', 'as4', 'as3', 'as2', 'vd13', 'vd12', 'vd11', 'vd10', 'vd9'],
        lengths: [4416, 17856, 15168, 19008, 15168, 14016, 12096, 12480, 14016, 12096, 17472, 22080, 17664, 9408, 8928, 9408, 10848, 10176, 9024, 9792, 9408, 8256, 8640, 10560, 10944, 10944, 10944, 384]
      },
      { material: 'motor_neuron',
        attribRange: [773552, 55294],
        indexRange: [1215904, 110411],
        bboxes: 3231624,
        names: ['vd9', 'vd8', 'vd7', 'vd6', 'vd5', 'vd4', 'vd3', 'db5', 'db4', 'da8', 'da4', 'da3', 'da2', 'vc5', 'uravr', 'm5', 'm3r', 'm2r', 'm1', 'dvb', 'va12', 'pda', 'pdb', 'vb11', 'va10', 'vb10', 'va9', 'vc6', 'vb9', 'va8', 'vb8'],
        lengths: [10176, 13632, 12480, 10944, 10944, 10944, 9792, 20160, 23232, 12096, 14400, 11712, 11328, 11328, 7872, 18624, 11328, 6336, 9408, 8640, 3264, 10560, 13248, 6336, 5952, 7488, 9408, 5184, 7104, 10176, 7137]
      },
      { material: 'motor_neuron',
        attribRange: [1547137, 55294],
        indexRange: [1989489, 110396],
        bboxes: 3231810,
        names: ['vb8', 'va7', 'vb7', 'va6', 'vc3', 'vb6', 'va5', 'vc2', 'vb5', 'va4', 'vc1', 'vb4', 'va3', 'db3', 'vb3', 'va2', 'hsnl', 'vc4', 'm4', 'm2l', 'm3l', 'smbvr', 'rmfr', 'rmgr', 'uradr', 'rmer', 'rmhr', 'smbdr', 'smddr'],
        lengths: [2655, 10560, 9792, 10176, 23304, 10944, 6720, 10560, 11328, 7104, 11328, 11328, 6720, 19776, 10560, 5568, 17856, 11328, 20160, 6336, 11328, 22080, 10560, 7488, 8640, 7008, 10560, 17856, 11565]
      },
      { material: 'motor_neuron',
        attribRange: [2320677, 55294],
        indexRange: [2763029, 110271],
        bboxes: 3231984,
        names: ['smddr', 'rmddr', 'rmdr', 'rmdvr', 'smdvr', 'rimr', 'rmed', 'rmel', 'rmev', 'smdvl', 'rmdvl', 'rmdl', 'riml', 'vd2', 'da1', 'vd1', 'as1', 'db1', 'dd1', 'va1', 'db2', 'vb1', 'vb2', 'rmfl', 'smbdl', 'smddl', 'rmhl'],
        lengths: [6675, 5952, 6720, 6720, 19776, 14016, 11904, 7008, 25152, 19776, 6720, 6720, 14016, 9408, 10176, 12480, 8256, 24384, 11328, 7488, 20928, 12864, 11712, 10560, 17856, 18240, 3978]
      },
      { material: 'motor_neuron',
        attribRange: [3093842, 9875],
        indexRange: [3172842, 19538],
        bboxes: 3232146,
        names: ['rmhl', 'rmddl', 'rmgl', 'uravl', 'uradl', 'smbvl'],
        lengths: [6582, 5952, 7488, 7872, 8640, 22080]
      }
    ],
    'd53efa90.Virtual_Worm_February_2012.utf8': [
      { material: 'neurunkfunc',
        attribRange: [0, 33050],
        indexRange: [264400, 66048],
        bboxes: 462544,
        names: ['alnr', 'plnr', 'canl', 'uryvr', 'auar', 'plnl', 'alnl', 'canr', 'urydr', 'ala', 'aual', 'urydl', 'uryvl'],
        lengths: [17472, 20544, 13632, 7872, 13248, 19776, 17472, 13632, 11712, 29952, 13248, 11712, 7872]
      }
    ],
    'dd73fee7.Virtual_Worm_February_2012.utf8': [
      { material: 'polymodalneuron',
        attribRange: [0, 24178],
        indexRange: [193424, 48296],
        bboxes: 338312,
        names: ['olqvr', 'il1vr', 'il1r', 'nsmr', 'mcr', 'mcl', 'olqdr', 'nsml', 'il1dr', 'avl', 'il1dl', 'il1vl', 'il1l', 'olqdl', 'olqvl'],
        lengths: [7872, 8256, 10944, 9408, 11712, 11712, 9408, 9408, 2268, 25152, 2268, 8256, 10944, 9408, 7872]
      }
    ],
    'b8859a42.Virtual_Worm_February_2012.utf8': [
      { material: 'sensoryneuron',
        attribRange: [0, 55294],
        indexRange: [442352, 109643],
        bboxes: 4930384,
        names: ['pvm', 'pvdr'],
        lengths: [14016, 314913]
      },
      { material: 'sensoryneuron',
        attribRange: [771281, 55294],
        indexRange: [1213633, 109391],
        bboxes: 4930396,
        names: ['pvdr'],
        lengths: [328173]
      },
      { material: 'sensoryneuron',
        attribRange: [1541806, 55294],
        indexRange: [1984158, 109433],
        bboxes: 4930402,
        names: ['pvdr', 'pder', 'avm', 'almr', 'pvr', 'plmr', 'phcr', 'phbr', 'phar', 'pvdl'],
        lengths: [22914, 20160, 15936, 12096, 28992, 17088, 9408, 7488, 7488, 186729]
      },
      { material: 'sensoryneuron',
        attribRange: [2312457, 55294],
        indexRange: [2754809, 109194],
        bboxes: 4930462,
        names: ['pvdl'],
        lengths: [327582]
      },
      { material: 'sensoryneuron',
        attribRange: [3082391, 55294],
        indexRange: [3524743, 109764],
        bboxes: 4930468,
        names: ['pvdl', 'il2vr', 'flpr', 'bagr', 'il2r', 'awcr', 'awbr', 'awar', 'askr', 'asir', 'aser', 'ashr', 'adlr', 'adfr', 'ader'],
        lengths: [152073, 7872, 18240, 11712, 8256, 14784, 13632, 13632, 13632, 14784, 16704, 13632, 13248, 13248, 3843]
      },
      { material: 'sensoryneuron',
        attribRange: [3854035, 55294],
        indexRange: [4296387, 110199],
        bboxes: 4930558,
        names: ['ader', 'pqr', 'phcl', 'phbl', 'phal', 'plml', 'pdel', 'alml', 'il2vl', 'cepdr', 'asgr', 'ollr', 'il2dr', 'afdr', 'cepvr', 'asjr', 'aqr', 'il2dl', 'bagl', 'cepvl', 'adel', 'flpl', 'adll', 'ashl', 'awbl', 'afdl', 'adfl', 'asel'],
        lengths: [8637, 9024, 9408, 7488, 7488, 17088, 19776, 12096, 7872, 12096, 11712, 14016, 8256, 13248, 10944, 14400, 14016, 8256, 11712, 10944, 12480, 18240, 13248, 13632, 13632, 13248, 13248, 4392]
      },
      { material: 'sensoryneuron',
        attribRange: [4626984, 21722],
        indexRange: [4800760, 43208],
        bboxes: 4930726,
        names: ['asel', 'awcl', 'asjl', 'cepdl', 'asil', 'askl', 'asgl', 'awal', 'olll', 'il2l'],
        lengths: [12312, 14784, 14400, 12096, 14784, 13632, 11712, 13632, 14016, 8256]
      }
    ]
  }
};
