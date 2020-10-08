################################################################################
##### RERF Commons Dict
################################################################################
# Joe rerf-v1, 2020-10-08

# ## Get the latest version of Dictionarytool
# git_dir="/Users/christopher/Documents/GitHub/uc-cdis" #change this to your local github directory
# cd $git_dir
#
# # # if you need it, clone the repo
# # git clone git@github.com:uc-cdis/gen3_dictionary_tools.git
#
# tool_dir="${git_dir}/gen3_dictionary_tools"
# cd $tool_dir
#
# git checkout master
# git pull origin master
#
# # latest working branch for gen3 dictionaries (2020-10)
# git checkout charlie_fix
# git pull origin charlie_fix

# setup dirs
dd_dir="/Users/christopher/Documents/Notes/RERF/dd/rerf_dict_joe" #change this to your local directory where you unpacked the archive
dd_name="rerf-v1"

tsv_in="${dd_dir}/${dd_name}/tsv_in"
tsv_out="${dd_dir}/${dd_name}/tsv_out"
yaml_in="${dd_dir}/${dd_name}/yaml_in"
yaml_out="${dd_dir}/${dd_name}/yaml_out"


# Download scripts:
script_dir="${dd_dir}/scripts"
mkdir -p $script_dir
cd $script_dir

wget https://github.com/uc-cdis/gen3_dictionary_tools/raw/charlie_fix/Dictionarytool/scripts/tsv2yaml.py
wget https://github.com/uc-cdis/gen3_dictionary_tools/raw/charlie_fix/Dictionarytool/scripts/schema_utils.py
wget https://github.com/uc-cdis/gen3_dictionary_tools/raw/charlie_fix/Dictionarytool/scripts/yaml2tsv.py

# pointers for tools
tsv2yaml="${script_dir}/tsv2yaml.py"
yaml2tsv="${script_dir}/yaml2tsv.py"


# For Joe's dictionary 2020-10-08
# Create the TSVs from YAML schemas

rm -r -f $yaml_out
python $tsv2yaml -i $tsv_in -o $yaml_out -e "tsv"

ls -l $yaml_out

# Move YAML and push to GitHub
git_dir="/Users/christopher/Documents/GitHub/uc-cdis"
repo_dir="${git_dir}/rerf_dictionary"
cd $repo_dir

# cut new branch from master for changed schemas
git checkout master
git pull origin master

new_branch="feat/rerf-v1"
git branch $new_branch
git checkout $new_branch

# move the newly created yaml schemas to the GitHub schemas dir
schemas_dir="${repo_dir}/gdcdictionary/schemas"
mv ${yaml_out}/*.yaml $schemas_dir

git add ${schemas_dir}/*yaml
git commit -a -m "updated yaml using tsv2yaml"
git push origin $new_branch

# go here, e.g., and create a pull request to see what changed, get approval, merge it to master branch, and release new dictionary!
https://github.com/uc-cdis/rerf_dictionary/pull/new/feat/rerf-v1


################################################################################
################################################################################
# Create the TSVs from new YAML schemas
dd_dir="/Users/christopher/Documents/Notes/RERF/dd/rerf_dict_joe" #change this to your local path
dd_name="rerf-v1"

script_dir="${dd_dir}/scripts"
yaml2tsv="${script_dir}/yaml2tsv.py"

git_dir="/Users/christopher/Documents/GitHub/uc-cdis"
repo_dir="${git_dir}/rerf_dictionary"
schemas_dir="${repo_dir}/gdcdictionary/schemas"

tsv_in="${dd_dir}/${dd_name}/tsv_in"
tsv_out="${dd_dir}/${dd_name}/tsv_out"
yaml_in="${dd_dir}/${dd_name}/yaml_in"
yaml_out="${dd_dir}/${dd_name}/yaml_out"

# clear whatever might be in yaml in
rm ${yaml_in}/*

# create TSVs of just what we input before
cp ${yaml_out}/*yaml $yaml_in
cp ${schemas_dir}/pro{gram,ject}.yaml $yaml_in
cp ${schemas_dir}/core_metadata_collection.yaml $yaml_in

rm -f ${tsv_out}/*.xlsx
python $yaml2tsv -i $yaml_in -o $tsv_out -d $dd_name


# OR copy the existing yaml from GitHub to "yaml_in"
git_dir="/Users/christopher/Documents/GitHub/uc-cdis"
repo_dir="${git_dir}/rerf_dictionary"
cd $repo_dir

git checkout feat/rerf-v1

cd $yaml_in
cp ${schemas_dir}/*yaml $yaml_in

rm -f ${tsv_out}/*.xlsx
python $yaml2tsv -i $yaml_in -o $tsv_out -d $dd_name
