import sys

def write_copyright():
  print \
"""/* Copyright (c) 2001 The Regents of the University of California through
   E.O. Lawrence Berkeley National Laboratory, subject to approval by the
   U.S. Department of Energy. See files COPYRIGHT.txt and
   cctbx/LICENSE.txt for further details.

   Revision history:
     Jan 2002: Created (Ralf W. Grosse-Kunstleve)

   *****************************************************
   THIS IS AN AUTOMATICALLY GENERATED FILE. DO NOT EDIT.
   *****************************************************

   Generated by:
     %s
 */""" % (sys.argv[0],)

arithmetic_unary_ops = ("-")
arithmetic_binary_ops = ("+", "-", "*", "/", "%")
arithmetic_in_place_binary_ops = ("+=", "-=", "*=", "/=", "%=")
logical_unary_ops = ("!")
logical_binary_ops = ("&&", "||")
boolean_ops = ("==", "!=", ">", "<", ">=", "<=")

reduction_functions_1arg = (
  "max_index", "min_index",
  "max", "min",
  "sum", "product",
  "mean",
)
reduction_functions_2arg = (
  "weighted_mean",
)

cmath_1arg = (
  'acos', 'cos', 'fmod', 'tan',
  'asin', 'cosh', 'tanh',
  'atan', 'exp', 'sin',
  'fabs', 'log', 'sinh',
  'ceil', 'floor', 'log10', 'sqrt',
)

cmath_2arg = (
  'fmod', 'pow', 'atan2',
)

cstdlib_1arg = (
  'abs',
)

class empty: pass

def decl_params(array_type_name, op_class, type_flags):
  v = empty
  if (array_type_name == "tiny"):
    if (type_flags == (1,1)):
      v.typelist = \
       ["typename ElementTypeLhs, typename ElementTypeRhs, std::size_t N"]
      v.return_type = (
        "tiny<",
        "  typename binary_operator_traits<",
        "    ElementTypeLhs, ElementTypeRhs>::%s, N>" % (op_class,))
      v.param_lhs = "tiny<ElementTypeLhs, N>"
      v.param_rhs = "tiny<ElementTypeRhs, N>"
    elif (type_flags == (1,0)):
      v.typelist = ["typename ElementTypeLhs, std::size_t N"]
      v.return_type = ("tiny<ElementTypeLhs, N>",)
      v.param_lhs = "tiny<ElementTypeLhs, N>"
      v.param_rhs = "ElementTypeLhs"
    elif (type_flags == (0,1)):
      v.typelist = ["typename ElementTypeRhs, std::size_t N"]
      v.return_type = ("tiny<ElementTypeRhs, N>",)
      v.param_lhs = "ElementTypeRhs"
      v.param_rhs = "tiny<ElementTypeRhs, N>"
  elif (array_type_name == "small"):
    if (type_flags == (1,1)):
      v.typelist = [
        "typename ElementTypeLhs, std::size_t NLhs,",
        "          typename ElementTypeRhs, std::size_t NRhs"]
      v.return_type = (
        "small<",
        "  typename binary_operator_traits<",
        "    ElementTypeLhs, ElementTypeRhs>::%s, (NLhs<NRhs?NLhs:NRhs)>" % (
          op_class,))
      v.param_lhs = "small<ElementTypeLhs, NLhs>"
      v.param_rhs = "small<ElementTypeRhs, NRhs>"
    elif (type_flags == (1,0)):
      v.typelist = ["typename ElementTypeLhs, std::size_t NLhs"]
      v.return_type = ("small<ElementTypeLhs, NLhs>",)
      v.param_lhs = "small<ElementTypeLhs, NLhs>"
      v.param_rhs = "ElementTypeLhs"
    elif (type_flags == (0,1)):
      v.typelist = ["typename ElementTypeRhs, std::size_t NRhs"]
      v.return_type = ("small<ElementTypeRhs, NRhs>",)
      v.param_lhs = "ElementTypeRhs"
      v.param_rhs = "small<ElementTypeRhs, NRhs>"
  elif (array_type_name == "versa"):
    if (type_flags == (1,1)):
      v.typelist = [
        "typename ElementTypeLhs, typename AccessorTypeLhs,",
        "          typename ElementTypeRhs, typename AccessorTypeRhs"]
      v.return_type = (
        "versa<",
        "  typename binary_operator_traits<",
        "    ElementTypeLhs, ElementTypeRhs>::%s, AccessorTypeLhs>" % (
          op_class,))
      v.param_lhs = "versa<ElementTypeLhs, AccessorTypeLhs>"
      v.param_rhs = "versa<ElementTypeRhs, AccessorTypeRhs>"
    elif (type_flags == (1,0)):
      v.typelist = ["typename ElementTypeLhs, typename AccessorTypeLhs"]
      v.return_type = ("versa<ElementTypeLhs, AccessorTypeLhs>",)
      v.param_lhs = "versa<ElementTypeLhs, AccessorTypeLhs>"
      v.param_rhs = "ElementTypeLhs"
    elif (type_flags == (0,1)):
      v.typelist = ["typename ElementTypeRhs, typename AccessorTypeRhs"]
      v.return_type = ("versa<ElementTypeRhs, AccessorTypeRhs>",)
      v.param_lhs = "ElementTypeRhs"
      v.param_rhs = "versa<ElementTypeRhs, AccessorTypeRhs>"
  else:
    if (type_flags == (1,1)):
      v.typelist = ["typename ElementTypeLhs, typename ElementTypeRhs"]
      v.return_type = (
        "%s<" %(array_type_name,),
        "  typename binary_operator_traits<",
        "    ElementTypeLhs, ElementTypeRhs>::%s>" % (op_class,))
      v.param_lhs = "%s<ElementTypeLhs>" % (array_type_name,)
      v.param_rhs = "%s<ElementTypeRhs>" % (array_type_name,)
    elif (type_flags == (1,0)):
      v.typelist = ["typename ElementTypeLhs"]
      v.return_type = ("%s<ElementTypeLhs>" % (array_type_name,),)
      v.param_lhs = "%s<ElementTypeLhs>" % (array_type_name,)
      v.param_rhs = "ElementTypeLhs"
    elif (type_flags == (0,1)):
      v.typelist = ["typename ElementTypeRhs"]
      v.return_type = ("%s<ElementTypeRhs>" % (array_type_name,),)
      v.param_lhs = "ElementTypeRhs"
      v.param_rhs = "%s<ElementTypeRhs>" % (array_type_name,)
  v.typelist[0] = "template <" + v.typelist[0]
  v.typelist[-1] += ">"
  return v

def algo_params(array_type_name, type_flags):
  v = empty()
  v.result_constructor_args = ""
  v.size_assert = ""
  v.loop_n = "N"
  if (array_type_name != "tiny"):
    sizer = "size"
    if (array_type_name == "versa"): sizer = "accessor"
    if (type_flags == (1,1)):
      v.result_constructor_args = "(lhs.%s())" % (sizer,)
      v.size_assert = """if (lhs.size() != rhs.size()) throw_range_error();
    """
      v.loop_n = "lhs.size()"
    elif (type_flags == (1,0)):
      v.result_constructor_args = "(lhs.%s())" % (sizer,)
      v.loop_n = "lhs.size()"
    else:
      v.result_constructor_args = "(rhs.%s())" % (sizer,)
      v.loop_n = "rhs.size()"
  v.index_lhs = ""
  v.index_rhs = ""
  if (type_flags[0]): v.index_lhs = "[i]"
  if (type_flags[1]): v.index_rhs = "[i]"
  return v

def format_list(list, indent):
  r = ""
  for line in list[:-1]:
    r += indent + line + "\n"
  return r + indent + list[-1]

def elementwise_binary_op(
      array_type_name, op_class, op_symbol, type_flags, function_name):
  d = decl_params(array_type_name, op_class, type_flags)
  a = algo_params(array_type_name, type_flags)
  print """%s
  inline
%s
  %s(
    const %s& lhs,
    const %s& rhs) {
%s
    result%s;
    %sfor(std::size_t i=0;i<%s;i++) result[i] = lhs%s %s rhs%s;
    return result;
  }
""" % (format_list(d.typelist, "  "),
       format_list(d.return_type, "  "),
       function_name, d.param_lhs, d.param_rhs,
       format_list(d.return_type, "    "),
       a.result_constructor_args, a.size_assert, a.loop_n,
       a.index_lhs, op_symbol, a.index_rhs)

def elementwise_inplace_binary_op(
      array_type_name, op_class, op_symbol, type_flags):
  d = decl_params(array_type_name, op_class, type_flags)
  a = algo_params(array_type_name, type_flags)
  print """%s
  inline
  %s&
  operator%s(
    %s& lhs,
    const %s& rhs) {
    %sfor(std::size_t i=0;i<%s;i++) lhs[i] %s rhs%s;
    return lhs;
  }
""" % (format_list(d.typelist, "  "),
       d.param_lhs,
       op_symbol, d.param_lhs, d.param_rhs,
       a.size_assert, a.loop_n,
       op_symbol, a.index_rhs)

def generate_elementwise_binary_op(
      array_type_name, op_class, op_symbol, function_name = None):
  if (function_name == None):
    function_name = "operator" + op_symbol
  for type_flags in ((1,1), (1,0), (0,1)):
    elementwise_binary_op(
      array_type_name, op_class, op_symbol, type_flags, function_name)

def generate_elementwise_inplace_binary_op(
      array_type_name, op_class, op_symbol):
  for type_flags in ((1,1), (1,0)):
    elementwise_inplace_binary_op(
      array_type_name, op_class, op_symbol, type_flags)

def reducing_boolean_op(array_type_name, op_symbol, type_flags):
  d = decl_params(array_type_name, "boolean", type_flags)
  a = algo_params(array_type_name, type_flags)
  truth_test_type = "ElementTypeRhs"
  if (type_flags[0]): truth_test_type = "ElementTypeLhs"
  if (op_symbol == "=="):
    if (a.size_assert != ""):
      a.size_assert = """if (lhs.size() != rhs.size()) return %s() != %s();
    """ % (truth_test_type, truth_test_type)
    tests = (
"""      if (lhs%s != rhs%s) return %s() != %s();"""
    % (a.index_lhs, a.index_rhs, truth_test_type, truth_test_type))
    final_op = "=="
  elif (op_symbol == "!="):
    if (a.size_assert != ""):
      a.size_assert = """if (lhs.size() != rhs.size()) return %s() == %s();
    """ % (truth_test_type, truth_test_type)
    tests = (
"""      if (lhs%s != rhs%s) return %s() == %s();"""
    % (a.index_lhs, a.index_rhs, truth_test_type, truth_test_type))
    final_op = "!="
  elif (op_symbol in ("<", ">")):
    tests = (
"""      if (lhs%s %s rhs%s) return %s() == %s();
      if (rhs%s %s lhs%s) return %s() != %s();"""
    % (a.index_lhs, op_symbol, a.index_rhs, truth_test_type, truth_test_type,
       a.index_rhs, op_symbol, a.index_lhs, truth_test_type, truth_test_type))
    final_op = "!="
  elif (op_symbol in ("<=", ">=")):
    tests = (
"""      if (!(lhs%s %s rhs%s)) return %s() != %s();"""
    % (a.index_lhs, op_symbol, a.index_rhs, truth_test_type, truth_test_type))
    final_op = "=="
  if (type_flags == (1,1)):
    return_type = [
      "typename binary_operator_traits<",
      "  ElementTypeLhs, ElementTypeRhs>::boolean"]
  elif (type_flags == (1,0)):
    return_type = [
      "typename binary_operator_traits<",
      "  ElementTypeLhs, ElementTypeLhs>::boolean"]
  else:
    return_type = [
      "typename binary_operator_traits<",
      "  ElementTypeRhs, ElementTypeRhs>::boolean"]
  print """%s
  inline
%s
  operator%s(
    const %s& lhs,
    const %s& rhs) {
    %sfor(std::size_t i=0;i<%s;i++) {
%s
    }
    return %s() %s %s();
  }
""" % (format_list(d.typelist, "  "),
       format_list(return_type, "  "),
       op_symbol, d.param_lhs, d.param_rhs,
       a.size_assert, a.loop_n, tests,
       truth_test_type, final_op, truth_test_type)

def generate_reducing_boolean_op(array_type_name, op_symbol):
  for type_flags in ((1,1), (1,0), (0,1)):
    reducing_boolean_op(array_type_name, op_symbol, type_flags)

def get_result_constructor_args(array_type_name, arg_name = "a"):
  if (array_type_name == "tiny"): return ""
  if (array_type_name == "versa"):
    return "(%s.accessor())" % (arg_name,)
  return "(%s.size())" % (arg_name,)

def generate_unary_ops(array_type_name):
  Ntemplate_head = ""
  Nresult = ""
  result_constructor_args = get_result_constructor_args(array_type_name)
  if (array_type_name in ("tiny", "small")):
    Ntemplate_head = ", std::size_t N"
    Nresult = ", N"
  elif (array_type_name == "versa"):
    Ntemplate_head = ", typename AccessorType"
    Nresult = ", AccessorType"
  for op_class, op_symbol in (("arithmetic", "-"),
                              ("logical", "!")):
    print """  template <typename ElementType%s>
  inline
  %s<
    typename unary_operator_traits<
      ElementType>::%s%s>
  operator%s(const %s<ElementType%s>& a) {
    %s<
      typename unary_operator_traits<
        ElementType>::%s%s> result%s;
    for(std::size_t i=0;i<a.size();i++) result[i] = %sa[i];
    return result;
  }
""" % (Ntemplate_head,
       array_type_name, op_class, Nresult,
       op_symbol, array_type_name, Nresult,
       array_type_name, op_class, Nresult,
       result_constructor_args,
       op_symbol)

def get_array_template_args(array_type_name):
  if (array_type_name in ("tiny", "small")):
    return ["typename ElementType", "std::size_t N"]
  if (array_type_name in ("ref", "versa")):
    return ["typename ElementType", "typename AccessorType"]
  return ["typename ElementType"]

def get_template_param(array_type_name):
  if (array_type_name in ("tiny", "small")):
    return ["ElementType", "N"]
  if (array_type_name in ("ref", "versa")):
    return ["ElementType", "AccessorType"]
  return ["ElementType"]

def assemble_template_args(args):
  result = args[0]
  for a in args[1:]: result += (", " + a)
  return result

def wrap_template_args(args):
  result = args[:]
  result[0] = "template<" + args[0]
  for i in xrange(1, len(result)-1): result[i] = "         " + result[i]
  if (len(result) == 1):
    result[-1] += ">"
  else:
    result[0] += ","
    result[-1] = "         " + result[-1] + ">"
  return result

def wrap_template_param(array_type_name, param):
  result = array_type_name + "<"
  for p in param[:-1]: result += (p + ", ")
  result += (param[-1] + ">")
  return result

def number_template_args(array_type_name, for_header, args, i):
  if (array_type_name != "tiny"):
    return [a + str(i) for a in args]
  if (i == 1 or not for_header):
    return [a + str(i) for a in args[:-1]] + [args[-1]]
  return [a + str(i) for a in args[:-1]]

def number_list(array_type_name, for_header, args, n_parameters):
  result = []
  for i in xrange(1, n_parameters+1):
    result.append(number_template_args(array_type_name, for_header, args, i))
  return result

def form_result_type(array_type_name, tp):
  if (array_type_name != "small"): return tp[0]
  return [tp[0][0], "(N1<N2?N1:N2)"]

def generate_1arg_reductions(array_type_name):
  template_args = get_array_template_args(array_type_name)
  template_param = get_template_param(array_type_name)
  header = wrap_template_args([assemble_template_args(template_args)])
  for function_name in reduction_functions_1arg:
    print """%s
  ElementType
  %s(const %s& a) {
    return %s(a.const_ref());
  }
""" % (format_list(header, "  "),
       function_name,
       wrap_template_param(array_type_name, template_param),
       function_name)

def generate_2arg_reductions(array_type_name):
  template_args = get_array_template_args(array_type_name)
  ta = number_list(array_type_name, 1, template_args, 2)
  template_param = get_template_param(array_type_name)
  tp = number_list(array_type_name, 0, template_param, 2)
  header = wrap_template_args([assemble_template_args(a) for a in ta])
  for function_name in reduction_functions_2arg:
    print """%s
  ElementType1
  %s(
    const %s& a1,
    const %s& a2) {
    return %s(a1.const_ref(), a2.const_ref());
  }
""" % (format_list(header, "  "),
       function_name,
       wrap_template_param(array_type_name, tp[0]),
       wrap_template_param(array_type_name, tp[1]),
       function_name)

def generate_1arg_element_wise(array_type_name):
  result_constructor_args = get_result_constructor_args(array_type_name)
  template_args = get_array_template_args(array_type_name)
  template_param = get_template_param(array_type_name)
  header = wrap_template_args([assemble_template_args(template_args)])
  for function_name in cmath_1arg + cstdlib_1arg:
    print """%s
  %s
  %s(const %s& a) {
    %s result%s;
    for(std::size_t i=0;i<a.size();i++) result[i] = std::%s(a[i]);
    return result;
  }
""" % (format_list(header, "  "),
       wrap_template_param(array_type_name, template_param),
       function_name,
       wrap_template_param(array_type_name, template_param),
       wrap_template_param(array_type_name, template_param),
       result_constructor_args,
       function_name)

def generate_2arg_element_wise(array_type_name):
  result_constructor_args = get_result_constructor_args(array_type_name, "a1")
  template_args = get_array_template_args(array_type_name)
  ta = number_list(array_type_name, 1, template_args, 2)
  template_param = get_template_param(array_type_name)
  tp = number_list(array_type_name, 0, template_param, 2)
  rt = form_result_type(array_type_name, tp)
  header = wrap_template_args([assemble_template_args(a) for a in ta])
  for function_name in cmath_2arg:
    print """%s
  %s
  %s(
    const %s& a1,
    const %s& a2) {
    %s result%s;
    for(std::size_t i=0;i<a1.size();i++) {
      result[i] = std::%s(a1[i], a2[i]);
    }
    return result;
  }
""" % (format_list(header, "  "),
       wrap_template_param(array_type_name, rt),
       function_name,
       wrap_template_param(array_type_name, tp[0]),
       wrap_template_param(array_type_name, tp[1]),
       wrap_template_param(array_type_name, rt), result_constructor_args,
       function_name)

def one_type(array_type_name):
  f = open("%s_operators.h" % (array_type_name,), "w")
  sys.stdout = f
  write_copyright()
  print """
#ifndef CCTBX_ARRAY_FAMILY_%s_OPERATORS_H
#define CCTBX_ARRAY_FAMILY_%s_OPERATORS_H
""" % ((array_type_name.upper(),) * 2)
  if (array_type_name != "ref"):
    print """#include <cmath>
#include <cstdlib>
#include <cctbx/array_family/operator_traits_builtin.h>"""
  print """#include <cctbx/array_family/reductions.h>

namespace cctbx { namespace af {
"""

  if (array_type_name != "ref"):
    generate_unary_ops(array_type_name)
    for op_symbol in arithmetic_binary_ops:
      generate_elementwise_binary_op(
        array_type_name, "arithmetic", op_symbol)
      generate_elementwise_inplace_binary_op(
        array_type_name, "arithmetic", op_symbol + "=")
    for op_symbol in logical_binary_ops:
      generate_elementwise_binary_op(
        array_type_name, "logical", op_symbol)
    for op_symbol, function_name in (
      ("==", "equal_to"),
      ("!=", "not_equal_to"),
      (">", "greater"),
      ("<", "less"),
      (">=", "greater_equal"),
      ("<=", "less_equal")):
      generate_elementwise_binary_op(
        array_type_name, "boolean", op_symbol, function_name)
    for op_symbol in boolean_ops:
      generate_reducing_boolean_op(array_type_name, op_symbol)
    generate_1arg_element_wise(array_type_name)
    generate_2arg_element_wise(array_type_name)
  generate_1arg_reductions(array_type_name)
  generate_2arg_reductions(array_type_name)

  print """}} // namespace cctbx::af

#endif // CCTBX_ARRAY_FAMILY_%s_OPERATORS_H""" % (array_type_name.upper(),)
  sys.stdout = sys.__stdout__
  f.close()

def run():
  one_type("ref")
  one_type("tiny")
  one_type("small")
  one_type("shared")
  one_type("versa")

if (__name__ == "__main__"):
  run()
