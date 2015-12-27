<?php if ( ! defined('BASEPATH')) exit('No direct script access allowed');

class molecules_model extends MY_Model{

    function molecules_model(){
        parent::__construct();
        $this->tbl = 'BOTANICULE';
    }

    function count_by($column, $match){
        $this->db->like($column, $match);
        $this->db->from($this->tbl);    
        return $this->db->count_all_results();
    } 

    function unique_counts($field_name){
        $this->db->distinct();
        $this->db->select($field_name);
        $this->db->where($field_name . '<>', '""');
        return $this->db->get($this->tbl)->num_rows();    
    }

    function get_paged_mol($tbl = 'BOTANICULE', $limit = 1, $offset = 1){
        $this->tbl = $tbl;
        $this->db->where('therapeutic_category != ', '')->where('molecule_type != ', '')->where('display_in_website', 1)->where('cd_structure != ', null)->order_by('molecule_name', 'asc');
        return $this->db->get($this->tbl, $limit, $offset);
    }

    function src_family($limit = 0){

        $sql = 'select source_family family, count(*) row_count from ' . $this->tbl . ' where source_family <> "" group by source_family order by 1 desc limit ' . $limit;
        return $this->db->query($sql);
    } 

    function thera_catg($limit = 0){

        $sql = 'select therapeutic_category tc, count(*) row_count from ' . $this->tbl . ' where therapeutic_category <> "" group by therapeutic_category order by 2 desc limit ' . $limit;
        return $this->db->query($sql);
    } 

    function family_plants($limit = 0){

        $sql = 'select source_family family, source_name plants, count(*) row_count from ' . $this->tbl . ' where source_family <> "" and source_name <> "" group by source_family, source_name order by 3 desc limit ' . $limit;
        return $this->db->query($sql);
    } 

    function decade_counts($limit = 0){
        $sql = 'select (a_year div 10) * "10" year, count(*) articles from l_articles where source_code="JNP" group by a_year div 10 order by a_year';
        return $this->db->query($sql)->result();    
    } 

    function get_last_updated_on($tbl = 'BOTANICULE'){
        $this->tbl = $tbl;
        $sql = "select max(Date_Imported) last_updated_on from " . $tbl . " where Date_Imported is not null order by 1 desc limit 1";
        return $this->db->query($sql)->row('last_updated_on');
    }
}
?>