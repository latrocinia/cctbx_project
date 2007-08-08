#ifndef IOTBX_PDB_RNA_DNA_ATOM_NAMES_H
#define IOTBX_PDB_RNA_DNA_ATOM_NAMES_H

#include <string>

namespace iotbx { namespace pdb {

//! Highly optimized dictionary of RNA/DNA atom name aliases.
namespace rna_dna_atom_names {

  //! Constants.
  namespace info_flags {

    static const unsigned none =      0x00000000U;
    static const unsigned a =         0x00000001U;
    static const unsigned c =         0x00000002U;
    static const unsigned g =         0x00000004U;
    static const unsigned u =         0x00000008U;
    static const unsigned da =        0x00000010U;
    static const unsigned dc =        0x00000020U;
    static const unsigned dg =        0x00000040U;
    static const unsigned dt =        0x00000080U;
    static const unsigned any_bit =   0x00000100U;
    static const unsigned any =       0x000001ffU;
    static const unsigned deuterium = 0x00000200U;

  } // namespace info_flags

  //! Translates atom name alias to reference name.
  struct info
  {
    const char* reference_name;
    unsigned flags;

    info() {}

    info(const char* work_name)
    :
      reference_name(0),
      flags(info_flags::none)
    {
      using namespace info_flags;
      switch (work_name[0])
      {
        case '1':
          if (work_name[1] == 'D') {
            flags |= deuterium;
          }
          else if (work_name[1] != 'H') {
            break;
          }
          switch (work_name[2])
          {
            case '2':
              if (work_name[3] == '\0') {
                reference_name = " H21";
                flags |= g | dg;
                return;
              }
              if (work_name[3] == '\'') {
                if (work_name[4] == '\0') {
                  reference_name = " H2'";
                  flags |= any;
                  return;
                }
              }
              break;

            case '4':
              if (work_name[3] != '\0') break;
              reference_name = " H41";
              flags |= c | dc;
              return;

            case '5':
              if (work_name[3] == '\'') {
                if (work_name[4] == '\0') {
                  reference_name = " H5'";
                  flags |= any;
                  return;
                }
                break;
              }
              if (work_name[3] == 'M') {
                if (work_name[4] == '\0') {
                  reference_name = " H71";
                  flags |= dt;
                  return;
                }
              }
              break;

            case '6':
              if (work_name[3] != '\0') break;
              reference_name = " H61";
              flags |= a | da;
              return;

            default:
              break;
          }
          flags = none;
          break;

        case '2':
          if (work_name[1] == 'D') {
            flags |= deuterium;
          }
          else if (work_name[1] != 'H') {
            break;
          }
          switch (work_name[2])
          {
            case '2':
              if (work_name[3] == '\0') {
                reference_name = " H22";
                flags |= g | dg;
                return;
              }
              if (work_name[3] == '\'') {
                if (work_name[4] == '\0') {
                  reference_name = "H2''";
                  flags |= da | dc | dg | dt;
                  return;
                }
              }
              break;

            case '4':
              if (work_name[3] != '\0') break;
              reference_name = " H42";
              flags |= c | dc;
              return;

            case '5':
              if (work_name[3] == '\'') {
                if (work_name[4] == '\0') {
                  reference_name = "H5''";
                  flags |= any;
                  return;
                }
                break;
              }
              if (work_name[3] == 'M') {
                if (work_name[4] == '\0') {
                  reference_name = " H72";
                  flags |= dt;
                  return;
                }
              }
              break;

            case '6':
              if (work_name[3] != '\0') break;
              reference_name = " H62";
              flags |= a | da;
              return;

            case 'O':
              if (work_name[3] == '\'') {
                if (work_name[4] == '\0') {
                  reference_name = "HO2'";
                  flags |= a | c | g | u;
                  return;
                }
                break;
              }
              if (work_name[3] == 'P') {
                if (work_name[4] == '\0') {
                  reference_name = "HOP2";
                  flags |= any;
                  return;
                }
              }
              break;

            default:
              break;
          }
          flags = none;
          break;

        case '3':
          if (work_name[1] == 'D') {
            flags |= deuterium;
          }
          else if (work_name[1] != 'H') {
            break;
          }
          switch (work_name[2])
          {
            case '5':
              if (work_name[3] == 'M') {
                if (work_name[4] == '\0') {
                  reference_name = " H73";
                  flags |= dt;
                  return;
                }
              }
              break;

            case 'O':
              if (work_name[3] == 'P') {
                if (work_name[4] == '\0') {
                  reference_name = "HOP3";
                  flags |= any;
                  return;
                }
              }
              break;

            default:
              break;
          }
          flags = none;
          break;

        case 'C':
          switch (work_name[1])
          {
            case '1':
              if (work_name[2] == '\'') {
                if (work_name[3] == '\0') {
                  reference_name = " C1'";
                  flags |= any;
                  return;
                }
              }
              break;

            case '2':
              if (work_name[2] == '\0') {
                reference_name = " C2 ";
                flags |= any;
                return;
              }
              if (work_name[2] == '\'') {
                if (work_name[3] == '\0') {
                  reference_name = " C2'";
                  flags |= any;
                  return;
                }
              }
              break;

            case '3':
              if (work_name[2] == '\'') {
                if (work_name[3] == '\0') {
                  reference_name = " C3'";
                  flags |= any;
                  return;
                }
              }
              break;

            case '4':
              if (work_name[2] == '\0') {
                reference_name = " C4 ";
                flags |= any;
                return;
              }
              if (work_name[2] == '\'') {
                if (work_name[3] == '\0') {
                  reference_name = " C4'";
                  flags |= any;
                  return;
                }
              }
              break;

            case '5':
              if (work_name[2] == '\0') {
                reference_name = " C5 ";
                flags |= any;
                return;
              }
              if (work_name[2] == '\'') {
                if (work_name[3] == '\0') {
                  reference_name = " C5'";
                  flags |= any;
                  return;
                }
                break;
              }
              if (work_name[2] == 'M') {
                if (work_name[3] == '\0') {
                  reference_name = " C7 ";
                  flags |= dt;
                  return;
                }
              }
              break;

            case '6':
              if (work_name[2] != '\0') break;
              reference_name = " C6 ";
              flags |= any;
              return;

            case '7':
              if (work_name[2] != '\0') break;
              reference_name = " C7 ";
              flags |= dt;
              return;

            case '8':
              if (work_name[2] != '\0') break;
              reference_name = " C8 ";
              flags |= a | g | da | dg;
              return;

            default:
              break;
          }
          break;

        case 'D':
          flags |= deuterium;
        case 'H':
          switch (work_name[1])
          {
            case '1':
              if (work_name[2] == '\0') {
                reference_name = " H1 ";
                flags |= g | dg;
                return;
              }
              if (work_name[2] == '\'') {
                if (work_name[3] == '\0') {
                  reference_name = " H1'";
                  flags |= any;
                  return;
                }
              }
              break;

            case '2':
              if (work_name[2] == '\0') {
                reference_name = " H2 ";
                flags |= a | da;
                return;
              }
              if (work_name[2] == '\'') {
                if (work_name[3] == '\0') {
                  reference_name = " H2'";
                  flags |= any;
                  return;
                }
                if (work_name[3] == '1') {
                  if (work_name[4] == '\0') {
                    reference_name = " H2'";
                    flags |= any;
                    return;
                  }
                  break;
                }
                if (work_name[3] == '\'' || work_name[3] == '2') {
                  if (work_name[4] == '\0') {
                    reference_name = "H2''";
                    flags |= da | dc | dg | dt;
                    return;
                  }
                }
                break;
              }
              if (work_name[2] == '1') {
                if (work_name[3] == '\0') {
                  reference_name = " H21";
                  flags |= g | dg;
                  return;
                }
                break;
              }
              if (work_name[2] == '2') {
                if (work_name[3] == '\0') {
                  reference_name = " H22";
                  flags |= g | dg;
                  return;
                }
              }
              break;

            case '3':
              if (work_name[2] == '\0') {
                reference_name = " H3 ";
                flags |= u | dt;
                return;
              }
              if (work_name[2] == '\'') {
                if (work_name[3] == '\0') {
                  reference_name = " H3'";
                  flags |= any;
                  return;
                }
                break;
              }
              if (work_name[2] == 'T') {
                if (work_name[3] == '\0') {
                  reference_name = "HO3'";
                  flags |= any;
                  return;
                }
              }
              break;

            case '4':
              if (work_name[2] == '\'') {
                if (work_name[3] == '\0') {
                  reference_name = " H4'";
                  flags |= any;
                  return;
                }
                break;
              }
              if (work_name[2] == '1') {
                if (work_name[3] == '\0') {
                  reference_name = " H41";
                  flags |= c | dc;
                  return;
                }
                break;
              }
              if (work_name[2] == '2') {
                if (work_name[3] == '\0') {
                  reference_name = " H42";
                  flags |= c | dc;
                  return;
                }
              }
              break;

            case '5':
              if (work_name[2] == '\0') {
                reference_name = " H5 ";
                flags |= c | u | dc;
                return;
              }
              if (work_name[2] == '\'') {
                if (work_name[3] == '\0') {
                  reference_name = " H5'";
                  flags |= any;
                  return;
                }
                if (work_name[3] == '1') {
                  if (work_name[4] == '\0') {
                    reference_name = " H5'";
                    flags |= any;
                    return;
                  }
                  break;
                }
                if (work_name[3] == '2' || work_name[3] == '\'') {
                  if (work_name[4] == '\0') {
                    reference_name = "H5''";
                    flags |= any;
                    return;
                  }
                }
                break;
              }
              if (work_name[2] == 'M') {
                if (work_name[3] == '1') {
                  if (work_name[4] == '\0') {
                    reference_name = " H71";
                    flags |= dt;
                    return;
                  }
                  break;
                }
                if (work_name[3] == '2') {
                  if (work_name[4] == '\0') {
                    reference_name = " H72";
                    flags |= dt;
                    return;
                  }
                  break;
                }
                if (work_name[3] == '3') {
                  if (work_name[4] == '\0') {
                    reference_name = " H73";
                    flags |= dt;
                    return;
                  }
                }
                break;
              }
              if (work_name[2] == 'T') {
                if (work_name[3] == '\0') {
                  reference_name = "HO5'";
                  flags |= any;
                  return;
                }
              }
              break;

            case '6':
              if (work_name[2] == '\0') {
                reference_name = " H6 ";
                flags |= c | u | dc | dt;
                return;
              }
              if (work_name[2] == '1') {
                if (work_name[3] == '\0') {
                  reference_name = " H61";
                  flags |= a | da;
                  return;
                }
                break;
              }
              if (work_name[2] == '2') {
                if (work_name[3] == '\0') {
                  reference_name = " H62";
                  flags |= a | da;
                  return;
                }
              }
              break;

            case '7':
              if (work_name[2] == '1') {
                if (work_name[3] == '\0') {
                  reference_name = " H71";
                  flags |= dt;
                  return;
                }
                break;
              }
              if (work_name[2] == '2') {
                if (work_name[3] == '\0') {
                  reference_name = " H72";
                  flags |= dt;
                  return;
                }
                break;
              }
              if (work_name[2] == '3') {
                if (work_name[3] == '\0') {
                  reference_name = " H73";
                  flags |= dt;
                  return;
                }
              }
              break;

            case '8':
              if (work_name[2] != '\0') break;
              reference_name = " H8 ";
              flags |= a | g | da | dg;
              return;

            case 'O':
              if (work_name[2] == '2') {
                if (work_name[3] == '\'') {
                  if (work_name[4] == '\0') {
                    reference_name = "HO2'";
                    flags |= a | c | g | u;
                    return;
                  }
                }
                break;
              }
              if (work_name[2] == '3') {
                if (work_name[3] == '\'') {
                  if (work_name[4] == '\0') {
                    reference_name = "HO3'";
                    flags |= any;
                    return;
                  }
                }
                break;
              }
              if (work_name[2] == '5') {
                if (work_name[3] == '\'') {
                  if (work_name[4] == '\0') {
                    reference_name = "HO5'";
                    flags |= any;
                    return;
                  }
                }
                break;
              }
              if (work_name[2] == 'P') {
                if (work_name[3] == '2') {
                  if (work_name[4] == '\0') {
                    reference_name = "HOP2";
                    flags |= any;
                    return;
                  }
                  break;
                }
                if (work_name[3] == '3') {
                  if (work_name[4] == '\0') {
                    reference_name = "HOP3";
                    flags |= any;
                    return;
                  }
                }
              }
              break;

            default:
              break;
          }
          flags = none;
          break;

        case 'N':
          switch (work_name[1])
          {
            case '1':
              if (work_name[2] != '\0') break;
              reference_name = " N1 ";
              flags |= any;
              return;

            case '2':
              if (work_name[2] != '\0') break;
              reference_name = " N2 ";
              flags |= g | dg;
              return;

            case '3':
              if (work_name[2] != '\0') break;
              reference_name = " N3 ";
              flags |= any;
              return;

            case '4':
              if (work_name[2] != '\0') break;
              reference_name = " N4 ";
              flags |= c | dc;
              return;

            case '6':
              if (work_name[2] != '\0') break;
              reference_name = " N6 ";
              flags |= a | da;
              return;

            case '7':
              if (work_name[2] != '\0') break;
              reference_name = " N7 ";
              flags |= a | g | da | dg;
              return;

            case '9':
              if (work_name[2] != '\0') break;
              reference_name = " N9 ";
              flags |= a | g | da | dg;
              return;

            default:
              break;
          }
          break;

        case 'O':
          switch (work_name[1])
          {
            case '1':
              if (work_name[2] == 'P') {
                if (work_name[3] == '\0') {
                  reference_name = " OP1";
                  flags |= any;
                  return;
                }
              }
              break;

            case '2':
              if (work_name[2] == '\0') {
                reference_name = " O2 ";
                flags |= c | u | dc | dt;
                return;
              }
              if (work_name[2] == '\'') {
                if (work_name[3] == '\0') {
                  reference_name = " O2'";
                  flags |= a | c | g | u;
                  return;
                }
                break;
              }
              if (work_name[2] == 'P') {
                if (work_name[3] == '\0') {
                  reference_name = " OP2";
                  flags |= any;
                  return;
                }
              }
              break;

            case '3':
              if (work_name[2] == '\'') {
                if (work_name[3] == '\0') {
                  reference_name = " O3'";
                  flags |= any;
                  return;
                }
                break;
              }
              if (work_name[2] == 'P' || work_name[2] == 'T') {
                if (work_name[3] == '\0') {
                  reference_name = " OP3";
                  flags |= any;
                  return;
                }
              }
              break;

            case '4':
              if (work_name[2] == '\0') {
                reference_name = " O4 ";
                flags |= u | dt;
                return;
              }
              if (work_name[2] == '\'') {
                if (work_name[3] == '\0') {
                  reference_name = " O4'";
                  flags |= any;
                  return;
                }
              }
              break;

            case '5':
              if (work_name[2] == '\'') {
                if (work_name[3] == '\0') {
                  reference_name = " O5'";
                  flags |= any;
                  return;
                }
                break;
              }
              if (work_name[2] == 'T') {
                if (work_name[3] == '\0') {
                  reference_name = " O5T";
                  flags |= any;
                  return;
                }
              }
              break;

            case '6':
              if (work_name[2] != '\0') break;
              reference_name = " O6 ";
              flags |= g | dg;
              return;

            case 'P':
              if (work_name[2] == '1') {
                if (work_name[3] == '\0') {
                  reference_name = " OP1";
                  flags |= any;
                  return;
                }
                break;
              }
              if (work_name[2] == '2') {
                if (work_name[3] == '\0') {
                  reference_name = " OP2";
                  flags |= any;
                  return;
                }
                break;
              }
              if (work_name[2] == '3') {
                if (work_name[3] == '\0') {
                  reference_name = " OP3";
                  flags |= any;
                  return;
                }
              }
              break;

            default:
              break;
          }
          break;

        case 'P':
          if (work_name[1] == '\0') {
            reference_name = " P  ";
            flags |= any;
            return;
          }
          break;

        default:
          break;
      }
    }

    std::string
    flags_as_string() const
    {
      using namespace info_flags;
      std::string result;
      if (flags & any_bit) {
        result += " ANY";
      }
      else {
        if (flags & a) result += " A";
        if (flags & c) result += " C";
        if (flags & g) result += " G";
        if (flags & u) result += " U";
        if (flags & da) result += " DA";
        if (flags & dc) result += " DC";
        if (flags & dg) result += " DG";
        if (flags & dt) result += " DT";
      }
      if (flags & deuterium) {
        result += " Deuterium";
      }
      if (result.size() == 0) return "None";
      return result.substr(1);
    }
  };

}}} // namespace iotbx::pdb::rna_dna_atom_names

#endif // IOTBX_PDB_RNA_DNA_ATOM_NAMES_H
