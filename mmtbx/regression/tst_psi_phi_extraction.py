from __future__ import division
from scitbx.array_family import flex
import iotbx.pdb
from mmtbx.conformation_dependent_library import generate_protein_threes

rec_1_residue = """\
CRYST1   41.566   72.307   92.870 108.51  93.02  90.06 P 1           4
ATOM   5466  N   ASN C 236      17.899  72.943  29.028  1.00 60.13           N
ATOM   5467  CA  ASN C 236      16.519  72.435  29.114  1.00 60.52           C
ATOM   5468  C   ASN C 236      16.377  70.925  29.327  1.00 60.49           C
ATOM   5469  O   ASN C 236      15.429  70.294  28.863  1.00 60.60           O
ATOM   5470  CB  ASN C 236      15.689  72.896  27.916  1.00 60.55           C
ATOM   5471  CG  ASN C 236      14.357  73.447  28.338  1.00 61.75           C
ATOM   5472  OD1 ASN C 236      14.256  74.609  28.768  1.00 62.86           O
ATOM   5473  ND2 ASN C 236      13.319  72.616  28.247  1.00 61.22           N
"""

rec_2_residues = """\
CRYST1   41.566   72.307   92.870 108.51  93.02  90.06 P 1           4
ATOM   5466  N   ASN C 236      17.899  72.943  29.028  1.00 60.13           N
ATOM   5467  CA  ASN C 236      16.519  72.435  29.114  1.00 60.52           C
ATOM   5468  C   ASN C 236      16.377  70.925  29.327  1.00 60.49           C
ATOM   5469  O   ASN C 236      15.429  70.294  28.863  1.00 60.60           O
ATOM   5470  CB  ASN C 236      15.689  72.896  27.916  1.00 60.55           C
ATOM   5471  CG  ASN C 236      14.357  73.447  28.338  1.00 61.75           C
ATOM   5472  OD1 ASN C 236      14.256  74.609  28.768  1.00 62.86           O
ATOM   5473  ND2 ASN C 236      13.319  72.616  28.247  1.00 61.22           N
ATOM   5474  N   LEU C 237      17.316  70.364  30.068  1.00 60.55           N
ATOM   5475  CA  LEU C 237      17.444  68.931  30.166  1.00 60.48           C
ATOM   5476  C   LEU C 237      17.815  68.555  31.581  1.00 60.06           C
ATOM   5477  O   LEU C 237      17.335  67.547  32.097  1.00 60.41           O
ATOM   5478  CB  LEU C 237      18.518  68.464  29.178  1.00 60.91           C
ATOM   5479  CG  LEU C 237      18.542  67.095  28.491  1.00 62.25           C
ATOM   5480  CD1 LEU C 237      17.407  66.153  28.923  1.00 63.18           C
ATOM   5481  CD2 LEU C 237      18.563  67.309  26.965  1.00 62.89           C
"""

rec_3_residues = """
CRYST1   69.211   49.956   52.557  90.00  90.00  90.00 P 1
ATOM      1  N   THR A   3      51.193  44.956  23.993  1.00 80.52           N
ATOM      2  CA  THR A   3      50.812  43.732  23.211  1.00 80.52           C
ATOM      4  CB  THR A   3      50.446  42.559  24.181  1.00 79.62           C
ATOM      6  OG1 THR A   3      50.206  41.358  23.433  1.00 79.62           O
ATOM      8  CG2 THR A   3      49.239  42.888  25.066  1.00 79.62           C
ATOM     12  C   THR A   3      49.657  44.014  22.221  1.00 80.52           C
ATOM     13  O   THR A   3      48.520  44.223  22.631  1.00 80.52           O
ATOM     17  N   GLY A   4      49.963  44.013  20.917  1.00 79.31           N
ATOM     18  CA  GLY A   4      49.030  44.458  19.892  1.00 79.31           C
ATOM     21  C   GLY A   4      48.761  43.480  18.761  1.00 79.31           C
ATOM     22  O   GLY A   4      47.790  42.725  18.808  1.00 79.31           O
ATOM     24  N   ALA A   5      49.581  43.499  17.715  1.00 78.81           N
ATOM     25  CA  ALA A   5      49.395  42.604  16.581  1.00 78.81           C
ATOM     27  CB  ALA A   5      49.774  43.314  15.283  1.00 77.40           C
ATOM     31  C   ALA A   5      50.195  41.315  16.714  1.00 78.81           C
ATOM     32  O   ALA A   5      50.258  40.537  15.757  1.00 78.81           O
"""

rec_4_residues = """
CRYST1   69.211   49.956   52.557  90.00  90.00  90.00 P 1
ATOM      1  N   THR A   3      51.193  44.956  23.993  1.00 80.52           N
ATOM      2  CA  THR A   3      50.812  43.732  23.211  1.00 80.52           C
ATOM      4  CB  THR A   3      50.446  42.559  24.181  1.00 79.62           C
ATOM      6  OG1 THR A   3      50.206  41.358  23.433  1.00 79.62           O
ATOM      8  CG2 THR A   3      49.239  42.888  25.066  1.00 79.62           C
ATOM     12  C   THR A   3      49.657  44.014  22.221  1.00 80.52           C
ATOM     13  O   THR A   3      48.520  44.223  22.631  1.00 80.52           O
ATOM     17  N   GLY A   4      49.963  44.013  20.917  1.00 79.31           N
ATOM     18  CA  GLY A   4      49.030  44.458  19.892  1.00 79.31           C
ATOM     21  C   GLY A   4      48.761  43.480  18.761  1.00 79.31           C
ATOM     22  O   GLY A   4      47.790  42.725  18.808  1.00 79.31           O
ATOM     24  N   ALA A   5      49.581  43.499  17.715  1.00 78.81           N
ATOM     25  CA  ALA A   5      49.395  42.604  16.581  1.00 78.81           C
ATOM     27  CB  ALA A   5      49.774  43.314  15.283  1.00 77.40           C
ATOM     31  C   ALA A   5      50.195  41.315  16.714  1.00 78.81           C
ATOM     32  O   ALA A   5      50.258  40.537  15.757  1.00 78.81           O
ATOM     34  N   GLN A   6      50.816  41.073  17.872  1.00 80.55           N
ATOM     35  CA  GLN A   6      51.642  39.880  18.018  1.00 80.55           C
ATOM     37  CB  GLN A   6      52.383  39.879  19.354  1.00 79.84           C
ATOM     40  CG  GLN A   6      53.264  41.072  19.596  1.00 79.84           C
ATOM     43  CD  GLN A   6      52.490  42.211  20.225  1.00 79.84           C
ATOM     44  OE1 GLN A   6      51.290  42.091  20.489  1.00 79.84           O
ATOM     45  NE2 GLN A   6      53.167  43.325  20.468  1.00 79.84           N
ATOM     48  C   GLN A   6      50.788  38.631  17.945  1.00 80.55           C
ATOM     49  O   GLN A   6      51.148  37.659  17.273  1.00 80.55           O
"""

rec_2_chains = """
CRYST1   49.945   53.842   33.425  90.00  90.00  90.00 P 1
ATOM   5466  N   ASN C 236      10.328  45.698  25.449  1.00 60.13           N
ATOM   5467  CA  ASN C 236       8.971  45.973  25.787  1.00 60.52           C
ATOM   5468  C   ASN C 236       8.271  44.664  25.724  1.00 60.49           C
ATOM   5469  O   ASN C 236       7.276  44.532  25.017  1.00 60.60           O
ATOM   5470  CB  ASN C 236       8.337  46.962  24.776  1.00 60.55           C
ATOM   5471  CG  ASN C 236       7.235  47.762  25.415  1.00 61.75           C
ATOM   5472  OD1 ASN C 236       6.331  47.222  26.063  1.00 62.86           O
ATOM   5473  ND2 ASN C 236       7.315  49.079  25.302  1.00 61.22           N
ATOM   5474  N   LEU C 237       8.820  43.663  26.441  1.00 60.55           N
ATOM   5475  CA  LEU C 237       8.420  42.305  26.286  1.00 60.48           C
ATOM   5476  C   LEU C 237       8.713  41.508  27.558  1.00 60.06           C
ATOM   5477  O   LEU C 237       7.907  41.421  28.503  1.00 60.41           O
ATOM   5478  CB  LEU C 237       9.159  41.598  25.114  1.00 60.91           C
ATOM   5479  CG  LEU C 237       9.365  42.136  23.662  1.00 62.25           C
ATOM   5480  CD1 LEU C 237      10.605  42.996  23.496  1.00 63.18           C
ATOM   5481  CD2 LEU C 237       9.419  40.966  22.765  1.00 62.89           C
TER
ATOM      1  N   THR A   3      40.527  19.363  20.612  1.00 80.52           N
ATOM      2  CA  THR A   3      41.278  18.625  19.636  1.00 80.52           C
ATOM      4  CB  THR A   3      40.971  17.090  19.710  1.00 79.62           C
ATOM      6  OG1 THR A   3      40.039  16.849  20.760  1.00 79.62           O
ATOM      8  CG2 THR A   3      42.308  16.246  19.999  1.00 79.62           C
ATOM     12  C   THR A   3      40.899  19.134  18.229  1.00 80.52           C
ATOM     13  O   THR A   3      39.780  19.542  17.983  1.00 80.52           O
ATOM     17  N   GLY A   4      41.890  19.246  17.384  1.00 79.31           N
ATOM     18  CA  GLY A   4      41.732  19.850  16.092  1.00 79.31           C
ATOM     21  C   GLY A   4      41.306  18.930  14.985  1.00 79.31           C
ATOM     22  O   GLY A   4      40.121  18.885  14.657  1.00 79.31           O
"""

rec_2_segids = """
CRYST1   49.945   53.842   33.425  90.00  90.00  90.00 P 1
ATOM   5466  N   ASN A 236      10.328  45.698  25.449  1.00 60.13           N
ATOM   5467  CA  ASN A 236       8.971  45.973  25.787  1.00 60.52           C
ATOM   5468  C   ASN A 236       8.271  44.664  25.724  1.00 60.49           C
ATOM   5469  O   ASN A 236       7.276  44.532  25.017  1.00 60.60           O
ATOM   5470  CB  ASN A 236       8.337  46.962  24.776  1.00 60.55           C
ATOM   5471  CG  ASN A 236       7.235  47.762  25.415  1.00 61.75           C
ATOM   5472  OD1 ASN A 236       6.331  47.222  26.063  1.00 62.86           O
ATOM   5473  ND2 ASN A 236       7.315  49.079  25.302  1.00 61.22           N
ATOM   5474  N   LEU A 237       8.820  43.663  26.441  1.00 60.55           N
ATOM   5475  CA  LEU A 237       8.420  42.305  26.286  1.00 60.48           C
ATOM   5476  C   LEU A 237       8.713  41.508  27.558  1.00 60.06           C
ATOM   5477  O   LEU A 237       7.907  41.421  28.503  1.00 60.41           O
ATOM   5478  CB  LEU A 237       9.159  41.598  25.114  1.00 60.91           C
ATOM   5479  CG  LEU A 237       9.365  42.136  23.662  1.00 62.25           C
ATOM   5480  CD1 LEU A 237      10.605  42.996  23.496  1.00 63.18           C
ATOM   5481  CD2 LEU A 237       9.419  40.966  22.765  1.00 62.89           C
TER
ATOM      1  N   THR A   3      40.527  19.363  20.612  1.00 80.52      seg  N
ATOM      2  CA  THR A   3      41.278  18.625  19.636  1.00 80.52      seg  C
ATOM      4  CB  THR A   3      40.971  17.090  19.710  1.00 79.62      seg  C
ATOM      6  OG1 THR A   3      40.039  16.849  20.760  1.00 79.62      seg  O
ATOM      8  CG2 THR A   3      42.308  16.246  19.999  1.00 79.62      seg  C
ATOM     12  C   THR A   3      40.899  19.134  18.229  1.00 80.52      seg  C
ATOM     13  O   THR A   3      39.780  19.542  17.983  1.00 80.52      seg  O
ATOM     17  N   GLY A   4      41.890  19.246  17.384  1.00 79.31      seg  N
ATOM     18  CA  GLY A   4      41.732  19.850  16.092  1.00 79.31      seg  C
ATOM     21  C   GLY A   4      41.306  18.930  14.985  1.00 79.31      seg  C
ATOM     22  O   GLY A   4      40.121  18.885  14.657  1.00 79.31      seg  O
"""

rec_2_acs_edge = """
CRYST1   69.211   49.956   52.557  90.00  90.00  90.00 P 1
ATOM      1  N   THR A   3      51.193  44.956  23.993  1.00 80.52           N
ATOM      2  CA  THR A   3      50.812  43.732  23.211  1.00 80.52           C
ATOM      3  CB  THR A   3      50.446  42.559  24.181  1.00 79.62           C
ATOM      4  OG1 THR A   3      50.206  41.358  23.433  1.00 79.62           O
ATOM      5  CG2 THR A   3      49.239  42.888  25.066  1.00 79.62           C
ATOM      6  C   THR A   3      49.657  44.014  22.221  1.00 80.52           C
ATOM      7  O   THR A   3      48.520  44.223  22.631  1.00 80.52           O
ATOM      8  N   GLY A   4      49.963  44.013  20.917  1.00 79.31           N
ATOM      9  CA  GLY A   4      49.030  44.458  19.892  1.00 79.31           C
ATOM     10  C   GLY A   4      48.761  43.480  18.761  1.00 79.31           C
ATOM     11  O   GLY A   4      47.790  42.725  18.808  1.00 79.31           O
ATOM     12  N  AALA A   5      49.581  43.499  17.715  0.50 78.81           N
ATOM     13  CA AALA A   5      49.395  42.604  16.581  0.50 78.81           C
ATOM     14  CB AALA A   5      49.774  43.314  15.283  0.50 77.40           C
ATOM     15  C  AALA A   5      50.195  41.315  16.714  0.50 78.81           C
ATOM     16  O  AALA A   5      50.258  40.537  15.757  0.50 78.81           O
ATOM     17  N  BALA A   5      49.681  43.499  17.715  0.50 78.81           N
ATOM     18  CA BALA A   5      49.495  42.604  16.581  0.50 78.81           C
ATOM     19  CB BALA A   5      49.874  43.314  15.283  0.50 77.40           C
ATOM     20  C  BALA A   5      50.295  41.315  16.714  0.50 78.81           C
ATOM     21  O  BALA A   5      50.358  40.537  15.757  0.50 78.81           O
END
"""

rec_2_acs_middle = """
CRYST1   69.211   49.956   52.557  90.00  90.00  90.00 P 1
ATOM      1  N   THR A   3      51.193  44.956  23.993  1.00 80.52           N
ATOM      2  CA  THR A   3      50.812  43.732  23.211  1.00 80.52           C
ATOM      3  CB  THR A   3      50.446  42.559  24.181  1.00 79.62           C
ATOM      4  OG1 THR A   3      50.206  41.358  23.433  1.00 79.62           O
ATOM      5  CG2 THR A   3      49.239  42.888  25.066  1.00 79.62           C
ATOM      6  C   THR A   3      49.657  44.014  22.221  1.00 80.52           C
ATOM      7  O   THR A   3      48.520  44.223  22.631  1.00 80.52           O
ATOM      8  N  AGLY A   4      49.963  44.013  20.917  0.50 79.31           N
ATOM      9  CA AGLY A   4      49.030  44.458  19.892  0.50 79.31           C
ATOM     10  C  AGLY A   4      48.761  43.480  18.761  0.50 79.31           C
ATOM     11  O  AGLY A   4      47.790  42.725  18.808  0.50 79.31           O
ATOM     12  N  BGLY A   4      50.063  44.013  20.917  0.50 79.31           N
ATOM     13  CA BGLY A   4      49.130  44.458  19.892  0.50 79.31           C
ATOM     14  C  BGLY A   4      48.861  43.480  18.761  0.50 79.31           C
ATOM     15  O  BGLY A   4      47.890  42.725  18.808  0.50 79.31           O
ATOM     16  N   ALA A   5      49.581  43.499  17.715  1.00 78.81           N
ATOM     17  CA  ALA A   5      49.395  42.604  16.581  1.00 78.81           C
ATOM     18  CB  ALA A   5      49.774  43.314  15.283  1.00 77.40           C
ATOM     19  C   ALA A   5      50.195  41.315  16.714  1.00 78.81           C
ATOM     20  O   ALA A   5      50.258  40.537  15.757  1.00 78.81           O
END
"""
rec_2_acs_middle_one_atom_1 = """
CRYST1   69.211   49.956   52.557  90.00  90.00  90.00 P 1
ATOM      1  N   THR A   3      51.193  44.956  23.993  1.00 80.52           N
ATOM      2  CA  THR A   3      50.812  43.732  23.211  1.00 80.52           C
ATOM      3  CB  THR A   3      50.446  42.559  24.181  1.00 79.62           C
ATOM      4  OG1 THR A   3      50.206  41.358  23.433  1.00 79.62           O
ATOM      5  CG2 THR A   3      49.239  42.888  25.066  1.00 79.62           C
ATOM      6  C   THR A   3      49.657  44.014  22.221  1.00 80.52           C
ATOM      7  O   THR A   3      48.520  44.223  22.631  1.00 80.52           O
ATOM      8  N  AGLY A   4      49.963  44.013  20.917  0.50 79.31           N
ATOM      9  N  BGLY A   4      50.063  44.013  20.917  0.50 79.31           N
ATOM     10  CA  GLY A   4      49.030  44.458  19.892  0.50 79.31           C
ATOM     11  C   GLY A   4      48.761  43.480  18.761  0.50 79.31           C
ATOM     12  O   GLY A   4      47.790  42.725  18.808  0.50 79.31           O
ATOM     16  N   ALA A   5      49.581  43.499  17.715  1.00 78.81           N
ATOM     17  CA  ALA A   5      49.395  42.604  16.581  1.00 78.81           C
ATOM     18  CB  ALA A   5      49.774  43.314  15.283  1.00 77.40           C
ATOM     19  C   ALA A   5      50.195  41.315  16.714  1.00 78.81           C
ATOM     20  O   ALA A   5      50.258  40.537  15.757  1.00 78.81           O
END
"""
rec_2_acs_middle_one_atom_2 = """
CRYST1   69.211   49.956   52.557  90.00  90.00  90.00 P 1
ATOM      1  N   THR A   3      51.193  44.956  23.993  1.00 80.52           N
ATOM      2  CA  THR A   3      50.812  43.732  23.211  1.00 80.52           C
ATOM      3  CB  THR A   3      50.446  42.559  24.181  1.00 79.62           C
ATOM      4  OG1 THR A   3      50.206  41.358  23.433  1.00 79.62           O
ATOM      5  CG2 THR A   3      49.239  42.888  25.066  1.00 79.62           C
ATOM      6  C   THR A   3      49.657  44.014  22.221  1.00 80.52           C
ATOM      7  O   THR A   3      48.520  44.223  22.631  1.00 80.52           O
ATOM      8  N   GLY A   4      49.963  44.013  20.917  0.50 79.31           N
ATOM      9  CA AGLY A   4      49.030  44.458  19.892  0.50 79.31           C
ATOM     13  CA BGLY A   4      49.130  44.458  19.892  0.50 79.31           C
ATOM     10  C   GLY A   4      48.761  43.480  18.761  0.50 79.31           C
ATOM     11  O   GLY A   4      47.790  42.725  18.808  0.50 79.31           O
ATOM     16  N   ALA A   5      49.581  43.499  17.715  1.00 78.81           N
ATOM     17  CA  ALA A   5      49.395  42.604  16.581  1.00 78.81           C
ATOM     18  CB  ALA A   5      49.774  43.314  15.283  1.00 77.40           C
ATOM     19  C   ALA A   5      50.195  41.315  16.714  1.00 78.81           C
ATOM     20  O   ALA A   5      50.258  40.537  15.757  1.00 78.81           O
END
"""
rec_2_acs_middle_one_atom_3 = """\
CRYST1   72.072   33.173   34.033  90.00  90.00  90.00 P 1
SCALE1      0.013875  0.000000  0.000000        0.00000
SCALE2      0.000000  0.030145  0.000000        0.00000
SCALE3      0.000000  0.000000  0.029383        0.00000
ATOM    519  N   HIS B   1       5.000   8.515  18.112  1.00 20.00           N
ATOM    520  CA  HIS B   1       5.999   8.713  17.074  1.00 20.00           C
ATOM    521  C   HIS B   1       7.157   9.627  17.517  1.00 20.00           C
ATOM    522  O   HIS B   1       8.302   9.165  17.614  1.00 20.00           O
ATOM    523  CB  HIS B   1       5.315   9.226  15.797  1.00 20.00           C
ATOM    524  HA  HIS B   1       6.434   7.742  16.835  1.00 20.00           H
ATOM    525  N   TRP B   2       6.845  10.900  17.805  1.00 20.00           N
ATOM    526  CA ATRP B   2       7.853  11.954  18.083  0.50 20.00           C
ATOM    556  CA BTRP B   2       7.453  11.454  18.083  0.50 20.00           C
ATOM    527  C   TRP B   2       8.071  12.262  19.565  1.00 20.00           C
ATOM    528  O   TRP B   2       8.355  13.406  19.941  1.00 20.00           O
ATOM    529  CB  TRP B   2       7.516  13.257  17.336  1.00 20.00           C
ATOM    530  HA  TRP B   2       8.809  11.606  17.692  1.00 20.00           H
ATOM    531  H  ATRP B   2       5.886  11.243  17.855  0.50 20.00           H
ATOM    532  D  BTRP B   2       5.886  11.243  17.855  0.50 20.00           D
ATOM    533  N   GLU B   3       7.910  11.239  20.396  1.00 20.00           N
ATOM    534  CA  GLU B   3       8.310  11.284  21.798  1.00 20.00           C
ATOM    535  C   GLU B   3       9.344  10.190  21.979  1.00 20.00           C
ATOM    536  O   GLU B   3      10.197  10.267  22.867  1.00 20.00           O
ATOM    537  CB  GLU B   3       7.115  11.041  22.731  1.00 20.00           C
ATOM    538  HA  GLU B   3       8.761  12.248  22.034  1.00 20.00           H
ATOM    539  H  AGLU B   3       7.474  10.360  20.122  0.50 20.00           H
ATOM    540  D  BGLU B   3       7.474  10.360  20.122  0.50 20.00           D
"""

rec_4_residues_isertions = """
CRYST1   69.211   49.956   52.557  90.00  90.00  90.00 P 1
ATOM      1  N   THR A   3      51.193  44.956  23.993  1.00 80.52           N
ATOM      2  CA  THR A   3      50.812  43.732  23.211  1.00 80.52           C
ATOM      4  CB  THR A   3      50.446  42.559  24.181  1.00 79.62           C
ATOM      6  OG1 THR A   3      50.206  41.358  23.433  1.00 79.62           O
ATOM      8  CG2 THR A   3      49.239  42.888  25.066  1.00 79.62           C
ATOM     12  C   THR A   3      49.657  44.014  22.221  1.00 80.52           C
ATOM     13  O   THR A   3      48.520  44.223  22.631  1.00 80.52           O
ATOM     17  N   GLY A   3A     49.963  44.013  20.917  1.00 79.31           N
ATOM     18  CA  GLY A   3A     49.030  44.458  19.892  1.00 79.31           C
ATOM     21  C   GLY A   3A     48.761  43.480  18.761  1.00 79.31           C
ATOM     22  O   GLY A   3A     47.790  42.725  18.808  1.00 79.31           O
ATOM     24  N   ALA A   3B     49.581  43.499  17.715  1.00 78.81           N
ATOM     25  CA  ALA A   3B     49.395  42.604  16.581  1.00 78.81           C
ATOM     27  CB  ALA A   3B     49.774  43.314  15.283  1.00 77.40           C
ATOM     31  C   ALA A   3B     50.195  41.315  16.714  1.00 78.81           C
ATOM     32  O   ALA A   3B     50.258  40.537  15.757  1.00 78.81           O
ATOM     34  N   GLN A   4      50.816  41.073  17.872  1.00 80.55           N
ATOM     35  CA  GLN A   4      51.642  39.880  18.018  1.00 80.55           C
ATOM     37  CB  GLN A   4      52.383  39.879  19.354  1.00 79.84           C
ATOM     40  CG  GLN A   4      53.264  41.072  19.596  1.00 79.84           C
ATOM     43  CD  GLN A   4      52.490  42.211  20.225  1.00 79.84           C
ATOM     44  OE1 GLN A   4      51.290  42.091  20.489  1.00 79.84           O
ATOM     45  NE2 GLN A   4      53.167  43.325  20.468  1.00 79.84           N
ATOM     48  C   GLN A   4      50.788  38.631  17.945  1.00 80.55           C
ATOM     49  O   GLN A   4      51.148  37.659  17.273  1.00 80.55           O
"""

pdb_1yjp = """
CRYST1   21.937    4.866   23.477  90.00 107.08  90.00 P 1 21 1      2
ATOM      1  N   GLY A   1      -9.009   4.612   6.102  1.00 16.77           N
ATOM      2  CA  GLY A   1      -9.052   4.207   4.651  1.00 16.57           C
ATOM      3  C   GLY A   1      -8.015   3.140   4.419  1.00 16.16           C
ATOM      4  O   GLY A   1      -7.523   2.521   5.381  1.00 16.78           O
ATOM      5  N   ASN A   2      -7.656   2.923   3.155  1.00 15.02           N
ATOM      6  CA  ASN A   2      -6.522   2.038   2.831  1.00 14.10           C
ATOM      7  C   ASN A   2      -5.241   2.537   3.427  1.00 13.13           C
ATOM      8  O   ASN A   2      -4.978   3.742   3.426  1.00 11.91           O
ATOM      9  CB  ASN A   2      -6.346   1.881   1.341  1.00 15.38           C
ATOM     10  CG  ASN A   2      -7.584   1.342   0.692  1.00 14.08           C
ATOM     11  OD1 ASN A   2      -8.025   0.227   1.016  1.00 17.46           O
ATOM     12  ND2 ASN A   2      -8.204   2.155  -0.169  1.00 11.72           N
ATOM     13  N   ASN A   3      -4.438   1.590   3.905  1.00 12.26           N
ATOM     14  CA  ASN A   3      -3.193   1.904   4.589  1.00 11.74           C
ATOM     15  C   ASN A   3      -1.955   1.332   3.895  1.00 11.10           C
ATOM     16  O   ASN A   3      -1.872   0.119   3.648  1.00 10.42           O
ATOM     17  CB  ASN A   3      -3.259   1.378   6.042  1.00 12.15           C
ATOM     18  CG  ASN A   3      -2.006   1.739   6.861  1.00 12.82           C
ATOM     19  OD1 ASN A   3      -1.702   2.925   7.072  1.00 15.05           O
ATOM     20  ND2 ASN A   3      -1.271   0.715   7.306  1.00 13.48           N
ATOM     21  N   GLN A   4      -1.005   2.228   3.598  1.00 10.29           N
ATOM     22  CA  GLN A   4       0.384   1.888   3.199  1.00 10.53           C
ATOM     23  C   GLN A   4       1.435   2.606   4.088  1.00 10.24           C
ATOM     24  O   GLN A   4       1.547   3.843   4.115  1.00  8.86           O
ATOM     25  CB  GLN A   4       0.656   2.148   1.711  1.00  9.80           C
ATOM     26  CG  GLN A   4       1.944   1.458   1.213  1.00 10.25           C
ATOM     27  CD  GLN A   4       2.504   2.044  -0.089  1.00 12.43           C
ATOM     28  OE1 GLN A   4       2.744   3.268  -0.190  1.00 14.62           O
ATOM     29  NE2 GLN A   4       2.750   1.161  -1.091  1.00  9.05           N
ATOM     30  N   GLN A   5       2.154   1.821   4.871  1.00 10.38           N
ATOM     31  CA  GLN A   5       3.270   2.361   5.640  1.00 11.39           C
ATOM     32  C   GLN A   5       4.594   1.768   5.172  1.00 11.52           C
ATOM     33  O   GLN A   5       4.768   0.546   5.054  1.00 12.05           O
ATOM     34  CB  GLN A   5       3.056   2.183   7.147  1.00 11.96           C
ATOM     35  CG  GLN A   5       1.829   2.950   7.647  1.00 10.81           C
ATOM     36  CD  GLN A   5       1.344   2.414   8.954  1.00 13.10           C
ATOM     37  OE1 GLN A   5       0.774   1.325   9.002  1.00 10.65           O
ATOM     38  NE2 GLN A   5       1.549   3.187  10.039  1.00 12.30           N
ATOM     39  N   ASN A   6       5.514   2.664   4.856  1.00 11.99           N
ATOM     40  CA  ASN A   6       6.831   2.310   4.318  1.00 12.30           C
ATOM     41  C   ASN A   6       7.854   2.761   5.324  1.00 13.40           C
ATOM     42  O   ASN A   6       8.219   3.943   5.374  1.00 13.92           O
ATOM     43  CB  ASN A   6       7.065   3.016   2.993  1.00 12.13           C
ATOM     44  CG  ASN A   6       5.961   2.735   2.003  1.00 12.77           C
ATOM     45  OD1 ASN A   6       5.798   1.604   1.551  1.00 14.27           O
ATOM     46  ND2 ASN A   6       5.195   3.747   1.679  1.00 10.07           N
ATOM     47  N   TYR A   7       8.292   1.817   6.147  1.00 14.70           N
ATOM     48  CA  TYR A   7       9.159   2.144   7.299  1.00 15.18           C
ATOM     49  C   TYR A   7      10.603   2.331   6.885  1.00 15.91           C
ATOM     50  O   TYR A   7      11.041   1.811   5.855  1.00 15.76           O
ATOM     51  CB  TYR A   7       9.061   1.065   8.369  1.00 15.35           C
ATOM     52  CG  TYR A   7       7.665   0.929   8.902  1.00 14.45           C
ATOM     53  CD1 TYR A   7       6.771   0.021   8.327  1.00 15.68           C
ATOM     54  CD2 TYR A   7       7.210   1.756   9.920  1.00 14.80           C
ATOM     55  CE1 TYR A   7       5.480  -0.094   8.796  1.00 13.46           C
ATOM     56  CE2 TYR A   7       5.904   1.649  10.416  1.00 14.33           C
ATOM     57  CZ  TYR A   7       5.047   0.729   9.831  1.00 15.09           C
ATOM     58  OH  TYR A   7       3.766   0.589  10.291  1.00 14.39           O
ATOM     59  OXT TYR A   7      11.358   2.999   7.612  1.00 17.49           O
"""

pdb_1yjp_minus_4 = """
CRYST1   21.937    4.866   23.477  90.00 107.08  90.00 P 1 21 1      2
ATOM      1  N   GLY A   1      -9.009   4.612   6.102  1.00 16.77           N
ATOM      2  CA  GLY A   1      -9.052   4.207   4.651  1.00 16.57           C
ATOM      3  C   GLY A   1      -8.015   3.140   4.419  1.00 16.16           C
ATOM      4  O   GLY A   1      -7.523   2.521   5.381  1.00 16.78           O
ATOM      5  N   ASN A   2      -7.656   2.923   3.155  1.00 15.02           N
ATOM      6  CA  ASN A   2      -6.522   2.038   2.831  1.00 14.10           C
ATOM      7  C   ASN A   2      -5.241   2.537   3.427  1.00 13.13           C
ATOM      8  O   ASN A   2      -4.978   3.742   3.426  1.00 11.91           O
ATOM      9  CB  ASN A   2      -6.346   1.881   1.341  1.00 15.38           C
ATOM     10  CG  ASN A   2      -7.584   1.342   0.692  1.00 14.08           C
ATOM     11  OD1 ASN A   2      -8.025   0.227   1.016  1.00 17.46           O
ATOM     12  ND2 ASN A   2      -8.204   2.155  -0.169  1.00 11.72           N
ATOM     13  N   ASN A   3      -4.438   1.590   3.905  1.00 12.26           N
ATOM     14  CA  ASN A   3      -3.193   1.904   4.589  1.00 11.74           C
ATOM     15  C   ASN A   3      -1.955   1.332   3.895  1.00 11.10           C
ATOM     16  O   ASN A   3      -1.872   0.119   3.648  1.00 10.42           O
ATOM     17  CB  ASN A   3      -3.259   1.378   6.042  1.00 12.15           C
ATOM     18  CG  ASN A   3      -2.006   1.739   6.861  1.00 12.82           C
ATOM     19  OD1 ASN A   3      -1.702   2.925   7.072  1.00 15.05           O
ATOM     20  ND2 ASN A   3      -1.271   0.715   7.306  1.00 13.48           N
ATOM     30  N   GLN A   5       2.154   1.821   4.871  1.00 10.38           N
ATOM     31  CA  GLN A   5       3.270   2.361   5.640  1.00 11.39           C
ATOM     32  C   GLN A   5       4.594   1.768   5.172  1.00 11.52           C
ATOM     33  O   GLN A   5       4.768   0.546   5.054  1.00 12.05           O
ATOM     34  CB  GLN A   5       3.056   2.183   7.147  1.00 11.96           C
ATOM     35  CG  GLN A   5       1.829   2.950   7.647  1.00 10.81           C
ATOM     36  CD  GLN A   5       1.344   2.414   8.954  1.00 13.10           C
ATOM     37  OE1 GLN A   5       0.774   1.325   9.002  1.00 10.65           O
ATOM     38  NE2 GLN A   5       1.549   3.187  10.039  1.00 12.30           N
ATOM     39  N   ASN A   6       5.514   2.664   4.856  1.00 11.99           N
ATOM     40  CA  ASN A   6       6.831   2.310   4.318  1.00 12.30           C
ATOM     41  C   ASN A   6       7.854   2.761   5.324  1.00 13.40           C
ATOM     42  O   ASN A   6       8.219   3.943   5.374  1.00 13.92           O
ATOM     43  CB  ASN A   6       7.065   3.016   2.993  1.00 12.13           C
ATOM     44  CG  ASN A   6       5.961   2.735   2.003  1.00 12.77           C
ATOM     45  OD1 ASN A   6       5.798   1.604   1.551  1.00 14.27           O
ATOM     46  ND2 ASN A   6       5.195   3.747   1.679  1.00 10.07           N
ATOM     47  N   TYR A   7       8.292   1.817   6.147  1.00 14.70           N
ATOM     48  CA  TYR A   7       9.159   2.144   7.299  1.00 15.18           C
ATOM     49  C   TYR A   7      10.603   2.331   6.885  1.00 15.91           C
ATOM     50  O   TYR A   7      11.041   1.811   5.855  1.00 15.76           O
ATOM     51  CB  TYR A   7       9.061   1.065   8.369  1.00 15.35           C
ATOM     52  CG  TYR A   7       7.665   0.929   8.902  1.00 14.45           C
ATOM     53  CD1 TYR A   7       6.771   0.021   8.327  1.00 15.68           C
ATOM     54  CD2 TYR A   7       7.210   1.756   9.920  1.00 14.80           C
ATOM     55  CE1 TYR A   7       5.480  -0.094   8.796  1.00 13.46           C
ATOM     56  CE2 TYR A   7       5.904   1.649  10.416  1.00 14.33           C
ATOM     57  CZ  TYR A   7       5.047   0.729   9.831  1.00 15.09           C
ATOM     58  OH  TYR A   7       3.766   0.589  10.291  1.00 14.39           O
ATOM     59  OXT TYR A   7      11.358   2.999   7.612  1.00 17.49           O
"""

rec_3_res_ac_h = """\
CRYST1   72.072   33.173   34.033  90.00  90.00  90.00 P 1
ATOM    519  N   HIS B   1       5.000   8.515  18.112  1.00 20.00           N
ATOM    520  CA  HIS B   1       5.999   8.713  17.074  1.00 20.00           C
ATOM    521  C   HIS B   1       7.157   9.627  17.517  1.00 20.00           C
ATOM    522  O   HIS B   1       8.302   9.165  17.614  1.00 20.00           O
ATOM    523  CB  HIS B   1       5.315   9.226  15.797  1.00 20.00           C
ATOM    524  HA  HIS B   1       6.434   7.742  16.835  1.00 20.00           H
ATOM    525  N   TRP B   2       6.845  10.900  17.805  1.00 20.00           N
ATOM    526  CA  TRP B   2       7.853  11.954  18.083  1.00 20.00           C
ATOM    527  C   TRP B   2       8.071  12.262  19.565  1.00 20.00           C
ATOM    528  O   TRP B   2       8.355  13.406  19.941  1.00 20.00           O
ATOM    529  CB  TRP B   2       7.516  13.257  17.336  1.00 20.00           C
ATOM    530  HA  TRP B   2       8.809  11.606  17.692  1.00 20.00           H
ATOM    531  H  ATRP B   2       5.886  11.243  17.855  0.50 20.00           H
ATOM    532  D  BTRP B   2       5.886  11.243  17.855  0.50 20.00           D
ATOM    533  N   GLU B   3       7.910  11.239  20.396  1.00 20.00           N
ATOM    534  CA  GLU B   3       8.310  11.284  21.798  1.00 20.00           C
ATOM    535  C   GLU B   3       9.344  10.190  21.979  1.00 20.00           C
ATOM    536  O   GLU B   3      10.197  10.267  22.867  1.00 20.00           O
ATOM    537  CB  GLU B   3       7.115  11.041  22.731  1.00 20.00           C
ATOM    538  HA  GLU B   3       8.761  12.248  22.034  1.00 20.00           H
ATOM    539  H  AGLU B   3       7.474  10.360  20.122  0.50 20.00           H
ATOM    540  D  BGLU B   3       7.474  10.360  20.122  0.50 20.00           D
"""

def exercise_phi_psi_extraction():
  for n_prox, raw_records in [
      ([0, 0], rec_1_residue),
      ([0, 0], rec_2_residues),
      ([4, 2], rec_3_residues),
      ([6, 4], rec_4_residues),
      ([0, 0], rec_2_chains),
      ([0, 0], rec_2_segids),
      ([8, 4], rec_2_acs_edge),
      ([8, 4], rec_2_acs_middle),
      ([6, 4], rec_4_residues_isertions),
      ([12, 10], pdb_1yjp),
      ([8, 4], pdb_1yjp_minus_4),
      ([4, 2], rec_3_res_ac_h),
      ([8, 4], rec_2_acs_middle_one_atom_1),
      ([8, 4], rec_2_acs_middle_one_atom_2),
      ([8, 4], rec_2_acs_middle_one_atom_3),
      ]:
    tmp_hierarchy = iotbx.pdb.input(
      source_info=None,
      lines=flex.split_lines(raw_records)).construct_hierarchy()
    for opp in range(2):
      proxies = []
      for three in generate_protein_threes(
          hierarchy=tmp_hierarchy,
          geometry=None):
        ppp = three.get_dummy_dihedral_proxies(only_psi_phi_pairs=opp)
        print three,'ppp',len(ppp)
        proxies.extend(ppp)
      print len(proxies), n_prox
      assert len(proxies) == n_prox[opp], \
         "Expected %d, got %d" % (
           n_prox[opp],
           len(proxies),
           )

if (__name__ == "__main__"):
  exercise_phi_psi_extraction()
