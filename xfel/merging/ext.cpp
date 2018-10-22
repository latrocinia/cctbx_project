#include <cctbx/boost_python/flex_fwd.h>
#include <boost/python/module.hpp>
#include <boost/python/class.hpp>
#include <boost/python/def.hpp>
#include <boost/python/list.hpp>
#include <scitbx/array_family/flex_types.h>
#include <scitbx/array_family/shared.h>
#include <scitbx/array_family/versa.h>
#include <scitbx/array_family/accessors/c_grid.h>
#include <cctbx/miller.h>
#include <dials/array_family/reflection_table.h>
#include <algorithm>

typedef cctbx::miller::index<> miller_index_t;

namespace sx_merging {
  void foo2(){
    std::cout <<"HELLO merging foo2"<< std::endl;
  }

  void get_hkl_chunks_cpp(dials::af::reflection_table reflections,
                          const scitbx::af::shared<miller_index_t>& hkl_list,
                          const scitbx::af::shared<int>& chunk_id_list,
                          boost::python::list hkl_chunks_cpp){

    // set up a map hkl:chunk_id
    std::map<miller_index_t, size_t> chunk_lookup;
    for(size_t i = 0UL; i < hkl_list.size(); ++i){
      chunk_lookup[hkl_list[i]] = (size_t)chunk_id_list[i];
    }

    SCITBX_ASSERT(reflections.contains("miller_index_asymmetric"));
    SCITBX_ASSERT(reflections.contains("intensity.sum.value"));
    SCITBX_ASSERT(reflections.contains("intensity.sum.variance"));

    scitbx::af::ref<miller_index_t> miller_index = reflections["miller_index_asymmetric"];
    scitbx::af::ref<double> intensity = reflections["intensity.sum.value"];
    scitbx::af::ref<double> variance = reflections["intensity.sum.variance"];

    miller_index_t* mi_ptr = miller_index.begin();
    double* intensity_ptr = intensity.begin();
    double* variance_ptr = variance.begin();


    int n_chunks = boost::python::len(hkl_chunks_cpp);
    std::vector<dials::af::reflection_table> tables;
    for(size_t i=0UL; i < n_chunks; ++i){
      tables.push_back(boost::python::extract<dials::af::reflection_table>(hkl_chunks_cpp[i]));
      SCITBX_ASSERT(tables.back().contains("miller_index_asymmetric"));
    }

    // cache all columns for all hkl chunks
    std::vector<scitbx::af::shared<miller_index_t> >  mi_cols;
    std::vector<scitbx::af::shared<double> >          intensity_cols;
    std::vector<scitbx::af::shared<double> >          variance_cols;

    for(size_t i=0UL; i < n_chunks; ++i){
      mi_cols.push_back(tables[i]["miller_index_asymmetric"]);
      intensity_cols.push_back(tables[i]["intensity.sum.value"]);
      variance_cols.push_back(tables[i]["intensity.sum.variance"]);
    }

    // distribute reflections over chunks
    for(size_t i=0UL; i < reflections.size(); ++i){
      miller_index_t  hkl       = *mi_ptr++;
      double          intensity = *intensity_ptr++;
      double          variance  = *variance_ptr++;

      if( 0 != chunk_lookup.count(hkl) )
      {
          size_t chunk_id  = chunk_lookup[hkl];
          mi_cols[chunk_id].push_back(hkl);
          intensity_cols[chunk_id].push_back(intensity);
          variance_cols[chunk_id].push_back(variance);
       }
    }
  }
}

using namespace boost::python;
namespace sx_merging{
namespace boost_python { namespace {

  void
  sx_merging_init_module() {
    using namespace boost::python;
    typedef return_value_policy<return_by_value> rbv;
    typedef default_call_policies dcp;

    def("foo2",&sx_merging::foo2);
    def("get_hkl_chunks_cpp",&sx_merging::get_hkl_chunks_cpp);
  }

}
}} // namespace sx_merging::boost_python::<anonymous>

BOOST_PYTHON_MODULE(sx_merging_ext)
{
  sx_merging::boost_python::sx_merging_init_module();
}
